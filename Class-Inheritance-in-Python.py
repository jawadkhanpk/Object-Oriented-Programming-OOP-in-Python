# Animal is parent class
class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, Exhale")

# Fish is the child class which is inheriting the properties of a parent class "Animal"
class Fish(Animal):
    def __init__(self):
        super().__init__()

    def swim(self):
        print("Moving in a Water")



nemo = Fish()
# Accessing attributes of parent class "Animal" by using object of a child class "Fish"
print(nemo.num_eyes)
nemo.breathe()

nemo.swim()