import json

def words_to_json(file_path, json_file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        words_list = file.read()

    # Split the words into a list
    words = [word.strip() for word in words_list.strip().split('\n')]

    # Save to JSON file as a list
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(words, json_file, indent=2)

    print(f"Words converted to JSON list and saved to {json_file_path}")


# Example usage
txt_file_path = "words.txt"
json_file_path = "words.json"
txt_file_path = r'e:\xbar-scripts\daily_words\magoosh_gre\magoosh.txt'
json_file_path = r'e:\xbar-scripts\daily_words\magoosh_gre\magoosh.json'
words_to_json(txt_file_path, json_file_path)
