class operador():

    def __init__(self,n1,n2,n3,n4,n5,n6):
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.n4 = n4
        self.n5 = n5
        self.n6 = n6


    def tiposOperadores(self):
        op1 =self.n1/self.n2
        op2 = self.n2//self.n1
        op3 = self.n3%self.n2
        op4 = self.n4//self.n5
        op5 = self.n5 / self.n6

        print(op1)
        print(op2)
        print(op3)
        print(op4)
        print(op5)

