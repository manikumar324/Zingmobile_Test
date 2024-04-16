class Person:
    def __init__(self):
        self.name=input()
        self.age=input()
        self.mobile=input()
    def print_info(self):
        print(self.name)
        print(self.age)
        print(self.mobile)

person1=Person()
person1.print_info()