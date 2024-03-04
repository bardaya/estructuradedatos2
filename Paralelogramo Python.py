class Paralelogramo:
    def __init__(self, base, altura):
        self.b = base
        self.h = altura
    def area(self):
        return self.b*self.h
    
ba = float(input("Ingrese la base: "))
alt = float(input("Ingrese la altura: "))
x = Paralelogramo(ba, alt)
print("El area es: ", x.area())