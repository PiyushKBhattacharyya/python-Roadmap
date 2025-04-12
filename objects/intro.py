class A:
    x = 0
    def fun(self):
        self.x += 2
        print(self.x)

a = A()
a.fun()
a.fun()