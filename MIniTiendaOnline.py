#función que genera el id sumando 1 al número de artículos existentes
def generar_id(articulos):    
    return len(articulos)+1
#función para crear un nuevo artículo y añadirlo a la lista
def crear_articulo(articulos):
    nombre=input("Nombre del artículo: ")
    #comprueba que el nombre no esté repetido
    if nombre not in articulos:
        precio=float(input("Precio (>0): "))
        #ver que el precio sea mayor que 0 (válido)
        while precio<=0:
            print("Precio no válido")
            precio=float(input("Precio (>0): "))
        stock=int(input("Stock (>=0): "))
        #ver que el stock no sea negativo
        while stock<0:
            print("Stock no válido")
            stock=int(input("Stock (>=0): "))
        #crear el diccionario del nuevo artículo
        nuevo={"id":generar_id(articulos),"nombre":nombre,"precio":precio,"stock":stock,"activo":True}
        articulos.append(nuevo)
        print("Artículo agregado")
    else:
        print("Este producto ya está en el inventario ")
#función para listar todos los artículos mostrando su información
def listar_articulos(articulos):
    #comprobar si hay artículos en la lista
    if len(articulos)==0:
        print("No hay artículos para mostrar.")
        return
    #recorrer la lista y mostrar la información
    for articulo in articulos:
        if articulo["activo"]:
            estado="Activo"
        else:
            estado="Inactivo"
        print(f"{articulo['id']} - {articulo['nombre']} - {articulo['precio']}€ - stock: {articulo['stock']} - {estado}")
#función para buscar un artículo por su id y enseña su información
def buscar_articulo_por_id(articulos):
    id_busqueda=int(input("Introduce el id del producto que quieres buscar: "))
    #ver que el id sea mayor que 0 (válido)
    while id_busqueda<0:
        print("Id no válido, debe ser mínimo 1, prueba otra vez ")
        id_busqueda=int(input("Introduce el id del producto que quieres buscar: "))
    #buscar el artículo en la lista
    for articulo in articulos:
        if articulo["id"]==id_busqueda:
            id_busqueda=articulo
            print(f"Artículo encontrado:")
            print(f"ID: {articulo['id']}")
            print(f"Nombre: {articulo['nombre']}")
            print(f"Precio: {articulo['precio']}")
            print(f"Stock: {articulo['stock']}")
            print(f"Activo: {articulo['activo']}")
        else:   
            print("No se encontró el artículo con id: ",id_busqueda)
#función para actualizar los datos de un artículo
def actualizar_articulo(articulos):
    id_actualizar=int(input("Introduce el id del producto que quieres actualizar: "))
    #ver que el id sea mayor que 0 (válido)
    while id_actualizar<0:
        print("Id no válido, debe ser mínimo 1, prueba otra vez ")
        id_actualizar=int(input("Introduce el id del producto que quieres actualizar: "))
    encontrado=False
    #recorrer artículos para buscar el a artículo con el id introducido
    for articulo in articulos:
        if articulo["id"]==id_actualizar:
            encontrado=True
            print(f"Editando el artículo con ID {id_actualizar}")
            nombre_nuevo=input("Introduce el nuevo nombre: ")
            precio_nuevo=float(input("Nuevo precio: "))
            #ver que el precio sea mayor que 0 (válido)
            while precio_nuevo<=0:
                print("Precio no válido, debe der mayor que 0, prueba otra vez")
                precio_nuevo=float(input("Nuevo precio: "))
            stock_nuevo=int(input("Introduce el nuevo stock: "))
            #ver que el stock sea mayor/igual que 0 (válido)
            while stock_nuevo<0:
                print("Stock no válido, debe ser mayor que 0 o igual, prueba otra vez ")
                stock_nuevo=int(input("Introduce el nuevo stock: "))
            #actualizar los datos
            articulo["nombre"]=nombre_nuevo
            articulo["precio"]=precio_nuevo
            articulo["stock"]=stock_nuevo
            print("Producto actualizado correctamente")
        if not encontrado:
            print("No se encontró ningún producto con ID ",id_actualizar)
#función para eliminar un artículo de la lista
def eliminar_articulo(articulos):
    id_eliminar=int(input("Introduce el id del producto que quieres eliminar "))
    #ver que el id sea mayor que 0 (válido)
    while id_eliminar<0:
        print("Id no válido, debe ser mínimo 1, prueba otra vez ")
        id_eliminar=int(input("Introduce el id del producto que quieres eliminar: "))
    encontrado=False
    #buscar el artículo y eliminarlo
    for articulo in articulos:
        if articulo["id"]==id_eliminar:
            encontrado=True
            articulos.remove(articulo)
            print("Artículo eliminado correctamente")
        if not encontrado:
            print("Artículo no encontrado")
#función para cambiar el estado de activo/inactivo de un artículo
def alternar_activo(articulos):
    id_busqueda=int(input("Introduce el id del producto que quieres buscar: "))
    #ver que el id sea mayor que 0 (válido)
    while id_busqueda<0:
        print("Id no válido, debe ser mínimo 1, prueba otra vez ")
        id_busqueda=int(input("Introduce el id del producto que quieres buscar: "))
    encontrado=False
    #buscar el artículo
    for articulo in articulos:
        if articulo["id"]==id_busqueda:
            encontrado=True
            #cambiar el estado
            articulo["activo"]=not articulo["activo"]
            #mostrar el nuevo estado
            if articulo["activo"]:
                estado="Activo"
            else:
                estado="Inactivo"
            print(f"El artículo '{articulo['nombre']}' ahora está {estado}.")
        if not encontrado:
            print("Arículo no encontrado")
#función que muestra las opciones
def menu(articulos):
    #muestra las opciones del menú
    print("-----------------------")
    print("1. Crear artículo")
    print("2. Listar artículos")
    print("3. Buscar artículo por ID")
    print("4. Actualizar artículo")
    print("5. Eliminar artículo")
    print("6. Alternar activo/inactivo")
    print("7. Salir")
#función principal que hace que funcione todo el programa
def menu_articulos():
    articulos=[]
    menu(articulos)
    opcion=int(input("Opción: "))
    #bucle hasta que se elija salir
    while opcion!=7:
        match opcion:
            case 1:
                crear_articulo(articulos)
            case 2:
                listar_articulos(articulos)
            case 3:
                buscar_articulo_por_id(articulos)
            case 4:
                actualizar_articulo(articulos)
            case 5:
                eliminar_articulo(articulos)
            case 6:
                alternar_activo(articulos)
            case 7:
                print("Saliendo...")
            case _:
                print("Opción no válida")
        #mostrar el menú de nuevo
        menu(articulos)
        opcion=int(input("Opción: "))
#llamar a la función que hace que funcione el programa
menu_articulos()
