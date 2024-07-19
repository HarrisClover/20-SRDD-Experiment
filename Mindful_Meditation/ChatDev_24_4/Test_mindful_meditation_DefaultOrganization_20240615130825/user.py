'''
This file contains the User class, which represents a user of the application. It includes methods for setting and getting user preferences, and for updating the user's progress after a meditation session.
'''
class User:
    def __init__(self):
        self.preferences = {}
        self.progress = {}
    def set_preferences(self, preferences):
        '''
        This method sets the user's meditation preferences.
        '''
        self.preferences = preferences
    def get_preferences(self):
        '''
        This method returns the user's meditation preferences.
        '''
        return self.preferences
    def update_progress(self, session):
        '''
        This method updates the user's progress based on the completed session.
        '''
        if session in self.progress:
            self.progress[session] += 1
        else:
            self.progress[session] = 1