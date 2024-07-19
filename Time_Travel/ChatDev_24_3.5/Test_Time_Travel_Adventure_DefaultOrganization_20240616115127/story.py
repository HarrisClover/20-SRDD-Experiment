'''
Story module
Contains the Story class responsible for managing the game's story and choices.
'''
class Story:
    def __init__(self):
        self.screens = {
            "intro": {
                "text": "Welcome to Time Travel Adventure! Choose your time period:",
                "choices": [
                    {"text": "Ancient Egypt", "next_screen": "egypt"},
                    {"text": "Medieval Europe", "next_screen": "medieval"},
                    {"text": "Future", "next_screen": "future"}
                ]
            },
            "egypt": {
                "text": "You are now in Ancient Egypt. What do you want to do?",
                "choices": [
                    {"text": "Explore the pyramids", "next_screen": "pyramids"},
                    {"text": "Meet Cleopatra", "next_screen": "cleopatra"},
                    {"text": "Go back to the intro", "next_screen": "intro"}
                ]
            },
            "medieval": {
                "text": "You are now in Medieval Europe. What do you want to do?",
                "choices": [
                    {"text": "Attend a jousting tournament", "next_screen": "jousting"},
                    {"text": "Visit a castle", "next_screen": "castle"},
                    {"text": "Go back to the intro", "next_screen": "intro"}
                ]
            },
            "future": {
                "text": "You are now in the future. What do you want to do?",
                "choices": [
                    {"text": "Explore a futuristic city", "next_screen": "city"},
                    {"text": "Meet robots", "next_screen": "robots"},
                    {"text": "Go back to the intro", "next_screen": "intro"}
                ]
            },
            "pyramids": {
                "text": "You are exploring the pyramids. What do you find?",
                "choices": [
                    {"text": "A hidden treasure", "next_screen": "treasure"},
                    {"text": "An ancient artifact", "next_screen": "artifact"},
                    {"text": "Go back to Egypt", "next_screen": "egypt"}
                ]
            },
            "cleopatra": {
                "text": "You meet Cleopatra. What do you talk about?",
                "choices": [
                    {"text": "Egyptian history", "next_screen": "history"},
                    {"text": "Her life as a queen", "next_screen": "queen"},
                    {"text": "Go back to Egypt", "next_screen": "egypt"}
                ]
            },
            "jousting": {
                "text": "You are watching a jousting tournament. Who do you support?",
                "choices": [
                    {"text": "The knight in red", "next_screen": "red_knight"},
                    {"text": "The knight in blue", "next_screen": "blue_knight"},
                    {"text": "Go back to Medieval Europe", "next_screen": "medieval"}
                ]
            },
            "castle": {
                "text": "You are visiting a castle. What do you want to see?",
                "choices": [
                    {"text": "The throne room", "next_screen": "throne_room"},
                    {"text": "The dungeon", "next_screen": "dungeon"},
                    {"text": "Go back to Medieval Europe", "next_screen": "medieval"}
                ]
            },
            "city": {
                "text": "You are exploring a futuristic city. What catches your attention?",
                "choices": [
                    {"text": "Flying cars", "next_screen": "flying_cars"},
                    {"text": "Virtual reality games", "next_screen": "vr_games"},
                    {"text": "Go back to the future", "next_screen": "future"}
                ]
            },
            "robots": {
                "text": "You meet robots. What do you want to learn about?",
                "choices": [
                    {"text": "Artificial intelligence", "next_screen": "ai"},
                    {"text": "Robotics", "next_screen": "robotics"},
                    {"text": "Go back to the future", "next_screen": "future"}
                ]
            },
            "treasure": {
                "text": "You found a hidden treasure! You win!",
                "choices": []
            },
            "artifact": {
                "text": "You found an ancient artifact. You learn about its history.",
                "choices": []
            },
            "history": {
                "text": "You learn about Egyptian history. It's fascinating!",
                "choices": []
            },
            "queen": {
                "text": "Cleopatra tells you about her life as a queen. It's inspiring!",
                "choices": []
            },
            "red_knight": {
                "text": "The knight in red wins the jousting tournament. You cheer!",
                "choices": []
            },
            "blue_knight": {
                "text": "The knight in blue wins the jousting tournament. You cheer!",
                "choices": []
            },
            "throne_room": {
                "text": "You see the majestic throne room. It's impressive!",
                "choices": []
            },
            "dungeon": {
                "text": "You explore the dark dungeon. It's spooky!",
                "choices": []
            },
            "flying_cars": {
                "text": "You experience flying cars. It's like a dream!",
                "choices": []
            },
            "vr_games": {
                "text": "You play virtual reality games. It's so much fun!",
                "choices": []
            },
            "ai": {
                "text": "You learn about artificial intelligence. It's mind-blowing!",
                "choices": []
            },
            "robotics": {
                "text": "You learn about robotics. It's fascinating!",
                "choices": []
            }
        }
        self.current_screen = "intro"
    def get_screen(self, screen_name):
        return self.screens.get(screen_name)
    def make_choice(self, choice):
        next_screen = choice.get("next_screen")
        if next_screen:
            self.current_screen = next_screen