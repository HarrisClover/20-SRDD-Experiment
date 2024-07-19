/*
This file defines the Player class. The Player class represents a player in the game.
*/
#ifndef PLAYER_H
#define PLAYER_H
#include <vector>
#include "Warrior.h"
class Player {
public:
    Player();
    void takeTurn();
    bool isDefeated();
private:
    std::vector<Warrior> warriors;
};
#endif