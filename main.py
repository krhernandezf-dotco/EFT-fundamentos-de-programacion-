arreglos={
    "FLO1"["ramo primavera","ramo","rosado","M",true,"primavera"],
    "FLO2"["caja elegante","caja","blanco","L",true,"todoaño"],
    "FLO3"["ramo solar","ramo","amarillo","S",false,"verano"],
    "FLO4"["centro mesa","centro","rojo","M",true"todo el año"],
    "FLO5"["ramo bosque","ramo","verde","L",false"otoño",],
    "FLO6"["caja noche","caja","morado","M",true"invierno"],
}

bodega={
    "FLO1"[15990,8]
    "FLO2"[2990,3]
    "FLO3"[9990,3]
    "FLO4"[24990,5]
    "FLO5"[1999,0]
    "FLO6"[22990,6]
}

opcion==1
while opcion!=6:
#menu principal 
print("1.-Unidades por tipo de arreglo")
print("2.-Busqueda de arreglos por rango de precios")
print("3.-Actualizar precio de rangos")
print("4.-Agregar arreglo")
print("5.- Elminidar arreglo")
print("6.-Salir")
 if opcion == 1:
        tipo = input("Ingrese tipo de arreglo: ")
        unidades_tipo(tipo, arreglos, bodega)
    elif opcion == 2:
        while True:
            try:
                minimo = int(input("Ingrese precio mínimo: "))
                maximo = int(input("Ingrese precio máximo: "))
                if minimo >= 0 and maximo >= minimo:
                    break
            except:
                print("Debe ingresar valores enteros")
        busqueda_precio(minimo, maximo, arreglos, bodega)
    elif opcion == 3:
        seguir = "s"
        while seguir.lower() == "s":
            codigo = input("Ingrese código del arreglo: ")
            try:
                nuevo = int(input("Ingrese nuevo precio: "))
                if nuevo > 0:
                    if actualizar_precio(codigo, nuevo, bodega):
                        print("Precio actualizado")
                    else:
                        print("El código no existe")
            except:
                print("Debe ingresar un número entero")
            seguir = input("¿Desea actualizar otro precio (s/n)?: ")
    elif opcion == 4:
        codigo = input("Ingrese código: ")
        nombre = input("Ingrese nombre: ")
        tipo = input("Ingrese tipo: ")
        color = input("Ingrese color principal: ")
        tamano = input("Ingrese tamaño (S/M/L): ").upper()
        tarjeta = input("¿Incluye tarjeta? (s/n): ").lower()
        temporada = input("Ingrese temporada: ")
        try:
            precio = int(input("Ingrese precio: "))
            unidades = int(input("Ingrese unidades: "))
        except:
            print("Precio o unidades inválidas")
            continue
        if not validar_texto(codigo):
            print("Código inválido")
        elif not validar_texto(nombre):
            print("Nombre inválido")
        elif not validar_texto(tipo):
            print("Tipo inválido")
        elif not validar_texto(color):
            print("Color inválido")
        elif not validar_tamano(tamano):
            print("Tamaño inválido")
        elif not validar_tarjeta(tarjeta):
            print("Tarjeta inválida")
        elif not validar_texto(temporada):
            print("Temporada inválida")
        elif not validar_precio(precio):
            print("Precio inválido")
        elif not validar_unidades(unidades):
            print("Unidades inválidas")
        else:
            incluye_tarjeta = False
            if tarjeta == "s":
                incluye_tarjeta = True
            if agregar_arreglo(codigo, nombre, tipo, color,
                               tamano, incluye_tarjeta,
                               temporada, precio, unidades,
                               arreglos, bodega):
                print("Arreglo agregado")
            else:
                print("El código ya existe")
    elif opcion == 5:
        codigo = input("Ingrese código del arreglo: ")
        if eliminar_arreglo(codigo, arreglos, bodega):
            print("Arreglo eliminado")
        else:
            print("El código no existe")
print("Programa finalizado.")