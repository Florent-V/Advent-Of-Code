import os


class PuzzleReader:
    def __init__(self, file, script_dir):
        self.file = file
        self.script_dir = script_dir

    @property
    def file(self):
        return self._file

    @file.setter
    def file(self, value):
        self._file = value

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