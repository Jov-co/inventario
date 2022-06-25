# in this archive we will to add the next items about the product
"""
code, name, stock, min stock, max stock, unit value
"""


from operator import index
from unicodedata import name


class products():
    def __init__(self) -> None:
        pass
    def add_product():
        """
        Agregamos los productos al sistema
        """
        code = input('Ingrese el codigo: ')
        name = input('Ingrese el nombre: ')
        stock = 0
        stock_min = int(input('Ingrese el stock minimo: '))
        stock_max = int(input('Ingrese el stock maximo: '))
        unit_value = int(input('Ingrese el valor unitario: '))
        return [code, name, stock, stock_min, stock_max,unit_value]

    def search_index(name = str):
        '''
        Ingresa el nombre por el que deseas ordenar
        '''
        index = ['codigo', 'nombre', 'stock', 'stock minimo', 'stock maximo', 'valor unitario']
        return index.index(name.lower())
    
    def burble_sorted(lis, index):
        idx = ['codigo', 'nombre', 'stock', 'stock minimo', 'stock maximo', 'valor unitario']
        order = idx.index(index.lower())
        for i in range(len(lis)-1):
            if lis[i][order] > lis[i+1][order]:
                lis[i], lis[i+1]  = lis[i+1] , lis[i]
                products.burble_sorted(lis, index)
        return lis

    def binary_search (list, order_by, search):
        """
        En el primer elemento list: ingresa la lista a buscar
        """
        lista = products.burble_sorted(list, order_by)
        order = products.search_index(order_by)
        steps = 0
        left = 0
        right = len(lista) - 1
        while lista[left][order] <= lista[right][order]:
            steps += 1
            middle_point = (left+right)//2
            if lista[middle_point][order] == search:
                return f"""
codigo: {lista[middle_point][0]}
nombre: {lista[middle_point][1]}
stock: {lista[middle_point][2]}
stock minimo: {lista[middle_point][3]}
stock maximo: {lista[middle_point][4]}
Valor unitario: ${lista[middle_point][5]}
                """
            if lista[middle_point][order] > search:
                right =middle_point - 1 
            if lista[middle_point][order] < search:
                left =middle_point + 1 
        return f'El elemento {search} no se encontro'