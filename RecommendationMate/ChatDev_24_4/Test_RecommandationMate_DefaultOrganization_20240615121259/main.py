'''
This is the main file that runs the movie recommendation software. 
It initializes the database, recommendation engine, user, and GUI. 
It also includes improved error handling to prevent the application from crashing and to provide a better user experience.
'''
import sys
import os
import tkinter as tk
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from database import Database
from recommendation_engine import RecommendationEngine
from user import User
from gui import GUI
class DatabaseError(Exception):
    pass
class RecommendationEngineError(Exception):
    pass
class UserError(Exception):
    pass
class GuiError(Exception):
    pass
def main():
    try:
        # Initialize database
        database = Database()
    except DatabaseError as e:
        print(f"Database initialization failed: {e}")
        return
    try:
        # Initialize recommendation engine
        recommendation_engine = RecommendationEngine(database)
    except RecommendationEngineError as e:
        print(f"Recommendation engine initialization failed: {e}")
        return
    try:
        # Initialize user
        user = User(recommendation_engine)
    except UserError as e:
        print(f"User initialization failed: {e}")
        return
    try:
        # Initialize GUI
        gui = GUI(user)
        # Run GUI
        gui.run()
    except GuiError as e:
        print(f"GUI initialization or running failed: {e}")
        return
if __name__ == "__main__":
    main()