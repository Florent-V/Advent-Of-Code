import requests

url = "https://adventofcode.com/2023/day/1"
page = requests.get(url,  verify=False)

# Voir le code html source
print(page.content)