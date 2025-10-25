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






#PARA VENTAS
def seleccionar_usuario_activo(usuarios):
    idUsuario = int(input("Introduce el ID del usuario: "))
    while idUsuario<=0:  # comprobamos que el ID sea mayor que 0
        print("ID no válido, prueba otra vez")
        idUsuario=int(input("Introduce el ID del usuario: "))
    for usuario in usuarios:  # recorremos todos los usuarios
        if usuario["id"]==idUsuario:  # si el id coincide
            print(f"Usuario activo: {usuario['nombre']}")
            return idUsuario  # devolvemos el id del usuario
    print("Usuario no encontrado.")  # si no se encuentra
    return None  # devuelve None si no existe
def anadir_al_carrito(carrito, articulos):
    idArticulo = int(input("ID del artículo: "))
    while idArticulo<=0:  # comprobamos que el ID sea válido
        print("ID no válido, prueba otra vez")
        idArticulo=int(input("Introduce el ID del artículo: "))
    articulo = None
    for articulo2 in articulos:  # buscamos el artículo en la lista
        if articulo2["id"] == idArticulo and articulo2["activo"]:  # debe estar activo
            articulo = articulo2
    if not articulo:  # si no se encuentra
        print("Artículo no encontrado o inactivo.")
        return
    cantidad = int(input("Cantidad: "))  # pedimos cantidad
    if cantidad < 1:  # cantidad mínima 1
        print("Cantidad no válida.")
        return
    if cantidad > articulo["stock"]:  # no se puede pasar del stock
        print(f"No hay stock suficiente. Stock disponible: {articulo['stock']}")
        return
    carrito.append((idArticulo, cantidad))  # añadimos el producto al carrito
    print("Artículo añadido al carrito.")
def quitar_del_carrito(carrito):
    idArticulo = int(input("ID del artículo que quieres eliminar: "))
    while idArticulo<=0:  # comprobamos que el ID sea válido
        print("ID no válido, prueba otra vez")
        idArticulo=int(input("Introduce el ID del artículo: "))
    for item in carrito:  # recorremos el carrito
        if item[0]==idArticulo:  # si el id coincide
            carrito.remove(item)  # lo quitamos
            print("Articulo eliminado correctamente")
    return  # salimos de la función
    print("Artículo no encontrado")  # este print nunca se ejecuta
def calcular_total_carrito(carrito,ariticulos):
    if len(carrito)>0:  # si el carrito no está vacío
        total=0
        print("Productos añadidos al carrito:")
        for idArticulo,cantidad in carrito:  # recorremos los productos del carrito
            articulo=None
            for articulo2 in ariticulos:  # buscamos el artículo en la lista
                if articulo2["id"]==idArticulo:  # si coincide el id
                    articulo=articulo2
            if articulo:  # si el artículo existe
                subtotal=cantidad*articulo["precio"]  # calculamos subtotal
                total=total+subtotal  # sumamos al total
                print(articulo["nombre"],",Cantidad: ",cantidad,",Subtotal: ",subtotal)
        print("Total: ",total)  # mostramos el total final
        return total  # devolvemos el total
    else:
        print("El carrito está vacío")  # si no hay productos
def confirmar_compra(carrito,articulos,usuario_activo,ventas):
    if usuario_activo is None:  # no se puede comprar sin usuario
        print("No hay un usuario activo, selecciona uno antes")
        return
    if len(carrito)==0:  # si el carrito está vacío
        print("El carrito está vacío, introduce productos para poder continuar")
        return
    total=calcular_total_carrito(carrito,articulos)  # calculamos el total de la compra
    for idArticulo, cantidad in carrito:  # comprobamos el stock
        articulo=None
        for articulo2 in articulos:
            if articulo2["id"]==idArticulo:
                articulo=articulo2
        if cantidad>articulo["stock"]:  # si no hay stock suficiente
            print("No hay stock suficiente")
            return
    for idArticulo, cantidad in carrito:  # restamos el stock
        articulo=None
        for articulo2 in articulos:
            if articulo2["id"]==idArticulo:
                articulo=articulo2
        articulo["stock"]=articulo["stock"]-cantidad  # actualizamos stock
    idVenta=len(ventas)+1  # creamos un id para la venta
    items=[]
    for idArticulo, cantidad in carrito:  # guardamos los artículos comprados
        articulo=None
        for articulo2 in articulos:
            if articulo2["id"]==idArticulo:
                articulo=articulo2
        items.append((idArticulo,cantidad,articulo["precio"]))  # añadimos a la lista de items
    venta={  # creamos el registro de la venta
        "id_venta":idVenta,
        "usuario_id":usuario_activo,
        "items":items,
        "total":total
    }
    ventas.append(venta)  # añadimos la venta a la lista de ventas
    carrito.clear()  # vaciamos el carrito
    print("Compra completada")  # mensaje de éxito
def historial_ventas_por_usuario(ventas,usuario_id):
    if usuario_id is None:  # si no hay usuario activo
        print("No hay un usuario activo")
        return
    print("Historial de ventas del usuario: ",usuario_id)
    ventas_usuario=[]
    for venta in ventas:  # recorremos todas las ventas
        if venta["usuario_id"]==usuario_id:  # si coinciden los id
            ventas_usuario.append(venta)  # añadimos a la lista
    if len(ventas_usuario)==0:  # si no tiene ventas
        print("El usuario: ",usuario_id," no tiene ventas registradas")
        return
    for venta in ventas_usuario:  # mostramos todas las ventas del usuario
        print("Número venta: ",venta["id_venta"],",Total: ",venta["total"])
        for idArticulo,cantidad,precio in venta["items"]:  # mostramos los artículos comprados
            print("Artículo: ",idArticulo,", Cantidad: ",cantidad,", Precio: ",precio)






#Menú "final"
#menú principal
def menu_inicio(articulos,usuarios):
    #mostrar opciones del menu
    print("-----------------------")
    print("1. Menú artículos")
    print("2. Menú usuarios")
    print("3. Menú ventas / carrito")
    print("4. Salir")
#funcionamiento menú principal
def menu_principal():
    articulos = []
    usuarios = []
    ventas = []
    carrito_actual = []
    usuario_activo = None
    opcion=0
    #bucle hasta que se elija salir
    while opcion!=4:
        menu_inicio(articulos,usuarios)
        opcion=int(input("Opción: "))
        match opcion:
            case 1:
                menu_articulos(articulos)
            case 2:
                menu_usuarios(usuarios)
            case 3:
                menu_ventas(usuarios, articulos, ventas, carrito_actual, usuario_activo)
            case 4:
                print("Saliendo...")              
            case _:
                print("Opción no válida")
#función principal que hace que funcione todo el programa de articulos
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
#función principal que hace que funcione todo el programa de usuarios
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
#función principal que hace que funcione todo el programa de ventas
def menu_ventas(usuarios, articulos, ventas, carrito_actual, usuario_activo):
    opcion=0
    while opcion!=8:
        print("-----------------------")
        print("VENTAS / CARRITO")
        print("1. Seleccionar usuario activo")
        print("2. Añadir artículo al carrito")
        print("3. Quitar artículo del carrito")
        print("4. Ver carrito")
        print("5. Confirmar compra")
        print("6. Historial de ventas por usuario")
        print("7. Vaciar carrito")
        print("8. Volver")
        opcion = int(input("Opción: "))  
        match opcion:
            case 1:
                usuario_activo = seleccionar_usuario_activo(usuarios)
            case 2:
                anadir_al_carrito(carrito_actual, articulos)
            case 3:
                quitar_del_carrito(carrito_actual)
            case 4:
                calcular_total_carrito(carrito_actual, articulos)
            case 5:
                confirmar_compra(carrito_actual, articulos, usuario_activo, ventas)
            case 6:
                historial_ventas_por_usuario(ventas, usuario_activo)
            case 7:
                carrito_actual.clear()
                print("Carrito vaciado.")
            case 8:
                print("Volviendo...")
                return
            case _:
                print("Opción no válida")
#llamar a la función que hace que funcione el programa
menu_principal()