'''
Meditation - Class for managing meditation sessions
'''
class Meditation:
    def __init__(self):
        self.style = ""
        self.duration = 0
        self.theme = ""
    def set_preferences(self):
        self.style = input("Enter your preferred meditation style: ")
        self.duration = int(input("Enter your preferred meditation duration (in minutes): "))
        self.theme = input("Enter your preferred meditation theme: ")
    def get_meditation_sessions(self):
        # Fetch meditation sessions from the database or API based on user preferences
        sessions = [
            {"name": "Session 1", "style": "style1", "duration": 10, "theme": "theme1"},
            {"name": "Session 2", "style": "style2", "duration": 15, "theme": "theme2"},
            {"name": "Session 3", "style": "style3", "duration": 20, "theme": "theme3"}
        ]
        filtered_sessions = []
        for session in sessions:
            if session["style"] == self.style and session["duration"] == self.duration and session["theme"] == self.theme:
                filtered_sessions.append(session["name"])
        return filtered_sessions
    def start_meditation(self):
        sessions = self.get_meditation_sessions()
        if len(sessions) == 0:
            print("No matching meditation sessions found.")
        else:
            print("Available meditation sessions:")
            for session in sessions:
                print(session)