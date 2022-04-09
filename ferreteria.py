from cgi import print_form
from email.headerregistry import AddressHeader
from functools import total_ordering


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
    [4, 'Ñuñoa     ', 2990],
    [5, 'La Reina', 2990]
]
i = 0

print("Sistema de Ferretaria 1.1")
print("========================")
print("")

def comunaslist():
  print("")
  print("\t\t\t ####*LISTA DE COMUNAS*####")
  print("")
  print("Comunas\t\t\tCódigo\t\t\t Precio")
  print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
  for z in range(0, 5):
    print(comunas[z][1], "\t\t\t", comunas[z]
          [0], "\t\t\t", comunas[z][2])
    print("")

print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
print("Selecione la comuna de despacho")



def listado():
  print("")
  print("\t\t\t ####*LISTA DE PRODUCTOS*####")
  print("")
  print("Producto\t\t\tCódigo\t\t\t Precio")
  print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
  for x in range(0, 10):
   print(precioproducto[x][1], "\t\t\t", precioproducto[x]
   [0], "\t\t\t", precioproducto[x][2])
   print("")



print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
print("Selecione el producto que desea comprar ")
listado()
carrito=0
total=0
while carrito == 0:
    try:
        codigo = int(input("Ingrese el código del producto: "))
    except: print("debe ingresar un numero")

    else:
        
        if codigo<11 and codigo>0:
            cantidad = int(input("Ingrese la cantidad: "))
            for x in range(0, 10):
                if codigo == precioproducto[x][0]:
                    print("")
                    print("Producto: ", precioproducto[x][1])
                    print("Cantidad: ", cantidad)
                    print("Precio: ", precioproducto[x][2] * cantidad)
                    print("")
                    subtotal=precioproducto[x][2] * cantidad
                    total=total+subtotal
           
                    confirmacion = input("Desea agregar otro producto? (S/N)  :  ")
                    if confirmacion =="s" or confirmacion == "n" and confirmacion!=int:
                        if confirmacion == "s":
                            listado()
                            print("tu total es",total) 
                
                
                            carrito = 0
                        else:
                            carrito = 1
                            print('tu total final es',total)

                            break
                    else:
                        print("debe ingresar una opcion valida")

                        confirmacion = input("Desea agregar otro producto? (S/N)  :  ")
                        if confirmacion =="s" or confirmacion == "n" and confirmacion!=int:
                            if confirmacion == "s":
                                listado()
                                print("tu total es",total)
                                carrito = 0
                            else:
                                carrito = 1
                                print('tu total final es',total)

                                break
                        else:
                            print("debe ingresar una opcion valida")
        else:
            print('Debe ingresar un numero entre 1 y 10')

comunaslist()    
carrito2=0
while carrito2 == 0:
    try:
        codigo2 = int(input("Ingrese el código de la comuna: "))
    except: print("debe ingresar un numero")

    else:
        if codigo2<6 and codigo>0:
            for x in range(0, 5):
                if codigo2 == comunas[x][0]:
                    print("")
                    print("Comuna: ", comunas[x][1])
                    print("Precio: ", comunas[x][2])
                    print("")
                    valor3=comunas[x][2]
                    carrito2=1

                    print("el valor total de su compra con despacho es ", (valor3+total))
        else:
                print('Debe ingresar un numero entre 1 y 5')      
