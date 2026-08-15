from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self, name, habitat):
        self.name = name
        self.habitat= habitat
    def display(self):
        print(f"name: {self.name} | habitat : {self.habitat}")

    @abstractmethod
    def speak(self):
        pass
class dog(Animal):
    def __init__(self, name, habitat , breed):
        super().__init__(name, habitat)
        self.breed = breed

    def speak(self):
        print(f"{self.name} ({self.breed}) says: WOOF! WOOF!")

class parrot(Animal):
    def __init__(self, name, habitat , phrase):
            super().__init__(name, phrase)
            self.phrase = phrase

    def speak(self):
            print(f"{self.name} says: {self.phrase}! {self.phrase}!")
    
