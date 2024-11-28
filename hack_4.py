"""
text: "fooziman" output => "foozimaN"
"""

def fn_hack_4():
    result = "fooziman"
    texto_final = []
    contador = 0
    for cadena in result:
        if contador == len(result)-1:
            letra = cadena.upper()
            texto_final.append(letra)
        else:
            texto_final.append(cadena)
        contador = contador + 1

    result = "".join(texto_final)
    return result

print(fn_hack_4())
