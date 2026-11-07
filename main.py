# Example 1

# class Human:
#     height = 170
#     satiety = 50
#
# class Student(Human):
#     satiety = 0
#
# class Worker(Human):
#     satiety = 100
#
# ostap = Student()
# viktor = Worker()
#
# print(ostap.satiety)
# print(viktor.satiety)
#
# print(ostap.height)
# print(viktor.height)
#
# # Example 2
#
# class Grandparent:
#     height = 170
#     satiety = 100
#     age = 60
#
# class Parent(Grandparent):
#     age = 40
#
# class Child(Parent):
#     height = 50
#
#     def __init__(self):
#         print(self.height)
#         print(self.satiety)
#         print(self.age)
#
#
# # Example 3
#
# class Hello_world:
#     hello = "Hello"
#     _hello = "_Hello"
#     __hello = "__Hello"
#
#     def __init__(self):
#         self.world = "World"
#         self._world = "_World"
#         self.__world = "__World"
#
#     def printer(self):
#         print(self.hello)
#         print(self._hello)
#         print(self.__hello)
#         print(self.world)
#         print(self._world)
#         print(self.__world)
#
# class Hi(Hello_world):
#
#     def hi_print(self):
#         print(self.hello)
#         print(self._hello)
#         print(self.__hello)
#         print(self.world)
#         print(self._world)
#
# hello_world = Hello_world()
# hi = Hi()
#
# hello_world.printer()
#
# hi.hi_print()

# Example 4

class Computer:
    def calculate(self):
        print("Caculating...")

class Display:
    def display(self):
        print("I display yhe imge on the screen...")

class Smartphone(Display, Computer):
    pass

phone = Smartphone()
phone.display()
phone.calculate()
