"""
text: "fooziman" output => "f00z1m@n"
"""

def fn_hack_5():
    result = "fooziman"
    texto_final = []
    for cadena in result:
        if cadena == "o":
            letra = "0"
            texto_final.append(letra)
        elif cadena ==  "i":
            letra = "1"
            texto_final.append(letra)
        elif cadena == "a":
            letra = "@"
            texto_final.append(letra)
        else:
            texto_final.append(cadena)

    result = "".join(texto_final)
    return result

print(fn_hack_5())