""""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    result = "fooziman"
    lista_resultante = []
    for valor in result:
        if valor == "o":
            lista_resultante.append("0")
        elif valor == "i":
            lista_resultante.append("1")
        elif valor == "a":
            lista_resultante.append("@")
        else:
            lista_resultante.append(valor.upper())

    result = lista_resultante
    return result

print(fn_hack_10())