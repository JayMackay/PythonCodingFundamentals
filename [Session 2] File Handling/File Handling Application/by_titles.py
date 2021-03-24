"""
A CSV file exists that contains data for women tennis players.
Use this file to display the players in ascending order of titles won.
Output should include first name, last name and number of titles.
"""

import csv
from operator import itemgetter
from pprint import pprint

def csv_to_list_of_dicts(csv_file_to_convert):
    list_of_dicts = []
    with open("women_tennis_players.csv") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            list_of_dicts.append(line)
    return list_of_dicts

# Read in CSV file
player_list = csv_to_list_of_dicts("women_tennis_players.csv")

# Convert Titles to integers so sort will work properly
for player in player_list:
    player["Titles"] = int(player["Titles"])

# Sort by Titles
players_by_titles = sorted(player_list, key=itemgetter("Titles"))

# Display result
#pprint(players_by_titles)

for player in players_by_titles:
    #print(f"{player['First Name']} {player['Last Name']}: {player['Titles']} titles")
    # The line above is too long. Can reformat it as:
    print(
        f"{player['First Name']} {player['Last Name']}: "
        f"{player['Titles']} titles"
    )
