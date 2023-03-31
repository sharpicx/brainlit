```
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█ ▄▄▀█ ▄▄▀█ ▄▄▀██▄██ ▄▄▀█ ███▄██▄ ▄
█ ▄▄▀█ ▀▀▄█ ▀▀ ██ ▄█ ██ █ ███ ▄██ █
█▄▄▄▄█▄█▄▄█▄██▄█▄▄▄█▄██▄█▄▄█▄▄▄██▄█
```
## Prologue
Before i created this tool, I have been thinking of how i could scrape quora answers. I have searched alot of informations in quora international mode to build a sluggish tool for scraping shits. And there was story that someone had reversed quora iOS and fetch its API. And then, he got permanently banned from quora because he published that thing.

Here are some:
* <https://www.quora.com/Why-doesnt-Quora-provide-an-API-1?no_redirect=1>
* <https://www.quora.com/Does-a-Quora-API-exist-for-Python>
* <https://www.quora.com/Is-there-any-proper-documentation-of-Quora-API-for-developer>
* <https://edmondlausposts.quora.com/Quora-Extension-API>

Then, because i have a life to work out, I leave that idea.


__Now, i write a small script to scrape brainly.co.id answers to help me learning and studying my school exams. This tool written for personal-use only.__

## Burpsuite
![img](https://i.postimg.cc/rpmfG1f6/image.png)

When i tried to search some texts in the searchbar, it would record the activities into the burpsuite. Well, i was so attracted because of that.

![img](https://i.postimg.cc/05M2Whzj/image.png)

Then i sent it to the repeater and i saw something cool that looks like deserialization using json formatted. And then, i modified it a little bit weird and had been testing it as well. Well, I was so curious to make an automated script for this at that time. Because i have to pass my exam :)

## GIF
[![asciicast](https://asciinema.org/a/572540.svg)](https://asciinema.org/a/572540)

## Installation
```
~$ apt-get install python-pip3 # Debian
~$ sudo pacman -S python-pip # Arch
~$ git clone https://github.com/sharpicx/brainlit.git
~$ cd brainlit
~/brainlit$ python -m pip install -r requirements.txt
~/brainlit$ python brainlit.py -h
```

## Credits
- <https://github.com/dwisiswant0/go-dork> i have been inspired by this project!
- <https://www.rexegg.com/regex-python.html> 
