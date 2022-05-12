# DESCIFRADO - HILL CIPHER


# MENSAJE ENCRIPTADO (DE 2 EN 2 LETRAS)
matriz = [15, 24]
# (1/DET(e))(ADJ(e transpuesta)
inversa = [21, 22,
           19, 18]

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '', '?', '!']

resultado1 = matriz[0]*inversa[0] + matriz[1]*inversa[2]
resultado2 = matriz[0]*inversa[1] + matriz[1]*inversa[3]

print(resultado1 % 29, ",", resultado2 % 29)

print(alfabeto[resultado1 % 29], ',', alfabeto[resultado2 % 29])
