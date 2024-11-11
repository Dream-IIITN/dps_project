from collections import Counter

# Frequency order for English letters (most to least common)
ENGLISH_FREQ_ORDER = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

def initialize_key(ciphertext):
    """
    Initialize an empty key with all uppercase letters in the ciphertext set to None.
    """
    return {c: None for c in set(ciphertext) if c.isalpha() and c.isupper()}

def apply_key(ciphertext, key):
    """
    Substitute characters in ciphertext based on the current key, leaving symbols unchanged.
    """
    return ''.join(key.get(c, c) if c.isalpha() and c.isupper() else c for c in ciphertext)

def split_words(ciphertext):
    """
    Split the ciphertext into individual words, preserving punctuation.
    """
    return [word.strip(",'.()") for word in ciphertext.split()]

def lock_crib_in_key(crib_word, cipher_word, key):
    """
    Attempt to map a crib word to a ciphertext word. If successful, lock the mappings in the key.
    """
    temp_key = key.copy()  # Make a temporary key to test mapping
    for c_char, crib_char in zip(cipher_word, crib_word):
        if temp_key[c_char] is None:
            temp_key[c_char] = crib_char  # Assign mapping
        elif temp_key[c_char] != crib_char:
            return False, key  # Conflict detected
    return True, temp_key  # No conflict, return the updated key

def fill_key_with_frequency(ciphertext, key):
    """
    Fill in the remaining mappings in the key using frequency analysis, only for unmapped letters.
    """
    # Frequency analysis on remaining unmapped characters in ciphertext
    letter_counts = Counter(c for c in ciphertext if c.isalpha() and c.isupper() and key[c] is None)
    sorted_cipher_letters = [c for c, _ in letter_counts.most_common()]

    # Remaining unused English letters based on frequency order
    unused_english_letters = [c for c in ENGLISH_FREQ_ORDER if c not in key.values()]

    # Map remaining ciphertext letters to remaining English letters
    for cipher_letter, plain_letter in zip(sorted_cipher_letters, unused_english_letters):
        key[cipher_letter] = plain_letter

    return key

def apply_cribs(ciphertext, cribs, key):
    """
    Applies cribs to the ciphertext, locking in mappings for unique matches.
    """
    cipher_words = split_words(ciphertext)
    
    for crib_word in cribs:
        crib_word = crib_word.upper()
        
        # Find all words of the same length as crib_word
        matches = [word for word in cipher_words if len(word) == len(crib_word)]
        
        # Only proceed if there's exactly one match for this crib word's length
        if len(matches) == 1:
            cipher_word = matches[0]
            success, updated_key = lock_crib_in_key(crib_word, cipher_word, key)
            if success:
                key = updated_key  # Lock in the crib mappings
    
    return key

def decrypt_with_cribs_and_frequency(ciphertext, cribs):
    """
    Decrypts the ciphertext by applying cribs first, then using frequency analysis for remaining mappings.
    """
    # Step 1: Initialize an empty key
    key = initialize_key(ciphertext)

    # Step 2: Apply each crib word to lock in mappings in the key
    key = apply_cribs(ciphertext, cribs, key)

    # Step 3: Use frequency analysis to fill in remaining mappings
    key = fill_key_with_frequency(ciphertext, key)

    # Step 4: Decrypt the ciphertext using the final key
    decrypted_text = apply_key(ciphertext, key)
    return decrypted_text, key

# Example usage
ciphertext = "SDJD ACOIDUX DRS PEUZCOJX DCE EPPERJODL DPAEUJP FK PDKENZDCSORN PERPOJOIE ORKFCVDJOFR KCFV ZRDZJMFCOTES DUUEPP, VOPZPE, FC WCEDUMEP. SDJD ACOIDUX ERPZCEP ORSOIOSZDLP' UFRJCFL FIEC JMEOC AECPFRDL SDJD, DLLFBORN JMEV JF SEUOSE MFB OJ OP UFLLEUJES, PJFCES, DRS PMDCES. PEUZCOJX, FR JME FJMEC MDRS, KFUZPEP FR OVALEVERJORN VEDPZCEP LOHE ERUCXAJOFR, KOCEBDLLP, DRS DUUEPP UFRJCFLP JF ACFJEUJ SDJD KCFV UXWEC JMCEDJP. JFNEJMEC, JMEX MELA VDORJDOR JCZPJ, UFVALX BOJM LENDL CENZLDJOFRP LOHE NSAC, DRS ACEIERJ OSERJOJX JMEKJ FC SDJD LEDHDNE. DP SONOJDL JCDRPKFCVDJOFR NCFBP, FCNDROTDJOFRP VZPJ ACOFCOJOTE SDJD ACOIDUX DRS PEUZCOJX JF ACFJEUJ WFJM UZPJFVECP DRS JMEOC FBR FAECDJOFRP ."
cribs = ["the", "and", "data", "organizations","transformation"]

# Decrypt the ciphertext
decrypted_text, key = decrypt_with_cribs_and_frequency(ciphertext, cribs)
print(f"Decrypted Text: {decrypted_text}")
print(f"Key: {key}")
