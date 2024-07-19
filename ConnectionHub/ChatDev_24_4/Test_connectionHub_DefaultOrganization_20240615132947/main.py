'''
This is the main entry point of the application. It handles user input and output, and uses the other classes to perform the necessary actions.
'''
import sqlite3
from user import User
import Group
import Content
import CareerOpportunity
# Connect to the SQLite database
conn = sqlite3.connect('social_network.db')
# Create a cursor object
c = conn.cursor()
# Create table for users
c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        profession TEXT
    )
''')
# Create table for connections
c.execute('''
    CREATE TABLE IF NOT EXISTS connections (
        id INTEGER PRIMARY KEY,
        sender_id INTEGER,
        receiver_id INTEGER,
        status TEXT
    )
''')
# Create table for groups
c.execute('''
    CREATE TABLE IF NOT EXISTS groups (
        id INTEGER PRIMARY KEY,
        name TEXT
    )
''')
# Create table for content
c.execute('''
    CREATE TABLE IF NOT EXISTS content (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        text TEXT
    )
''')
# Create table for career opportunities
c.execute('''
    CREATE TABLE IF NOT EXISTS career_opportunities (
        id INTEGER PRIMARY KEY,
        company TEXT,
        position TEXT,
        description TEXT
    )
''')
# Commit the changes
conn.commit()
def main():
    # Create a new user
    user = User(conn)
    user.create_profile()
    # Create a new group
    group = Group.Group(conn)
    group.create_group()
    # Create a new piece of content
    content = Content.Content(conn)
    content.create_content()
    # Create a new career opportunity
    career_opportunity = CareerOpportunity.CareerOpportunity(conn)
    career_opportunity.create_career_opportunity()
if __name__ == "__main__":
    main()
# Close the connection
conn.close()