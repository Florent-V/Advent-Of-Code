import requests
from bs4 import BeautifulSoup


class ExtractPuzzle:
    BASE_URL = "https://adventofcode.com"

    def __init__(self, aoc_id, year, day):
        self.aoc_id = aoc_id
        self.year = year
        self.day = day
        self.cookies = {'session': aoc_id}

    @property
    def aoc_id(self):
        return self._aoc_id

    @aoc_id.setter
    def aoc_id(self, value):
        self._aoc_id = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        self._year = value

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, value):
        self._day = value

    @property
    def cookies(self):
        return self._cookies

    @cookies.setter
    def cookies(self, value):
        self._cookies = value

    def download_puzzle(self):
        url = f"{self.BASE_URL}/{self._year}/day/{self._day}/input"
        print(f"Téléchargement de l'input depuis {url}...")
        response = requests.get(url, cookies=self._cookies)
        if response.status_code != 200:
            print(f"Erreur lors de la requête : {response.status_code}")
            raise Exception("Erreur lors de la requête")
        return response.text

    def download_puzzle_light(self):
        url = f"{self.BASE_URL}/{self._year}/day/{self._day}"
        page = requests.get(url)
        if page.status_code != 200:
            print(f"Erreur lors de la requête : {page.status_code}")
            raise Exception("Erreur lors de la requête")
        soup = BeautifulSoup(page.content, 'html.parser')
        return soup.pre.string
