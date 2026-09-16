def mostrar_menu():
        print("\nMostrar el Menu")
        print("1 - Ver todos los posts")
        print("2 - Buscar por titulo")
        print("3 - Filtrar por tag")
        print("4 - Validar publicaciones")
        print("5 - Salir")



        try:
            opcion = int(input("Seleccioná una opción (1-5): ").strip())
            return opcion
        except ValueError:
                return -1
       
       


