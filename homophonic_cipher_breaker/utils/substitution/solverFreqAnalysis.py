from collections import Counter
import string


english_frequency_order = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

def frequency_analysis(ciphertext):
    """Performs frequency analysis on the ciphertext and tries to guess the substitution."""
    
    letter_counts = Counter(ciphertext)
    
    
    letter_counts = {k: v for k, v in letter_counts.items() if k in string.ascii_uppercase}
    sorted_counts = sorted(letter_counts.items(), key=lambda item: item[1], reverse=True)
    
    
    cipher_to_plain = {}
    for i, (cipher_letter, _) in enumerate(sorted_counts):
        if i < len(english_frequency_order):
            cipher_to_plain[cipher_letter] = english_frequency_order[i]
    
    return cipher_to_plain

def decrypt_with_guess(ciphertext, cipher_to_plain):
    """Decrypts the ciphertext using the guessed letter mappings."""
    decrypted_text = ''.join(cipher_to_plain.get(char, char) for char in ciphertext)
    return decrypted_text


ciphertext = "JRGR TXYNRUC RKJ QBUZXYGC RXB BQQBKGYRI RQTBUGQ FO QROBLZRXJYKL QBKQYGYNB YKOFXDRGYFK OXFD ZKRZGVFXYWBJ RUUBQQ, DYQZQB, FX SXBRUVBQ. JRGR TXYNRUC BKQZXBQ YKJYNYJZRIQ' UFKGXFI FNBX GVBYX TBXQFKRI JRGR, RIIFMYKL GVBD GF JBUYJB VFM YG YQ UFIIBUGBJ, QGFXBJ, RKJ QVRXBJ. QBUZXYGC, FK GVB FGVBX VRKJ, OFUZQBQ FK YDTIBDBKGYKL DBRQZXBQ IYPB BKUXCTGYFK, OYXBMRIIQ, RKJ RUUBQQ UFKGXFIQ GF TXFGBUG JRGR OXFD UCSBX GVXBRGQ. GFLBGVBX, GVBC VBIT DRYKGRYK GXZQG, UFDTIC MYGV IBLRI XBLZIRGYFKQ IYPB LJTX, RKJ TXBNBKG YJBKGYGC GVBOG FX JRGR IBRPRLB. RQ JYLYGRI GXRKQOFXDRGYFK LXFMQ, FXLRKYWRGYFKQ DZQG TXYFXYGYWB JRGR TXYNRUC RKJ QBUZXYGC GF TXFGBUG SFGV UZQGFDBXQ RKJ GVBYX FMK FTBXRGYFKQ."



