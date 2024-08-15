# Filter Search

This tool is made with Python and is used to filter search results in the terminal, reducing ads and irrelevant content, making research more efficient.

## Installation
Install the selenium library

`
pip install selenium
`


Download the driver, if you use firefox download the [geckodriver](https://github.com/mozilla/geckodriver/releases) and if you use chrome you can download [chromdriver](https://getwebdriver.com/chromedriver#stable)

After download the driver, move the driver into folder you want, in my case I put the driver in /usr/local/bin

`
cp -v ~/Downloads/geckodriver /usr/local/bin # if you use firefox
`

`
cp -v ~/Downloads/chromdriver /usr/local/bin # if you use chrome
`

After that give access to driver

`
cd /usr/local/bin
`

`
chmod +x geckodriver # firefox
`

`
chmod +x chromdriver # chrome
`

Edit the .bashrc or .zshrc
`
alias s="python /path/to/multi_search_chrome.py" # Chrome
`

`
alias s="python /path/to/multi_search_firefox.py" # Firefox
`

Note: This tools only search in reddit, medium and stackoverflow, if you want add site to search you can add by edit sites = ["reddit.com", "stackoverflow.com", "medium.com", "Add Site you want"] in python file

save and source .bashrc or .zshrc
For test that open the terminal and type 

`s The query what you want to find`
