# self parameter is the referenceto thr current instance of the class, and is use to variable that belongs to the class
class sample:
    def __init__(self):
        print("shikhar")
        print(self)

    def disp(self):
        print("shikharsjdois")

obj1=sample()
print(obj1)
