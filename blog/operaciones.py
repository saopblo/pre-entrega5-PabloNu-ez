def listar_posts(lista):
    print("\n--- Todos los posts ---")
    for post in lista:
        print(f"Título: {post['titulo']} | Autor: {post['autor']['nombre']}")




def buscar_por_titulo(lista, termino):


    print("\n--- Buscar por título ---")
    termino_busqueda = str(termino).lower().strip()
    return [
            p for p in lista
            if termino_busqueda in str(p.get("titulo", "")).lower()
        ]


def filtrar_por_tag(lista, tag):
    print("\n--- Filtrar por tag ---")
    resultados_tag = []
    for post in lista:
        for etiqueta in post["tags"]:
            if etiqueta.lower() == tag.lower():
                resultados_tag.append(post)
                break
    return resultados_tag
