#funcion par calcular el perimetro de un rectangulo
def perimetro_rectangulo(base, altura):
    return 2 * (base + altura)

#solicitar datos al usuario
#lote 1
base = float(input("Ingrese la base del rectángulo 1: "))
altura = float(input("Ingrese la altura del rectángulo 1: "))
#lote 2
base2 = float(input("Ingrese la base del rectángulo 2: "))
altura2 = float(input("Ingrese la altura del rectángulo 2: "))
#lote 3
base3 = float(input("Ingrese la base del rectángulo 3: "))
altura3 = float(input("Ingrese la altura del rectángulo 3: "))

#calcular perimetro para cada lote
perimetro1 = perimetro_rectangulo(base, altura)
perimetro2 = perimetro_rectangulo(base2, altura2)
perimetro3 = perimetro_rectangulo(base3, altura3)

#mostrar resultados
print("El perímetro del rectángulo 1 es:", perimetro1)
print("El perímetro del rectángulo 2 es:", perimetro2)
print("El perímetro del rectángulo 3 es:", perimetro3)

#determinar el rectángulo con mayor perímetro
if perimetro1 > perimetro2 and perimetro1 > perimetro3:
    print("El rectángulo 1 tiene el mayor perímetro.")
elif perimetro2 > perimetro1 and perimetro2 > perimetro3:
    print("El rectángulo 2 tiene el mayor perímetro.")
else:
    print("El rectángulo 3 tiene el mayor perímetro.")
