# Filter Search

This tool make by python and use to filter the search with terminal because too many ads and unnecessary for research eficiently

## Installation
Install the selenium library
'pip install selenium'


Download the driver, if you use firefox download the [geckodriver](https://github.com/mozilla/geckodriver/releases) and if you use chrome you can download [chromdriver](https://getwebdriver.com/chromedriver#stable)

After download the driver, move the driver into folder you want, in my case I put the driver in /usr/local/bin

`
cp -v ~/Downloads/geckodriver /usr/local/bin # if you use firefox
cp -v ~/Downloads/chromdriver /usr/local/bin # if you use chrome
`

After that give access to driver

`
cd /usr/local/bin
chmod +x geckodriver # firefox
chmod +x chromdriver # chrome
`

Edit the .bashrc or .zshrc
`
alias s="python /path/to/search.py"
`

save and source .bashrc or .zshrc
