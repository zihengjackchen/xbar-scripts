import json

def save_words_to_json(input_file_path, output_json_path):
    with open(input_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    words = [line.split("###")[0].strip() for line in lines if "###" in line]

    with open(output_json_path, 'w', encoding='utf-8') as json_file:
        json.dump(words, json_file, indent=2)


# Example usage
txt_file_path = r'e:\xbar-scripts\daily_words\vocab_builder\vocab_builder.txt'
json_file_path = r'e:\xbar-scripts\daily_words\vocab_builder\vocab_builder.json'
save_words_to_json(txt_file_path, json_file_path)
