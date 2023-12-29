alfabetoOriginal = "abcdefghijklmnñopqrstuvwxyz"

def playfair():
    """
    Menú que permite al usuario cifrar o descifrar un texto.
    -Entradas y restricciones:
    -op = Es un string que debe tener un número del 1 al 3.
    -textoInicial = String del texto a cifrar sin usar signos de puntuación ni números.
    -palabraClave = Una sola palabra, sin espacios ni signos de puntuación.
    -Salidas:
    -El texto debidamente cifrado o descifrado, dependiendo de la opción elegida por el usuario.
    """
    op = "0"
    while op != "3":
        print("Cifrado PlayFair modificado")
        print("1) Cifrado")
        print("2) Descifrado")
        print("3) Salir")
        op = input("Dígite la opción que desea usar: ")
        if op == "1":
            textoInicial = ingresaString("Dígite su texto a cifrar: ","")
            palabraClave = ingresaString("Dígite su palabra clave: ","")
            print("Su texto cifrado es: " + playfairCod(textoInicial, palabraClave))
            input()
        elif op == "2":
            palabraClave = ingresaString("Dígite su palabra clave: ","")
            textoInicial = ingresaString("Dígite su texto a descifrar: ",palabraClave)
            print("Su texto descifrado es: " + playfairDec(textoInicial,palabraClave))
            input()
        elif op != "3":
            op = input("Dígite una opción válida: ")
    imprimirMensajeDespedida()

def playfairCod(texto, palabra):
    """
    Subrutina que se encarga de cifrar un texto.
    Entradas y restricciones:
    -texto = String del texto a cifrar sin usar signos de puntuación ni números.
    -palabra: Una sola palabra clave, sin espacios ni signos de puntuación.
    Salidas:
    -totalPalabras: El string texto cifrado por medio de desplazamientos en el alfabeto.
    """
    matriz = crearMatriz(palabra)
    textoConvertido = ""
    i = 0
    while i < len(texto):
        if i > 0 and texto[i] != " ":
            if texto[i-1] == texto[i]:
                textoConvertido += "1"
        textoConvertido += texto[i]
        i += 1
    textoUsar = textoConvertido.split()
    for palabraTexto in textoUsar:
        palabraInsertar = palabraTexto
        if len(palabraTexto) % 2 != 0:
            palabraInsertar = palabraTexto + "1"
        textoUsar.insert(textoUsar.index(palabraTexto),palabraInsertar)
        textoUsar.remove(palabraTexto)
    totalPalabras = []
    for palabrasTexto in textoUsar:
        totalPalabras.append(palabraCod(palabrasTexto,matriz))
    return " ".join(totalPalabras)

def palabraCod(textoUsar, matriz):
    """
    Subrutina que se encarga de cifrar una palabra por medio del método PlayFair modificado.
    Entradas y restricciones:
    -textoUsar = Una única palabra. String, sin espacios y de longitud par.
    -matriz: Una lista que contiene 30 caracteres en agrupaciones de 5 letras por cada índice.
    Salidas:
    -textoCifrado: El texto cifrado por medio del método PlayFair modificado.
    """
    posiciones = []
    for palabraTexto in textoUsar:
        for letra in palabraTexto:
            for fila in matriz:
                if letra in fila:
                    posiciones.append((matriz.index(fila),matriz[matriz.index(fila)].index(letra)))
    textoCifrado =""
    i = 0
    while i < len(posiciones):
        pareja1 = posiciones[i]
        pareja2 = posiciones[i+1]
        if pareja1[0] != pareja2[0] and pareja1[1] != pareja2[1]:
            textoCifrado += matriz[pareja1[0]][pareja2[1]] + matriz[pareja2[0]][pareja1[1]]
        elif pareja1 [0] == pareja2[0] and pareja1[1] != pareja2[1]:
            if pareja1[1] == 4:
                pos1 = 0
            else:
                pos1 = pareja1[1]+1
            if pareja2[1] == 4:
                pos2 = 0
            else:
                pos2 = pareja2[1]+1
            textoCifrado += matriz[pareja1[0]][pos1] + matriz[pareja2[0]][pos2]
        elif pareja1 [0] != pareja2[0] and pareja1[1] == pareja2[1]:
            if pareja1[0] == 5:
                pos1 = 0
            else:
                pos1 = pareja1[0]+1
            if pareja2[0] == 5:
                pos2 = 0
            else:
                pos2 = pareja2[0]+1
            textoCifrado += matriz[pos1][pareja1[1]] + matriz[pos2][pareja2[1]]
        i += 2
    return textoCifrado

def playfairDec(texto, palabra):
    """
    Subrutina que se encarga de descifrar un texto por medio del método PlayFair modificado.
    Entradas y restricciones:
    -texto = String del texto a descifrar sin usar signos de puntuación ni números.
    -palabra: Una sola palabra clave, sin espacios ni signos de puntuación.
    Salidas:
    -totalPalabras: El string texto descifrado por medio del método PlayFair modificado.
    """
    matriz = crearMatriz(palabra)
    textoUsar = texto.split()
    for palabraTexto in textoUsar:
        palabraInsertar = palabraTexto
        if len(palabraTexto) % 2 != 0:
            palabraInsertar = palabraTexto + "1"
        textoUsar.insert(textoUsar.index(palabraTexto),palabraInsertar)
        textoUsar.remove(palabraTexto)
    totalPalabras = []
    for palabrasTexto in textoUsar:
        totalPalabras.append(palabraDec(palabrasTexto,matriz))
    return " ".join(totalPalabras)

def palabraDec(textoUsar, matriz):
    """
    Subrutina que se encarga de descifrar una palabra
    Entradas y restricciones:
    -textoUsar = Una única palabra. String, sin espacios y de longitud par.
    -matriz: Una lista que contiene 30 caracteres en agrupaciones de 5 letras por cada índice.
    Salidas:
    -textoCifrado: El texto descifrado por medio del método PlayFair modificado.
    """
    posiciones = []
    for palabraTexto in textoUsar:
        for letra in palabraTexto:
            for fila in matriz:
                if letra in fila:
                    posiciones.append((matriz.index(fila),matriz[matriz.index(fila)].index(letra)))
    textoCifrado =""
    i = 0
    while i < len(posiciones):
        pareja1 = posiciones[i]
        pareja2 = posiciones[i+1]
        if pareja1[0] != pareja2[0] and pareja1[1] != pareja2[1]:
            primeraLetra = matriz[pareja1[0]][pareja2[1]]
            if primeraLetra.isnumeric():
                primeraLetra = ""
            segundaLetra = matriz[pareja2[0]][pareja1[1]]
            if segundaLetra.isnumeric():
                segundaLetra = ""
            textoCifrado += primeraLetra + segundaLetra
        elif pareja1 [0] == pareja2[0] and pareja1[1] != pareja2[1]:
            if pareja1[1] == 0:
                pos1 = 4
            else:
                pos1 = pareja1[1]-1
            if pareja2[1] == 0:
                pos2 = 4
            else:
                pos2 = pareja2[1]-1
            primeraLetra = matriz[pareja1[0]][pos1]
            if primeraLetra.isnumeric():
                primeraLetra = ""
            segundaLetra = matriz[pareja2[0]][pos2]
            if segundaLetra.isnumeric():
                segundaLetra = ""
            textoCifrado += primeraLetra + segundaLetra
        elif pareja1 [0] != pareja2[0] and pareja1[1] == pareja2[1]:
            if pareja1[0] == 0:
                pos1 = 5
            else:
                pos1 = pareja1[0]-1
            if pareja2[0] == 0:
                pos2 = 5
            else:
                pos2 = pareja2[0]-1
            primeraLetra = matriz[pos1][pareja1[1]]
            if primeraLetra.isnumeric():
                primeraLetra = ""
            segundaLetra = matriz[pos2][pareja2[1]]
            if segundaLetra.isnumeric():
                segundaLetra = ""
            textoCifrado +=  primeraLetra + segundaLetra
        i += 2
    return textoCifrado

def crearMatriz(palabra):
    """
    Subrutina que se encarga de crear una matriz que se usará para el
    cifrado y descifrado de datos.
    Entradas y restricciones:
    -palabra: Una sola palabra clave, sin espacios ni signos de puntuación.
    Salidas:
    -nuevaMatriz: Una lista que funcionará como matriz, la cual contendrá
    el alfabeto organizando primero la palabra ingresada por el usuario y
    luego el resto del alfabeto, sin repetir letras y rellenando al final
    con números a partir del 1 hasta que hayan 30 caracteres en total y se
    hagan agrupaciones de 5 letras por cada índice de la lista.
    """
    global alfabetoOriginal
    nuevoAlfabeto = ""
    for letra in palabra:
        if not letra in nuevoAlfabeto:
            nuevoAlfabeto += letra
    for letraAlfabeto in alfabetoOriginal:
        for letraTexto in nuevoAlfabeto:
            if letraTexto == letraAlfabeto:
                letraAlfabeto = ""
        nuevoAlfabeto += letraAlfabeto
    letraExtra = 1
    while len(nuevoAlfabeto) != 30:
        nuevoAlfabeto += str(letraExtra)
        letraExtra += 1
    p = 0
    alfabetoDivido = ""
    for letra in nuevoAlfabeto:
        if p != 0 and p % 5 == 0:
            alfabetoDivido += " " + letra
        else:
            alfabetoDivido += letra
        p += 1
    nuevaMatriz = alfabetoDivido.split()
    return nuevaMatriz

def ingresaString(mensaje,palabra):
    """
    Subrutina que indica si el valor ingresado es un string o no. En caso de no ser
    un string, entonces vuelve a solicitar el valor hasta cumplir con la verificación.
    Entradas y restricciones:
    -caracteres: Cadena de texto.
    Salidas: caracteres sin mayúsculas ni espacios.
    """
    global alfabetoOriginal
    if palabra == "":
        caracteres = input(mensaje)
        while not caracteres.replace(" ","").isalpha():
            caracteres = input("Ingrese un valor válido: ")
    else:
        matriz = crearMatriz(palabra)
        caracteres = input(mensaje)
        validacion = 0
        for letra in caracteres.replace(" ",""):
            if letra in "".join(matriz):
                validacion += 1
        while validacion < len(caracteres.replace(" ","")):
            validacion = 0
            caracteres = input("Dígite un texto válido: ")
            for letra in caracteres.replace(" ",""):
                if letra in "".join(matriz):
                    validacion += 1
    caracteres = caracteres.lower()
    caracteres = caracteres.replace("á", "a")
    caracteres = caracteres.replace("é", "e")
    caracteres = caracteres.replace("í", "i")
    caracteres = caracteres.replace("ó", "o")
    caracteres = caracteres.replace("ú", "u")
    caracteres = caracteres.replace("ü", "u")
    return caracteres

def imprimirMensajeDespedida():
    """
    Subrutina que imprime un mensaje de despedida.
    Entradas: Ninguna.
    Salidas: El mensaje de despedida.
    Restricciones: Ninguna.
    """
    print("Regresando al menú principal.")
    input()