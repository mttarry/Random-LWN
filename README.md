# Random-LWN
Maybe I was too lazy to search for it, but I couldn't find a "Random Article" functionality on [LWN.net](https://lwn.net/) like [Wikipedia has](https://en.wikipedia.org/wiki/Wikipedia:Random). Since I like to read at least one technical Linux article article a day, I thought it'd be neat to just grab a random kernel/security article from LWN and have it pasted to my clipboard for easy entry into my browser.

Hence this simple project, which took me ~15 minutes to build.

## Usage
`python3 main.py -c k` for copying a random Kernel article to your clipboard  
`python3 main.py -c s` for copying a random Security article to your clipboard  


## Dependencies
Use `pip3` to install `pyperclip` and `BeautifulSoup`, if you don't already have these installed. In order for pyperclip to work on Linux, you may also need [xclip](https://github.com/astrand/xclip).

`pip3 install pyperclip`  
`pip3 install BeautifulSoup4`

### Credits
Shoutout to [LWN](https://lwn.net/) for consistently producing high-quality, technical Linux content. 



`

