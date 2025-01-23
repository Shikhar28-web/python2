class student:
    count=0
    _section='EB'

    def method1(self):
        return 'Method1'
    
    def _method2(self):
        return 'Method2'
    
    def __method3(self):
        return 'Method3'
    

obj1=student()
print(obj1.count)
print(obj1._section)
print(obj1.method1())
print(obj1._method2())
print(obj1.__method3())
