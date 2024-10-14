from especificas import *

def init():   
    redirigir_opcion()
    

def mostrar_menu():
    '''
        Muestra las opciones de menu
    ''' 
    menu= '''
=== MENU ===

1. Calcular el inventario total (stock disponible) de cada sucursal .
2. Promedio de unidades de cada producto entre todos los depósitos.
3. Determinar el nombre de el/los productos con más stock de cada sucursal.
4. El o los productos con mayor existencias en dólares entre todos los depósitos.
5. Crear un informe detallado con las unidades disponibles por sucursal, ordenadas de
forma ascendente. SIN COMPLETAR
6. Salir
''' 
    print (menu)

def redirigir_opcion()->None:
    opcion=0
    matriz=subir_valores()
    
    while opcion !=6:
        print(mostrar_menu())
        opcion=int(input("Ingrese su opcion:"))

        match opcion:
            case 1:
                mostrar_array(calcular_inventario(matriz))
            case 2:
                mostrar_array(promedio_de_unidades(matriz))
            case 3:
                mostrar_array(producto_mayor_por_sucursal(matriz))
            case 4:
                mostrar_array_anidado(producto_de_mayor_valor_monetario(matriz))
            # case 5:
            case _: 
                print("Ingrese una de las opciones.")

