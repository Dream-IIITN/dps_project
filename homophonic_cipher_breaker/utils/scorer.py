def character_similarity_score(original_text, deciphered_text):
    original_text = original_text.lower()
    deciphered_text = deciphered_text.lower()
    length = min(len(original_text), len(deciphered_text))
    
    matches=0
    for i in range(length):
        if original_text[i]==deciphered_text[i]:
            matches=matches+1
            
    score=matches/length*100 if length > 0 else 0
    
    return score

original_text = "Data privacy and security are essential aspects of safeguarding sensitive information from unauthorized access, misuse, or breaches. Data privacy ensures individuals' control over their personal data, allowing them to decide how it is collected, stored, and shared. Security, on the other hand, focuses on implementing measures like encryption, firewalls, and access controls to protect data from cyber threats. Together, they help maintain trust, comply with legal regulations like GDPR, and prevent identity theft or data leakage. As digital transformation grows, organizations must prioritize data privacy and security to protect both customers and their own operations."
deciphered_text = "KAUX  YDNOEWL  MAM  FCASTB0L  GDC  CKKEROBGL  ANYSAYK  YC  JERUVSEXMIAE  JCRKIOBOE  KXCYVJZOIYP  RTYR  SXGHUQPXIILJ  GAAUJJ,  JNKHKA,  WD  IVZXWDAU.  JAUG  YVBOXAL  UADSNZU  IAMHOKMSABU'  AWROVYD  WOLD  UZWKV  YLDUVPMB  JGUM,  FBFZMBAE  GCLJ  OY  JEAKJL  DZM  NO  IK  AYLLKWOGM,  J0ZTZK,  BAM  KZBXSK.  DAWHDHGL,  ZA  0CE  PUDSN  MBAK,  CVAHDZJ  RY  NRYFGJUROHRV  JCGKSXUK  BIBA  AXWVLYTIRH,  CHVGMELDJ,  APJ  AAAEUK  AVXTNZBU  UW  YXWGKAU  KXTG  CNPJ  ALIUT  0MNLG0F.  OVEAYDZN,  ODLL  ZGBY  RGKXGFKH  UNSJO,  WGJYDL  NBOD  BGVGD  VWEHLBUNGXD  BIBE  EKYT,  XYM  YTGOKYY  KJGXOITL  OZZCU  VT  MB0B  DLGBZEK.  EK  JKVBUML  0XZHKRWTJBYHWY  ETRNU,  GXVBRIIMGBVRN  JSK0  YVIZDKTIIE  JEOF  YVNOZAL  GHJ  UGAHVKUL  TG  YVPOEAO  IGGZ  WHJUZJZTJ  XAJ  YWCIT  ZNP  GYZNAYIYHK."


score = character_similarity_score(original_text, deciphered_text)
print(f"Character Similarity Score: {score:.4f}")
