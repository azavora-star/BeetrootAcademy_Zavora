
# Robots.txt
# Download and save to file robots.txt from wikipedia, twitter websites etc. 

import requests

robots = requests.get('https://www.google.com/robots.txt')

with open("robots.txt", mode="w") as file:
    file.write(robots.text)