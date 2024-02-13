""""
ANALISIS SINTAXIS
"""
    
#del list[len(list)-1]
#tokens = [("(", ""), ("v", "4"),(")","")]
def parentesis_okay(tokens: list)->bool:
    ultimo_elem = len(tokens)-1
    if not(tokens[0][0] == "(" and tokens[ultimo_elem][0] == ")"):
        return False
    else: 
        pila = []
        for i in range(ultimo_elem + 1):
            if tokens[i][0] == "(":
                pila.append("(")
            elif tokens[i][0] == ")":
                tamanio_pila = len(pila)
                if tamanio_pila > 0:
                    del pila[tamanio_pila-1]
                else:
                    return False
        
        if len(pila) == 0:
            return True
        else: 
            return False
# (def nombre (4))
# (("(", ""), ("def", ""), ("nombre", "funcion"), ("var", "4"), (")", ""))


tokens = [("(", ""), ("(",""),("v", "4"),(")","")]
print(parentesis_okay(tokens))    


def funcion_bien_definida(tokens: list)->bool:
    if tokens[0][0] == "name":
        if tokens[1][0] == "(":
            centinela = (tokens[2][0] == "var")
            if centinela:
                i = 3
                while centinela: 
                    if tokens[i][0] == ")":
                        centinela = False
                    i+=1
                     
        
                    