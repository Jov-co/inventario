import modules.products as p
from os import system as s


store = []
app_runing = True


if __name__ == "__main__":
    s('cls')
    while app_runing:
        print("""
1. Agregar producto
2. Buscar producto
3. Ajuste de inventario
3. Salir
        """)
        option = int(input(': '))
        if option == 1:
            store.append(p.products.add_product())
            print(store)
        elif option == 2:
            print(p.products.binary_search(store, 'nombre', 'jabon'))
        elif option == 3:
            pass
        elif option == 4:
            pass