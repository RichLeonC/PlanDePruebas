alfabetoOriginal = "abcdefghijklmnñopqrstuvwxyz"

def vigenere():
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
        print("Cifrado Vigenere")
        print("1) Cifrado")
        print("2) Descifrado")
        print("3) Salir")
        op = input("Dígite la opción que desea usar: ")
        if op == "1":
            textoInicial = ingresaString("Dígite su texto a cifrar: ")
            palabraClave = ingresaString("Dígite su palabra clave: ")
            print("Su texto cifrado es: " + vigenereCod(textoInicial,palabraClave))
            input()
        elif op == "2":
            textoInicial = ingresaString("Dígite su texto a descifrar: ")
            palabraClave = ingresaString("Dígite su palabra clave: ")
            print("Su texto cifrado es: " + vigenereDec(textoInicial,palabraClave))
            input()
        elif op != "3":
            op = input("Dígite una opción válida: ")
    imprimirMensajeDespedida()

def vigenereCod(texto, palabra):
    """
    Subrutina que se encarga de cifrar un texto usando el método vigenere.
    Entradas y restricciones:
    -texto = String del texto a cifrar sin usar signos de puntuación ni números.
    -palabra: Una sola palabra clave, sin espacios ni signos de puntuación.
    Salidas:
    -textoFinal: El string texto cifrado por medio del método vigenere.
    """
    global alfabetoOriginal
    cifrador = crearCifrador(texto, palabra)
    textoFinal = ""
    p = 0
    for letraTexto in texto:
        if letraTexto == " ":
            textoFinal += " "
            p += 1
        for letraAlfabeto in alfabetoOriginal:
            if letraTexto == letraAlfabeto:
                textoFinal += alfabetoOriginal[(alfabetoOriginal.index(letraTexto) + alfabetoOriginal.index(cifrador[p])) % 27]
                p += 1
    return textoFinal

def vigenereDec(texto, palabra):
    """
    Subrutina que se encarga de descifrar un texto usando el método vigenere.
    Entradas y restricciones:
    -texto = String del texto a descifrar sin usar signos de puntuación ni números.
    -palabra: Una sola palabra clave, sin espacios ni signos de puntuación.
    Salidas:
    -textoFinal: El string texto cifrado por medio del método vigenere.
    """
    global alfabetoOriginal
    cifrador = crearCifrador(texto, palabra)
    textoFinal = ""
    p = 0
    for letraTexto in texto:
        if letraTexto == " ":
            textoFinal += " "
            p += 1
        for letraAlfabeto in alfabetoOriginal:
            if letraTexto == letraAlfabeto:
                textoFinal += alfabetoOriginal[(alfabetoOriginal.index(letraTexto) - alfabetoOriginal.index(cifrador[p])) % 27]
                p += 1
    return textoFinal
    
def crearCifrador(texto, palabra):
    """
    Subrutina que se encarga de crear una cadena de texto que repita la palabra
    clave en el mismo orden que el texto ingresado el usuario para cifrar.
    Entradas y restricciones:
    -texto = String del texto sin usar signos de puntuación ni números.
    -palabra: Una sola palabra clave, sin espacios ni signos de puntuación.
    Salidas:
    -cifrador: Un string del mismo tamaño que el texto ingresado por el usuario
    solo que únicamente repite la palabra clave
    """
    cifrador = ""
    p = 0
    for n in texto:
        if n == " ":
            cifrador += " "
        else:
            if p == len(palabra):
                p = 0
            cifrador += palabra[p]
            p += 1
    return cifrador

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