class Persona:
    #this es más usado en un otros lenguajes pero se pueden usar los dos 
    def __init__(this, n, e, *v, **d):
        this.nombre = n
        this.edad = e
        this.valores = v
        this.diccionario = d
    def desplegar(this):
        print("Nombre:", this.nombre)
        print("Edad::", this.edad)
        print("Valores(tupla):",this.valores)
        print("Diccionario:",this.diccionario)
        
p1 = Persona("Juan",28)
print(p1.nombre)
print(p1.edad)

''' p2 = Persona("Jose Luis",21)
p2.desplegar()
 '''
p3 = Persona("Joche", 28, 2,4,5 )
p3.desplegar()

p4 = Persona("Paola",33 , 3,4,5,6, m="manzana", p="pera")

p4.desplegar()