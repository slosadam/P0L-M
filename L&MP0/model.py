""""
ANALISIS SINTAXIS
"""
    
#del list[len(list)-1]
#tokens = [("(", ""), ("v", "4"),(")","")]

#run-dirs sacara el len y debe ser mayor a 0
funciones = {
    "skip" : 1, 
    "null" : 0, 
}


variables_globales = set()

#variables_globales.add()

tokens_jr = [("fun", "skip"),("var", "cornelio"), (")", "")]

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

tokens = [("name", "fo"),("(",""),("var", "4"),(")","")]
#print(parentesis_okay(tokens))    

def llamar_funcion(tokens: list)-> bool:
    if tokens[0][1] in funciones:
        centinela = (tokens[1][0] == "var")
        contador = 0
        i = 1
        while centinela:
            if tokens[i][0]== ")":
                centinela = False
            elif tokens[i][0] == "var":
                contador += 1
            else: 
                return False
            i+=1
        return contador == funciones[tokens[0][1]]
    else:
        return False
    
print(llamar_funcion(tokens_jr))

def funcion_bien_definida(tokens: list)->bool:
    if tokens[0][0] == "name":
        if tokens[1][0] == "(":
            variables = set()
            centinela = (tokens[2][0] == "var")
            if centinela:
                i = 3
                variables.add(tokens[2][1])
                while centinela: 
                    if tokens[i][0] == ")":
                        centinela = False
                    elif tokens[i][0] == "var":
                        variables.add(tokens[i][1])
                    else:
                        return False
                    i+=1
            else: 
                return False
        else:
            return False
    else: 
        return False
#print(funcion_bien_definida(tokens))
    
                     
        
                    