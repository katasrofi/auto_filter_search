import sys
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time

def search_with_selenium(driver, query, site, first_search=False):
    # Buat URL pencarian dengan filter situs
    search_url = f"https://www.bing.com/search?q=site:{site} {query}"

    if first_search:
        # Buka URL di tab pertama
        driver.get(search_url)
    else:
        # Buka tab baru dengan URL pencarian
        driver.execute_script(f"window.open('{search_url}', '_blank');")

        # Alihkan ke tab baru
        driver.switch_to.window(driver.window_handles[-1])

    time.sleep(2)

if __name__ == "__main__":
    # Ambil query dari argumen command line
    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
    else:
        query = input("Masukkan query pencarian: ")

    # Inisialisasi driver untuk Firefox sekali
    path = '/usr/local/bin/geckodriver'
    service = Service(executable_path=path)
    options = Options()
    options.add_argument('--incognito')

    driver = webdriver.Chrome(service=service, options=options)

    # Daftar situs yang ingin dicari
    sites = ["reddit.com", "stackoverflow.com", "medium.com"]

    # Pencarian pertama
    search_with_selenium(driver, query, sites[0], first_search=True)

    # Pencarian berikutnya
    for site in sites[1:]:
        search_with_selenium(driver, query, site)
