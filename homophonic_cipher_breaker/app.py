from flask import Flask,render_template,request,jsonify
from cipher_breaker import load_dataset, initial_key_setup, hill_climb,apply_key
from utils.scorer import character_similarity_score
from utils.substitution.solverFreqAnalysis import frequency_analysis,decrypt_with_guess
from utils.substitution.solverCribbing import decrypt_with_cribs_and_frequency
from utils.substitution.solveWithBiTri import decrypt_with_bitri
from utils.homophonic.solverHillClimb import hill_climb_attack
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process_cipher', methods=['POST'])
def process_cipher():
    approach = request.form.get('approach')
    ciphertext = load_dataset("datasets/cipher.txt")
    origionaltext = load_dataset("datasets/origional.txt")
    HomoCipherText = load_dataset("datasets/cipherHomo.txt")
    decipheredText = None
    cribs = None  # Default is None
    
    # Check if cribs were provided when cribbing approach is selected
    if approach == "Frequency analysis + Cribbing on substitution cipher":
        cribs_input = request.form.get('cribs')
        if cribs_input:
            cribs = cribs_input.split(",")  # Convert comma-separated cribs into a list

    if approach == "Frequency analysis on substitution cipher":
        decipheredText, key = decrypt_with_bitri(ciphertext)
    elif approach == "Frequency analysis + Cribbing on substitution cipher":
        if cribs:  # Proceed with cribs if available
            decipheredText, key = decrypt_with_cribs_and_frequency(ciphertext, cribs)
    elif approach == "Hill climbing approach on homophonic substitution cipher":
        decipheredText, key = hill_climb_attack(HomoCipherText)
    elif approach == "Frequency analysis + Bigram/Trigram analysis on substitution cipher":
        key = frequency_analysis(ciphertext)
        decipheredText = decrypt_with_guess(ciphertext, key)

    score = character_similarity_score(origionaltext, decipheredText)
    formatted_key_mapping = {letter: ", ".join(symbols) for letter, symbols in key.items()}

    return render_template('result.html',
                           key_mapping=formatted_key_mapping,
                           cipher_text=ciphertext,
                           decoded_message=decipheredText,
                           score=score)



if __name__=="__main__":
    app.run(debug=True)