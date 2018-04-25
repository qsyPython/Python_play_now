class Cat(object):
    def say(self):
        print("i am cat")

class Dog(object):
    def say(self):
        print("I am dog")

class Duck(object):
    def say(self):
        print("I am a duck")

animal = Cat

animal().say()

class Animal():
    def say(self):
        print("i am a animal")

class Dog(
    Animal):
    def say(self):
        print("I am dog")

