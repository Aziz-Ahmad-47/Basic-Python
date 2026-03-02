class A:
    def sumA(self):
        print(10+50)
class B:
    def sumB(self):
        print(20+20)
class C(A,B):
    def sumC(self):
        print(10+20)

c=C()
c.sumA()
c.sumB()
c.sumC()