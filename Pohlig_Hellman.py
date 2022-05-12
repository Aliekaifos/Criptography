# CIFRADO POHLIG-HELLMAN
# SIN ABECEDARIO

#MENSAJE
lista = [1,4,19,17,0,24,0,11]
listacif = []
listades = []

p = 181
e = 97
#SE NECESITA ENCONTRAR D (ALGORITMO EUCLIDEANO)
d = 13

print("Cifrar mensaje")
for  i in lista:
    resultado = (i**e)%(p)
    print(i, "**", e, "mod",p,"=", resultado)
    listacif.append(resultado)
print(listacif)
print()


print("Descifrar mensaje")
for x in listacif:
    resultado2 = (x ** d) % (p)
    print(x, "**", d, "mod", p, "=", resultado2)
    listades.append(resultado2)
print(listades)
