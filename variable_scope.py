# defination : Attributes that are shared across all instance of a class. they belong to the class itself and not any specific instance
# Scope: shared among all instance of class
# use case: used for data or properties that are comman to all object of class
# Declared: inside the class defination, but outside of any instance methods


class student:
    count=0         # class variable
    def __init__(self,name,rolln):
        self.name=name     # instance variable
        self.rolln=rolln

#print(student.count)
obj1=student('ravi',22)
obj2 = student('monu',43)
print(obj1.count)
print(obj2.count)


print(obj2.name)
print(obj2.rolln)