print("Biemvenido! \nAqui podras obtener todas las combinaciones posibles\nde un numero de elementos (Facturas) para una cantidad total.\n")
#n = int(input("Ingresa el número total de facturas: "))
print("Ingresa las facturas (Recuerda utilizar espacio entre cantidades, \nuna vez listo presiona la tecla enter):\n ")
x = [float(i) for i in input().split()]
obo = float(input("\nIngresa el pago objetivo: "))
print("\nLas combinaciones son:\n")
def programa(numbers, target, partial=[]):
    s = sum(partial)
    if s == target:
        print("%s=%s" % (partial, target))
    if s >= target:
        return

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i+1:]
        programa(remaining, target, partial + [n])

if __name__ == "__main__":
    programa(x, obo)
input("\nPresiona enter para terminar el programa.")