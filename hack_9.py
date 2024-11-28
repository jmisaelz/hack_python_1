"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    result = [1,2,3]
    lista_resultante = []
    contador = 1
    while contador <= 3:
        lista_resultante.append(contador)
        lista_resultante.append('@')
        contador = contador + 1
    result = lista_resultante
    return result

print(fn_hack_9())