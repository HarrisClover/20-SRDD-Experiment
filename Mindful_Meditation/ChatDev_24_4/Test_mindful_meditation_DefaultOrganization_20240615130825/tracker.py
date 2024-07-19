'''
This file contains the Tracker class, which represents a tracking system for the application. It includes methods for tracking and retrieving user progress.
'''
class Tracker:
    def __init__(self):
        self.progress = {}
    def track(self, session):
        '''
        This method tracks a meditation session.
        '''
        if session in self.progress:
            self.progress[session] += 1
        else:
            self.progress[session] = 1
    def get_progress(self):
        '''
        This method returns the user's progress.
        '''
        return self.progress