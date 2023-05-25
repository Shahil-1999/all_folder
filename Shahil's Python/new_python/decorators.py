def func(xyz):
    def rexce():
        print("executing")
        xyz()
        print("executed")
    return rexce

@func
def abc():
    print("apple")
abc()