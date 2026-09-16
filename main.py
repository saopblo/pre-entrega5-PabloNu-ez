from blog.datos import posts
from blog.menu import mostrar_menu
from blog.operaciones import listar_posts, buscar_por_titulo, filtrar_por_tag
from blog.validaciones import validar_post

def main():
    while True:
        opcion=mostrar_menu()


        if opcion == 1:
            listar_posts(posts)




        elif opcion == 2:
            busqueda = input("\nBuscar por título: ").strip().lower()
            resultados = buscar_por_titulo(posts, busqueda)




            if resultados:
                print("\nResultados encontrados:")
                for post in resultados:
                    print(f"- {post['titulo']} | Autor: {post['autor']['nombre']}")
            else:
                print("No se encontraron posts que coincidan con la búsqueda.")




        elif opcion == 3:
            busqueda_tag = input("\nFiltrar por tag: ").strip().lower()
            resultados_filtrados = filtrar_por_tag(posts, busqueda_tag)




            if resultados_filtrados:
                print(f"\nPosts con el tag '{busqueda_tag}':")
                for post in resultados_filtrados:
                    print(f"- {post['titulo']} | Autor: {post['autor']['nombre']}")
            else:
                print("No se encontaron los tags buscados")




        elif opcion == 4:
            print("\n--- Validando publicaciones ---")
            for i, post in enumerate(posts, start=1):
                try:
                    es_valido, mensaje = validar_post(post)
                    if es_valido:
                        print(f"Post {i}: {mensaje}")
                    else:
                        print(f"Post {i}: error - {mensaje}")
                except Exception as e:
                    print(f"Post {i}: error inesperado - {e}")




        elif opcion == 5:
            print("\nGracias por usar el sistema del blog. ¡Hasta luego!")
            break




        else:
            print("Opción inválida, intenta de nuevo")




if __name__ == "__main__":
    main()