import json
import os
from time import sleep

class TextManager:
    _instance = None

    def __init__(self):
        self.speed = 0.1
        self.codes = {
            "wait": self.timer,
            "speed": self.set_speed,
            "os": self.os_commands,
            "input": self.show_input
        }
        with open("./texts.json", "rb") as file:
            self.texts = json.loads(file.read())
  
    def __new__(cls):
        # https://www.educative.io/edpresso/how-to-create-a-singleton-class-in-python
        if cls._instance is None:
            cls._instance = super(TextManager, cls).__new__(cls)
        return cls._instance

    def typewritter(self, text):
        while len(text) > 0:

            # Special commands.
            while text[0:2] == "[$":
                key = text[2: text.find("=")]
                value = text[text.find("=") + 1: text.find("]")]
                text = text[text.find("]") + 1:]
                self.codes[key](value)
            
            if len(text):
                sleep(self.speed)
                print(text[0], end="", flush=True)
                text = text[1:]
        sleep(1)
        print("\n")

    def timer(self, value):
        sleep(float(value))

    def set_speed(self, value):
        self.speed = 1/float(value)

    def os_commands(self, value):
        os.system(value)

    def show_input(self, value):
        input(value)

if __name__ == "__main__":
    t = TextManager()