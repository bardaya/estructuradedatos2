class Complex:
    def _init_(self,realpart,imagpart):
        self.r=realpart
        self.i=imagpart
re=float(input("Ingrese la parte real: "))
im=float(input("Ingrese la parte imaginaria: "))
x= Complex(re, im)
x.r, x.i