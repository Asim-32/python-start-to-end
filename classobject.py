"""Class and obejct in python"""

# class Person():
#     def function(self):
#         print("working")

# obj = Person()
# obj.function()
# --------------------------------------------------

""" Constructer in python """
class Mynewclass():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f'{self.name}({self.age})'

obj = Mynewclass("manas", 20)
print(obj)