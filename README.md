# Advent Of Code

This repository contains my solutions to the [Advent of Code](https://adventofcode.com/) challenges.

You could find the solution for each puzzle in his own folder, with the input file and the code to solve it.

You could also use this repo to solve the puzzles by yourself. This repo contains some utilities to help you with that.
- in root folder of this repo you could find a `init.py` file that will create a new folder with the structure to solve the puzzles :
  - /{year}/
    - /Day_{day}/
      - input.txt
      - input_light.txt
      - main.py
  To use this file you need to export the `AOC_ID` environment variable with your session cookie from the advent of code website.
  You could do that by running `export AOC_ID=<your_session_cookie>` in your terminal.
  To get your session cookie you need to log in to the advent of code website and get the value of the `session` cookie.
- some useful functions to read the input files
- some useful functions to test your code
- some useful functions to help you to solve the puzzles