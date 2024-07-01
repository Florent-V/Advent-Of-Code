# Advent Of Code

## Solution

This repository contains my solutions to the [Advent of Code](https://adventofcode.com/) challenges and also some utilities to help you solve the puzzles.

You could find my solutions for each puzzle in his own folder (`aoc_{year}/Day_{day}`), with the input file and the code to solve it.

But you could also use this repository to solve the puzzles by yourself. This repository contains some utilities to help you with that.

## Prerequisites

If you want to use the full potential of this repository you need to respect the following prerequisites:
- You need to have Python 3 installed on your machine.
- You need to install the libraries in the `requirements.txt` file. You could do that by running the following command:
```bash
pip install -r requirements.txt
```
- You need to have the `AOC_ID` environment variable set with your session cookie from the advent of code website. You can get your session cookie by logging in to the advent of code website and getting the value of the `session` cookie. To set the `AOC_ID` environment variable you could run the following command:
```bash
export AOC_ID=<your_session_cookie>
```
To make this change permanent you could add this line to your `.bashrc` or `.zshrc` file. Depending on your shell.


## Program

Le but principal de ce programme est de vous accompagner dans la résolution des puzzles de l'Advent of Code. Ce programme va, dans un premier temps, créer une structure de dossier pour y inclure chaque puzzle et un fichier pour le résoudre :
  - /aoc_{year}/
    - /Day_{day}/
      - input.txt
      - input_light.txt
      - solution.py

Le fichier `solution.py` contient les méthodes `part_1` et `part_2` qu'il faudra implémenter pour résoudre les deux parties du puzzle du jour. Vous pouvez également implémenter d'autres fonctions pour vous aider à résoudre les puzzles. Gardez à l'esprit que les fonctions `part_1` et `part_2` seront appelées par les méthodes `solve` et `solve_both` qui sont présentes dans la classe `SolutionBase` dans d'autres commandes du programme.

This repo also contains some utilities to help you with that.
- some useful functions to read the input files
- some useful functions to help you to solve the puzzles

## Use Cases

### Initialize the structure of folders and files for a puzzle
To create the structure of folders and files for a puzzle you could run the following command:
```bash
python3 aoc.py -y <year> -d <day> -c
```

Exemple :
```bash
python3 aoc.py -y 2023 -d 1 -c
```

This command will create the following structure:
```
/aoc_2023/
  /Day_1/
    input.txt
    input_light.txt
    solution.py
```

The `input.txt` file contains the input of the puzzle and the `input_light.txt` file contains a light version of the input that you could use to test your code. The content of the `input_light.txt` file is manually extracted from the website of the advent of code. Sometimes the content of the `input_light.txt` file could be wrong, so you should copy/paste the content of the example from the website to the `input_light.txt` file.

The `solution.py` file contains the base code to solve the puzzle. This file contains a class that extends the `SolutionBase` class and implements the `part_1` method and the `part_2` method. The `SolutionBase` contains some useful methods to read the input files, run the solutions functions, chronometer the execution time, and test the solutions functions.

The function `part_1` and `part_2` are the functions that you should implement to solve the puzzles. This functions will be called by the `--solve` argument that will run the `part_1` and/or `part_2` functions and print the results.

If you have already created the structure of folders and files for a puzzle you could use the `-f` or `--force` argument to overwrite the existing files, including the `solution.py`. So be careful with this argument.

### Run function during the development

To run the function that you are developing you could run the following command:
```bash
python3 aoc.py -y <year> -d <day> -exec <function_name>
```

For example, you make a function called `do_something` in the `solution.py` file and you want to test it, you could run the following command:
```bash
python3 aoc.py -y 2023 -d 1 -exec do_soemthing
```

Be careful, this command line won't work on the following functions:
- `part_1`
- `part_2`
- `solve`
- `solve_both`


### Run the solution for one part of the puzzle

To run your solution you could run the following command:
```bash
python3 aoc.py -y <year> -d <day> -sol <part>
```

For example, if you want to run the solution of the first part of the puzzle of the first day of the year 2023 you could run the following command:
```bash
python3 aoc.py -y 2023 -d 1 -sol 1
```

If you want to run the solution of the second part of the puzzle of the first day of the year 2023 you could run the following command:
```bash
python3 aoc.py -y 2023 -d 1 -sol 2
```

This command will run the `part_1` or `part_2` function of the `solution.py` file, print the result and chronometer the execution time.

### Run the solution for both part of the puzzle

To run the solution for both parts of the puzzle you could run the following command:
```bash
python3 aoc.py -y <year> -d <day> -r
```

For example, if you want to run the solution of the first and the second part of the puzzle of the first day of the year 2023 you could run the following command:
```bash
python3 aoc.py -y 2023 -d 1 -r
```

This command will run the `part_1` and `part_2` functions of the `solution.py` file, print the results and chronometer the execution time.


### Use the complete input file

By default, the program will use the `input_light.txt` file to run the solutions. Be carefull your `input_light.txt` file is correct. If you want to use the `input.txt` file you could use the `-a` or `--all` argument.

```bash
python3 aoc.py -y <year> -d <day> -a

```

For example, if you want to run the solution of the first part of the puzzle of the first day of the year 2023 with the complete input file you could run the following command:
```bash
python3 aoc.py -y 2023 -d 1 -sol 1 -a
```