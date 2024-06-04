import os
import csv

cosas = []

with open("trabajo.csv", "w", newline="") as csvarchivo:
    escritor = csv.writer(csvarchivo)
    escritor.writerow(["nombre", "color", "raza"])

while True:
    print("1. agregar perro: ")
    print("2. ver perros: ")
    print("3. chao ctm")

    opc = int(input("ingrese opcion: "))
    if opc == 1:
        while True:
            nombre = input("ingrese nombre de su perro: ")
            if len(nombre)>3 and nombre.isalpha():
                print("nombre agregado con exito")
                break
            else:
                print("ta malo mi compa")
        while True:
            color =input("ingrese el color de su perro: ")
            if len(color)>3 and color.isalpha(): #busque en google y no hay ningun color que tenga menos de 4 letras (en español)
                print("color valido")
                break
            else:
                print("el color agregado no es valido")
        while True:       
            raza = input("ingrese la raza de su perro: ")
            if len(raza)>4 and color.isalpha():
                print("se agrego bien")
                break
            else:
                print("ta malo compa")
        cosas = [nombre, color, raza]

        with open("trabajo.csv", "a+", newline="") as csvarchivo:
            escritor = csv.writer(csvarchivo)
            escritor.writerow(cosas)

    elif opc == 2:
        with open("trabajo.csv", "r", newline="") as csvarchivo:
            lector = csv.reader(csvarchivo)
            for cosas in lector:
                print(cosas)

    elif opc == 3:
        print("ta bueno, bye pipipipipipipi")

