class Caja:
    def __init__(self,l,a,h):
        self.l = l
        self.a = a
        self.h = h
    def calcular_V(self):
        return self.l * self.a * self.h

print("Programa para calcular el Volumen de un caja \n")
largo = int(input("Ingresar el largo de la caja:"))
ancho = int(input("Ingresar el ancho de la caja:"))
alto  = int(input("Ingresar el alto de la caja:"))

caja = Caja(largo, ancho, alto)

print("El volimen de la caja es:",caja.calcular_V(),"cm^3")