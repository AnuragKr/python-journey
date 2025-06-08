class Person:
    description = "general person"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("My name is {} and I am {} years old.".format(self.name, self.age))

    def eat(self, food):
        print("{} eats {}".format(self.name, food))

    def action(self):
        print("{} jumps".format(self.name))

class Baby(Person):
    description = "baby"

    def speak(self):
        print("yipee yipee yipee")

    def nap(self):
        print("{} takes a nap".format(self.name))

person = Person("Steve", 20)
person.speak()
person.eat("pasta")
person.action()

baby = Baby("Ian", 1)
baby.speak()
baby.eat("Baby food")
baby.action()

print(person.description)
print(baby.description)
