#mostrar el precio de la estancia en el hotel
#preguntar si va en temporada alta o baja
#mostrar los royalty points obtenidos
#mostrar los costos de las actividades en total


#1. Precio por noche en temporada baja es de 4000, en temporada alta de 8000
#2. Por cada 10 pesos gastados, se obtiene 1 royal point
#3. (por día) Spa = 2000, kids club = 300, actividades acuáticas = 1000
def precio_noches(temporada, cantidad_de_noches):
    if (temporada == "1"):
        precio_estancia = cantidad_de_noches * 8000
    elif (temporada == "2"):
        precio_estancia = cantidad_de_noches * 4000
    else:
        print("Input inválido")
    return precio_estancia


def puntos(precio_estancia):
    royal_points = precio_estancia / 10
    return royal_points


spa = 0
kidsclub = 0
acuat = 0
precio_servicios = 0
cantidad_acuat = 0
cantidad_kids = 0
cantidad_spa = 0


def actividades(precio_servicios, servicios, cantidad_spa, cantidad_kids,
                cantidad_acuat, spa, kidsclub, acuat):
    if (servicios == "1"):
        spa = cantidad_spa * 2000
        precio_servicios = spa
    elif (servicios == "1,2" or "2,1"):
        spa = cantidad_spa * 2000
        kidsclub = cantidad_kids * 300
        precio_servicios = spa + kidsclub
    elif (servicios == "1,2,3" or "2,3,1" or "3,2,1" or "3,1,2" or "2,1,3"):
        spa = cantidad_spa * 2000
        kidsclub = cantidad_kids * 300
        acuat = cantidad_acuat * 1000
        precio_servicios = spa + kidsclub + acuat
    elif (servicios == "1,3" or "3,1"):
        spa = cantidad_spa * 2000
        acuat = cantidad_acuat * 1000
        precio_servicios = spa + acuat
    elif (servicios == "2"):
        kidsclub = cantidad_kids * 300
        precio_servicios = kidsclub
    elif (servicios == "3"):
        acuat = cantidad_acuat * 1000
        precio_servicios = acuat
    elif (servicios == "2,3" or "3,2"):
        acuat = cantidad_acuat * 1000
        kidsclub = cantidad_kids * 300
        precio_servicios = acuat + kidsclub
    else:
        print("Input inválido")
    return precio_servicios


def precio_total(precio_estancia, precio_servicios):
    total = precio_estancia + precio_servicios
    return total


temporada = input("Es temporada: \n 1) Alta \n 2) Baja \n")
cantidad_de_noches = int(input("Cuántas noches se va a quedar?\n"))
servicios = input(
    "Cuáles servicios desea disfrutar durante su estancia? (separar con coma y sin espacios) \n 1)SPA \n 2) Kids Club \n 3) Actividades Acuáticas \n"
)

if (servicios == "1"):
    cantidad_spa = int(input("Cuántos días de SPA gusta?\n"))
elif (servicios == "2"):
    cantidad_kids = int(input("Cuántos días de Kids Club gusta?\n"))
elif (servicios == "3"):
    cantidad_acuat = int(
        input("Cuántos días de Actividades Acuáticas gusta?\n"))
elif (servicios == "1,2"):  #or "2,1"):
    cantidad_spa = int(input("Cuántos días de SPA gusta?\n"))
    cantidad_kids = int(input("Cuántos días de Kids Club gusta?\n"))
elif (servicios == "1,3"):  #or "3,1"):
    cantidad_spa = int(input("Cuántos días de SPA gusta?\n"))
    cantidad_acuat = int(
        input("Cuántos días de Actividades Acuáticas gusta?\n"))
elif (servicios == "2,3"):  #or "3,1"):
    cantidad_kids = int(input("Cuántos días de Kids Club gusta?\n"))
    cantidad_acuat = int(
        input("Cuántos días de Actividades Acuáticas gusta?\n"))
elif (servicios == "1,2,3"):  #or "2,3,1" or "3,2,1" or "3,1,2" or "2,1,3"):
    cantidad_spa = int(input("Cuántos días de SPA gusta?\n"))
    cantidad_acuat = int(
        input("Cuántos días de Actividades Acuáticas gusta?\n"))
    cantidad_kids = int(input("Cuántos días de Kids Club gusta?\n"))
else:
    print("Input inválido")

precio_estancia = precio_noches(temporada, cantidad_de_noches)
royal_points = puntos(precio_estancia)
precio_servicios = actividades(precio_servicios, servicios, cantidad_spa,
                               cantidad_kids, cantidad_acuat, spa, kidsclub,
                               acuat)
total = precio_total(precio_estancia, precio_servicios)

print("El precio por " + str(cantidad_de_noches) + " noches es de: $" +
      str(precio_estancia))
print("Los Royalty Points obtenidos son: " + str(royal_points))
print("El precio de sus actividades es de: $" + str(precio_servicios))
print("El total a pagar es de: $" + str(total))
