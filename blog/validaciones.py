from blog.datos import posts


from blog.datos import estados_post

def validar_post(post):
    claves = ("id", "titulo", "contenido", "autor", "tags", "estado")
   
    for clave in claves:
        if clave not in post:
            return False, f"Error: falta la clave obligatoria '{clave}'."
   
    if not isinstance(post["titulo"], str) or not post["titulo"].strip():
        return False, "Error: el título no puede estar vacío."
       
    if not isinstance(post["tags"], (set, list, tuple)):
        return False, "Error: 'tags' debe ser una colección (set o lista)."
   
    if not isinstance(post["autor"], dict):
            return False, "El campo 'autor' debe ser un diccionario."
    if "nombre" not in post["autor"] or not str(post["autor"]["nombre"]).strip():
            return False, "El diccionario 'autor' debe contener la clave 'nombre'."
    if post["estado"] not in estados_post:
            return False, f"El estado '{post['estado']}' no es válido. Estados permitidos: {estados_post}."
   




    return True, "Se valido post"