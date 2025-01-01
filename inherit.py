class Parent(object):
    def spam(self):
        print('Parent.spam')

class A(Parent):
    def spam(self):
        print('A.spam')
        super().spam()

class B(A):
    def spam(self):
        print('B.spam')
        super().spam()

class C(Parent):
    def spam(self):
        print('C.spam')
        super().spam()

class D(Parent):
    def spam(self):
        print('D.spam')
        super().spam()

class E(A, C, D):
    pass

class F(D, A, C):
    pass

# super method calls the class based on the __mro__ order.

#e = E()
#e.spam()

#E.__mro__

#f = F()
#f.spam()
#F.__mro__

