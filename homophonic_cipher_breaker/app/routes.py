# app/routes.py
from flask import Blueprint, request, render_template, jsonify
from .cipher_breaker import load_dataset, initial_key_setup, hill_climb

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/process_cipher', methods=['POST'])
def process_cipher():
    dataset_path = request.form.get('dataset')
    ciphertext = load_dataset(dataset_path)

    key_map = initial_key_setup(ciphertext)
    best_key, best_score = hill_climb(ciphertext, key_map)

    return jsonify({
        'key_mapping': best_key,
        'score': best_score,
        'plaintext': apply_key(ciphertext, best_key)
    })

def apply_key(ciphertext, key_map):
    plaintext = ''.join([key_map.get(char, char) for char in ciphertext])
    return plaintext
