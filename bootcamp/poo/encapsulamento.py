class Test_sem_prop:
    def __init__(self,x = None):
        self._x = x 
    def x(self):
        return self._x or 0
prop1 = Test_sem_prop()
print(prop1.x())

class Test_com_prop:
    def __init__(self,x = None):
        self._x = x 
    @property
    def x(self):
        return self._x or 0
    @x.setter
    def x(self,value):
        self._x = value
     
    
prop2 = Test_com_prop(10)
print(prop2.x)