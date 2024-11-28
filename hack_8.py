"""
list: [1,3,5,7,9] output => [3,5,7]
"""

def fn_hack_8():
    result = [1,3,5,7,9]
    lista_resultante = []
    for valor in result:
        if valor != 1 and valor != 9:
            lista_resultante.append(valor)
        
    result = lista_resultante
    return result

print(fn_hack_8())