class a ():
    classvar1 = "i am class A"
    def __init__(self):
        self.var1 = "i am inside class A's Constructor"
        self.classvar1 = "Instane of class A"
        self.special = "Special"

class b (a):
    classvar1 = "i am class B"
    def __init__(self):
        self.var1 = "i am inside class B's Constructor"
        self.classvar1 = "Instane of class B"
        super().__init__()

   

x = a()
y = b()
print(y.classvar1)