'''
This file contains the Ability class which represents a special ability that a unit can use.
'''
class Ability:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def use(self, user, target):
        # Use the ability on the target unit
        pass
    # Other ability-related methods and properties
    def __str__(self):
        return f"Ability: {self.name}\nDescription: {self.description}"
    def get_name(self):
        return self.name
    def get_description(self):
        return self.description
    def set_name(self, name):
        self.name = name
    def set_description(self, description):
        self.description = description