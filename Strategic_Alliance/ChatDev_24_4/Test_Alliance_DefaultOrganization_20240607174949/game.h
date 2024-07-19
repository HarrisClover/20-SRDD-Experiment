/*
This file contains the declaration of the Game class. The Game class represents the game itself and contains information about the players, alliances, and territories.
*/
#include "player.h"
#include "alliance.h"
#include "territory.h"
#include <vector>
class Game {
public:
    void start();
    void initializeGame();
    bool isGameOver();
    void endGame();
private:
    std::vector<Player> players;
    std::vector<Alliance> alliances;
    std::vector<Territory> territories;
};