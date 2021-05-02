class Aritmetica:
    """Es la clase que se utiliza para el procesamiento
    atirmetico"""
    def __init__(self, operando1, operando2):
        self.operando1 = operando1
        self.operando2 = operando2
    
    def  sumar(self):
        """Se realiza la operación con los atributos de 
        la clase"""
        return self.operando1 + self.operando2  
    def restar(self):
        return self.operando1 - self.operando2
    
    def multi(self):
        return self.operando1 * self.operando2
    
    def div(self):
        if(self.operando2 == 0):
            print("MATH ERROR")
        else:
            return self.operando1 / self.operando2
        

#Creamos un objeto 
arith = Aritmetica(5 , 5)
arith2 = Aritmetica(5 , 5)
arith3 = Aritmetica(5 , 5)
arith4 = Aritmetica(5 , 0)


print("Resultado de la suma:",arith.sumar())
print("Resultado de la resta:",arith2.restar())
print("Resultado de la Multiplicación:",arith3.multi())
print("Resultado de la División:",arith4.div())

