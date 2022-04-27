from utils.text_manager import TextManager
import os

class MainMenu:
    """
    This class shows the starting texts of the adventure and
    communicates with the game controller to start a game.
    """
    def __init__(self):
        os.system('clear')
        self.text = TextManager().texts["main_menu"]
        self.options = {
            "1": self.start_game,
            "2": self.end_game,
            "3": self.end_game
        }
        self.input_error = False
        self.display_title()

    def display_title(self):
        """
        Displays main text and handles user input to select an option.
        """
        while True:
            print(self.text["title"])
            print(self.text["sub_title" if not self.input_error else "input_error"]) 
            for i in range(3):
                print(self.text[f"opt{i + 1}"])
            try:
                self.input_error = False
                self.options[input(self.text["input"])]()
            except KeyError:
                self.input_error = True
                os.system('clear')
                

    def start_game(self):
        """
        Displays main story and starts the game.
        """
        story = TextManager().texts["intro_story"]
        for i in story.keys():
            TextManager().typewritter(story[i])
        exit()


    def end_game(self):
        print(self.text["end_game"])
        exit()