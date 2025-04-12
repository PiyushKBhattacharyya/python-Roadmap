class A():
    x = 0
    name =''
    def __init__(self, name):
        self.name = name
        print(self.name, 'constructed')
    def fun(self):
        self.x += 1
        print(self.name, 'count', self.x)
        
b = A('HI')
c= A('BYE')
b.fun()
c.fun()