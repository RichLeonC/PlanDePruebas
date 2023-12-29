alfabeto = "abcdefghijklmnñopqrstuvwxyz"

def cesar():
    """
    Menú que permite al usuario cifrar o descifrar un texto.
    -Entradas y restricciones:
    -op = Es un string que debe tener un número del 1 al 3.
    -textoInicial = String del texto a cifrar sin usar signos de puntuación ni números.
    -Desplazamiento = Número entero.
    -Salidas:
    -El texto debidamente cifrado o descifrado, dependiendo de la opción elegida por el usuario.
    """
    op = "0"
    while op != "3":
        print("Cifrado César")
        print("1) Cifrado")
        print("2) Descifrado")
        print("3) Volver")
        op = input("Dígite la opción que desea usar: ")
        if op == "1":
            textoInicial = ingresaString("Ingrese su texto a cifrar: ")
            desplazamiento = ingresaInt()
            print("Su texto cifrado es: " + cesarCod(textoInicial,desplazamiento))
            input()
        elif op == "2":
            textoInicial = ingresaString("Ingrese su texto a descifrar: ")
            desplazamiento = ingresaInt()
            print("Su texto descifrado es: " + cesarDec(textoInicial,desplazamiento))
            input()
        elif op != "3":
            op = input("Dígite una opción válida: ")
    imprimirMensajeDespedida()

def cesarCod(texto, desplazamiento):
    """
    Subrutina que se encarga de cifrar un texto usando el método César.
    Entradas y restricciones:
    -texto = String del texto a cifrar sin usar signos de puntuación ni números.
    -desplazamiento: Un número entero.
    Salidas:
    -textoFinal: El string texto cifrado por medio del método César.
    """
    global alfabeto
    textoFinal = ""
    for letraTexto in texto:
        if letraTexto == " ":
            textoFinal += " "
        for letraAlfabeto in alfabeto:
            if letraTexto == letraAlfabeto:
                textoFinal += alfabeto[(alfabeto.index(letraTexto) + desplazamiento) % 27]
    return textoFinal

def cesarDec(texto, desplazamiento):
    """
    Subrutina que se encarga de descifrar un texto usando el método César.
    Entradas y restricciones:
    -texto = String del texto a descifrar sin usar signos de puntuación ni números.
    -desplazamiento: Un número entero.
    Salidas:
    -textoFinal: El string texto descifrado por medio del método César.
    """
    global alfabeto
    textoFinal = ""
    for letraTexto in texto:
        if letraTexto == " ":
            textoFinal += " "
        for letraAlfabeto in alfabeto:
            if letraTexto == letraAlfabeto:
                textoFinal += alfabeto[(alfabeto.index(letraTexto) - desplazamiento) % 27]
    return textoFinal

def ingresaString(mensaje):
    """
    Subrutina que indica si el valor ingresado es un string o no. En caso de no ser
    un string, entonces vuelve a solicitar el valor hasta cumplir con la verificación.
    Entradas y restricciones:
    -caracteres: Cadena de texto sin utilizar signos de puntuación a excepción de tildes y diéresis en la u.
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

def ingresaInt():
    """
    Subrutina que indica si el valor ingresado es numérico o no. En caso de no ser
    un numérico, entonces vuelve a solicitar el valor hasta cumplir con la verificación.
    Entradas y restricciones:
    -num: Un número entero.
    Salidas: El número que fue ingresado como string convertido en entero.
    """
    num = input("Dígite su desplazamiento: ")
    while not num.lstrip("-").isnumeric():
        num = input("Por favor, ingrese un valor válido: ")
    return int(num)

def imprimirMensajeDespedida():
    """
    Subrutina que imprime un mensaje de despedida.
    Entradas: Ninguna.
    Salidas: El mensaje de despedida.
    Restricciones: Ninguna.
    """
    print("Regresando al menú principal.")
    input()