import sys
import argparse
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
import time
import os
import json

CONFIG_FILE = 'config.json'

# Create function to load config file
def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    else:
        return {"sites": ["reddit.com", "stackoverflow.com", "medium.com"]}

# Function for saving new site
def save_config(config):
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=4)

def search_with_selenium(driver, query, site, first_search=False):
    # Create URL search with special filter
    search_url = f"https://www.{search_engine}/search?q=site:{site} {query}"

    if first_search:
        # Open URL in first windows
        driver.get(search_url)
    else:
        # Open URL in new tab
        driver.execute_script(f"window.open('{search_url}', '_blank');")

        # Open new tab and search with new queries
        driver.switch_to.window(driver.window_handles[-1])

    time.sleep(2)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Search with Selenium and filter sites.")

    # Argument for query
    parser.add_argument("query", nargs="*", help="Query to search.")

    # Argument for add new sites
    parser.add_argument("-a", "--add-site", type=str, help="Add a site to search.")

    # Argument for delete sites
    parser.add_argument("-D", "--delete", type=str, help='Delete the sites')

    # Argument for change the engine search
    parser.add_argument("-s", "--search-engine", type=str, default="bing.com", help="Set search engine (default: bing.com).")

    # Argument for change the browser
    parser.add_argument("-d", "--default-browser", type=str, choices=["firefox", "chrome"], default="firefox", help="Set default browser (firefox or chrome).")

    args = parser.parse_args()

    # Load the config
    config = load_config()

    # Add sites
    if args.add_site:
        config['sites'].append(args.add_site)
        save_config(config)
        print(f'Site {args.add_site} added to the config')

    # Delete sites
    if args.delete:
        if args.delete in config["sites"]:
            config["sites"].remove(args.delete)
            save_config(config)
            print(f'Site {args.delete} remove from the config')

        else:
            print(f'Site {args.delete} not found from the config')
    # Query from command line or users input
    if args.query:
        query = " ".join(args.query)
    else:
        query = input("Masukkan query pencarian: ")

    # Declare default browser
    if args.default_browser == "firefox":
        path = '/usr/local/bin/geckodriver'
        service = FirefoxService(executable_path=path)
        options = FirefoxOptions()
        options.add_argument('--incognito')
        driver = webdriver.Firefox(service=service, options=options)
    elif args.default_browser == "chrome":
        path = '/usr/local/bin/chromedriver'
        service = ChromeService(executable_path=path)
        options = ChromeOptions()
        options.add_argument('--incognito')
        driver = webdriver.Chrome(service=service, options=options)

    # Determine the search engine
    search_engine = args.search_engine

    # First search
    search_with_selenium(driver, query, config["sites"][0], first_search=True)

    # Next search
    for site in config["sites"][1:]:
        search_with_selenium(driver, query, site)

