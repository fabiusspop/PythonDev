# Method Resolution Order (MRO)
# uses DFS
class A:
    num = 10

class B(A):
    pass

class C(A):
    num = 1

class D(B, C):
    pass

print(D.num)
print(D.mro())
D.num  # D --> B --> C --> A --> obj
D.__str__
print("-------------")

class X: pass
class Y: pass
class Z: pass
class A(X, Y): pass
class B(Y, Z): pass
class M(B, A, Z): pass

print(M.__mro__)  # uses DEPTH FIRST SEARCH (DFS)


