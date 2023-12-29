alfabetoOriginal = "abcdefghijklmnñopqrstuvwxyz"

def monoAlfabeticoPalabraClave():
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
        print("Cifrado monoalfabético con palabra clave")
        print("1) Cifrado")
        print("2) Descifrado")
        print("3) Salir")
        op = input("Dígite la opción que desea usar: ")
        if op == "1":
            textoInicial = ingresaString("Dígite su texto a cifrar: ")
            palabraClave = ingresaString("Dígite su palabra clave: ")
            print("Su texto cifrado es: " + monoCod(textoInicial,palabraClave))
            input()
        elif op == "2":
            textoInicial = ingresaString("Dígite su texto a descifrar: ")
            palabraClave = ingresaString("Dígite su palabra clave: ")
            print("Su texto descifrado es: " + monoDec(textoInicial,palabraClave))
            input()
        elif op != "3":
            op = input("Dígite una opción válida")
    imprimirMensajeDespedida()

def monoCod(texto, palabra):
    """
    Subrutina que se encarga de cifrar un texto usando el método
    monoalfabético con palabra clave.
    Entradas y restricciones:
    -texto = String del texto a cifrar sin usar signos de puntuación ni números.
    -palabra: Una sola palabra clave, sin espacios ni signos de puntuación.
    Salidas:
    -textoFinal: El string texto cifrado por medio del método
    monoalfabético con palabra clave.
    """
    global alfabetoOriginal
    alfabetoCodificado = crearAlfabeto(palabra)
    textoFinal = ""
    for letraTexto in texto:
        if letraTexto == " ":
            textoFinal += " "
        for letraAlfabeto in alfabetoOriginal:
            if letraTexto == letraAlfabeto:
                textoFinal += alfabetoCodificado[alfabetoOriginal.index(letraTexto)]
    return textoFinal

def monoDec(texto, palabra):
    """
    Subrutina que se encarga de descifrar un texto usando el método
    monoalfabético con palabra clave.
    Entradas y restricciones:
    -texto = String del texto a descifrar sin usar signos de puntuación ni números.
    -palabra: Una sola palabra clave, sin espacios ni signos de puntuación.
    Salidas:
    -textoFinal: El string texto descifrado por medio del método
    monoalfabético con palabra clave.
    """
    global alfabetoOriginal
    alfabetoCodificado = crearAlfabeto(palabra)
    textoFinal = ""
    for letraTexto in texto:
        if letraTexto == " ":
            textoFinal += " "
        for letraAlfabeto in alfabetoCodificado:
            if letraTexto == letraAlfabeto:
                textoFinal += alfabetoOriginal[alfabetoCodificado.index(letraTexto)]
    return textoFinal

def crearAlfabeto(palabra):
    """
    Subrutina que se encarga de organizar las letras del alfabeto
    a partir de una palabra ingresada.
    Entradas y restricciones:
    -palabra: Una sola palabra, sin espacios ni signos de puntuación.
    Salidas:
    -nuevoAlfabeto: Un nuevo alfabeto que es el resultado de organizar
    el alfabeto convencional al posicionar la palabra ingresada por
    el usuario al inicio y a partir de ahí colocar las demás letras
    del abecedario sin repetirlas.
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
    return nuevoAlfabeto

def ingresaString(mensaje):
    """
    Subrutina que indica si el valor ingresado es un string o no. En caso de no ser
    un string, entonces vuelve a solicitar el valor hasta cumplir con la verificación.
    Entradas y restricciones:
    -caracteres: Cadena de texto.
    Salidas: caracteres sin mayúsculas ni espacios.
    """
    caracteres = input(mensaje)
    while not caracteres.replace(" ","").isalpha():
        caracteres = input("Sólo se permiten letras: ")
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