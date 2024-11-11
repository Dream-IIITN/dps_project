import collections

# Define expected letter frequencies in English (simplified)
# This is a list of letters in decreasing order of frequency
english_frequencies = ['E', 'T', 'A', 'O', 'I', 'N', 'S', 'H', 'R', 'D', 'L', 'C', 'U', 'M', 'P', 'B', 'V', 'K', 'G', 'W', 'F', 'Y', 'Z', 'X', 'Q', 'J']

# Analyze frequency of characters in ciphertext
def analyze_frequency(ciphertext):
    # Split the ciphertext by spaces to get individual numbers
    numbers = ciphertext.split()
    
    # Count the frequency of each number
    frequency = collections.Counter(numbers)
    
    # Sort numbers by frequency (most common first)
    sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_frequency

# Perform the attack by using frequency analysis
def frequency_analysis_attack(ciphertext):
    # Analyze the frequency of numbers in the ciphertext
    sorted_frequency = analyze_frequency(ciphertext)
    
    # Map the most frequent numbers to the most frequent English letters
    number_to_letter = {}
    for i, (number, _) in enumerate(sorted_frequency):
        if i < len(english_frequencies):
            # Map number to corresponding letter based on frequency order
            number_to_letter[number] = english_frequencies[i]
    
    # Decrypt the ciphertext by replacing numbers with letters
    decrypted_text = []
    for number in ciphertext.split():
        if number in number_to_letter:
            decrypted_text.append(number_to_letter[number])
        else:
            decrypted_text.append(number)  # For numbers that don't have a mapping
    
    # Join decrypted text into a string
    return ''.join(decrypted_text)

# Sample ciphertext (encrypted text)
ciphertext = "21 31 1 25   17 68 40 65 70 62 12   45 5 97   98 41 57 87 26 58 0 12   34 68 41   41 47 47 78 85 13 58 34 90   31 92 17 35 57 95 47   69 67   82 70 7 27 29 87 70 77 97 80 5 96   82 41 85 47 80 91 58 65 78   99 51 67 69 3 30 89 91 54 69 22   7 26 69 59   87 51 34 76 1 75 48 77 54 28 64 4   34 57 57 27 82 82 ,   30 40 47 76 47 83 ,   88 68   2 3 11 25 62 42 83 79 .   4 31 53 34   17 3 58 65 25 57 12   27 5 94 87 14 11 79   80 5 97 50 65 99 97 87 31 84 79 '   57 88 85 91 3 69 16   88 65 64 68   1 37 10 99 3   17 64 68 79 55 22 45 84   4 34 53 45 ,   72 84 20 63 71 58 5 96   86 93 64 30   13 69   56 78 57 99 4 64   42 63 71   40 91   80 47   57 69 90 90 73 62 13 60 97 ,   82 0 63 26 11 21 ,   6 5 97   47 37 6 77 35 21 .   94 83 62 76 68 50 86 12 ,   63 5   0 93 78   48 53 42 35 14   19 6 5 21 ,   67 55 57 76 94 11 82   33 43   40 59 17 20 60 30 27 85 39 50 85 29   30 41 34 47 87 77 27 47   84 80 32 83   83 51 62 3 12 17 52 54 33 24 ,   67 50 3 60 71 70 90 16 82 ,   31 22 4   31 57 57 44 79 47   57 55 51 52 14 63 84 79   1 88   17 77 88 86 73 57 1   21 25 52 34   67 14 48 30   57 12 2 27 26   0 19 14 64 34 0 98 .   13 55 96 83 95 42 11 14 ,   39 42 64 12   37 60 84 17   59 34 99 51 86 72 99 24   1 14 87 82 13 ,   62 8 30 17 16 12   66 58 91 42   84 60 29 34 16   3 10 96 76 90 6 53 40 8 51 94   84 54 32 78   96 21 17 26 ,   25 43 97   17 26 60 65 73 43 95   99 4 60 51 91 80 52 12   39 37 11 67 1   55 26   97 6 0 6   16 64 34 32 89 96 73 .   70 47   4 99 29 58 1 45 90   0 77 89 24 47 7 88 26 30 6 95 50 88 43   96 26 33 66 79 ,   8 77 29 6 85 54 28 45 86 58 55 85 92   30 87 47 0   17 3 54 63 68 99 52 80 28 78   56 70 91 72   17 3 40 65 89 57 12   34 24 56   79 60 57 76 3 99 53 12   52 8   17 3 48 39 44 57 13   2 8 86 37   62 76 82 1 63 30 11 26 82   25 5 56   95 36 41 80 26   63 66 22   8 17 11 14 31 95 80 69 24 47 ."

# Perform frequency analysis attack
decrypted_text = frequency_analysis_attack(ciphertext)
print(f"Decrypted Text: {decrypted_text}")
