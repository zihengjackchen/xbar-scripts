#!/usr/bin/env python3

# <xbar.title>Daily Words</xbar.title>
# <xbar.version>v1.1.0</xbar.version>
# <xbar.author>zihengjackchen</xbar.author>
# <xbar.author.github>zihengjackchen</xbar.author.github>
# <xbar.desc>Learn new words in your menu bar!</xbar.desc>
# <xbar.dependencies>python3</xbar.dependencies>
# <xbar.image>https://raw.githubusercontent.com/zihengjackchen/xbar-scripts/main/daily_words/demo.png</xbar.image>
# <xbar.abouturl>https://github.com/zihengjackchen/xbar-scripts/blob/main/daily_words/README.md</xbar.abouturl>
# <xbar.var>string(API_KEY): Your wordnik API key. Neeed for GRE, Vocab Builder, random.</xbar.var>
# <xbar.var>select(VAR_CATEGORY="CS Glossary"): Which category you want to display [CS Glossary, CS Wiki, GRE, Vocab Builder, random]</xbar.var>
# <xbar.var>number(PRINT_LENGTH=50): Number of characters to print each line.</xbar.var>


import requests
import os
import random

# Make sure to change these variables in the xbar plugin browser before using this script
API_KEY = os.environ.get('USERNAME')
VAR_CATEGORY = os.environ.get('VAR_CATEGORY')
PRINT_LENGTH = int(os.environ.get('PRINT_LENGTH', 50))

# Or change them manually if script is used alone
# API_KEY = ""
# VAR_CATEGORY = ""

category_to_asset_url = {
  "CS Glossary": "https://raw.githubusercontent.com/zihengjackchen/xbar-scripts/main/daily_words/assets/cs_glossary/cs_glossary.json",
  "CS Wiki": "https://raw.githubusercontent.com/zihengjackchen/xbar-scripts/main/daily_words/assets/cs_wiki/cs_wiki.json",
  "GRE": "https://raw.githubusercontent.com/zihengjackchen/xbar-scripts/main/daily_words/assets/magoosh_gre/magoosh.json",
  "Vocab Builder": "https://raw.githubusercontent.com/zihengjackchen/xbar-scripts/main/daily_words/assets/vocab_builder/vocab_builder.json",
  "random": ""
}

asset_url = category_to_asset_url[VAR_CATEGORY]

def format_long_string(input_string, line_length):
    words = input_string.split()
    lines = []
    current_line = ""

    for word in words:
        if len(current_line) + len(word) <= line_length:
            current_line += word + " "
        else:
            lines.append(current_line.strip())
            current_line = word + " "

    # Add the last line
    lines.append(current_line.strip())

    # Print the formatted lines
    for line in lines:
        print(line)
  

if VAR_CATEGORY in ["CS Glossary", "CS Wiki"]:
  data_dict = {}
  try:
    # Download JSON file from the URL
    response = requests.get(asset_url)
    response.raise_for_status()  # Check for errors

    # Parse JSON into a dictionary
    data_dict = response.json()

  except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
    exit()
  
  chosen_entry = random.choice(data_dict)
  print(chosen_entry["term"])
  print("---")

  for exp in chosen_entry["explanations"]:
    format_long_string(exp, PRINT_LENGTH)
    print("---")
  
  exit()



# Setting up for API call
elif VAR_CATEGORY in ["GRE", "Vocab Builder", "random"]:
  if not API_KEY:
    print("⚠️ API_KEY NEEDED")
    print("---")
    print("Please fill in the API_KEY or choose another word category")
    exit()
  
  # endpoint = 'https://leetcode.com/graphql/'

  # current_date = datetime.now().date()
  # current_year = current_date.year
  # current_month = current_date.month

  # variables = {"username": "23", "limit": 10, "year": current_year, "month": current_month}

  # # Prepare the request headers and payload
  # headers = {
  #     'Content-Type': 'application/json',
  #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
  # }

  # # Your GraphQL query with variables
  # graphql_query = '''
  # query UserQueries($username: String!, $limit: Int!, $year: Int!, $month: Int!) {
  #   streakCounter {
  #     streakCount
  #   }

  #   activeDailyCodingChallengeQuestion {
  #     date
  #     userStatus
  #     link
  #     question {
  #       acRate
  #       difficulty
  #       frontendQuestionId: questionFrontendId
  #       status
  #       title
  #     }
  #   }

  #   allQuestionsCount {
  #     difficulty
  #     count
  #   }

  #   matchedUser(username: $username) {
  #     submitStats {
  #       acSubmissionNum {
  #         difficulty
  #         count
  #         submissions
  #       }
  #     }
  #   }

  #   userContestRanking(username: $username) {
  #     attendedContestsCount
  #     rating
  #     globalRanking
  #     topPercentage
  #   }

  #   userContestRankingHistory(username: $username) {
  #     trendDirection
  #   }

  #   userStatus {
  #     userId
  #     isPremium
  #     username
  #     checkedInToday
  #   }

  #   recentAcSubmissionList(username: $username, limit: $limit) {
  #     title
  #     titleSlug
  #     timestamp
  #   }

  #   dailyCodingChallengeV2(year: $year, month: $month) {
  #     weeklyChallenges {
  #       date
  #       userStatus
  #       link
  #       question {
  #         acRate
  #         difficulty
  #         frontendQuestionId: questionFrontendId
  #         status
  #         title
  #       }
  #     }
  #   }

  #   isEasterEggCollected

  #   validTimeTravelTicketCount
  #   redeemedTimeTravelTicketCount
  # }
  # '''

  # payload = {'query': graphql_query, 'variables': variables}
  # cookies = {'LEETCODE_SESSION': LEETCODE_SESSION, 'csrftoken': CSRFTOKEN}

  # response = requests.post(endpoint, headers=headers, json=payload, cookies=cookies)
  # response_json = response.json()

  # if response.status_code != 200:
  #   print("⚠️ SERVER ERROR")
  #   print("---")
  #   print(f"Status code: {response.status_code}")
  #   print("---")
  #   print("Leetcode Status 🔗| href=https://status.leetcode.com/")
  #   print("Leetcode Homepage 🔗| href=https://leetcode.com/")
  #   exit()
  pass