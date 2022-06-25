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
        list.burble_sorted(list, order_by)
        order = products.search_index(order_by)
        steps = 0
        left = 0
        right = len(list) - 1
        while left[order] <= right[order]:
            steps += 1
            middle_point = (left+right)//2
            if list[middle_point] == search:
                return 'Valor encontrado en {0} pasos en la posición {1}'.format(steps, middle_point)
            if list[middle_point] > search:
                right =middle_point - 1 
            if list[middle_point] < search:
                left =middle_point + 1 
        return f'El elemento {search} no se encontro'