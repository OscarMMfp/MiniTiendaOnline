#definir la función de generar el id, sumando 1 a la longitud del diccionario
def generar_id(articulos):    
    return len(articulos)+1
#definir la función de crear artículo
def crear_articulo(articulos):
    nombre=input("Nombre del artículo: ")
    if nombre not in articulos:
        precio=float(input("Precio (>0): "))
        while precio<=0:
            print("Precio no válido")
            precio=float(input("Precio (>0): "))
        stock=int(input("Stock (>=0): "))
        while stock<0:
            print("Stock no válido")
            stock=int(input("Stock (>=0): "))
        nuevo={"id":generar_id(articulos),"nombre":nombre,"precio":precio,"stock":stock,"activo":True}
        articulos.append(nuevo)
        print("Artículo agregado")
    else:
        print("Este producto ya está en el inventario ")
        
def listar_articulos(articulos):
    if len(articulos)==0:
        print("No hay artículos para mostrar.")
        return
    for articulo in articulos:
        estado = "Activo"
        if articulo["activo"]:
            estado = "Activo"
        else:
            estado = "Inactivo"
        print(f"{articulo['id']} - {articulo['nombre']} - {articulo['precio']}€ - stock: {articulo['stock']} - {estado}")

def buscar_articulo_por_id(articulos):
    id_busqueda=int(input("Introduce el id del producto que quieres buscar: "))
    while id_busqueda<0:
        print("Id no válido, debe ser mínimo 1, prueba otra vez ")
        id_busqueda=int(input("Introduce el id del producto que quieres buscar: "))
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

def actualizar_articulo(articulos):
    id_actualizar=int(input("Introduce el id del producto que quieres actualizar: "))
    while id_actualizar<0:
        print("Id no válido, debe ser mínimo 1, prueba otra vez ")
        id_actualizar=int(input("Introduce el id del producto que quieres actualizar: "))
    encontrado=False
    for articulo in articulos:
        if articulo["id"]==id_actualizar:
            encontrado=True
            print(f"Editando el artículo con ID {id_actualizar}")
            nombre_nuevo=input("Introduce el nuevo nombre: ")
            precio_nuevo=float(input("Nuevo precio: "))
            while precio_nuevo<=0:
                print("Precio no válido, debe der mayor que 0, prueba otra vez")
                precio_nuevo=float(input("Nuevo precio: "))
            stock_nuevo=int(input("Introduce el nuevo stock: "))
            while stock_nuevo<0:
                print("Stock no válido, debe ser mayor que 0 o igual, prueba otra vez ")
                stock_nuevo=int(input("Introduce el nuevo stock: "))
            articulo["nombre"] = nombre_nuevo
            articulo["precio"] = precio_nuevo
            articulo["stock"] = stock_nuevo
            print("Producto actualizado correctamente")
        if not encontrado:
            print("No se encontró ningún producto con ID ",id_actualizar)

def eliminar_articulo(articulos):
    id_eliminar=int(input("Introduce el id del producto que quieres eliminar "))
    while id_eliminar<0:
        print("Id no válido, debe ser mínimo 1, prueba otra vez ")
        id_eliminar=int(input("Introduce el id del producto que quieres eliminar: "))
    encontrado=False
    for articulo in articulos:
        if articulo["id"]==id_eliminar:
            encontrado=True
            articulos.remove(articulo)
            print("Artículo eliminado correctamente")
        if not encontrado:
            print("Artículo no encontrado")

def alternar_activo(articulos):
    id_busqueda = int(input("Introduce el id del producto que quieres buscar: "))
    while id_busqueda<0:
        print("Id no válido, debe ser mínimo 1, prueba otra vez ")
        id_busqueda=int(input("Introduce el id del producto que quieres buscar: "))
    encontrado=False
    for articulo in articulos:
        if articulo["id"]==id_busqueda:
            encontrado=True
            articulo["activo"] = not articulo["activo"]
            if articulo["activo"]:
                estado = "Activo"
            else:
                estado = "Inactivo"
            print(f"El artículo '{articulo['nombre']}' ahora está {estado}.")
        if not encontrado:
            print("Arículo no encontrado")

def menu(articulos):
    print("-----------------------")
    print("1. Crear artículo")
    print("2. Listar artículos")
    print("3. Buscar artículo por ID")
    print("4. Actualizar artículo")
    print("5. Eliminar artículo")
    print("6. Alternar activo/inactivo")
    print("7. Salir")

def menu_articulos():
    articulos=[]
    menu(articulos)
    opcion=int(input("Opción: "))
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
        menu(articulos)
        opcion=int(input("Opción: "))
menu_articulos()