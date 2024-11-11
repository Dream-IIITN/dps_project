from collections import Counter


ENGLISH_FREQ_ORDER = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

def initialize_key(ciphertext):
    return {c: None for c in set(ciphertext) if c.isalpha() and c.isupper()}

def apply_key(ciphertext, key):
    return ''.join(key.get(c, c) if c.isalpha() and c.isupper() else c for c in ciphertext)

def split_words(ciphertext):
    return [word.strip(",'.()") for word in ciphertext.split()]

def lock_crib_in_key(crib_word, cipher_word, key):
    temp_key = key.copy()  
    for c_char, crib_char in zip(cipher_word, crib_word):
        if temp_key[c_char] is None:
            temp_key[c_char] = crib_char  
        elif temp_key[c_char] != crib_char:
            return False, key  
    return True, temp_key  

def fill_key_with_frequency(ciphertext, key):
    
    letter_counts = Counter(c for c in ciphertext if c.isalpha() and c.isupper() and key[c] is None)
    sorted_cipher_letters = [c for c, _ in letter_counts.most_common()]

    
    unused_english_letters = [c for c in ENGLISH_FREQ_ORDER if c not in key.values()]

    
    for cipher_letter, plain_letter in zip(sorted_cipher_letters, unused_english_letters):
        key[cipher_letter] = plain_letter

    return key

def apply_cribs(ciphertext, cribs, key):
    cipher_words = split_words(ciphertext)
    
    for crib_word in cribs:
        crib_word = crib_word.upper()
        
        
        matches = [word for word in cipher_words if len(word) == len(crib_word)]
        
        
        if len(matches) == 1:
            cipher_word = matches[0]
            success, updated_key = lock_crib_in_key(crib_word, cipher_word, key)
            if success:
                key = updated_key  
    
    return key

def decrypt_with_cribs_and_frequency(ciphertext, cribs):
    
    key = initialize_key(ciphertext)

    
    key = apply_cribs(ciphertext, cribs, key)

    
    key = fill_key_with_frequency(ciphertext, key)

    
    decrypted_text = apply_key(ciphertext, key)
    return decrypted_text, key


ciphertext = "SDJD ACOIDUX DRS PEUZCOJX DCE EPPERJODL DPAEUJP FK PDKENZDCSORN PERPOJOIE ORKFCVDJOFR KCFV ZRDZJMFCOTES DUUEPP, VOPZPE, FC WCEDUMEP. SDJD ACOIDUX ERPZCEP ORSOIOSZDLP' UFRJCFL FIEC JMEOC AECPFRDL SDJD, DLLFBORN JMEV JF SEUOSE MFB OJ OP UFLLEUJES, PJFCES, DRS PMDCES. PEUZCOJX, FR JME FJMEC MDRS, KFUZPEP FR OVALEVERJORN VEDPZCEP LOHE ERUCXAJOFR, KOCEBDLLP, DRS DUUEPP UFRJCFLP JF ACFJEUJ SDJD KCFV UXWEC JMCEDJP. JFNEJMEC, JMEX MELA VDORJDOR JCZPJ, UFVALX BOJM LENDL CENZLDJOFRP LOHE NSAC, DRS ACEIERJ OSERJOJX JMEKJ FC SDJD LEDHDNE. DP SONOJDL JCDRPKFCVDJOFR NCFBP, FCNDROTDJOFRP VZPJ ACOFCOJOTE SDJD ACOIDUX DRS PEUZCOJX JF ACFJEUJ WFJM UZPJFVECP DRS JMEOC FBR FAECDJOFRP ."
cribs = ["the", "and", "data", "organizations","transformation"]
