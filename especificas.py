matriz=[ 
    [128, 355, 422], 
    [367, 105, 256], 
    [482, 203, 379], 
    [150, 477, 320], 
    [291, 167, 401], 
    [354, 232, 488], 
    [59, 275, 182], 
    [420, 384, 121], 
    [219, 499, 305], 
    [136, 411, 267] ] 

valores=[999,1499,799]

#0. Ingresar valores para la matriz
def subir_valores()->list:
    sucursales = int(input("¿Cuántas sucursales desea cargar? Ingrese cantidad: "))
    depositos = []
    
    for i in range(sucursales):
        array_temporal = []  #
        for k in range(3):
            valor = input(f"Ingrese el valor para el depósito {i} - {que_producto_es(k)}: ")
            array_temporal.append(valor)  # Agregamos el valor ingresado a la lista
        depositos.append(array_temporal)  # Agregamos la lista de productos al depósito
    
    return depositos

 


#1. Calcular el inventario total (stock disponible) de cada sucursal . Listo

def calcular_inventario(sucursal:list)->list:
    '''
    Calcula inventario por cada sucursal

    Args:
        sucursal(list): Lista doble a iterar.
    
    Return:
        Resultado de la suma del stock por sucursal.
    '''
    inventario_por_sucursal=[]

    for local in sucursal:
        suma=0
        for stock in local:
            suma+=stock
        inventario_por_sucursal.append(suma)
    return inventario_por_sucursal

def mostrar_array(matriz:list)->None:
    '''
    Itera los elementos de una matriz para mostrarlos de forma ordenada.

    Args:
        matriz(list): Lista a iterar.
    
    Return:
        None
    '''
    for i in matriz:
        print(i)

#2. Promedio de unidades de cada producto entre todos los depósitos.
def promedio_de_unidades(sucursales:list)->list:
    '''
    Calcula el promedio de la cantidad de cada producto sobre la cantidad total de stock

    Args:
        depositos(list): Lista de depositos con su stock
    Return:
        Lista con el porcentaje del promedio de cada producto.
    '''
    total_stock=0
    total_notebook=0
    total_smartphone=0
    total_tablet=0

    inv_total=calcular_inventario(sucursales)
    for i in inv_total:
        total_stock+=i
 
    for i in sucursales: 
        total_notebook+=i[0]
        total_smartphone+=i[1]
        total_tablet+=i[2]
    
    resultado=[]
    resultado.append(calcular_promedio(total_notebook,total_stock))
    resultado.append(calcular_promedio(total_smartphone,total_stock))
    resultado.append(calcular_promedio(total_tablet,total_stock))
    
    return resultado

def calcular_promedio(cantidad:int, total:int)->float:
    '''
    Calcula el promedio de la cantidad elegida contra el total real. 

    Args:
        cantidad(int): Cantidad para calcular.
        total(int): Total del universo.
    
    Return:
        Promedio de la cantidad sobre el total
    '''
    calculo_promedio=((cantidad * 100 )/ total)

    promedio=round(calculo_promedio,2)
    return promedio

#3. Determinar el nombre de el/los productos con más stock de cada sucursal.

def que_producto_es(indice:int)->str:
    '''
    Determina que producto es mediante el indice de posicion en el array.
    
    Args:
        indice(int): Valor entre 0 y 2.
    
    Return:
        Nombre del producto en el indice.
    '''
    if indice==0:
        return 'Notebook'
    if indice==1:
        return 'Smartphone'
    if indice==2:
        return 'Tablet'

def producto_mayor_por_sucursal(sucursales:list)->list:
    '''
    Determina cual es el producto mayor por sucursal. 

    Args:
        sucursales(list): Lista con las sucursales.
    
    Return:
        Lista con el nombre de cada producto con mayor stock por sucursal.
    '''
    mayor_por_sucursal=[]

    for sucursal in sucursales:
        indice_mayor=0
        cantidad_del_mayor=0
        for i,stock_producto in enumerate(sucursal):
            if stock_producto>cantidad_del_mayor:
                cantidad_del_mayor=stock_producto
                indice_mayor=i

        mayor_por_sucursal.append(que_producto_es(indice_mayor))
    
    return mayor_por_sucursal

#4. El o los productos con mayor existencias en dólares entre todos los depósitos.

def producto_de_mayor_valor_monetario(depositos:list)->list:
    '''
    Determina cual es el producto por deposito con mayor valor monetario.

    Args:
        depositos(list): Lista de depositos con su stock.
    
    Return:
        Nombre de los productos con su respectiva recaudacion.
    '''
    array_resultado=[]
    for deposito in depositos:
        producto_con_mayor_valor=0
        mayor_valor_monetario=0
        array_temporal=[]

        for k in range(len(deposito)):
            valor_actual_monetario= deposito[k] * valores[k]

            if valor_actual_monetario>mayor_valor_monetario:
                mayor_valor_monetario=valor_actual_monetario
                producto_con_mayor_valor=k

        array_temporal.append(que_producto_es(producto_con_mayor_valor))
        array_temporal.append(mayor_valor_monetario)
        array_resultado.append(array_temporal)  
    return array_resultado

def mostrar_array_anidado(array:list)->None:
    '''
    Muestra un array anidado de forma ordenada.

    Args:
        array(list):Matriz anidada.
    
    Return:
        None.
    '''
    #Notrebook, 900000
    for i in array:
        cadena=''
        cadena+=i[0]
        cadena+=', '
        cadena+=str(i[1])
        print (cadena)

#5. Crear un informe detallado con las unidades disponibles por sucursal, ordenadas de
#forma ascendente. 

def ordenar_array_ascendente(array:list)->list:
    '''
    Ordena un array en forma ascendete
    
    Args:
        Array(list): Array a ordenar
    
    Return:
        Array ordenado.
    ''' 
    array_a_ordenar=array.copy()
    n = len(array)  
     
    for i in range(n):    
        #128
        for k in range(i, n):

            if array_a_ordenar[i] < array_a_ordenar[k]:
                c = array_a_ordenar[i] 
                array_a_ordenar[i] = array_a_ordenar[k]
                array_a_ordenar[k] = c 

    return array_a_ordenar


def crear_informe_por_deposito(deposito:list)->list:
    '''
    Crea un informa del stock del deposito ordenado de mayor a menor.

    Args:
        depositos(list): Deposito a corroborar y ordenar.
    
    Return:
        Productos ordenador de mayor a menor por deposito
    
    '''
    array_resultado=[]

    for i in deposito:
        #111-333-555
        array_temporal=[]
        producto_actual=0
         
            