'''
This file contains the Game class which manages the overall game logic.
'''
from player import Player
from territory import Territory
class Game:
    def __init__(self):
        # Initialize game variables
        self.players = []
        self.territories = []
        self.current_player = None
    def start(self):
        # Create players and territories
        self.create_players()
        self.create_territories()
        # Set the first player as the current player
        self.current_player = self.players[0]
        # Start the game loop
        self.game_loop()
    def create_players(self):
        # Create two players for now
        player1 = Player("Player 1")
        player2 = Player("Player 2")
        self.players.append(player1)
        self.players.append(player2)
    def create_territories(self):
        # Create some territories for the game
        territory1 = Territory("Territory 1")
        territory2 = Territory("Territory 2")
        territory3 = Territory("Territory 3")
        self.territories.append(territory1)
        self.territories.append(territory2)
        self.territories.append(territory3)
    def game_loop(self):
        game_over = False
        while not game_over:
            # Display game state
            self.display_game_state()
            # Get player's action
            action = self.current_player.get_action()
            # Process player's action
            self.process_action(action)
            # Check if the game is over
            game_over = self.check_game_over()
            if game_over:
                break
            # Switch to the next player
            self.switch_player()
    def display_game_state(self):
        print("Current player:", self.current_player.name)
        print("Territories:")
        for territory in self.territories:
            print(territory.name)
    def process_action(self, action):
        # Process the player's action here
        if action == "conquer":
            territory = self.current_player.conquer_territory(self.territories)
            if territory:
                print(f"{self.current_player.name} conquered {territory.name}!")
            else:
                print("No territory available to conquer.")
        elif action == "defend":
            territory = self.current_player.defend_territory(self.territories)
            if territory:
                print(f"{self.current_player.name} defended {territory.name}!")
            else:
                print("No territory owned to defend.")
        else:
            print("Invalid action!")
    def check_game_over(self):
        # Check if the game is over
        if len(self.territories) == 0:
            return True
        else:
            return False
    def switch_player(self):
        # Switch to the next player
        current_player_index = self.players.index(self.current_player)
        next_player_index = (current_player_index + 1) % len(self.players)
        self.current_player = self.players[next_player_index]