# app/cipher_breaker.py
import numpy as np

def load_dataset(path):
    with open(path, 'r') as f:
        return f.read().strip()

def initial_key_setup(ciphertext):
    # Initialize key and distribution, for simplicity assume English frequency
    frequencies = {'E': 12.7, 'T': 9.1, 'A': 8.2}  # Sample, complete as necessary
    key_map = {}
    # Here, you would generate an initial mapping
    # Random assignment based on expected frequencies
    return key_map

def score_key(ciphertext, key_map):
    # Compute score based on the digram frequencies, scoring as per nested hill-climb method
    score = 0
    # Use digram or trigram analysis to score this key_map
    # E.g., with a matrix or dict storing expected English frequencies
    return score

def hill_climb(ciphertext, key_map):
    # Outer layer of hill climb
    best_score = score_key(ciphertext, key_map)
    best_key = key_map.copy()
    improved = True

    while improved:
        improved = False
        for swap_a, swap_b in possible_swaps(key_map):
            swapped_key = swap(key_map, swap_a, swap_b)
            score = score_key(ciphertext, swapped_key)
            if score > best_score:
                best_key = swapped_key
                best_score = score
                improved = True
                key_map = swapped_key
    return best_key, best_score

def possible_swaps(key_map):
    # Generate possible pairs for swapping letters in the key
    keys = list(key_map.keys())
    return [(keys[i], keys[j]) for i in range(len(keys)) for j in range(i + 1, len(keys))]

def swap(key_map, a, b):
    # Swap letters in key_map and return new map
    new_key = key_map.copy()
    new_key[a], new_key[b] = new_key[b], new_key[a]
    return new_key
