#!/usr/bin/env python3

# <xbar.title>Daily Words</xbar.title>
# <xbar.version>v1.1.0</xbar.version>
# <xbar.author>zihengjackchen</xbar.author>
# <xbar.author.github>zihengjackchen</xbar.author.github>
# <xbar.desc>Learn new words in your menu bar!</xbar.desc>
# <xbar.dependencies>python3</xbar.dependencies>
# <xbar.image>https://raw.githubusercontent.com/zihengjackchen/xbar-scripts/main/leetcode_reminder/demo.png</xbar.image>
# <xbar.abouturl>https://github.com/zihengjackchen/xbar-scripts/blob/main/leetcode_reminder/README.md</xbar.abouturl>
# <xbar.var>string(API_KEY): Your wordnik API key. Neeed for GRE, Vocab Builder, random.</xbar.var>
# <xbar.var>select(VAR_CATEGORY="random"): Which category you want to display [CS Glossary, CS Wiki, GRE, Vocab Builder, random]</xbar.var>
# <xbar.var>number(PRINT_LENGTH=20): Number of characters to print each line.</xbar.var>


import requests
from datetime import datetime
import os
import random

# Make sure to change these variables in the xbar plugin browser before using this script
API_KEY = os.environ.get('USERNAME')
VAR_CATEGORY = os.environ.get('VAR_CATEGORY')
PRINT_LENGTH = os.environ.get('PRINT_LENGTH')

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

if not (API_KEY and VAR_CATEGORY in ["GRE", "Vocab Builder", "random"]):
  print("⚠️ API_KEY NEEDED")
  print("---")
  print("Please fill in the API_KEY or choose another word category")
  exit()

def format_long_string(input_string, line_length=20):
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

    # Print lines with dashes if a word is broken
    for line in lines:
        print(line)
  
# Setting up for API call
if VAR_CATEGORY in ["GRE", "Vocab Builder", "random"]:
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

elif VAR_CATEGORY in ["CS Glossary", "CS Wiki"]:
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

  for exp in chosen_entry["explanations"]:
    format_long_string(exp, PRINT_LENGTH)
    print("---")
  
  exit()






# if "errors" in response_json:
#   print("⚠️ USERNAME ERROR")
#   print("---")
#   print(f"Check your input username")
#   print("---")
#   print("Leetcode Status 🔗| href=https://status.leetcode.com/")
#   print("Leetcode Homepage 🔗| href=https://leetcode.com/")
#   exit()

# if not response_json['data']['userStatus']['userId']:
#   print("⚠️ TOKEN ERROR")
#   print("---")
#   print(f"Check your input tokens")
#   print("---")
#   print("Leetcode Status 🔗| href=https://status.leetcode.com/")
#   print("Leetcode Homepage 🔗| href=https://leetcode.com/")
#   exit()

# try:
#   # Another API call to get leet coin count
#   leet_coin_url = "https://leetcode.com/points/api/total/"
#   leet_coin_response = requests.get(leet_coin_url, headers=headers, json=payload, cookies=cookies)

#   leet_coin = "ERROR"
#   if leet_coin_response.status_code == 200:
#       leet_coin = leet_coin_response.json()['points']

# except:
#   print("⚠️ ERROR GETTING LEETCOIN")
#   print("---")
#   print("Check your input variables")
#   print("---")
#   print("Leetcode Status 🔗| href=https://status.leetcode.com/")
#   print("Leetcode Homepage 🔗| href=https://leetcode.com/")
#   exit()

# try:
#   # Parsing
#   limit_tickets = 3 - response_json['data']["validTimeTravelTicketCount"] + response_json['data']["redeemedTimeTravelTicketCount"]
#   usable_tickets = min(limit_tickets, leet_coin // 70)

#   is_premium = response_json["data"]["userStatus"]["isPremium"]
#   lc_username = response_json["data"]["userStatus"]["username"]
#   checked_in = response_json["data"]["userStatus"]["checkedInToday"]
#   easter_egg_collected = response_json["data"]["isEasterEggCollected"]

#   title = response_json["data"]["activeDailyCodingChallengeQuestion"]["question"]["title"]
#   question_id = response_json["data"]["activeDailyCodingChallengeQuestion"]["question"]["frontendQuestionId"]
#   user_status_daily = response_json["data"]["activeDailyCodingChallengeQuestion"]["userStatus"]
#   if user_status_daily == "NotStart":
#     user_status_daily_str = "Incomplete 😨"
#   elif user_status_daily == "Finish":
#     user_status_daily_str = "Completed 🥳"
#   link = response_json["data"]["activeDailyCodingChallengeQuestion"]["link"]
#   difficulty = response_json["data"]["activeDailyCodingChallengeQuestion"]["question"]["difficulty"]
#   ac_rate = response_json["data"]["activeDailyCodingChallengeQuestion"]["question"]["acRate"]
#   difficulty_color = color_easy
#   if difficulty == "Hard":
#     difficulty_color = color_hard
#   elif difficulty == "Medium":
#     difficulty_color = color_medium

#   user_status_weekly = response_json["data"]["dailyCodingChallengeV2"]["weeklyChallenges"][-1]["userStatus"]
#   link_weekly = response_json["data"]["dailyCodingChallengeV2"]["weeklyChallenges"][-1]["link"]
#   title_weekly = response_json["data"]["dailyCodingChallengeV2"]["weeklyChallenges"][-1]["question"]["title"]
#   question_id_weekly = response_json["data"]["dailyCodingChallengeV2"]["weeklyChallenges"][-1]["question"]["frontendQuestionId"]
#   if user_status_weekly == "NotStart":
#     user_status_weekly_str = "Incomplete 😨"
#   elif user_status_weekly == "Finish":
#     user_status_weekly_str = "Completed 🥳"
#   difficulty_weekly = response_json["data"]["dailyCodingChallengeV2"]["weeklyChallenges"][-1]["question"]["difficulty"]
#   ac_rate_weekly = response_json["data"]["dailyCodingChallengeV2"]["weeklyChallenges"][-1]["question"]["acRate"]
#   difficulty_color_weekly = color_easy
#   if difficulty_weekly == "Hard":
#     difficulty_color_weekly = color_hard
#   elif difficulty_weekly == "Medium":
#     difficulty_color_weekly = color_medium

#   recent_subs = [(sub["title"], sub["titleSlug"]) for sub in response_json["data"]["recentAcSubmissionList"]]

#   streak_days = response_json["data"]["streakCounter"]["streakCount"]

#   all_solved_count = sum(item["count"] for item in response_json["data"]["allQuestionsCount"] if item["difficulty"] in ["Easy", "Medium", "Hard"])
#   easy_count = next(item["count"] for item in response_json["data"]["allQuestionsCount"] if item["difficulty"] == "Easy")
#   medium_count = next(item["count"] for item in response_json["data"]["allQuestionsCount"] if item["difficulty"] == "Medium")
#   hard_count = next(item["count"] for item in response_json["data"]["allQuestionsCount"] if item["difficulty"] == "Hard")

#   user_all_solved_count = sum(item["count"] for item in response_json["data"]["matchedUser"]["submitStats"]["acSubmissionNum"] if item["difficulty"] in ["Easy", "Medium", "Hard"] )
#   user_easy_count = next(item["count"] for item in response_json["data"]["matchedUser"]["submitStats"]["acSubmissionNum"] if item["difficulty"] == "Easy")
#   user_median_count = next(item["count"] for item in response_json["data"]["matchedUser"]["submitStats"]["acSubmissionNum"] if item["difficulty"] == "Medium")
#   user_hard_count = next(item["count"] for item in response_json["data"]["matchedUser"]["submitStats"]["acSubmissionNum"] if item["difficulty"] == "Hard")

#   # Do not parse for contest info if no contest attended
#   has_contest = "userContestRanking" in response_json["data"] and response_json["data"]["userContestRanking"] and "attendedContestsCount" in response_json["data"]["userContestRanking"]
#   if has_contest:
#     contest_count = response_json["data"]["userContestRanking"]["attendedContestsCount"]
#     contest_rating = response_json["data"]["userContestRanking"]["rating"]
#     contest_ranking = response_json["data"]["userContestRanking"]["globalRanking"]
#     contest_percentage = response_json["data"]["userContestRanking"]["topPercentage"]
#     contest_trend = response_json["data"]["userContestRankingHistory"][-1]["trendDirection"]

#     if contest_trend == "UP":
#       contest_trend = '↗️'
#     elif contest_trend == "DOWN":
#       contest_trend = '↘️'
#     else:
#       contest_trend = '➡️'

#   # Printing the UI
#   if user_status_daily == "Finish":
#     print(user_status_daily_str)
#   else:
#     print(f"{countdown + countdown_color}")
#     print(f"{countdown_alt + countdown_color}")
#   print("---")

#   if is_premium:
#     print(f"{lc_username} 🔗|href=https://leetcode.com/{USERNAME} | color={color_premium} ")
#   else:
#     print(f"{lc_username} 🔗|href=https://leetcode.com/{USERNAME}")

#   print(f"--LeetCoin: {leet_coin}")
#   if checked_in:
#     print(f"--Daily Check-In (Completed)")
#   else:
#     print(f"--Daily Check-In 🔗| href=https://leetcode.com{link}")

#   if easter_egg_collected:
#     print(f"--Collect Easter Egg (Completed)")
#   else:
#     print(f"--Collect Easter Egg 🔗| href=https://leetcode.com/contest")


#   print("---")
#   print(f"Daily Challenge 🔗| href=https://leetcode.com{link}")
#   print(f"--{question_id}. {title} | color={difficulty_color} ")
#   print(f"--Difficulty: {difficulty} ({ac_rate:.2f}% Accepted)| color={difficulty_color}")
#   print("-----")
#   print(f"--Status: {user_status_daily_str}")
#   print(f"--Countdown: {countdown_full + countdown_color}")
#   print(f"--Streak: {streak_days}")
#   print(f"--Usable Time Travel Tickets: {usable_tickets}")

#   # Do not show weekly problem if not premium
#   if is_premium:
#     print(f"Weekly Challenge 🔗| href=https://leetcode.com{link_weekly}")
#     print(f"--{question_id_weekly}. {title_weekly} | color={difficulty_color_weekly}")
#     print(f"--Difficulty: {difficulty_weekly} ({ac_rate_weekly:.2f}% Accepted) | color={difficulty_color_weekly}")
#     print("-----")
#     print(f"--Status: {user_status_weekly_str}")

#   print("---")
#   print(f"Progress")
#   print(f"--Easy: {user_easy_count}/{easy_count} | color={color_easy}")
#   print(f"--Medium: {user_median_count}/{medium_count} | color={color_medium}")
#   print(f"--Hard: {user_hard_count}/{hard_count} | color={color_hard}")
#   print("-----")
#   print(f"--All: {user_all_solved_count}/{all_solved_count}")

#   # Do not show contest if no contest attended
#   if has_contest:
#     print("Contest 🔗| href=https://leetcode.com/contest")
#     print(f"--Rating: {int(contest_rating)} {contest_trend}")
#     print(f"--Ranking: {contest_ranking}")
#     print(f"--Top {contest_percentage}%")
#     print(f"--Attended: {contest_count}")

#   print("Recent Submissions")
#   for sub, sub_slug in recent_subs:
#     print(f"--{sub} 🔗| href=https://leetcode.com/problems/{sub_slug}")

#   print("---")
#   print("Leetcode Homepage 🔗| href=https://leetcode.com/")

# except:
#   print("⚠️ PARSING ERROR")
#   print("---")
#   print("Check your input variables")
#   print("---")
#   print("Leetcode Status 🔗| href=https://status.leetcode.com/")
#   print("Leetcode Homepage 🔗| href=https://leetcode.com/")
#   exit()