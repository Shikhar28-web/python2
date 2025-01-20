# class student:
#     count=0

# # student.count = 23
# obj1 = student()
# obj2=student()
# obj1.count=20
# print(student.count)




class student:
    count= 0
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
        student.count +=1
    @classmethod
    def get_count(cls):
        return f'student count = {cls.count}'


obj1=student("shikhar",27)
obj2=student("shivi",90)

print(obj1.get_count())
