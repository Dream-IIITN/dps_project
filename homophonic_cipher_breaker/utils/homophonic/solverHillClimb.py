import random
import math


frequencies = {
    'A': 8.17, 'B': 1.49, 'C': 2.78, 'D': 4.25, 'E': 12.70,
    'F': 2.23, 'G': 2.02, 'H': 6.09, 'I': 6.97, 'J': 0.15,
    'K': 0.77, 'L': 4.03, 'M': 2.41, 'N': 6.75, 'O': 7.51,
    'P': 1.93, 'Q': 0.10, 'R': 5.99, 'S': 6.33, 'T': 9.06,
    'U': 2.76, 'V': 0.98, 'W': 2.36, 'X': 0.15, 'Y': 1.97, 'Z': 0.07
}   


def decrypt(text, cipher_map):
    decrypted_text = []
    words = text.split("  ")  
    
    for word in words:
        decrypted_word = []
        for num in word.split():
            decrypted_word.append(cipher_map.get(num, num))  
        decrypted_text.append(''.join(decrypted_word))
    
    return '  '.join(decrypted_text)  


def fitness(decrypted_text):
    
    letter_count = {char: decrypted_text.count(char) for char in set(decrypted_text) if char.isalpha()}
    total_letters = sum(letter_count.values())
    fitness_score = 0.0

    
    for letter, count in letter_count.items():
        expected_freq = frequencies.get(letter.upper(), 0) / 100.0
        actual_freq = count / total_letters if total_letters > 0 else 0
        fitness_score += math.exp(-abs(expected_freq - actual_freq))  

    return fitness_score


def hill_climb_attack(ciphertext):
    
    numbers = [str(i) for i in range(1, 101)]  
    letters = list(frequencies.keys())  
    random.shuffle(letters)  
    cipher_map = {numbers[i]: letters[i % len(letters)] for i in range(len(numbers))}  

    current_decrypted = decrypt(ciphertext, cipher_map)
    current_fitness = fitness(current_decrypted)
    iterations = 0
    max_iterations = 10000  
    temperature = 1.0  
    cooling_rate = 0.99  

    while iterations < max_iterations:
        iterations += 1
        
        new_cipher_map = cipher_map.copy()
        num1, num2 = random.sample(numbers, 2)  
        new_cipher_map[num1], new_cipher_map[num2] = new_cipher_map[num2], new_cipher_map[num1]

        new_decrypted = decrypt(ciphertext, new_cipher_map)
        new_fitness = fitness(new_decrypted)

        
        if new_fitness > current_fitness or random.uniform(0, 1) < temperature:
            cipher_map = new_cipher_map
            current_decrypted = new_decrypted
            current_fitness = new_fitness

        
        temperature *= cooling_rate

        
        if current_fitness > 0.95:
            break

    return current_decrypted, cipher_map



