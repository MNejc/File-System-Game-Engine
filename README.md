# Minimalistic Game Engine - Windows File Explorer Games

## Overview
This is an **old project from 2022**. It is a minimalistic game engine that lets you play games directly inside a folder in Windows File Explorer. Included are **Flappy Bird** and **Minesweeper**, for demonstation.

## How It Works
The engine uses Windows File Explorer as its display and input system. The game scene is shown as a folder, where each interactive element is represented by a shortcut file (.lnk) with an icon. These shortcuts act as buttons, and clicking one triggers an action stored in a text file.

Every frame, the engine reads this text file to determine the player's input and updates the game by modifying the folder contents. New icons are assigned from a sprite folder, and the scene refreshes based on Explorer’s update cycle.

This system is not fast or smooth—Windows Explorer only refreshes the screen about every seconds, making quick reaction games like Flappy Bird difficult to play. However, it works well for turn-based games like Minesweeper, where the slower update rate is not an issue.

## Included Games
### **Minesweeper**
A simple version of the classic game. Click tiles to reveal numbers or mines. The game ends when you find all safe tiles or click a mine.

### **Flappy Bird**
A basic version of Flappy Bird. Click to make the bird jump and avoid obstacles. The game is slower than usual due to the engine's limitations.

## Screenshots
### Flappy Bird
![Flappy Bird](FlappyBird%20Screenshot.png)

### Minesweeper
![Minesweeper](MineSweeper%20Screenshot.png)

## Files in the Project
- `engine.py` - The main engine that can be used as library to make games.
- `flappybird.py` - Flappy Bird demo.
- `minesweeper.py` - Minesweeper demo.
- `sprites/` - Folder with game icons.
- `game/` - The folder where the game is played.

## Dependencies
Install dependencies:
```sh
pip install pywin32
```

## Running the Games
1. Run a game script:
   ```sh
   python flappybird.py
   ```
   or
   ```sh
   python minesweeper.py
   ```
2. Open the **game folder** to play.
