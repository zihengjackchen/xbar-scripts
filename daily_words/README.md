# Daily Words for xbar

![Demo](demo.png)

## Overview

The "Daily Words" xbar script is designed to present a random word or concept, accompanied by an explanation. This script offers convenience by maintaining the visibility of this information on your screen, aiding in focused learning. Additionally, you have the flexibility to explore words from various sources, including the GRE test, vocab builder textbook, CS glossary, or CS wiki. This versatility allows you to tailor your learning experience to different domains and subjects.

## Features
- Random Word Display: The script presents a random word or concept each time it runs, providing variety in your daily learning routine.
- Explanation Included: Each displayed word or concept is accompanied by an explanation, aiding in a quick understanding of the term.
- Information Visibility: By having this educational content always visible on your screen, the script makes it easier for you to stay focused on learning.
- Source Options: Choose words from different sources, including the Magoosh GRE Words, Vocab Builder Textbook, CS Glossary, or CS Wiki. This allows you to tailor your learning experience to various domains and subjects.


## Configuration

Before using the script, make sure to configure the following variables by either:
- Filling them in the xbar plugin browser if it's used with xbar
![xbar-plugin-browser](xbar-plugin-browser.png)
- Or filling them manually if it's used alone 
   ```python
   API_KEY = ""
   VAR_CATEGORY = "CS Glossary"
   PRINT_LENGTH = 50
   ```

## Variables
- `USERNAME`:

## Requirements
- Python 3
- Dependencies: requests

## Installation
1. Make the script executable:
   ```
   chmod +x daily_words.py
   ```
2. Add the script to your xbar plugins directory.


## References
1. [xbar - The BitBar Replacement](https://xbarapp.com/)
2. [CS Glossary](http://marvin.cs.uidaho.edu/Teaching/CS112/terms.pdf)
3. [CS Wiki](https://en.wikipedia.org/wiki/Glossary_of_computer_science)
4. [Magoosh GRE](https://s3.amazonaws.com/magoosh.resources/magoosh-gre-1000-words_oct01.pdf)
5. [Vocabulary Builder](https://quizlet.com/805832637/the-vocabulary-builder-workbook-flash-cards/)


