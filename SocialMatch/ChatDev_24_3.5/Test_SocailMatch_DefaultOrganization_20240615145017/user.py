'''
This file defines the User class.
'''
class User:
    def __init__(self, user_id, name, interests):
        self.user_id = user_id
        self.name = name
        self.interests = interests
    def __str__(self):
        return f"User ID: {self.user_id}, Name: {self.name}, Interests: {self.interests}"