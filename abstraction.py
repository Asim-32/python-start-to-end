# from abc import  ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def printarea():
#         return 0

# class Square(Shape):
#     stype = "square"
#     sides = 4
#     def __init__(self):
#         self.height = 4
#         self.width = 4
#     def __str__(self):
#         return f"{self.stype} height = {self.height} and width = {self.width}"

#     def printarea(self):
#         area = self.height * self.width
#         return area


# obj = Square()
# print(obj)
# print(obj.printarea())






class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    def explain(self):
        return f"This employee is {self.fname} {self.lname}"


hindustani_supporter = Employee("Hindustani", "Supporter")
print(hindustani_supporter.explain())