'''
This file contains the User class, which represents a user of the application.
'''
class User:
    def __init__(self, username, interests):
        self.username = username
        self.interests = interests
    def get_interests(self):
        return self.interests