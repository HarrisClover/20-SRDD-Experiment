/*
This file contains the implementation of the Game class. The Game class represents the game itself and contains information about the players, alliances, and territories.
*/
#include "game.h"
#include <iostream>
void Game::start() {
    // Initialize game state
    initializeGame();
    // Main game loop
    while (!isGameOver()) {
        for (Player &player : players) {
            // Each player takes a turn
            player.takeTurn();
        }
    }
    // End game and declare winner
    endGame();
}
void Game::initializeGame() {
    // Create players
    players.push_back(Player("Player 1"));
    players.push_back(Player("Player 2"));
    // Create alliances
    alliances.push_back(Alliance("Alliance 1"));
    alliances.push_back(Alliance("Alliance 2"));
    // Assign players to alliances
    alliances[0].addPlayer(players[0]);
    alliances[1].addPlayer(players[1]);
    // Create territories and assign them to alliances
    territories.push_back(Territory("Territory 1", alliances[0]));
    territories.push_back(Territory("Territory 2", alliances[1]));
}
bool Game::isGameOver() {
    // Check if all territories have been claimed
    for (Territory &territory : territories) {
        if (territory.getAlliance() == nullptr) {
            return false;
        }
    }
    return true;
}
void Game::endGame() {
    // Determine the winner based on the alliance with the most territories
    Alliance *winner = nullptr;
    int maxTerritories = 0;
    for (Alliance &alliance : alliances) {
        int numTerritories = alliance.getTerritories().size();
        if (numTerritories > maxTerritories) {
            maxTerritories = numTerritories;
            winner = &alliance;
        }
    }
    if (winner != nullptr) {
        std::cout << "The winner is " << winner->getName() << "!\n";
    } else {
        std::cout << "The game is a draw!\n";
    }
    // Clean up game state if necessary
    players.clear();
    alliances.clear();
    territories.clear();
}