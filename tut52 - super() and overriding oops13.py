class A:
    classVar1 = 'I am a class variable in class A'
    def __init__(self):
        self.var1 = 'I am inside class A\'s constructor'
        self.classVar1 = 'Instance variable in class A'
        self.special = 'Special var, this must be run even after overriding'

class B(A):
    classVar2 = 'I am in class B'
    def __init__(self):
        super().__init__()   # will run class A init (that's it)
        self.var1 = 'I am inside class B\'s constructor'
        self.classVar1 = 'Instance variable in class B'
        print(super().classVar1)   # will return classvar1 of class A

a = A()
b = B()

print(b.special)
print(b.var1)
print(b.classVar1)