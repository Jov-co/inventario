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
            print('indique por que elemento desea buscar \n>>> codigo, nombre, stock, stock minimo, stock maximo, Valor unitario')
            busqueda = input(': ').lower()
            element = input(f'Ingrese el {busqueda} del elemento a buscar: ').lower()
            print(p.products.binary_search(store, busqueda, element))
        elif option == 3:
            pass
        elif option == 4:
            pass