#!/usr/bin/env python3

TABLA_ORIGINAL = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
TABLA_CIFRADA  = "3WoODjVQip7wdJMTtG0ZAlf5arbRY9mgvHLyBEcXq6PnIFCzUeu4Kh8Sk2sxN1"


def encrypt(texto):
    tabla = str.maketrans(TABLA_ORIGINAL, TABLA_CIFRADA)
    return texto.translate(tabla)


def decrypt(texto):
    tabla = str.maketrans(TABLA_CIFRADA, TABLA_ORIGINAL)
    return texto.translate(tabla)


if __name__ == "__main__":
    while True:
        print("\n=== ENCRYPT.PRG Python ===")
        print("1 - Encriptar")
        print("2 - Desencriptar")
        print("0 - Salir")

        opcion = input("\nOpcion: ")

        if opcion == "1":
            valor = input("Texto a encriptar: ")
            print("Resultado:", encrypt(valor))

        elif opcion == "2":
            valor = input("Texto a desencriptar: ")
            print("Resultado:", decrypt(valor))

        elif opcion == "0":
            break

        else:
            print("Opción inválida")
