#validaciones 
def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese opción: "))
            if opcion >= 1 and opcion <= 6:
                return opcion
            else:
                print("Debe seleccionar una opción válida")
        except:
            print("Debe ingresar un número entero")
def unidades_tipo(tipo, arreglos, bodega):
    total = 0
    for codigo in arreglos:
        if arreglos[codigo]lower() == tipo.lower():
            total = total + bodega[codigo]
    print("El total de unidades disponibles es:", total)
def busqueda_precio(p_min, p_max, arreglos, bodega):
    lista = []
    for codigo in bodega:
        precio = bodega[codigo][0]
        unidades = bodega[codigo][1]
        if precio >= p_min and precio <= p_max and unidades > 0:
            nombre = arreglos[codigo][0]
            lista.append(nombre + "--" + codigo)
    lista.sort()
    if len(lista) == 0:
        print("No hay arreglos en ese rango de precios")
    else:
        print("Los arreglos encontrados son:", lista)
def buscar_codigo(codigo, bodega):
    codigo = codigo.upper()
    if codigo in bodega:
        return True
    return False
def actualizar_precio(codigo, nuevo_precio, bodega):
    if buscar_codigo(codigo, bodega):
        codigo = codigo.upper()
        bodega[codigo][0] = nuevo_precio
        return True
    return False
def validar_texto(texto):
    if texto.strip() == "":
        return False
    return True
def validar_tamano(tamano):
    tamano = tamano.upper()
    if tamano  "S" or tamano  "M" or tamano == "L":
        return True
    return False
def validar_tarjeta(valor):
    valor = valor.lower()
    if valor  "s" or valor  "n":
        return True
    return False
def validar_precio(precio):
    if precio > 0:
        return True
    return False
def validar_unidades(unidades):
    if unidades >= 0:
        return True
    return False
def agregar_arreglo(codigo, nombre, tipo, color, tamano,incluye_tarjetas,temporada,precios,unidades,arreglos,bodegas)
    codigo = codigo.upper()
    if buscar_codigo(codigo, bodega):
        return False
    arreglos[codigo] = [
        "nombre"
        "tipo"
        "color"
        "tamano"
        "incluye_tarjeta"
        "temporada"
    ]
    bodega[codigo] = [
        precio,
        unidades
    ]
    return True
def eliminar_arreglo(codigo, arreglos, bodega):
    if buscar_codigo(codigo, bodega):
        codigo = codigo.upper()
        del arreglos[codigo]
        del bodega[codigo]
        return True
    return False
