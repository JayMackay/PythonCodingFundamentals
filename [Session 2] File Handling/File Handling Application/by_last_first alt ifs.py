import csv
from operator import itemgetter
from pprint import pprint

def csv_to_list_of_dicts(csv_file_to_convert):
    """Convert a CSV file to a list of dictionaries.
    """

    list_of_dicts = []

    with open(csv_file_to_convert) as csv_file:
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

for player in players_by_last_first:
    # This is called a conditional expression or ternary operator
    retired = player["Retired"] if player["Retired"] else "Present"

    print(
        f"{player['First Name']} {player['Last Name']}: "
        f"{player['Turned Pro']} - {retired}"
    )

for player in players_by_last_first:
    retired =  player["Retired"] or "Present"

    print(
        f"{player['First Name']} {player['Last Name']}: "
        f"{player['Turned Pro']} - {retired}"
    )
