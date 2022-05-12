# OBTENER LAS COORDENADAS PARA UNA CURVA ELIPTICA
# OBTENER LA TABLA

# CAMBIAR PARAMETROS
zi = 29
z = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]
a = 4
b = 6

tabla = []
for y in z:
    y2 = (y**2)%zi
    tabla.append(y2)

# TABLA DE Y | Y**2
tablay2 = []
i = 0
print("Tabla de equivalencias de 'y' y 'y**2'")
for w in tabla:
    print(i,'|',w)
    tablay2.append(w)
    i += 1


# COORDENADAS DE LA CURVA ELIPTICA
for x in z:
    y2 = (x)**3+a*(x)+b
    print()
    print('if x = ',x,'y2 = ', y2%zi)
    yy2 = y2 % zi
    for t in tablay2:
        if t == yy2:
            try:
                pos1 = tablay2.index(t)
                print(x, ',', pos1)
                try:
                    pos2 = tablay2.index(t, pos1+1, zi)
                    print(x, ',', pos2)
                except:
                    print("solo existe una coordenada")
                break
            except:
                print("subindice", t, "no esta en lista")


