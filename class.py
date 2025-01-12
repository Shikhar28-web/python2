# self parameter is the referenceto thr current instance of the class, and is use to variable that belongs to the class
# self ka matlb vo object jis k lya ye call kiya jara h
class student:
    name='shikhar'
    roll_no=2415800076
    mobile=7011309036
    father_name='akshay kumar verma'
    def detail(self):
        print(f'{self.name} father name is {self.father_name}')


a=student()
b=student()
b.name="ram"
# a.name='verma'


print(b.name)
print(a.roll_no,a.name)
a.detail()