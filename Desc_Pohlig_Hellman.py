# DESCIFRADO POHLIG-HELLMAN}
#ABECEDARIO
# tarea 13

lista = []
listacif = [685,0,323,934,997,352,535,11,352,323,323,32,0,644,32,11]
listades = []
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
palabrades = []
p = 1013
e =5
# ENCONTRAR D CON ALGORITMO EUCLIDEANO
d = 405

for x in listacif:
    resultado2 = (x ** d) % (p)
    print(x, "**", d, "mod", p, "=", resultado2,"=",alfabeto[resultado2])
    listades.append(resultado2)
print()


for y in listades:
    palabrades.append(alfabeto[y])

print(palabrades)
