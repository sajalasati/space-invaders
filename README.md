# Space Invaders

[![Language](https://img.shields.io/badge/language-python-blue.svg?style=flat)](https://www.python.org)
[![Module](https://img.shields.io/badge/module-pygame-brightgreen.svg?style=flat)](http://www.pygame.org/news.html)
![Release](https://img.shields.io/badge/release-v1.0-orange.svg?style=flat)

## About

Space Invaders is a two-dimensional fixed shooter game in which the player controls a ship by moving it horizontally across the bottom of the screen and firing at aliens. The spaceship in this game can fire two types of missiles - one is slower but kills enemy on contact while other is faster but only freezes the enemy on contact (the player is awarded points accordingly). The aim of game is to score maximum.

This game has been written using Python and pygame.

**Important** to note that the game has been tested on **ONLY** Linux-based OSs, and _may not_ work on Windows.

## Dependencies

- The only dependency required is **pygame** which can be installed using following set of commands:
  - `sudo add-apt-repository ppa:thopiekar/pygame`
  - `sudo apt-get update`
  - `sudo apt-get install python3-pygame`
- Or instead if you want to run it inside a virtual environment, run the command:
  - `pip3 install pygame`

## How To Play

- If you have the correct version of Python and Pygame installed, you can run the program in the command prompt / terminal.

```bash
cd space-invaders
python main.py
```

**Note:** If you're using Python 3, replace the command "python" with "python3"

## Controls

- Controls follow traditional classic titles (A,D) for left and right movement of missile
- To fire a slow missile press `spacebar`
- To fire a fast missile press `s`
- To quit, press `q`
