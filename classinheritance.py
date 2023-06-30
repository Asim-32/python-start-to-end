# class Vehical:
#     def __init__(self,brand,price):
#         self.brand = brand
#         self.price = price

#     def __str__(self):
#         return f"this is the return string function of class {self.brand}, {self.price}"

#     def max_speed(self, speedVal):
#         print(f"Max Speed:: {speedVal}")

# class Nexon(Vehical):
#     def __init__(self, brand,price, rating):
#        self.rating = rating
#        super().__init__(brand,price)

#     def carRating(self,comment):
#         return f"best car of 2023 having rating:: {self.rating} and comment:: {comment}"

# obj  = Nexon("TATA","12L",5)
# print(obj)
# obj.max_speed("200/h")
# print(obj.carRating("good working"))


# ------------------------------------------------------

# multilevel inheritance
# class A():
#     def printname(self):
#          print("A")

# class B(A):
#     def newfunction(self):
#         print("B")
# class C(B):
#     def func(self):
#         print("C")



# obj = C()
# obj.func()
# obj.printname()
# obj.newfunction()
# ---------------------------------------------------------

# multiple inheritance
class Name():
    def return_name(self):
        print("ABC")
class Age():
    def return_age(self):
        print(30)

class Person(Name,Age):
    pass


obj = Person();
obj.return_name()
obj.return_age()






