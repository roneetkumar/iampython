class Animal:
    def walk(self):
        print("walking")


class Dog(Animal):
    def bark(self):
        print('bark')


class Cat(Animal):
    def meow(self):
        print("meow")


dog = Dog()
cat = Cat()
