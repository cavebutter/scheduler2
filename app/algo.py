import json
import random
import sqlite3
import datetime


def get_team_names_simple(level: str) -> list:
    conn = sqlite3.connect('little_league.db')
    cursor = conn.cursor()

    query = "SELECT name FROM Teams INNER JOIN Levels on Teams.level_id = Levels.ID where Levels.level = ?"
    cursor.execute(query, (level,))
    team_names = [row[0] for row in cursor.fetchall()]
    conn.close()
    return team_names



def assign_matchups(config_file) -> list:
    # Read and parse the configuration file
    with open(config_file, 'r') as file:
        config = json.load(file)

    matchups = []

    # Iterate over each level in the configuration file
    for level in config['levels']:
        level_name = level['name']
        games_per_season = level['games_per_season']

        # Retrieve the teams for the current level from the database
        teams = get_team_names_simple(level_name)

        # Check if the number of teams is odd
        if len(teams) % 2 != 0:
            # Add a 'Bye' team to indicate an off-week
            teams.append('Bye')

        # Generate matchups for the level
        for i in range(games_per_season):
            # Shuffle the list of teams for random matchups
            random.shuffle(teams)

            # Create matchups by pairing teams from the list
            level_matchups = []
            for j in range(0, len(teams), 2):
                team1 = teams[j]
                team2 = teams[j+1]
                level_matchups.append((team1, team2))

            matchups.append((level_name, level_matchups))

    return matchups


