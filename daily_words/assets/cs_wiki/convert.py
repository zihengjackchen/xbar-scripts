from bs4 import BeautifulSoup
import json
import re

def clean_text(text):
    # Remove "\u20xx" patterns
    cleaned_text = re.sub(r'\\u20[0-9]{2}', '', text)
    return cleaned_text.strip()

def parse_html_to_json(html_file_path, json_file_path):
    with open(html_file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    data = []
    glossary_entries = soup.find_all('dt', class_='glossary')

    for entry in glossary_entries:
        a_tag = entry.find('a')
        if a_tag:
            term = a_tag.text.strip()

            explanations = []
            next_tag = entry.find_next_sibling()

            while next_tag and next_tag.name == 'dd' and 'glossary' in next_tag.get('class', []):
                explanation = clean_text(next_tag.text)
                # Remove numbers surrounded by square brackets
                explanation = re.sub(r'\[\d+\]', '', explanation)
                explanations.append(explanation)
                next_tag = next_tag.find_next_sibling()

            data.append({
                "term": term,
                "explanations": explanations
            })

    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=2)

def remove_empty_explanations(json_file_path):
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    # Filter out entries with empty explanations
    filtered_data = [entry for entry in data if entry['explanations']]

    # Save the modified data back to the file
    with open(json_file_path, 'w') as file:
        json.dump(filtered_data, file, indent=2)

# Example usage
html_file_path = r'e:\xbar-scripts\daily_words\cs_wiki\cs_wiki.html'
json_file_path = r'/Users/ziheng/xbar-scripts/daily_words/assets/cs_wiki/cs_wiki.json'
# parse_html_to_json(html_file_path, json_file_path)
remove_empty_explanations(json_file_path)
