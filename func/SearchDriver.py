import time

# Make a function to open the browser
def search_with_selenium(driver,
                         query,
                         site,
                         first_search=False,
                         SearchEngine=None,
                         VpnExtension=None):
    # Create URL search with special filter
    search_url = f"https://www.{SearchEngine}/search?q=site:{site} {query}"

    if first_search:
        # Install the vpn
        driver.install_addon(VpnExtension, temporary=True)

        # Close the tab installations
        search_window = driver.current_window_handle
        for handle in driver.window_handles:
            if handle != search_window:
                driver.switch_to.window(handle)
                driver.close()

        # Open URL in first windows
        driver.switch_to.window(search_window)
        driver.get(search_url)
    else:
        # Open URL in new tab
        driver.execute_script(f"window.open('{search_url}', '_blank');")

        # Open new tab and search with new queries
        driver.switch_to.window(driver.window_handles[-1])

    time.sleep(2)
