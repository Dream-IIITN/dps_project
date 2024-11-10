# English letter and bigram frequency data (simplified example)
import random
from collections import Counter
english_letter_freq = {
    'E': 12.7, 'T': 9.1, 'A': 8.2, 'O': 7.5, 'I': 7.0, 'N': 6.7, 'S': 6.3,
    'H': 6.1, 'R': 6.0, 'D': 4.3, 'L': 4.0, 'C': 2.8, 'U': 2.8, 'M': 2.4,
    'W': 2.4, 'F': 2.2, 'G': 2.0, 'Y': 2.0, 'P': 1.9, 'B': 1.5, 'V': 1.0,
    'K': 0.8, 'J': 0.2, 'X': 0.2, 'Q': 0.1, 'Z': 0.1
}
english_bigram_freq = {
    'TH': 1.52, 'HE': 1.28, 'IN': 0.94, 'ER': 0.94, 'AN': 0.82, 'RE': 0.68,
    'ND': 0.63, 'AT': 0.59, 'ON': 0.57, 'NT': 0.56, 'HA': 0.56, 'ES': 0.56
    # Add more bigrams for better accuracy
}

def load_dataset(path):
    with open(path, 'r') as f:
        return f.read().strip()

def initial_key_setup(ciphertext):
    unique_symbols = list(set(ciphertext))
    random.shuffle(unique_symbols)

    # Map symbols to letters based on English frequency
    key_map = {letter: [] for letter in english_letter_freq.keys()}
    for i, symbol in enumerate(unique_symbols):
        letter = list(english_letter_freq.keys())[i % len(english_letter_freq)]
        key_map[letter].append(symbol)

    return key_map

def score_key(ciphertext, key_map):
    # Map each symbol in the ciphertext to its current guessed letter
    reverse_map = {symbol: letter for letter, symbols in key_map.items() for symbol in symbols}
    decoded_text = ''.join(reverse_map.get(char, '?') for char in ciphertext)

    # Frequency-based scoring with single letters and bigrams
    letter_counts = Counter(decoded_text)
    bigram_counts = Counter(decoded_text[i:i+2] for i in range(len(decoded_text) - 1))

    score = 0
    for letter, freq in english_letter_freq.items():
        actual_freq = (letter_counts[letter] / len(decoded_text)) * 100
        score -= abs(freq - actual_freq)  # Minimize difference from expected frequencies

    for bigram, freq in english_bigram_freq.items():
        actual_freq = (bigram_counts[bigram] / (len(decoded_text) - 1)) * 100
        score -= abs(freq - actual_freq)  # Penalize bigram frequency deviations

    return score

def hill_climb(ciphertext, key_map):
    best_score = score_key(ciphertext, key_map)
    best_key = key_map.copy()
    improved = True

    while improved:
        improved = False
        for letter, i, j in possible_swaps(key_map):
            swapped_key = swap(key_map, letter, i, j)
            score = score_key(ciphertext, swapped_key)
            if score > best_score:
                best_key = swapped_key
                best_score = score
                improved = True
                key_map = swapped_key
    return best_key, best_score

def possible_swaps(key_map):
    letters = list(key_map.keys())
    swaps = []
    for letter in letters:
        if len(key_map[letter]) > 1:
            for i in range(len(key_map[letter])):
                for j in range(i + 1, len(key_map[letter])):
                    swaps.append((letter, i, j))
    return swaps

def swap(key_map, letter, i, j):
    new_key = {k: v[:] for k, v in key_map.items()}
    new_key[letter][i], new_key[letter][j] = new_key[letter][j], new_key[letter][i]
    return new_key

def apply_key(ciphertext, key_map):
    reverse_map = {symbol: letter for letter, symbols in key_map.items() for symbol in symbols}
    return ''.join(reverse_map.get(char, '?') for char in ciphertext)