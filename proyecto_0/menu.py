import cesar
import monoalfabetico_palabraclave
import vigenere
import playfair
import railfence

def main():
    """
    Menú que se encarga de dirigir al usuario al método de cifrado de su preferencia.
    -Entradas y restricciones:
    -op = Es un string que debe tener un número del 1 al 6.
    -Salidas: Ejecución de la función que llama al método de cifrado deseado.
    """
    print("Bienvenido, aquí podrá encontrar diversos sistemas de cifrado que puede utilizar.")
    op = "0"
    while op != "6":
        print("Menú principal")
        print("1) Cifrado César")
        print("2) Cifrado monoalfabético con palabra clave")
        print("3) Cifrado Vigenere")
        print("4) Cifrado Playfair modificado")
        print("5) Cifrado Rail Fence")
        print("6) Salir")
        op = input("Dígite la opción que desea usar: ")
        if op == "1":
            cesar.cesar()
        elif op == "2":
            monoalfabetico_palabraclave.monoAlfabeticoPalabraClave()
        elif op == "3":
            vigenere.vigenere()
        elif op == "4":
            playfair.playfair()
        elif op == "5":
            railfence.railfence()
        elif op != "6":
            op = input("Dígite una opción válida")
    imprimirMensajeDespedida()

def imprimirMensajeDespedida():
    """
    Subrutina que imprime un mensaje de despedida.
    Entradas: Ninguna.
    Salidas: El mensaje de despedida.
    Restricciones: Ninguna.
    """
    print("Gracias por usar este programa.")
    input()

main()