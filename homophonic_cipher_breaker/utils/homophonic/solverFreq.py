from collections import Counter
import string

# Frequency of letters in English text (in order from most to least common)
english_frequency_order = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

def frequency_analysis_homo(ciphertext):
    """Performs frequency analysis on the ciphertext and tries to guess the substitution."""
    # Count the frequency of each number in the ciphertext
    number_counts = Counter(ciphertext.split())
    
    # Sort the numbers by frequency (descending)
    sorted_counts = sorted(number_counts.items(), key=lambda item: item[1], reverse=True)
    
    # Map the most frequent numbers to the most common English letters
    letter_to_numbers = {}
    for i, (number, _) in enumerate(sorted_counts):
        letter = english_frequency_order[i % len(english_frequency_order)]
        if letter not in letter_to_numbers:
            letter_to_numbers[letter] = []
        letter_to_numbers[letter].append(number)
    
    return letter_to_numbers

def decrypt_homo_freq(ciphertext, letter_to_numbers):
    """Decrypts the ciphertext using the guessed number-to-letter mappings."""
    # Split the ciphertext by spaces, but keep track of the spaces and punctuation
    ciphertext_parts = []
    current_part = []
    
    # We will preserve the spaces and punctuation marks in the ciphertext to manage word boundaries
    for char in ciphertext:
        if char in " ,.'()":  # Punctuation to be ignored, but kept in decrypted text
            if current_part:
                ciphertext_parts.append(''.join(current_part))
                current_part = []
            ciphertext_parts.append(char)  # Keep punctuation as is
        elif char == " ":
            if current_part:
                ciphertext_parts.append(''.join(current_part))
                current_part = []
            ciphertext_parts.append(" ")  # Keep the space
        else:
            current_part.append(char)
    
    if current_part:
        ciphertext_parts.append(''.join(current_part))  # Append the last part if it exists
    
    # Create a reverse mapping from number to letter
    number_to_letter = {}
    for letter, numbers_list in letter_to_numbers.items():
        for number in numbers_list:
            number_to_letter[number] = letter
    
    # Rebuild the decrypted text while considering space and punctuation logic
    decrypted_text = ''
    prev_was_space = False
    for part in ciphertext_parts:
        if part == " ":
            if prev_was_space:
                decrypted_text += " "  # Add a single space only if it's not already a space after another space
            prev_was_space = True
        elif part in " ,.'()":  # If it's punctuation, add it directly
            decrypted_text += part
            prev_was_space = False
        else:
            # Process numbers and replace them with letters
            numbers = part.split()
            decrypted_text += ''.join(number_to_letter.get(num, num) for num in numbers)
            prev_was_space = False
    
    return decrypted_text


