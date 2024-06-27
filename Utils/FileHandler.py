import os


class FileHandler:

    def __init__(self, directory, file_name, content):
        self.directory = directory
        self.file_name = file_name
        self.content = content

    # generate getter and setter for directory
    @property
    def directory(self):
        return self._directory

    @directory.setter
    def directory(self, value):
        self._directory = value

    # generate getter and setter for file
    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, value):
        self._file_name = value

    # generate getter and setter for content
    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value

    def reinitialise(self, directory=None, file=None, content=None):
        self.__init__(directory, file, content)

    def write_file(self):
        os.makedirs(self._directory, exist_ok=True)
        with open(f"{self._directory}/{self.file_name}", "w") as f:
            f.write(self._content.rstrip('\n'))
        print(f"Fichier créé dans {self._directory}")
        return f"{self._directory}/{self.file_name}"

    def read_file(self):
        try:
            with open(f"{self._directory}/{self.file_name}", "r") as f:
                self._content = f.read()
                return self._content
        except FileNotFoundError:
            print(f"Le fichier {self._directory}/{self.file_name} n'a pas été trouvé")
        return

    def copy_file(self, origin, destination):
        try:
            with open(origin, "r") as f:
                self._content = f.read()
        except FileNotFoundError:
            print(f"Le fichier {origin} n'a pas été trouvé")
        with open(destination, "w") as f:
            f.write(self._content)
        print(f"Fichier copié de {origin} vers {destination}")
        return
