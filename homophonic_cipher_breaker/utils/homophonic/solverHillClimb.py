import random
import string
from collections import Counter

# Frequency of letters in English (approximate)
ENGLISH_FREQ = {
    'e': 0.127, 't': 0.090, 'a': 0.081, 'o': 0.075, 'i': 0.070,
    'n': 0.067, 's': 0.063, 'h': 0.061, 'r': 0.060, 'd': 0.043,
    'l': 0.040, 'c': 0.028, 'u': 0.028, 'm': 0.024, 'f': 0.022,
    'p': 0.019, 'g': 0.017, 'b': 0.015, 'v': 0.010, 'k': 0.008,
    'x': 0.002, 'q': 0.001, 'j': 0.001, 'z': 0.001, 'y': 0.001
}

# Function to calculate the "fitness" of the decrypted text
def fitness_function(decrypted_text):
    letter_count = Counter(decrypted_text)
    total_letters = sum(letter_count.values())
    if total_letters == 0:
        return 0  # Avoid division by zero

    # Calculate the frequency of each letter in the decrypted text
    letter_freq = {char: letter_count.get(char, 0) / total_letters for char in string.ascii_lowercase}
    
    # Calculate the fitness score by comparing frequencies with English frequencies
    score = 0
    for char in string.ascii_lowercase:
        score += abs(letter_freq.get(char, 0) - ENGLISH_FREQ.get(char, 0))
    
    return score

# Generate a random initial substitution cipher for numbers (1-100) to capital letters
def generate_random_cipher():
    letters = list(string.ascii_uppercase)
    numbers = [str(i) for i in range(1, 101)]  # Numbers from 1 to 100
    random.shuffle(letters)
    cipher_map = dict(zip(numbers, letters))
    return cipher_map

# Apply a substitution cipher to the ciphertext (handling multi-digit numbers)
def apply_substitution(ciphertext, cipher_map):
    decrypted_text = []
    current_number = ''
    
    # Iterate through the ciphertext
    for char in ciphertext:
        if char.isdigit():
            current_number += char  # Collect digits to form a multi-digit number
        elif char == ' ':
            if current_number:  # If we have a number, apply the substitution
                if current_number in cipher_map:
                    decrypted_text.append(cipher_map[current_number])  # Map the multi-digit number to a letter
                else:
                    decrypted_text.append('?')  # If the number isn't in the cipher map, show a placeholder
                current_number = ''  # Reset number collection
            decrypted_text.append(' ')  # Preserve space
        elif char in string.punctuation:
            decrypted_text.append(char)  # Preserve punctuation as is
        else:
            if current_number:  # If we have a number, apply the substitution
                if current_number in cipher_map:
                    decrypted_text.append(cipher_map[current_number])
                else:
                    decrypted_text.append('?')
                current_number = ''  # Reset number collection
            decrypted_text.append(char)  # Directly append other characters (e.g., letters if any)
    
    # Handle any remaining number at the end of the ciphertext
    if current_number:
        if current_number in cipher_map:
            decrypted_text.append(cipher_map[current_number])
        else:
            decrypted_text.append('?')
    
    return ''.join(decrypted_text)

# Hill Climbing Algorithm to break the homophonic cipher
def hill_climb(ciphertext, max_iterations=1000):
    # Step 1: Generate an initial random substitution map for numbers (1-100) to letters
    current_cipher_map = generate_random_cipher()
    current_decrypted = apply_substitution(ciphertext, current_cipher_map)
    current_fitness = fitness_function(current_decrypted)

    print(f"Initial fitness: {current_fitness}")
    
    # Step 2: Hill climbing loop
    for iteration in range(max_iterations):
        # Step 3: Create a neighboring solution (swap two numbers in the current map)
        neighbor_cipher_map = current_cipher_map.copy()
        # Select two random numbers to swap
        num1, num2 = random.sample(list(current_cipher_map.keys()), 2)
        neighbor_cipher_map[num1], neighbor_cipher_map[num2] = neighbor_cipher_map[num2], neighbor_cipher_map[num1]
        
        # Step 4: Apply the new cipher and evaluate its fitness
        neighbor_decrypted = apply_substitution(ciphertext, neighbor_cipher_map)
        neighbor_fitness = fitness_function(neighbor_decrypted)
        
        # Step 5: If the neighbor is better (lower fitness score), accept it
        if neighbor_fitness < current_fitness:
            current_cipher_map = neighbor_cipher_map
            current_decrypted = neighbor_decrypted
            current_fitness = neighbor_fitness
            print(f"Iteration {iteration + 1}: Better solution found, fitness: {current_fitness}")
    
    return current_decrypted, current_cipher_map

# Example ciphertext (homophonic substitution cipher where numbers map to letters)
ciphertext = "12 3 4 89"

# Running the hill climb attack
decrypted_text, cipher_map = hill_climb(ciphertext)
print(f"\nDecrypted text: {decrypted_text}")
print(f"Cipher Map: {cipher_map}")
