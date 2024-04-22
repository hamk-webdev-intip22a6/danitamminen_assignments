import json
import os

def load_dictionary(file_name, default_dictionary):
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return default_dictionary

def save_dictionary(dictionary, file_name):
    try:
        with open(file_name, 'w') as file:
            json.dump(dictionary, file, indent=4)
    except IOError:
        print("Error: Unable to save the dictionary.")

def search_word(dictionary, word):
    if word in dictionary:
        print(f"Translation: {dictionary[word]}")
    else:
        print("Word not found. Please input a definition.")
        definition = input("Definition: ")
        dictionary[word] = definition
        print("Word added to dictionary.")

def main():
    dictionary_file = "C:\\Users\\danit\\Downloads\\Web-ohjelmointi\\Web-ohjelmointi\\Python dictionary and JSON\\dictionary.json"
    default_dictionary = {
        "koira": "dog",
        "kissa": "cat",
        "maito": "milk",
        "kahvi": "coffee",
        "suklaa": "chocolate"
    }

    if os.path.exists(dictionary_file):
        dictionary = load_dictionary(dictionary_file, default_dictionary)
    else:
        dictionary = default_dictionary

    try:
        while True:
            word = input("Enter a word to translate (or press Enter to exit): ")
            if not word:
                break
            search_word(dictionary, word)
    finally:
        save_dictionary(dictionary, dictionary_file)

if __name__ == "__main__":
    main()