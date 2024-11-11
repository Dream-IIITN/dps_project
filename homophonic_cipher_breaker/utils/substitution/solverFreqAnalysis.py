from collections import Counter
import string

# Frequency of letters in English text (in order from most to least common)
english_frequency_order = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

def frequency_analysis(ciphertext):
    """Performs frequency analysis on the ciphertext and tries to guess the substitution."""
    # Count the frequency of each letter in the ciphertext
    letter_counts = Counter(ciphertext)
    
    # Remove non-alphabet characters and sort by frequency
    letter_counts = {k: v for k, v in letter_counts.items() if k in string.ascii_uppercase}
    sorted_counts = sorted(letter_counts.items(), key=lambda item: item[1], reverse=True)
    
    # Map the most frequent letters in the ciphertext to the most common English letters
    cipher_to_plain = {}
    for i, (cipher_letter, _) in enumerate(sorted_counts):
        if i < len(english_frequency_order):
            cipher_to_plain[cipher_letter] = english_frequency_order[i]
    
    return cipher_to_plain

def decrypt_with_guess(ciphertext, cipher_to_plain):
    """Decrypts the ciphertext using the guessed letter mappings."""
    decrypted_text = ''.join(cipher_to_plain.get(char, char) for char in ciphertext)
    return decrypted_text

# Example ciphertext (encrypted with a substitution cipher)
ciphertext = "JRGR TXYNRUC RKJ QBUZXYGC RXB BQQBKGYRI RQTBUGQ FO QROBLZRXJYKL QBKQYGYNB YKOFXDRGYFK OXFD ZKRZGVFXYWBJ RUUBQQ, DYQZQB, FX SXBRUVBQ. JRGR TXYNRUC BKQZXBQ YKJYNYJZRIQ' UFKGXFI FNBX GVBYX TBXQFKRI JRGR, RIIFMYKL GVBD GF JBUYJB VFM YG YQ UFIIBUGBJ, QGFXBJ, RKJ QVRXBJ. QBUZXYGC, FK GVB FGVBX VRKJ, OFUZQBQ FK YDTIBDBKGYKL DBRQZXBQ IYPB BKUXCTGYFK, OYXBMRIIQ, RKJ RUUBQQ UFKGXFIQ GF TXFGBUG JRGR OXFD UCSBX GVXBRGQ. GFLBGVBX, GVBC VBIT DRYKGRYK GXZQG, UFDTIC MYGV IBLRI XBLZIRGYFKQ IYPB LJTX, RKJ TXBNBKG YJBKGYGC GVBOG FX JRGR IBRPRLB. RQ JYLYGRI GXRKQOFXDRGYFK LXFMQ, FXLRKYWRGYFKQ DZQG TXYFXYGYWB JRGR TXYNRUC RKJ QBUZXYGC GF TXFGBUG SFGV UZQGFDBXQ RKJ GVBYX FMK FTBXRGYFKQ."

# Perform frequency analysis and generate a guessed decryption mapping
cipher_to_plain = frequency_analysis(ciphertext)
print("Guessed Mapping:", cipher_to_plain)

# Decrypt the ciphertext using the guessed mapping
decrypted_text = decrypt_with_guess(ciphertext, cipher_to_plain)
print("Decrypted Text (with guessed mapping):", decrypted_text)

