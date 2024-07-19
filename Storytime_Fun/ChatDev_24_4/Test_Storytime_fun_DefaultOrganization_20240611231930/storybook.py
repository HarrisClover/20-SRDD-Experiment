'''
This is the main file for the StoryBook application. It contains the StoryBook class, which represents a storybook. The class has been updated to include methods for creating and customizing storybook elements and saving the storybook data.
'''
import json
class StoryBook:
    def __init__(self, title):
        self.title = title
        self.pages = []
        self.characters = []
        self.themes = []
        self.settings = []
        self.interactive_elements = []
        self.voice_overs = []
        self.sound_effects = []
    def create_page(self, text, image):
        page = {'text': text, 'image': image}
        self.pages.append(page)
    def create_character(self, name, description, image):
        character = {'name': name, 'description': description, 'image': image}
        self.characters.append(character)
    def create_theme(self, name, description):
        theme = {'name': name, 'description': description}
        self.themes.append(theme)
    def create_setting(self, name, description, image):
        setting = {'name': name, 'description': description, 'image': image}
        self.settings.append(setting)
    def create_interactive_element(self, type, data):
        interactive_element = {'type': type, 'data': data}
        self.interactive_elements.append(interactive_element)
    def create_voice_over(self, text, voice_file):
        voice_over = {'text': text, 'voice_file': voice_file}
        self.voice_overs.append(voice_over)
    def create_sound_effect(self, name, sound_file):
        sound_effect = {'name': name, 'sound_file': sound_file}
        self.sound_effects.append(sound_effect)
    def save_storybook(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.__dict__, f)