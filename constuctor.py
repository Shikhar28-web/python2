# it tells class that i am giving this thing to it

class person:
    def __init__(self,n,o):
        print(" i am shikhar verma")
        self.name = n
        self.occ = o

    def info(self):
        print(f'{self.name} is a {self.occ}')

a=person("shikhar","engennier")
b=person("ram","developer")
a.info()
b.info()