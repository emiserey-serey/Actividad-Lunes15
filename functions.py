def agregar_libro(libros):
    titulo = input("Agregar el titulo del libro\n")
    
    for libro in libros:
        if libro["titulo"].lower() == titulo.lower():
            print("Error: El libro ya existe")
            return
    autor = input("Ingrese el autor del libro\n")
    nuevo_libro = {
        "titulo": titulo,
        "autor": autor,
        "disponible": True
    }
    libros.append(nuevo_libro)
    print("¡Libro agregado correctamente!")
    
def mostrar_libros(libros):
    if len(libros) == 0:
        print("No hay libros registrados")
        return
    print("===== LISTA DE LIBROS =====\n")
    for libro in libros:
        print(f"Título: {libro['titulo']}")
        print(f"Autor: {libro['autor']}")

        if libro["disponible"]:
            print("Estado: Disponible")
        else:
            print("Estado: Prestado")
            
def buscar_libro(libros):
    titulo = input("Ingrese el título a buscar:\n")
    for libro in libros:
        if libro["titulo"].lower() == titulo.lower():
        
            print("\nLibro encontrado:")
            print(f"Título: {libro['titulo']}")
            print(f"Autor: {libro['autor']}")
    
            if libro["disponible"]:
                print("Estado: Disponible")
            else:
                print("Estado: Prestado")
    
            return


