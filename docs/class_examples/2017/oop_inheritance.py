

class A(object):
    def __init__(self, x):
        self.x = x
    
    def foo(self):
        print "in A.foo", type(self)
        return self.x

class A2(object):
    def __init__(self, x2):
        self.x2 = x2
    
    def foo(self):
        print "in A2.foo", type(self)
        return self.x2


class B(A):
    def __init__(self, x, y):
        A.__init__(self, x)
        self.y=y
        
    def bar(self):
        print "in B.bar"
        
class C(A, A2):
    def __init__(self):
        A.__init__(self, 6)
        A2.__init__(self, 7)
        
    def foo(self):
        print "C.foo calls both"
        x = A.foo(self)
        x2 = A2.foo(self)
        return x + x2 

a=A(2)
b=B(3, 8)
a.foo()
b.foo()
b.bar()
print b.x

print "!!!!!!"
c=C()
print c.x, c.x2
print c.foo()

class MyA(A):
    def foo(self, *args, **kwargs):
        print args, kwargs
        ret = A.foo(self, *args, **kwargs)
        print ret
        return ret

mya = MyA(3)
mya.foo()
