'''
This class represents a user in the system. It has methods for creating a profile, searching for other users, sending connection requests, accepting connection requests, joining groups, posting content, participating in discussions, and discovering career opportunities.
'''
class User:
    def __init__(self, conn):
        self.conn = conn
        self.profile = {}
        self.connections = []
        self.groups = []
        self.contents = []
        self.opportunities = []
    def create_profile(self):
        name = input("Enter your name: ")
        profession = input("Enter your profession: ")
        self.profile['name'] = name
        self.profile['profession'] = profession
        c = self.conn.cursor()
        c.execute("INSERT INTO users (name, profession) VALUES (?, ?)", (name, profession))
        self.conn.commit()
        print("Profile created successfully!")
    def search_users(self, name):
        c = self.conn.cursor()
        c.execute("SELECT * FROM users WHERE name LIKE ?", ('%' + name + '%',))
        results = c.fetchall()
        return results
    def send_connection_request(self, user_id):
        c = self.conn.cursor()
        c.execute("INSERT INTO connections (sender_id, receiver_id, status) VALUES (?, ?, 'pending')", (self.profile['id'], user_id))
        self.conn.commit()
        print("Connection request sent!")
    def accept_connection_request(self, connection_id):
        c = self.conn.cursor()
        c.execute("UPDATE connections SET status = 'accepted' WHERE id = ?", (connection_id,))
        self.conn.commit()
        print("Connection request accepted!")
    def join_group(self, group_id):
        c = self.conn.cursor()
        c.execute("INSERT INTO user_group (user_id, group_id) VALUES (?, ?)", (self.profile['id'], group_id))
        self.conn.commit()
        print("Joined group successfully!")
    def post_content(self, content):
        c = self.conn.cursor()
        c.execute("INSERT INTO content (user_id, text) VALUES (?, ?)", (self.profile['id'], content))
        self.conn.commit()
        print("Content posted successfully!")
    def participate_in_discussion(self, discussion_id, message):
        c = self.conn.cursor()
        c.execute("INSERT INTO discussions (discussion_id, user_id, message) VALUES (?, ?, ?)", (discussion_id, self.profile['id'], message))
        self.conn.commit()
        print("Participated in discussion successfully!")
    def discover_career_opportunities(self):
        c = self.conn.cursor()
        c.execute("SELECT * FROM career_opportunities")
        results = c.fetchall()
        return results