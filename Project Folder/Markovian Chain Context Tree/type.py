import random
import string
import tkinter as tk
from tkinter import filedialog

def preprocess_text(file_path):
    with open(file_path, 'r') as file:
        text = file.read().lower()
        text = text.translate(str.maketrans('', '', string.punctuation))
        words = text.split()
    return words

def create_sequence_prediction_model(words):
    model = {}
    for i in range(len(words) - 1):
        current_word = words[i]
        next_word = words[i + 1]
        if current_word in model:
            model[current_word].append(next_word)
        else:
            model[current_word] = [next_word]
    return model

def generate_prediction(model, input_word):
    if input_word in model:
        next_words = model[input_word]
        prediction = random.choice(next_words)
    else:
        prediction = random.choice(list(model.keys()))  # Random word as fallback
    return prediction

file_path = filedialog.askopenfilename()

if file_path:
    words = preprocess_text(file_path)
    model = create_sequence_prediction_model(words)

    curr_word = 'hello'
    words = [curr_word]
    for x in range(50):
        curr_word = generate_prediction(model, curr_word)
        words.append(curr_word)

    print(' '.join(words))
else:
    print("No file selected.")