# solicitar numeros al usuario
print("INGRESE LAS MEDIDAS DEL CUADRADO Y EL CUBO")
num1 = float(input("Ingrese el primer número del cuadrado: "))
num1 = float(input("Ingrese el segundo número del cuadrado: "))
num2 = float(input("Ingrese el primer número del cubo: "))
num2 = float(input("Ingrese el segundo número del cubo: "))


#realizar calculos
cuadrado = num1 ** 2
cubo = num2 ** 2

# compara y mostrar los relustados
if cuadrado > cubo:
    print("el primer numero del cuadrado es mayor que el segundo numero del cubo")
elif cuadrado < cubo:
    print("el segundo numero del cubo es mayor que el primer numero del cuadrado")
else: cuadrado == cubo
print("primer numero del cuadrado es igual al segundo numero del cubo")