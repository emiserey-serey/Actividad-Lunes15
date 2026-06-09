from functions import *

libros = []

while True:
    
    print("===== BIBLIOTECA =====")
    print("1. Agregar libro")
    print("2. Mostrar libros")
    print("3. Buscar libro")
    print("4. Prestar libro")
    print("5. Devolver libro")
    print("6. Eliminar libro")
    print("7. Modificar libro")
    print("8. Mostrar estadísticas")
    print("9. Salir")
    
    opcion = int(input("Ingrese una opción!\n"))
    if opcion == "1":
        agregar_libro(libros)

    elif opcion == "2":
        mostrar_libros(libros)

    elif opcion == "3":
        buscar_libro(libros)

    elif opcion == "4":
        prestar_libro(libros)

    elif opcion == "5":
        devolver_libro(libros)

    elif opcion == "6":
        eliminar_libro(libros)

    elif opcion == "7":
        modificar_libro(libros)

    elif opcion == "8":
        mostrar_estadisticas(libros)

    elif opcion == "9":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida. Intente nuevamente.")
    
