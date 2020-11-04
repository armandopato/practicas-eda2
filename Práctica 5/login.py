from Database import Usuario
from HashTable import HashTable


def initializeHashTable(table, initialList=None):
    if initialList is None:
        initialList = Usuario.GetUsuariosDB(1000)
    for userEntry in initialList:
        table.insert(userEntry.username, userEntry)


def login(tablaHash, username, password):
    user = tablaHash.search(username)

    if user is None:
        return print("Usuario no encontrado")

    if user.password == password:
        return print("Acceso autorizado, bienvenido/a", user.fullname)
    else:
        return print("Acceso denegado: Contraseña incorrecta")


def testLogin():
    hashTable = HashTable(1000)
    initializeHashTable(hashTable)
    print("Factor de carga:", hashTable.getLoadFactor())
    print("Número máximo de colisiones:", hashTable.getMaxCollisions(), "\n")

    login(hashTable, "brevierk", "lF4RnE")
    login(hashTable, "brevierk", "Contraseña incorrecta")
    login(hashTable, "Usuario inexistente", "Contraseña")
    print()
