import re
import json

def parse_text_to_json(input_file, output_file, encoding='utf-8'):
    with open(input_file, 'r', encoding=encoding) as file:
        text = file.read()

    entries = re.split(r'\n(?=\w+ - )', text.strip())

    data = []
    for entry in entries:
        term, explanation = entry.split(' - ', 1)
        term = term.strip()
        
        explanations = [e.strip() for e in re.split(r'\s(?=a\)|b\))', explanation)]

        data.append({
            "term": term,
            "explanations": explanations
        })

    # Create JSON structure
    json_data = json.dumps(data, indent=2)

    # Save to a file
    with open(output_file, 'w', encoding=encoding) as json_file:
        json_file.write(json_data)


# Example usage
if __name__ == "__main__":
    input_file = "cs_glossary\cs_glossary.txt"  # Change this to the path of your input file
    output_file = "cs_glossary\output.json"  # Change this to the desired output file name

    parse_text_to_json(input_file, output_file)
    print(f"Output saved to {output_file}")



