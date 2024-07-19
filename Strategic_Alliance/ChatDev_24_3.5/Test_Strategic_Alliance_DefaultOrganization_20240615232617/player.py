'''
This file contains the Player class which represents a player in the game.
'''
class Player:
    def __init__(self, name):
        self.name = name
    def get_action(self):
        # Get the player's action
        action = input("Enter your action (conquer/defend): ")
        return action
    def conquer_territory(self, territories):
        # Select a territory to conquer
        print("Available territories to conquer:")
        for i, territory in enumerate(territories):
            print(f"{i+1}. {territory.name}")
        choice = input("Enter the number of the territory to conquer: ")
        try:
            index = int(choice) - 1
            territory = territories[index]
            territories.remove(territory)
            return territory
        except (ValueError, IndexError):
            return None
    def defend_territory(self, territories):
        # Select a territory to defend
        print("Owned territories to defend:")
        for i, territory in enumerate(territories):
            print(f"{i+1}. {territory.name}")
        choice = input("Enter the number of the territory to defend: ")
        try:
            index = int(choice) - 1
            territory = territories[index]
            return territory
        except (ValueError, IndexError):
            return None