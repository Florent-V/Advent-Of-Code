import os, sys


class FileHandler:
    
    @staticmethod
    def get_path():
        # return os.path.dirname(os.path.realpath(sys.argv[0]))
        # return os.path.dirname(os.path.abspath(__file__))
        # return os.path.dirname(os.path.realpath(__file__))
        return path if os.path.isdir(path := os.path.realpath(sys.argv[0])) else os.path.dirname(path)
    
    @staticmethod
    def write_file(directory, file_name, content):
        os.makedirs(directory, exist_ok=True)
        with open(f"{directory}/{file_name}", "w") as f:
            f.write(content.rstrip('\n'))
        print(f"{directory}/{file_name}")
        return f"{directory}/{file_name}"

    @staticmethod
    def read_file(directory, file_name):
        try:
            with open(f"{directory}/{file_name}", "r") as f:
                content = f.read()
                return content
        except FileNotFoundError:
            print(f"Le fichier {directory}/{file_name} n'a pas été trouvé")
        return

    @staticmethod
    def copy_file(origin, destination):
        try:
            with open(origin, "r") as f:
                content = f.read()
        except FileNotFoundError:
            print(f"Le fichier {origin} n'a pas été trouvé")
        with open(destination, "w") as f:
            f.write(content)
        print(f"Fichier copié de {origin} vers {destination}")
        return
