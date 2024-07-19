/*
This file implements the Game class. The Game class controls the game loop and manages the state of the game.
*/
#include "Game.h"
Game::Game() : player1(), player2(), battlefield() {}
void Game::run() {
    while (!gameOver()) {
        player1.takeTurn();
        if (gameOver()) break;
        player2.takeTurn();
    }
    announceWinner();
}
bool Game::gameOver() {
    // Game is over if any player's team is completely defeated
    return player1.isDefeated() || player2.isDefeated();
}
void Game::announceWinner() {
    // The player who is not defeated is the winner
    if (player1.isDefeated()) {
        std::cout << "Player 2 is the winner!" << std::endl;
    } else {
        std::cout << "Player 1 is the winner!" << std::endl;
    }
}