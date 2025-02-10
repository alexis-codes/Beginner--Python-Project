#Parent class/Superclass
class Animal:
    def speak(self):
        print("Animal is speaking")

#Child/Sub-/Derived class
class Dog(Animal) :
    def bark(self):
        print("Dog is barking")

class cat :
    def meow(self):
        print("Cat is meowing")

a = Animal()

d = Dog()
c = cat()