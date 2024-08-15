# Filter Search

This tool is made with Python and is used to filter search results in the terminal, reducing ads and irrelevant content, making research more efficient.

## Installation
Install the selenium library

`
pip install selenium
`

Or you can create new environment

`
python3 -m venv search
`

`
source search/bin/activate
`

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
alias s="python /path/to/multi_search.py"
`

save and source .bashrc or .zshrc
For test that open the terminal and type 

`s The query what you want to find`


## Features

| Option | Description |
|--------|-------------|
| `-a`   | Add new sites into config file (permanent)|
| `-s`   | Change the default search engine (temporary)|
| `-d`   | Change default browser (Choice only: `firefox` or `chrome`) (temporary) |
| `-D`   | Delete the sites from config.json (permanent)|

example:

`
s query -a huggingface.com
`

`
s query -s duckduckgo.com
`

`
s query -d chrome
`

`
s query -D huggingface.com
`

