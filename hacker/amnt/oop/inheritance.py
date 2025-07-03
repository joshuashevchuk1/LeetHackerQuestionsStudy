class Animal:
    def __init__(self):
        print("Animal initialized")

class Dog(Animal):
    def __init__(self):
        super().__init__()
        print("Dog initialized")