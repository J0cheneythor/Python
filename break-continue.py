#Imprimir solo las letras a
for letra in "Holanda":
    if letra == "a":
        print(letra)
        #Para imprimir la primera letra a
        break
else: 
    print("Fin ciclo for") 
print("Continua el programa")

#imprimir solo los numeros pares

# for i in range(6):
#     if( i % 2 == 0):
#       print(i)
#utilizando continue
for i in range(6):
    if( i % 2 != 0):
        continue
    print(i)