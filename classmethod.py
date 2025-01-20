class student:
    count=0
    section='EB'

    def __init__(self,name):
        self.name=name
        student.count +=1
    @classmethod
    def disp_count(cls):
        return f' student count is {cls.count}'


# main code

obj1=student("monu")
obj1.count=100
obj2=student("sonu")
print(obj1.disp_count())