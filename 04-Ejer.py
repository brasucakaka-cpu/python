# porcentaje de descuento fijo
DESCUENTO_FIJO = 5  # %

# procesamiento de producto 1
print("==datos del producto 1==")
producto = input("nombre del producto : ")
precio = float(input("precio del producto $: "))
cantidad = int(input("cantidad del producto : "))
if cantidad >= 10:
    total = precio * cantidad * (1 - DESCUENTO_FIJO / 100)
    print("total a pagar con descuento:", total)
else:
    total = precio * cantidad
    print("precio final sin descuento:", total)

# procesamiento de producto 2
print("==datos del producto 2==")
producto = input("nombre del producto : ")
precio = float(input("precio del producto $: "))
cantidad = int(input("cantidad del producto : "))
if cantidad >= 10:
    total = precio * cantidad * (1 - DESCUENTO_FIJO / 100)
    print("total a pagar con descuento:", total)
else:
    total = precio * cantidad
    print("precio final sin descuento:", total)