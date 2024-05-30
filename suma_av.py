#Función que suma n cantidad de numeros a,b,c,d,e...
def sumav():
    nums = []
    print("---Función Suma Avanzada---")
    print()
    print("Inserta los numeros a sumar")
    print("presiona f para terminar")
    n = input("primer numero: ")
    if n != 'f':
        n = int(n)
        nums.append(n)
    while True:
        n = input("siguiente numero: ")
        if n == 'f':
            break
        n = int(n)
        nums.append(n)
    
    print("fin de incersión...")
    print()
    r = sum(nums)
    print(f"La suma de todos los numeros que ingresaste es igual a: {r}")
    print()

