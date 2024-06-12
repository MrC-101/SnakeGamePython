class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Breathe")


class Fish(Animal):
    def __init__(self):
        super().__init__()
        self.environment = "underwater"
        self.num_eyes = 3

    def breathe(self):
        super().breathe()
        print("doing this underwater")
    def swim(self):
        print("Swim underwater")

animal = Animal()
fish = Fish()


print(fish.environment)
print(fish.num_eyes)
fish.swim()
fish.breathe()
