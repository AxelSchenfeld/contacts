from storage import contacts


def addContact():
    print("\n --- Añadir contacto ---")
    name = input("Ingresa el nombre del contacto: ")
    phone = input("Ingresa el número de teléfono: ")
    email = input("Ingresa el email: ")
    address = input("Ingresa la dirección: ")
    contacts[name] = {
        "teléfono": phone,
        "email": email,
        "dirección": address
    }
    print(f"El contacto {name} fue añadido con exito")


def viewContacts():
    print("\n --- Mostrar todos los contactos ---")
    if contacts:
        for name, info in contacts.items():
            print(
                f"Nombre: {name}| Teléfono: {info['teléfono']}| "
                f"Email: {info['email']}| Dirección: {info['dirección']}"
            )
    else:
        print("No hay contactos guardados")
    print("\n --- Fin de la lista ---")


def searchContact():
    print("\n --- Buscar contacto ---")
    name = input("Ingresa el nombre del contacto a buscar: ")
    if name in contacts:
        print(f"Detalles del contacto {name}:")
        print(f"Teléfono: {contacts[name]['teléfono']}")
        print(f"Email: {contacts[name]['email']}")
        print(f"Dirección: {contacts[name]['dirección']}")
        print("\n --- Fin de los detalles ---")
    else:
        print(f"El contacto {name} no fue encontrado")


def editContact():
    print("\n --- Editar contacto ---")
    name = input("Ingresa el nombre del contacto a editar: ")
    if name in contacts:
        print(f"Detalles actuales del contacto {name}:")
        print(f"Teléfono: {contacts[name]['teléfono']}")
        print(f"Email: {contacts[name]['email']}")
        print(f"Dirección: {contacts[name]['dirección']}")
        print("\n --- Fin de los detalles ---")
        phone = input("Ingresa el nuevo número de teléfono: ")
        email = input("Ingresa el nuevo email: ")
        address = input("Ingresa la nueva dirección: ")
        contacts[name] = {
            "teléfono": phone,
            "email": email,
            "dirección": address
        }
        print(f"El contacto {name} fue editado con éxito")
    else:
        print(f"El contacto {name} no fue encontrado")

def deleteContact():
    print("\n --- Eliminar contacto ---")
    name = input("Ingresa el nombre del contacto a eliminar: ")
    if name in contacts:
        del contacts[name]
        print(f"El contacto {name} fue eliminado con éxito")
    else:
        print(f"El contacto {name} no fue encontrado")

