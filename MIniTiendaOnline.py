#PARA ARTÍCULOS
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
    encontrado=False
    #buscar el artículo en la lista
    for articulo in articulos:
        if articulo["id"]==id_busqueda:
            encontrado=True
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
            for articulo2 in articulos:
                if articulo2["nombre"]==nombre_nuevo:
                    print("Este nombre ya está registrado")
                    return
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







#PARA USUARIOS
#función que genera el id sumando 1 al número de usuarios existentes
def generar_id(usuarios):    
    return len(usuarios)+1
#función para crear un nuevo usuario y añadirlo a la lista
def crear_usuario(usuarios):
    nombre=input("Nombre del Usuario: ")
    #pedir email
    email=input("Email: ")
    #Comprobación básica de formato
    while "@" not in email or "." not in email:
        print("Email no válido. Debe contener '@' y '.'")
        email = input("Introduce un email válido: ")
    #ver que el email no esté repetido
    for usuario in usuarios:
        if usuario["email"]==email:
            print("Este email ya está registrado")
            return
    #crear el diccionario del nuevo usuario
    nuevo={"id":generar_id(usuarios),"nombre":nombre,"email":email,"activo":True}
    usuarios.append(nuevo)
    print("Usuario agregado")
#función para listar todos los usuarios mostrando su información
def listar_usuarios(usuarios):
    #comprobar si hay usuarios en la lista
    if len(usuarios)==0:
        print("No hay usuarios para mostrar.")
        return
    #recorrer la lista y mostrar la información
    for usuario in usuarios:
        if usuario["activo"]:
            estado="Activo"
        else:
            estado="Inactivo"
        print(f"{usuario['id']} - {usuario['nombre']} -Email: {usuario['email']} - {estado}")
#función para buscar un usuario por su id y enseña su información
def buscar_usuario_por_id(usuarios):
    id_busqueda=int(input("Introduce el id del usuario que quieres buscar: "))
    #ver que el id sea mayor que 0 (válido)
    while id_busqueda<0:
        print("Id no válido, debe ser mínimo 1, prueba otra vez ")
        id_busqueda=int(input("Introduce el id del usuario que quieres buscar: "))
    encontrado=False
    #buscar el usuario en la lista
    for usuario in usuarios:
        if usuario["id"]==id_busqueda:
            id_busqueda=usuario
            encontrado=True
            print(f"Usuario encontrado:")
            print(f"ID: {usuario['id']}")
            print(f"Nombre: {usuario['nombre']}")
            print(f"Email: {usuario['email']}")
            print(f"Activo: {usuario['activo']}")
        else:   
            print("No se encontró el usuario con id: ",id_busqueda)
#función para actualizar los datos de un usuario
def actualizar_usuario(usuarios):
    id_actualizar=int(input("Introduce el id del usuario que quieres actualizar: "))
    #ver que el id sea mayor que 0 (válido)
    while id_actualizar<0:
        print("Id no válido, debe ser mínimo 1, prueba otra vez ")
        id_actualizar=int(input("Introduce el id del usuario que quieres actualizar: "))
    encontrado=False
    #recorrer usuario para buscar el usuario con el id introducido
    for usuario in usuarios:
        if usuario["id"]==id_actualizar:
            encontrado=True
            print(f"Editando el usuarios con ID {id_actualizar}")
            nombre_nuevo=input("Introduce el nuevo nombre: ")
            email_nuevo=input("Introduce el nuevo email: ")
            #Comprobación básica de formato
            while "@" not in email_nuevo or "." not in email_nuevo:
                print("Email no válido. Debe contener '@' y '.'")
                email_nuevo = input("Introduce un email válido: ")
            #ver que el email introducido no esté ya en la lista y si está, volver a preguntar
            for usuario2 in usuarios:
                if usuario2["email"]==email_nuevo:
                    print("Este email ya está registrado")
                    return
            #actualizar los datos
            usuario["nombre"]=nombre_nuevo
            usuario["email"]=email_nuevo
            print("Producto actualizado correctamente")                
    if not encontrado:
        print("No se encontró ningún usuario con ID ",id_actualizar)
#función para eliminar un usuario de la lista
def eliminar_usuario(usuarios):
    id_eliminar=int(input("Introduce el id del usuario que quieres eliminar: "))
    #ver que el id sea mayor que 0 (válido)
    while id_eliminar<0:
        print("Id no válido, debe ser mínimo 1, prueba otra vez ")
        id_eliminar=int(input("Introduce el id del usuario que quieres eliminar: "))
    encontrado=False
    #buscar el usuario y eliminarlo
    for usuario in usuarios:
        if usuario["id"]==id_eliminar:
            encontrado=True
            usuarios.remove(usuario)
            print("Usuario eliminado correctamente")
    if not encontrado:
        print("Usuario no encontrado")
#función para cambiar el estado de activo/inactivo de un usuario
def alternar_activo(usuarios):
    id_busqueda=int(input("Introduce el id del usuario que quieres buscar: "))
    #ver que el id sea mayor que 0 (válido)
    while id_busqueda<0:
        print("Id no válido, debe ser mínimo 1, prueba otra vez ")
        id_busqueda=int(input("Introduce el id del usuario que quieres buscar: "))
    encontrado=False
    #buscar el usuario
    for usuario in usuarios:
        if usuario["id"]==id_busqueda:
            encontrado=True
            #cambiar el estado
            usuario["activo"]=not usuario["activo"]
            #mostrar el nuevo estado
            if usuario["activo"]:
                estado="Activo"
            else:
                estado="Inactivo"
            print(f"El usuario '{usuario['nombre']}' ahora está {estado}.")
    if not encontrado:
        print("Usuario no encontrado")







#Menú "final"
#menú principal
def menu_inicio(articulos,usuarios):
    #mostrar opciones del menu
    print("-----------------------")
    print("1. Menú artículos")
    print("2. Menú usuarios")
    print("3. Salir")
#funcionamiento menú principal
def menu_principal():
    articulos=[]
    usuarios=[]
    opcion=0
    #bucle hasta que se elija salir
    while opcion!=3:
        menu_inicio(articulos,usuarios)
        opcion=int(input("Opción: "))
        match opcion:
            case 1:
                menu_articulos(articulos)
            case 2:
                menu_usuarios(usuarios)
            case 3:
                print("Saliendo...")
            case _:
                print("Opción no válida")
#función principal que hace que funcione todo el programa
def menu_articulos(articulos):
    opcion=0
    #bucle hasta que se elija salir
    while opcion!=7:
        #muestra las opciones del menú
        print("-----------------------")
        print("1. Crear artículo")
        print("2. Listar artículos")
        print("3. Buscar artículo por id")
        print("4. Actualizar artículo")
        print("5. Eliminar artículo")
        print("6. Alternar activo/inactivo")
        print("7. Volver")
        opcion=int(input("Opción: "))
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
                print("Volviendo...")
                return
            case _:
                print("Opción no válida")
#función principal que hace que funcione todo el programa
def menu_usuarios(usuarios):
    opcion=0
    #bucle hasta que se elija salir
    while opcion!=7:
        #muestra las opciones del menú
        print("-----------------------")
        print("1. Crear usuario")
        print("2. Listar usuarios")
        print("3. Buscar usuario por id")
        print("4. Actualizar usuario")
        print("5. Eliminar usuario")
        print("6. Alternar activo/inactivo")
        print("7. Volver")
        opcion=int(input("Opción: "))           
        match opcion:
            case 1:
                crear_usuario(usuarios)
            case 2:
                listar_usuarios(usuarios)
            case 3:
                buscar_usuario_por_id(usuarios)
            case 4:
                actualizar_usuario(usuarios)
            case 5:
                eliminar_usuario(usuarios)
            case 6:
                alternar_activo(usuarios)
            case 7:
                print("Volviendo...")
                return
            case _:
                print("Opción no válida")
#llamar a la función que hace que funcione el programa
menu_principal()