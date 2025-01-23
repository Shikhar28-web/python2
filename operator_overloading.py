class custom:
    def __init__(self,value):
        self.value=value
    def __add__(self,other):
        if isinstance(other,custom):
            return self.value + other.value
        else:
            return custom(self.value+other)
    def __sub__(self,other):
        if isinstance(other,custom):
            return self.value - other.value
        else:
            return custom(self.value-other)
        
    def __mul__(self,other):
        if isinstance(other,custom):
            return self.value * other.value
        else:
            return custom(self.value*other)
    def __truediv__(self,other):
        if isinstance(other,custom):
            return self.value / other.value
        else:
            return custom(self.value/other)
    def __str__(self):
        return f'{self.value}'
    
    
    

    
# main code
a=custom(12)
b=custom(23)
ty=b
c=a+ty

print(c,type(c))