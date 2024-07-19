manual.md

```
# Alliance Conqueror

A turn-based strategy game where players build and manage their own alliance, working together to conquer territories and defeat other rival alliances.

## Quick Install

Before you can run the game, you need to install a C++ compiler. Here are some options:

- GCC: Can be installed with the GNU Compiler Collection. On Ubuntu, you can use the command `sudo apt install build-essential`.

- Clang: Can be installed with the LLVM project. On Ubuntu, you can use the command `sudo apt install clang`.

- MSVC: Comes with the Visual Studio IDE for Windows.

After installing a compiler, you can compile the game using the command `g++ main.cpp game.cpp -o game` (replace `g++` with your compiler if not using GCC).

## 🤔 What is this?

Alliance Conqueror is a strategy game where players form alliances and compete to conquer territories. The game is turn-based, meaning each player takes a turn to make their moves. The game continues until all territories have been claimed, at which point the alliance with the most territories is declared the winner.

## 🎮 How to Play

1. Run the game using the command `./game`.

2. The game will automatically create two players and two alliances, and assign each player to an alliance.

3. Each player will take a turn to make their moves. This could involve attacking a territory, defending their own territory, or moving their forces.

4. The game ends when all territories have been claimed. The alliance with the most territories is declared the winner.

## 📖 Documentation

Please see the included code files for full documentation on:

- The main game loop (`main.cpp`)

- The Game class, which represents the game itself (`game.h`, `game.cpp`)

- The Player, Alliance, and Territory classes (not shown in this manual, but included in the code)

Remember, the key to winning Alliance Conqueror is strategy. Good luck, and may the best alliance win!
```