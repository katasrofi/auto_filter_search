import sys
import argparse
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from func import save_config, load_config, search_with_selenium
import time
import os

# Path to absolute dir
scrip_dir = os.path.dirname(os.path.abspath(__file__))

# Join the path to Config File
CONFIG_FILE = os.path.join(scrip_dir,
                           'config',
                           'config.json')

# VPN Extensions
vpn_extension = os.path.join(scrip_dir,
                             'extensions',
                             'uvpn_unlimited_vpn-7.1.6.xpi')

# Declare the app
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Search with Selenium and filter sites.")

    # Argument for query
    parser.add_argument("query",
                        nargs="*",
                        help="Query to search.")

    # Argument for add new sites
    parser.add_argument("-a", "--add-site",
                        type=str,
                        help="Add a site to search.")

    # Argument for delete sites
    parser.add_argument("-D", "--delete",
                        type=str,
                        help='Delete the sites')

    # Argument for change the engine search
    parser.add_argument("-s", "--search-engine",
                        type=str,
                        default="bing.com",
                        help="Set search engine (default: bing.com).")

    # Argument for change the browser
    parser.add_argument("-d", "--default-browser",
                        type=str,
                        choices=["firefox", "chrome"],
                        default="firefox",
                        help="Set default browser (firefox or chrome).")

    args = parser.parse_args()

    # Load the config
    config = load_config(CONFIG_FILE)

    # Add sites
    if args.add_site:
        # Append the new site
        config['sites'].append(args.add_site)

        # Save to config file
        save_config(CONFIG_FILE, config)

        # Print Add new site is success
        print(f'Site {args.add_site} added to the config')

    # Delete sites
    if args.delete:
        # Delete site from config file
        if args.delete in config["sites"]:
            config["sites"].remove(args.delete)

            # Save the changes
            save_config(CONFIG_FILE, config)

            # Print the deletes is success
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
        # Path to GeckoDriver
        path = '/usr/local/bin/geckodriver'

        # Path to Profile
        profile_path = "~/.mozilla/firefox/*.default"

        # Declare the Service and Options
        service = FirefoxService(executable_path=path)
        options = FirefoxOptions()

        # Set the argument
        options.set_preference("profile",
                               profile_path)
        options.add_argument('--incognito')

        # Execute the driver
        driver = webdriver.Firefox(service=service,
                                   options=options)
    elif args.default_browser == "chrome":
        # Path to ChromeDriver
        path = '/usr/local/bin/chromedriver'

        # Declare the Service and Options
        service = ChromeService(executable_path=path)
        options = ChromeOptions()

        # Set The argument
        options.add_argument('--incognito')

        # Execute the driver
        driver = webdriver.Chrome(service=service,
                                  options=options)

    # Determine the search engine
    search_engine = args.search_engine

    # First search
    search_with_selenium(driver,
                         query,
                         config["sites"][0],
                         first_search=True,
                         SearchEngine=search_engine,
                         VpnExtension=vpn_extension)

    # Next search
    for site in config["sites"][1:]:
        search_with_selenium(driver,
                             query,
                             site,
                             SearchEngine=search_engine)
