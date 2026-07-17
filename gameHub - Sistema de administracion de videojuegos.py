
def mostrar_menu():
    print("------------- MENÚ PRINCIPAL -------------")
    print("1. stock por plataforma")
    print("2. busqueda de juegos por rango de precio")
    print("3. actualizar precio de juego")
    print("4. agregar juego")
    print("5. eliminar juego")
    print("6. salir")
    print("-------------")

def leer_opcion():
    while True:
        try:
            opcion = int(input("ingrese opcion: "))
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("Debe seleccionar una opcion valida")
                mostrar_menu()
        except ValueError:
            print("debe seleccionar una opcion valida")
            mostrar_menu()


def stock_plataforma(juegos, inventario, plataforma):
    total = 0
    for codigo in juegos:
        if juegos[codigo][1].lower() == plataforma.lower():
            total += inventario[codigo][1]
    print("el total de stock disponibles es:", total)


def busqueda_precios(juegos, inventario, precio_min, precio_max):
    resultados = []
    for codigo in inventario:
        precio = inventario[codigo][0]
        stock = inventario[codigo][1]
        if precio_min <= precio <= precio_max and stock != 0:
            titulo = juegos[codigo][0]
            resultados.append(titulo + "--" + codigo)
    resultados.sort()
    if len(resultados) == 0:
        print("no hay juegos en ese rango de precios.")
    else:
        print("los juegos encontrados son:", resultados)

def buscar_codigo(inventario, codigo):
    return codigo in inventario

def actualizar_precio(inventario, codigo, nuevo_precio):
    if buscar_codigo(inventario, codigo):
        inventario[codigo][0] = nuevo_precio
        return True
    else:
        return False

def eliminar_juego(juegos, inventario, codigo):
    if buscar_codigo(inventario, codigo):
        del juegos[codigo]
        del inventario[codigo]
        return True
    else:
        return False
    
def validar_codigo(juegos, inventario, codigo):
    if codigo.strip() == "":
        return False
    if codigo in juegos or codigo in inventario:
        return False
    return True

def validar_titulo(titulo):
    return titulo.strip() != ""

def validar_plataforma(plataforma):
    return plataforma.strip() != ""

def validar_genero(genero):
    return genero.strip() != ""

def validar_clasificacion(clasificacion):
    return clasificacion == 'E' or clasificacion == 'T' or clasificacion == 'M'

def validar_multiplayer(valor):
    return valor == 's' or valor == 'n'

def validar_editor(editor):
    return editor.strip() != ""

def validar_precio(precio):
    return precio > 0

def validar_stock(stock):
    return stock >= 0



def agregar_juego(juegos, inventario, codigo, titulo, plataforma, genero,
                   clasificacion, multiplayer, editor, precio, stock):
    if codigo in juegos:
        return False
    juegos[codigo] = [titulo, plataforma, genero, clasificacion, multiplayer, editor]
    inventario[codigo] = [precio, stock]
    return True

def main():
    juegos = {
        'G001': ['Eclipse Runner', 'PC', 'accion', 'T', True, 'NovaStudio'],
        'G002': ['Puzzle Atlas', 'Switch', 'puzzle', 'E', False, 'BrightWorks'],
        'G003': ['Sky Legends', 'PS5', 'aventura', 'T', True, 'OrionGames'],
        'G004': ['Racing Pulse', 'PC', 'carreras', 'E', True, 'VelocityLab'],
        'G005': ['Mystic Farm', 'Switch', 'simulacion', 'E', False, 'GreenSeed'],
        'G006': ['Shadow Tactics', 'Xbox', 'estrategia', 'M', False, 'IronGate']
    }
    
    inventario = {
        'G001': [9990, 7],
        'G002': [19990, 0],
        'G003': [42990, 3],
        'G004': [14990, 5],
        'G005': [17990, 9],
        'G006': [39990, 2]
    }

    opcion = 0
    while opcion != 6:
        mostrar_menu()
        opcion = leer_opcion()

        if opcion == 1:
            plataforma = input("Ingrese plataforma a consultar: ")
            stock_plataforma(juegos, inventario, plataforma)

        elif opcion == 2:
            while True:
                try:
                    p_min = int(input("Ingrese precio mínimo: "))
                    p_max = int(input("Ingrese precio máximo: "))
                    if p_min >= 0 and p_max >= 0 and p_min <= p_max:
                        break
                    else:
                        print("Debe ingresar valores enteros")
                except ValueError:
                    print("Debe ingresar valores enteros")
            busqueda_precios(juegos, inventario, p_min, p_max)

        elif opcion == 3:
            continuar = 's'
            while continuar == 's':
                codigo = input("Ingrese código del juego: ").strip().upper()
                try:
                    nuevo_precio = int(input("Ingrese nuevo precio: "))
                except ValueError:
                    nuevo_precio = -1

                if not validar_precio(nuevo_precio):
                    print("El precio debe ser un entero positivo")
                elif actualizar_precio(inventario, codigo, nuevo_precio):
                    print("Precio actualizado")
                else:
                    print("el codigo no existe")

                continuar = input("¿Desea actualizar otro precio (s/n)?: ").strip().lower()

        elif opcion == 4:
            codigo = input("ingrese codigo del juego: ").strip().upper()
            titulo = input("ingrese titulo: ")
            plataforma = input("ingrese plataforma: ")
            genero = input("ingrese genero: ")
            clasificacion = input("ingrese clasificacion: ")
            multiplayer_str = input("¿es multiplayer? (s/n): ").strip().lower()
            editor = input("ingrese editor: ")

            try:
                precio = int(input("ingrese precio: "))
            except ValueError:
                precio = -1

            try:
                stock = int(input("ingrese stock: "))
            except ValueError:
                stock = -1

            if not validar_codigo(juegos, inventario, codigo):
                print("El código no es válido o ya existe")
            elif not validar_titulo(titulo):
                print("El título no es válido")
            elif not validar_plataforma(plataforma):
                print("La plataforma no es válida")
            elif not validar_genero(genero):
                print("El género no es válido")
            elif not validar_clasificacion(clasificacion):
                print("La clasificación no es válida")
            elif not validar_multiplayer(multiplayer_str):
                print("Debe ingresar 's' o 'n'")
            elif not validar_editor(editor):
                print("El editor no es válido")
            elif not validar_precio(precio):
                print("El precio no es válido")
            elif not validar_stock(stock):
                print("El stock no es válido")
            else:
                multiplayer = True if multiplayer_str == 's' else False
                if agregar_juego(juegos, inventario, codigo, titulo, plataforma, genero,
                                  clasificacion, multiplayer, editor, precio, stock):
                    print("Juego agregado")
                else:
                    print("el código ya existe")

        elif opcion == 5:
            codigo = input("ingrese codigo del juego: ").strip().upper()
            if eliminar_juego(juegos, inventario, codigo):
                print("Juego eliminado")
            else:
                print("el codigo no existe")

        elif opcion == 6:
            print("programa finalizado.")


main()