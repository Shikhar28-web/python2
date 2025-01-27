# single inheritance

# class Parent:
#     def show(self):
#         print("This is a method in the Parent class.")

# class Child(Parent):
#     def display(self):
#         print("This is a method in the Child class.")

# obj = Child()
# obj.show()    
# obj.display() 




# multiple inheitance

# class Parent1:
#     def method1(self):
#         print("This is method1 from Parent1.")

# class Parent2:
#     def method2(self):
#         print("This is method2 from Parent2.")

# class Child(Parent1, Parent2):
#     def method3(self):
#         print("This is method3 from Child.")

# obj = Child()
# obj.method1()  
# obj.method2() 
# obj.method3()  


#3. Multi-level Inheritance

# class Grandparent:
#     def method1(self):
#         print("This is a method from the Grandparent class.")

# class Parent(Grandparent):
#     def method2(self):
#         print("This is a method from the Parent class.")

# class Child(Parent):
#     def method3(self):
#         print("This is a method from the Child class.")


# obj = Child()
# obj.method1()  # From Grandparent
# obj.method2()  # From Parent
# obj.method3()  # From Child



#Hybrid inheitance

class Base:
    def method1(self):
        print("This is a method in the Base class.")

class Child1(Base):
    def method2(self):
        print("This is a method in the Child1 class.")

class Child2(Base):
    def method3(self):
        print("This is a method in the Child2 class.")

class GrandChild(Child1, Child2):
    def method4(self):
        print("This is a method in the GrandChild class.")

obj = GrandChild()
obj.method1()  # From Base
obj.method2()  # From Child1
obj.method3()  # From Child2
obj.method4()  # From GrandChild