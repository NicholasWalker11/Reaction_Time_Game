import json
import os

# Leaderboard
reaction_times_list = []
MAX_LEADERBOARD_ENTRIES = 10
LEADERBOARD_FILE = 'leaderboard.json'


def save_leaderboard(): # Save the leaderboard to a JSON file
    try:
        with open(LEADERBOARD_FILE, 'w') as f:
            json.dump(reaction_times_list, f)
    except Exception as e:
        print(f"Error saving leaderboard: {e}")


def load_leaderboard(): # Load the leaderboard from a JSON file
    global reaction_times_list
    try:
        if os.path.exists(LEADERBOARD_FILE):
            with open(LEADERBOARD_FILE, 'r') as f:
                reaction_times_list = json.load(f)
                return reaction_times_list
    except Exception as e:
        print(f"Error loading leaderboard: {e}")
        reaction_times_list = []
    return reaction_times_list
