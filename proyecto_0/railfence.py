def railfence():
    """
    Menú que permite al usuario cifrar o descifrar un texto.
    -Entradas y restricciones:
    -op = Es un string que debe tener un número del 1 al 3.
    -textoInicial = String del texto a cifrar sin usar signos de puntuación ni números.
    -Salidas:
    -El texto debidamente cifrado o descifrado, dependiendo de la opción elegida por el usuario.
    """
    op = "0"
    while op != "3":
        print("Cifrado Rail Fence")
        print("1) Cifrado")
        print("2) Descifrado")
        print("3) Salir")
        op = input("Dígite la opción que desea usar: ")
        if op == "1":
            textoInicial = ingresaString("Ingrese su texto a cifrar: ")
            print("Su texto cifrado es: " + railfenceCod(textoInicial))
            input()
        elif op == "2":
            textoInicial = ingresaString("Ingrese su texto a descifrar: ")
            print("Su texto descifrado es: " + railfenceDec(textoInicial))
            input()
        elif op != "3":
            op = input("Dígite una opción válida: ")
    imprimirMensajeDespedida()

def railfenceCod(texto):
    """
    Subrutina que se encarga de cifrar un texto usando el método Rail Fence.
    Entradas y restricciones:
    -texto = String del texto a cifrar sin usar signos de puntuación ni números.
    Salidas:
    -textoCifrado: El string texto cifrado usando el método Rail Fence.
    """
    while len(texto) % 4 != 0:
        texto += " "
    texto = texto.replace(" ","-")
    superior = ""
    central = ""
    inferior = "" 
    for i in range(0,len(texto)):
        if i % 4 == 0:
            superior += texto[i]
        elif i % 2 != 0:
            central += texto[i]
        elif i % 2 == 0:
            inferior += texto[i]
    texto = superior + central + inferior
    textoCifrado = ""
    i = 0
    while i != len(texto):
        if (i - 4) % 5 == 0:
            textoCifrado += texto[i] + " "
        else:
            textoCifrado += texto[i]
        i += 1
    return textoCifrado

def railfenceDec(texto):
    """
    Subrutina que se encarga de descifrar un texto usando el método Rail Fence.
    Entradas y restricciones:
    -texto = String del texto a descifrar sin usar signos de puntuación ni números.
    Salidas:
    -textoCifrado: El string texto descifrado usando el método Rail Fence.
    """
    texto = texto.replace(" ","")
    superior = ""
    central = ""
    inferior = ""
    for i in range(0,len(texto)):
        if len(superior) < len(texto) / 4:
            superior += texto[i]
        elif len(central) < len(texto) / 2:
            central += texto[i]
        else:
            inferior += texto[i]
    textoCifrado = ""
    iSuperior = 0
    iCentral = 0
    iInferior = 0
    for i in range(0,len(texto)):
        if i % 4 == 0:
            textoCifrado += superior[iSuperior]
            iSuperior += 1
        elif i % 2 != 0:
            textoCifrado += central[iCentral]
            iCentral += 1
        elif i % 2 == 0:
            textoCifrado += inferior[iInferior]
            iInferior += 1
    textoCifrado = textoCifrado.replace("-"," ")
    textoCifrado = textoCifrado.strip()
    return textoCifrado

def ingresaString(mensaje):
    """
    Subrutina que indica si el valor ingresado es un string o no. En caso de no ser
    un string, entonces vuelve a solicitar el valor hasta cumplir con la verificación.
    Entradas y restricciones:
    -caracteres: Cadena de texto.
    Salidas: caracteres sin mayúsculas ni espacios.
    """
    caracteres = input(mensaje)
    if mensaje == "Ingrese su texto a cifrar: ":
        while not caracteres.replace(" ","").isalpha():
            caracteres = input("Sólo se permiten letras: ")
    else:
        textoVerifica = caracteres.replace("-"," ")
        while not textoVerifica.replace(" ","").isalpha():
            caracteres = input("Ingrese un mensaje válido: ")
            textoVerifica = caracteres.replace("-"," ")
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