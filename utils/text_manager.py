import json

class TextManager:
    _instance = None

    def __init__(self):
        with open("./texts.json", "rb") as file:
            self.texts = json.loads(file.read())
  
    def __new__(cls):
        # https://www.educative.io/edpresso/how-to-create-a-singleton-class-in-python
        if cls._instance is None:
            cls._instance = super(TextManager, cls).__new__(cls)
        return cls._instance

if __name__ == "__main__":
    t = TextManager()