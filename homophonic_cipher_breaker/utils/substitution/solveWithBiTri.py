from collections import Counter


COMMON_ONE_LETTER_WORDS = ['A', 'I']
COMMON_TWO_LETTER_WORDS = ['TO', 'OF', 'IN', 'IT', 'IS', 'AS', 'AT', 'BE', 'WE', 'HE', 'SO', 'ON', 'AN', 'OR', 'DO', 'IF', 'UP', 'BY', 'MY']
COMMON_THREE_LETTER_WORDS = ['THE', 'AND', 'ARE', 'FOR', 'NOT', 'BUT', 'HAD', 'HAS', 'WAS', 'ALL', 'ANY', 'ONE', 'MAN', 'OUT', 'YOU', 'HIS', 'HER', 'CAN']


def extract_words(text):
    return text.split()


def apply_key_to_text(ciphertext, key):
    deciphered_text = ''
    for char in ciphertext:
        if char == ' ' or char in ".,'()":  
            deciphered_text += char
        else:
            deciphered_text += key.get(char, char)  
    return deciphered_text


def update_key_with_common_words(ciphertext, key):
    words = extract_words(ciphertext)
    
    
    for word in words:
        if len(word) == 1:
            if word not in key:
                key[word] = 'A' if 'A' not in key.values() else 'I'
    
    
    for word in words:
        if len(word) == 2 and word not in key:
            for common_word in COMMON_TWO_LETTER_WORDS:
                if set(common_word).isdisjoint(key.values()):
                    for i, letter in enumerate(word):
                        if letter not in key:
                            key[letter] = common_word[i]
                    break
    
    
    for word in words:
        if len(word) == 3 and word not in key:
            for common_word in COMMON_THREE_LETTER_WORDS:
                if set(common_word).isdisjoint(key.values()):
                    for i, letter in enumerate(word):
                        if letter not in key:
                            key[letter] = common_word[i]
                    break
    
    return key


def frequency_analysis(ciphertext):
    letter_counts = Counter(c for c in ciphertext if c.isalpha())  
    return letter_counts.most_common()


def update_key_with_frequency_analysis(ciphertext, key):
    letter_counts = frequency_analysis(ciphertext)
    english_frequencies = {'E': 0.127, 'T': 0.090, 'A': 0.082, 'O': 0.075, 'I': 0.070, 'N': 0.067, 'S': 0.063, 'H': 0.061, 'R': 0.060, 'D': 0.043, 'L': 0.040, 'U': 0.028, 'C': 0.027, 'M': 0.024, 'F': 0.022, 'P': 0.019, 'G': 0.016, 'B': 0.014, 'Y': 0.014, 'V': 0.010, 'K': 0.008, 'J': 0.007, 'X': 0.002, 'Q': 0.001, 'Z': 0.001}
    
    
    sorted_ciphertext_letters = [item[0] for item in letter_counts]
    sorted_english_letters = sorted(english_frequencies, key=english_frequencies.get, reverse=True)
    
    
    for cipher_letter, english_letter in zip(sorted_ciphertext_letters, sorted_english_letters):
        if cipher_letter not in key:  
            key[cipher_letter] = english_letter
    
    return key


def decrypt_with_bitri(ciphertext):
    key = {}

    
    key = update_key_with_common_words(ciphertext, key)

    
    key = update_key_with_frequency_analysis(ciphertext, key)

    
    deciphered_text = apply_key_to_text(ciphertext, key)

    return deciphered_text, key



