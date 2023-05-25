class Dad:
    basketball = 1

class Son(Dad):
    dance = 2
    def isdance(self):
        return f"yes i can dance {self.dance} no. of times"

class GrandSon(Son):
    dance = 6
    def isdance(self):
        return f"yes i can dance {self.dance} no. of times" #overwrite Son class

a = Dad()
b = Son()
c = GrandSon()
print(c.isdance())
print(c.basketball)
