/*
This file defines the Game class. The Game class controls the game loop and manages the state of the game.
*/
#ifndef GAME_H
#define GAME_H
#include "Player.h"
#include "Battlefield.h"
class Game {
public:
    Game();
    void run();
private:
    Player player1;
    Player player2;
    Battlefield battlefield;
    bool gameOver();
    void announceWinner();
};
#endif