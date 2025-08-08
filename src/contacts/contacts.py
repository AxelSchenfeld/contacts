from menuFunctions import addContact, deleteContact, editContact, searchContact, viewContacts


def menu():
    print("\n --- Menú Principal ---")
    print("1. Añadir contacto")
    print("2. Buscar contacto")
    print("3. Mostrar todos los contactos")
    print("4. Editar contacto")
    print("5. Eliminar contacto")
    print("6. Salir")
    return input("Elige una opción: ")

def main():
    while True:
        option = menu()
        if option == "1":
            addContact()
        elif option == "2":
            searchContact()
        elif option == "3":
            viewContacts()
        elif option == "4":
            editContact()
        elif option == "5":
            deleteContact()
        elif option == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, elige una opción del menú.")
    print("Programa finalizado")

if __name__ == "__main__":
    main()
