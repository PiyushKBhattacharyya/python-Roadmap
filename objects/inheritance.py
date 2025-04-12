class Fun:
    x = 0
    name = ''
    def __init__(self, name):
        self.name = name
        print(self.name, "construcyed")
    def fun(self):
        self.x += 1
        print(self.name, "count", self.x)
    
class Fun2(Fun):
    p = 0
    def don(self):
        self.p += 1
        self.fun()
        print(self.name, "points", self.p)
        
b = Fun("HI")
b.fun()
c = Fun2("BYE")
c.fun()
c.don()