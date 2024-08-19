import json
import os

# Create function to load config file
def load_config(CONFIG_FILE):
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    else:
        return {"sites": ["reddit.com", "stackoverflow.com", "medium.com"]}

# Function for saving new site
def save_config(CONFIG_FILE, config):
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=4)
