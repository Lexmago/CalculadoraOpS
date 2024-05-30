#Calculadora Open Source
#Stefan Martinez
from suma_func import sum
from resta_func import rest
from multi_func import multi
from div_func import div
from suma_av import sumav

#Menú principal

running = True

print("----Calculadora OpS----")
print()
print("Selecciona la operación:")
print()
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
print("5. Suma Avanzada")
print("6. Salir")
print()

while running:
    opcion_s = int(input("operación: "))
    print()
    if opcion_s == 1:
        sum()
    elif opcion_s == 2:
        rest()
    elif opcion_s == 3:
        multi()
    elif opcion_s == 4:
        div()
    elif opcion_s == 5:
        sumav()
    elif opcion_s == 6:
        print("Programa Terminado...")
        break
    else:
        print("Escribe un numero valido...")


