'''
This file contains the MatchMaker class, which is responsible for matching users based on their interests.
'''
from user import User
class MatchMaker:
    def __init__(self):
        self.users = []
    def add_user(self, user):
        for existing_user in self.users:
            if existing_user.username == user.username:
                existing_user.interests = user.interests
                return
        self.users.append(user)
    def find_matches(self, user):
        matches = []
        user_interests = user.get_interests()
        for potential_match in self.users:
            if potential_match != user:
                shared_interests = set(user_interests).intersection(potential_match.get_interests())
                if len(shared_interests) > 0:
                    matches.append(potential_match)
        return matches
    def get_matches_for(self, user):
        matches = self.find_matches(user)
        matches_names = [match.username for match in matches]
        return ', '.join(matches_names)