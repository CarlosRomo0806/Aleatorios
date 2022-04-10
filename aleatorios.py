import nacl.utils

def numeroAleatorio(tamaño):
    return nacl.utils.random(tamaño)

def main():
    numero = numeroAleatorio(32)
    print(numero.hex())
    
def Interfaz():
    print("Números aleatorios con PyNacl")
    print("1. Comienza\n0. Terminar")
    opcion = int(input("Eliges: "))
    if opcion:
        main()
        return 1
    else:
        return 0

salir = 1
while salir:
    salir = Interfaz()