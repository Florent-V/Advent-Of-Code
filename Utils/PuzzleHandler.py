import requests, os
from bs4 import BeautifulSoup
from datetime import datetime


class PuzzleHandler:
    BASE_URL = "https://adventofcode.com"

    def __init__(self, year, day):
        self.year = year
        self.day = day
        self.aoc_id = self.get_session_id()
        self.puzzle = None
        self.puzzle_light = None

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
    
    def get_session_id(self):
      session_id = os.getenv("AOC_ID")
      if not session_id:
          raise ValueError("La variable d'environnement AOC_ID n'est pas définie \n")
      return session_id
    
    def check_availability(self):
        date = datetime(year=self.year, month=12, day=self.day)
        if date > datetime.now():
            raise ValueError(f"Puzzle for Day {self.day} of {self.year} is not available yet.")
        
    def download(self):
        self.check_availability()
        self.puzzle = self.download_puzzle()
        self.puzzle_light = self.download_puzzle_light()
        return self.puzzle, self.puzzle_light

    def download_puzzle(self):
        url = f"{self.BASE_URL}/{self._year}/day/{self._day}/input"
        print(f"Download input from {url}...")
        # response = requests.get(url, cookies={ 'session': self.aoc_id })
        # Comment the previous line and uncomment the next one if you have SSL error
        response = requests.get(url, cookies={ 'session': self.aoc_id }, verify=False)
        if response.status_code != 200:
            print(f"Request error. Error code : {response.status_code}")
            raise Exception("Request error")
        return response.text

    def download_puzzle_light(self):
        url = f"{self.BASE_URL}/{self._year}/day/{self._day}"
        print(f"Download input_light from {url}...")
        # page = requests.get(url)
        # Comment the previous line and uncomment the next one if you have SSL error
        page = requests.get(url, verify=False)
        if page.status_code != 200:
            print(f"Request error. Error code : {page.status_code}")
            raise Exception("Request error")
        soup = BeautifulSoup(page.content, 'html.parser')
        return soup.pre.string

    def read_file(self):
        # Obtenir le chemin absolu du répertoire contenant le script
        # script_dir = os.path.dirname(os.path.abspath(__file__))
        print('scrip_dir', self.script_dir)
        # Construire le chemin absolu vers le fichier input.txt
        input_file_path = os.path.join(self.script_dir, self.file)
        print('input_file_path', input_file_path)
        # Ouvrir et lire le fichier
        with open(input_file_path) as f:
            return f.read().split("\n")