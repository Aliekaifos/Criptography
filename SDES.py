from __future__ import print_function
import base64
import sys
import re
import pyfiglet
import itertools

result = pyfiglet.figlet_format("S-DES",  font="slant")
print(result)
# GENERACION DE LLAVES
def generacionDeLlaves():
    IP = [2, 4, 1, 6, 3, 9, 0, 8, 7, 5]
    p10 = []
    key = input('llave: ')
    keylist = list(key)

    # Permutacion inicial (Primeros al final y segundos al principio)
    for elemento in IP:
        p10.append(int(keylist[elemento]))

    # L y R
    KL = []
    KR = []

    for l in range(0, 5):
        KL.append(p10[l])

    for r in range(5, 10):
        KR.append(p10[r])

    # Movimiento circular a la izq
    CIRC = [1, 2, 3, 4, 0]
    Lcirc = []
    Rcirc = []
    for x in CIRC:
        Lcirc.append(KL[x])
        Rcirc.append(KR[x])

    # Las juntamos y le damos en su madre a 2
    posiciones = [9, 8]
    juntas = []

    for elem in Lcirc:
        juntas.append(elem)
    for elem in Rcirc:
        juntas.append(elem)

    for i in posiciones:
        juntas.pop(i)

    k1 = juntas

    # Generacion de k2
    Lcirc1 = []
    Rcirc1 = []
    CIRC1 = [2, 3, 4, 0, 1]

    for i in CIRC1:
        Lcirc1.append(Lcirc[i])
        Rcirc1.append(Rcirc[i])

    k2 = []

    for x in Lcirc1:
        k2.append(x)
    for x in Rcirc1:
        k2.append(x)

    # Le damos en su madre a 2
    for i in posiciones:
        k2.pop(i)

    generacionDeLlaves.k1 = k1
    generacionDeLlaves.k2 = k2

    # Ya tenemos k1 y k2
mensajes = ['11010011','10101010','11111111','00000000']
# S-DES
def sdes(k1, k2):

    c_list = ''
    IPm = [1, 5, 2, 0, 3, 7, 4, 6]
    IPinv = [3, 0, 2, 4, 6, 1, 7, 5]

    for elemento in mensajes:
        elementobin = elemento

        perm = ""
        for i in IPm:
            perm += elemento[i]

        # dividimos en L y R
        mL = []
        mR = []
        mR1 = []

        for x in range(0, 4):
            mL.append(int(perm[x]))
        for x in range(4, 8):
            mR.append(int(perm[x]))
            mR1.append(int(perm[x]))
        # Posteriormente, usaremos mR sin los bits agregados, por eso creamos otra lista


        # Trabajamos con R
        i = 0
        xorR = []
        agregar = [1, 0, 1, 0]

        #Expansion 1
        for x in mR:
            mR.append(x)
            if len(mR) == 8:
                break

        for bit in mR:
            xor = bit ^ k1[i]
            i = i + 1
            xorR.append(xor)

        sbox0 = {'0000': '01', '0001': '00', '0010': '11', '0011': '10',
                 '0100': '11', '0101': '10', '0110': '01', '0111': '00',
                 '1000': '00', '1001': '10', '1010': '01', '1011': '11',
                 '1100': '00', '1101': '01', '1110': '11', '1111': '10'}

        sbox1 = {'0000': '00', '0001': '01', '0010': '10', '0011': '11',
                 '0100': '10', '0101': '00', '0110': '01', '0111': '11',
                 '1000': '11', '1001': '00', '1010': '01', '1011': '10',
                 '1100': '10', '1101': '01', '1110': '00', '1111': '11'}

        # Dividimos mR en izq y der

        mRizq = []
        mRder = []
        ordensbox = [0, 3, 1, 2]

        for j in range(0, 4):
            mRizq.append(str(xorR[j]))

        for j in range(4, 8):
            mRder.append(str(xorR[j]))

        # Acomodamos en x1,x4,x2,x3 cada lado

        mRizqstr = ''
        mRderstr = ''

        for num in ordensbox:
            mRizqstr += mRizq[num]
        for num in ordensbox:
            mRderstr += mRder[num]

        # Se aplica la sbox0 y se concatenan los resultados de ambos lados

        res = sbox0[mRizqstr] + sbox0[mRderstr]
        resLIST = list(res)
        resLIST = list(map(int, resLIST))

        # Aplicamos permutacion P4 al resultado concatenado de la aplicacion de la sbox
        p4 = [1, 3, 2, 0]

        resLIST_p4 = []

        for num in p4:
            resLIST_p4.append(resLIST[num])
        Lprima = []
        Lprima1 = []
        # Agregamos Lprima1 para usarla despues
        # porque a Lprima le agregamos 4 bits en el proceso

        for bit in range(0, 4):
            xor = mL[bit] ^ resLIST_p4[bit]
            Lprima.append(xor)
            Lprima1.append(xor)
        # Ahroa trabajamos ahora con Lprima
        xorL = []
        agregar = [1, 0, 1, 0]

        #Expansion 2
        for j in Lprima:
            Lprima.append(j)
            if len(Lprima) == 8:
                break

        i = 0

        for bit in Lprima:
            xor = bit ^ k2[i]
            i = i + 1
            xorL.append(xor)

        # Dividimos Lprima en izq y der y aplicamos sbox0
        LprimaIZQ = []
        LprimaDER = []
        ordensbox = [0, 3, 1, 2]

        for num in range(0, 4):
            LprimaIZQ.append(str(xorL[num]))
        for num in range(4, 8):
            LprimaDER.append(str(xorL[num]))

        # Acomodamos los bits m1,m4,m2,m3

        LprimaIZQ_str = ''
        LprimaDER_str = ''

        for elemento in ordensbox:
            LprimaIZQ_str += LprimaIZQ[elemento]
        for elemento in ordensbox:
            LprimaDER_str += LprimaDER[elemento]

        # Se aplica la sbox0 y se concatenan los resultados

        res1 = sbox0[LprimaIZQ_str] + sbox0[LprimaDER_str]
        res1LIST = list(res1)
        res1LIST = list(map(int, res1LIST))
        p4 = [1, 3, 2, 0]

        # Aplicamos permutacion p4
        res1LIST_p4 = []
        for numero in p4:
            res1LIST_p4.append(res1LIST[numero])

        Rprima = []

        for bit in range(0, 4):
            xor = mR1[bit] ^ res1LIST_p4[bit]
            Rprima.append(xor)
        Rprima_y_Lprima = []

        for num in Rprima:
            Rprima_y_Lprima.append(num)
        for num in Lprima1:
            Rprima_y_Lprima.append(num)

        # Hacemos IP^-1
        c = ''
        for i in IPinv:
            c += str(Rprima_y_Lprima[i])
        c_list = c_list + c

    sdes.c_list = c_list
    sys.stdout.write(str(elementobin) + ' --> ' + str(c) + '\r')




op = input("Seleccione una opción a buscar [1]Encriptar/[2]Desencriptar/[3]Encriptacion doble: ")
while(op == str() or op.isalpha() or op.isspace() or int(op) < 0 or int(op) > 3):
        op = input("Seleccione una opción a buscar [1]Encriptar/[2]Desencriptar/[3]Encriptacion doble: ")

if(int(op) == 1):
    # ENCRIPTAR
    generacionDeLlaves()

    # IMAGEN A BASE64
    archivo = input("Introduzca path de archivo a encriptar (jpg/png): ")
    with open(archivo, 'rb') as binary_file:
        binary_file_data = binary_file.read()
        base64_encoded_data = base64.b64encode(binary_file_data)
        base64_message = base64_encoded_data.decode('utf-8')

    mensaje = bytes(base64_message, encoding='utf8')
    decoded = base64.decodebytes(mensaje)

    # BASE64 A BINARIO
    bina = "".join(["{:08b}".format(x) for x in decoded])

    # BINA INTO GROUPS OF 8
    mensajes = [bina[i:i + 8] for i in range(0, len(bina), 8)]

    k1 = generacionDeLlaves.k1
    k2 = generacionDeLlaves.k2

    print('[+] Encriptando...')
    sdes(k1, k2)
    c_list = sdes.c_list

    path_sinjpg = re.sub(r'.jpg', "", archivo)
    path_sinpng = re.sub(r'.png', "", path_sinjpg)

    hola = open(path_sinpng+'_encrip.jpg', 'w')
    hola.write(c_list)
    print('\n [+] Hecho!')

if(int(op) == 2):
    # DESENCRIPTAR

    generacionDeLlaves()

    mensajes = []
    bina1 = ''

    # EXTRAER EL BINARIO ERNCRIPTADO
    pathdes = input('Introduzca path a archivo encriptado: ')
    with open(pathdes) as file_enc:
        for line in file_enc:
            bina1 += line

    # BINA1 INTO GROUPS OF 8
    mensajes = [bina1[i:i+8] for i in range(0, len(bina1), 8)]

    k1 = generacionDeLlaves.k2
    k2 = generacionDeLlaves.k1

    print('[+] Desencriptando...')
    sdes(k1, k2)
    c_list = sdes.c_list

    # CONVERTIR BITS A IMAGEN
    def bitstring_to_bytes(s):
        v = int(s, 2)
        b = bytearray()
        while v:
            b.append(v & 0xff)
            v >>= 8
        return bytes(b[::-1])

    base = (bitstring_to_bytes(c_list))
    data = base64.b64encode(base)

    path_sintxt = re.sub(r'_encrip.jpg', "", pathdes)
    path_sinkey = re.sub(r'_encrip.png', "", path_sintxt)

    with open(path_sinkey+'_dec.jpg','wb') as file_to_save:
        decoded_image_data = base64.decodebytes(data)
        file_to_save.write(decoded_image_data)
    print('\n [+] Hecho!')

if(int(op) == 3):
    # Encriptar doble

    generacionDeLlaves()

    mensajes = []
    bina1 = ''

    # EXTRAER EL BINARIO ERNCRIPTADO
    pathdes = input('Introduzca path a archivo para encriptacion doble: ')
    with open(pathdes) as file_enc:
        for line in file_enc:
            bina1 += line

    # BINA1 INTO GROUPS OF 8
    mensajes = [bina1[i:i+8] for i in range(0, len(bina1), 8)]

    k1 = generacionDeLlaves.k1
    k2 = generacionDeLlaves.k2

    print('[+] Desencriptando...')
    sdes(k1, k2)
    c_list = sdes.c_list

    # CONVERTIR BITS A IMAGEN
    def bitstring_to_bytes(s):
        v = int(s, 2)
        b = bytearray()
        while v:
            b.append(v & 0xff)
            v >>= 8
        return bytes(b[::-1])

    base = (bitstring_to_bytes(c_list))
    data = base64.b64encode(base)

    path_sintxt = re.sub(r'_encrip.jpg', "", pathdes)
    path_sinkey = re.sub(r'_encrip.png', "", path_sintxt)

    with open(path_sinkey+'_encriptado-doble.jpg','wb') as file_to_save:
        decoded_image_data = base64.decodebytes(data)
        file_to_save.write(decoded_image_data)
    print('\n [+] Hecho!')
