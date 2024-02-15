""""
ANALISIS SINTAXIS
"""
    
#del list[len(list)-1]
#tokens = [("(", ""), ("v", "4"),(")","")]

#run-dirs sacara el len y debe ser mayor a 0
funciones = {
    "move": 1,
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
def delimitador(tokens: list)->int:
    i=0
    abiertos=1 
    """""
    Quizás la métrica de la indexación induce un espacio topológico, aparantemente discreto, sobre la lista. 
    Sea tau una familia de subconjuntos de la lista.
    En primer lugar, el vacío y la lista completa pertenecen a tau.
    As,i mismo, la unión arbitraria de elementos de tau, pertenece a tau.
    Consideremos el conjunto A, una unión arbitraria no vacía de elementos de tau.
    Para todo x en  A se cumple que la bola centrada en x de radio 1 es igual a {x}, luego {x} está contenido en A.
    Concluimos que A es un abierto y por ende la unión arbitraria está en tau.
    Por último, por el mismo argumento, la intersección finita de elementos de tau está en tau.
    Concluimos que tau es un espacio topológico.
    Ahora, la demostración de que la indexación es una métrica queda como ejercicio para el lector.
    """""
    centinela = True
    while centinela:
        if tokens[i][0] == "()":
            abiertos+=1
        elif tokens[i][0] == ")":
            abiertos-=1
        if abiertos == 0:
            centinela = False
        i+=1
    return i

def defvar(tokens: list)->bool:
    if len(tokens)==3:
        if tokens[0][0]== "name":
            variables_globales.add(tokens[0][1])
            if tokens[1][0] == "num":
                return True
            else:
                return False
        return False    
    return False

# Asignar debe llamarse cuando la función que se detecte sea "=".
def asignar(tokens: list)->bool:
    if len(tokens)==3:
        if tokens[0][1] in variables_globales:
            if tokens[1][0] == "num":
                return True
            else:
                return False
        return False    
    return False

def put(tokens: list)->bool:
    if len(tokens)==3:
        if tokens[0][0]== ":balloons" or tokens[0][0]== ":chips":
            if tokens[1][1] in variables_globales:
                return True
            else:
                return False
        else:
            return False
    return False

def move(tokens: list)-> bool:
    if len(tokens) == 2:
        if tokens[1][0] in variables_globales:
            return True
        else:
            return False
    else:
        return False   

def llamar_funcion(tokens: list)-> bool:    
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

#Hace falta completar los condicionales con las demás funciones
def recorrer_llamado(tokens: list)->bool:
    if tokens[0][1] in funciones:
        return llamar_funcion(tokens)
    if tokens[0][1] == "put":
        return put(tokens)
    if tokens[0][1] == "move":
        return move(tokens)
    else:
        return False
    
#print(llamar_funcion(tokens_jr))

def funcion_bien_definida(tokens: list)->bool:
    if tokens[0][0] == "name":
        if tokens[1][0] == "(":
            variables = set()
            centinela = (tokens[2][0] == "var")
            i = 3
            if centinela:
                variables.add(tokens[2][1])
                variables_globales.add(tokens[2][1])
                while centinela: 
                    if tokens[i][0] == ")":
                        centinela = False
                    elif tokens[i][0] == "var":
                        variables.add(tokens[i][1])
                        variables_globales.add(tokens[i][1])
                    else:
                        return False
                    i+=1
            if i< len(tokens):
                centinela = tokens[i][0]=="fun"
                if centinela:
                    while centinela:
                        delimitador = delimitador(tokens[i:len(tokens)])
                        nuevo_limite=i+delimitador
                        if not recorrer_llamado(tokens[i:nuevo_limite]):
                            return False
                        if nuevo_limite+1<len(tokens): 
                            i=nuevo_limite+1
                        else:
                            centinela = False
                if tokens[i][0]==")":
                    funciones[tokens[0][0]:len(variables)]
                    for i in variables:
                        variables_globales.remove(i)
                    return True
            else:
                return False    
        else:
            return False
    else: 
        return False
print(funcion_bien_definida(tokens))
    
                     
        
                    