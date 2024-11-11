from flask import Flask,render_template,request,jsonify
from cipher_breaker import load_dataset, initial_key_setup, hill_climb,apply_key
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process_cipher', methods=['POST'])
def process_cipher():
    dataset_path = request.form.get('dataset')
    ciphertext = load_dataset(dataset_path)

    key_map = initial_key_setup(ciphertext)
    best_key, best_score = hill_climb(ciphertext, key_map)
    plaintext = apply_key(ciphertext, best_key)

    formatted_key_mapping = {letter: ", ".join(symbols) for letter, symbols in best_key.items()}

    return render_template('result.html', 
                           key_mapping=formatted_key_mapping,
                           cipher_text=ciphertext,
                           decoded_message=plaintext,
                           score=best_score)


if __name__=="__main__":
    app.run(debug=True)