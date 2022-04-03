

precioproducto = [
    [1, "Tornillos", 1000],
    [2, "Caja de Clavos", 1200],
    [3, "Pintura Blanca", 10990],
    [4, "broca cemento", 600],
    [5, "alicate punta", 1590],
    [6, "la gotita", 1190],
    [7, "yeso blanco", 1090],
    [8, "saco cemento", 22990],
    [9, "tarugos pack", 1990],
    [10, "agorex 10ml", 1590],
]

comunas = [
    [1, 'Las Condes', 3990],
    [2, 'Vitacura', 3990],
    [3, 'Providencia', 3990],
    [4, 'Ñuñoa', 2990],
    [5, 'La Reina', 2990]
]
i = 0

print("Sistema de Ferretaria 1.1")
print("========================")
print("")


print("")
print("\t\t\t ####*LISTA DE PRODUCTOS*####")
print("")
print("Producto\t\t\tCódigo\t\t\t Precio")
print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")


for x in range(0, 10):
    print(precioproducto[x][1], "\t\t\t", precioproducto[x]
          [0], "\t\t\t", precioproducto[x][2])
    print("")


print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
print("Selecione el producto que desea comprar ")

carrito=0
while carrito == 0:
    codigo = int(input("Ingrese el código del producto: "))
    cantidad = int(input("Ingrese la cantidad: "))
    for x in range(0, 10):
        if codigo == precioproducto[x][0]:
            print("")
            print("Producto: ", precioproducto[x][1])
            print("Cantidad: ", cantidad)
            print("Precio: ", precioproducto[x][2] * cantidad)
            print("")
            confirmacion = input("Desea agregar otro producto? (S/N)  :  ")
            if confirmacion == "s":
                carrito = 0
            else:
                carrito = 1
                break

            
        
   
