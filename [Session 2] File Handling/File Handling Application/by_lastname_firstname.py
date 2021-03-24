"""
A CSV file exists that contains data for women tennis players.
Use this file to display the years the players turned pro and retired.
Output should be in ascending order of last name, then first name.
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

# Multilevel sort by Last Name then First Name
players_by_firstname = sorted(player_list, key=itemgetter("First Name"))
players_by_last_first = sorted(players_by_firstname, key=itemgetter("Last Name"))

# Display result
#pprint(players_by_last_first)
"""
for player in players_by_last_first:
    print(
        f"{player['First Name']} {player['Last Name']}: "
        f"{player['Turned Pro']} - {player['Retired']}"
    )
"""
"""
for player in players_by_last_first:
    # The following works because empty string is treated as false
    if player["Retired"]:
        retired = player["Retired"]
    else:
        retired = "Present"

    print(
        f"{player['First Name']} {player['Last Name']}: "
        f"{player['Turned Pro']} - {retired}"
    )
"""

for player in players_by_last_first:
    retired = player["Retired"]
    if not retired:
        retired = "Present"

    print(
        f"{player['First Name']} {player['Last Name']}: "
        f"{player['Turned Pro']} - {retired}"
    )
