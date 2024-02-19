""""
ANALISIS SINTAXIS
"""
funciones = {
    "move": 1,
    "skip" : 1, 
    "null" : 0,
    "isZero" : 1,
    "not":1,
    "facing?": 1,
    "blocked?": 0,
    "can-put?" :2,
    "can-pick" :2 ,
    "can-move?" :1, 
}

#cambio de rama prueba


variables_globales = set(["0","1","2","3","4","5","6","7","8","9",":LEFT",":RIGHT",":AROUND",":NORTH","SOUTH",":EAST",":WEST",
                          ":FRONT",":BACK",":BALLOONS",":CHIPS","DIM","MYXPOS","MYYPOS","MYCHIPS","MYBALLOONS","BALLOONSHERE",
                          "CHIPSHERE","SPACES","FACING?", "BLOCKED?", "CAN-PUT?", "CAN-PICK", "CAN-MOVE?"])

for i in range(0, 100001):
    variables_globales.add(str(i))
    
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
   
def delimitador(tokens: list)->int:
    i=0
    abiertos=1 
    centinela = True
    while centinela:
        if tokens[i][0] == "(":
            abiertos+=1
        elif tokens[i][0] == ")":
            abiertos-=1
        if abiertos == 0:
            centinela = False
        i+=1
    return i

def defvar(tokens: list)->bool:
    if len(tokens)==4:
        if tokens[1][0]== "var":
            variables_globales.add(tokens[1][1])
            if tokens[2][0] == "var":
                return True
            else:
                return False
        return False    
    return False

# Asignar debe llamarse cuando la función que se detecte sea "=".
def asignar(tokens: list)->bool:
    if len(tokens)==4:
        if tokens[1][1] in variables_globales:
            if tokens[2][0] == "var":
                return True
            else:
                return False
        return False    
    return False

def put(tokens: list)->bool:
    if len(tokens)==4:
        if tokens[1][1]== ":balloons" or tokens[1][1]== ":chips":
            if tokens[2][1] in variables_globales:
                if tokens[3][0] == ")":
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    return False

def pick(tokens: list)->bool:
    if len(tokens)==4:
        if tokens[1][1]== ":balloons" or tokens[1][1]== ":chips":
            if tokens[2][1] in variables_globales:
                if tokens[3][0] == ")":
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    return False


def turn(tokens: list)->bool:
    if len(tokens)==3:
        if tokens[1][1]== ":left" or tokens[1][1]== ":right" or tokens[1][1] == ":around":
                if tokens[2][0] == ")":
                    return True
                else:
                    return False
        else:
            return False
    return False

def face(tokens: list)->bool:
    if len(tokens)==3:
        if tokens[1][1]== ":north" or tokens[1][1]== ":west" or tokens[1][1] == ":south" or tokens[1][1] == ":east" :
                if tokens[2][0] == ")":
                    return True
                else:
                    return False
        else:
            return False
    return False

def run_dirs(tokens: list)-> bool:
    if len(tokens) > 1:
        i=1
        centinela=True
        while i<len(tokens)-1 and centinela:
            if tokens[i][1] != ":front" and tokens[i][1] != ":right" and tokens[i][1] != ":left" and tokens[i][1] != ":back":
                return False
            i+=1
        if tokens[i][0]== ")":
            return True
        else:
            return False
    else:
        return False   


def move_dir(tokens: list)-> bool:
    if len(tokens) == 4:
        if tokens[1][1] in variables_globales:
            if tokens[2][1]== ":front" or tokens[2][1]== ":right" or tokens[2][1] == ":left" or tokens[2][1] == ":back" :
                if tokens[3][0] == ")":
                    return True
                else: return False
            else:
                return False
        else:
            return False
    else:
        return False   

def move_face(tokens: list)-> bool:
    if len(tokens) == 4:
        if tokens[1][1] in variables_globales:
            if tokens[2][1]== ":north" or tokens[2][1]== ":west" or tokens[2][1] == ":south" or tokens[2][1] == ":east" :
                if tokens[3][0] == ")":
                    return True
                else: return False
            else:
                return False
        else:
            return False
    else:
        return False   

def facing_cond(tokens: list)->bool:
    if len(tokens) == 3:
        if tokens[1][1] == ":north" or tokens[1][1] == ":south" or tokens[1][1] == ":east" or tokens[1][1] == ":west":
            if tokens[2][0] == ")":
                return True
            else:
                return False
        else: 
            return False
    else:
        return False
    
def can_put(tokens: list)->bool:
    if len(tokens)==4:
        if tokens[1][1]== ":balloons" or tokens[1][1]== ":chips":
            if tokens[2][1] in variables_globales:
                if tokens[3][0] == ")":
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    return False

def can_pick(tokens: list)->bool:
    if len(tokens)==4:
        if tokens[1][1]== ":balloons" or tokens[1][1]== ":chips":
            if tokens[2][1] in variables_globales:
                if tokens[3][0] == ")":
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    return False

def can_move(tokens:list)->bool:
    if len(tokens)==3:
        if tokens[1][1]== ":north" or tokens[1][1]== ":west" or tokens[1][1] == ":south" or tokens[1][1] == ":east" :
                if tokens[2][0] == ")":
                    return True
                else:
                    return False
        else:
            return False
    return False

def not_cond(tokens:list)->bool:
    if len(tokens) == 3:
        if tokens[1][1] == "facing?" or tokens[1][1] == "blocked?" or tokens[1][1] == "can-put?" or tokens[1][1] == "can-pick?" or tokens[1][1]=="isZeor?" or tokens[1][1] == "can-move?":
            if tokens[2][0] == ")":
                return True
            else:
                return False
        else: 
            return False
    else:
        return False

def isZero(tokens: list)->bool:
    if len(tokens) == 4:
        if tokens[1][1] == "myChips" or tokens[1][1] == "myBalloons":
            if tokens[2][1] in variables_globales:
                if tokens[3][0] == ")":
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    return False

#revisar si funcion blocked es necesaria o puede ser aplicada igual que null
def blocked(tokens: list)-> bool:
    if len(tokens) == 0:
        if tokens[1][1] == ")":
            return True
        else:
            return False
    else:
        return False
        

def if_cond(tokens: list)->bool:
    i = 0
    if tokens[0][0] == "if":
        i += 1
        
        if tokens[1][1] == "facing?" or tokens[1][1] == "blocked?" or tokens[1][1] == "can-put?" or tokens[1][1] == "can-pick?" or tokens[1][1]=="isZeor?" or tokens[1][1] == "not" or tokens[1][1] == "can-move?":
            i+=1
            if tokens[2][1] in variables_globales:
                i+=1
                if tokens[3][0] == ")":
                    i+= 1
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False
    

def repeate(tokens: list)->bool:
    i = 0
    if tokens[0][0] == "loop":
        i += 1
        if tokens[1][1] == "facing?" or tokens[1][1] == "blocked?" or tokens[1][1] == "can-put?" or tokens[1][1] == "can-pick?" or tokens[1][1]=="isZeor?" or tokens[1][1] == "not" or tokens[1][1] == "can-move?":
            i+= 1
            if tokens[2][1] in variables_globales: # no se si este bien 
                i+= 1
                if tokens[3][0] == ")":
                    i+=1
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else: 
        return False
   
def repeate_times(tokens: list)->bool:
    i = 0
    if tokens[0][0] == "repeat":
        i+= 1
        if tokens[1][1] > 0 and tokens[1][1] in variables_globales:
            i+= 1
            if tokens[2][1] in variables_globales:
                i+= 1
                if tokens[3][0] == ")":
                    i+= 1
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False
    
      
def llamar_funcion(tokens: list)-> bool:    
    if len(tokens) == funciones[tokens[0][1]] + 2:
        centinela = (tokens[1][1] in variables_globales)
        contador = 0
        i = 1
        while centinela:
            if tokens[i][0]== ")":
                centinela = False
            elif tokens[i][1] in variables_globales:
                contador += 1
            else: 
                return False
            i+=1
        return contador == funciones[tokens[0][1]]
    else:
        return False

#Hace falta completar los condicionales con las demás funciones
def recorrer_llamado_funcion(tokens: list)->bool:
    tamaño=len(tokens)
    if tokens[0][1] in funciones:
        return llamar_funcion(tokens[0:tamaño])
    elif tokens[0][1] == "put":
        return put(tokens[0:tamaño])
    elif tokens[0][1] == "move-dir":
        return move_dir(tokens[0:tamaño])
    elif tokens[0][1] == "=":
        return asignar(tokens[0:tamaño])
    elif tokens[0][1] == "pick":
        return pick(tokens[0:tamaño])
    elif tokens[0][1] == "turn":
        return turn(tokens[0:tamaño])
    elif tokens[0][1] == "face":
        return face(tokens[0:tamaño])
    elif tokens[0][1] == "move-face":
        return move_face(tokens[0:tamaño])
    elif tokens[0][1] == "run-dirs":
        return run_dirs(tokens[0:tamaño])
    if tokens[0][1] == "facing?":
        return facing_cond(tokens[0:tamaño])
    elif tokens[0][1] == "can-put?":
        return can_put(tokens[0:tamaño])
    elif tokens[0][1] == "can-pick?":
        return can_pick(tokens[0:tamaño])
    elif tokens[0][1] == "can-move?":
        return can_move(tokens[0:tamaño])
    elif tokens[0][1] == "not":
        return not_cond(tokens[0:tamaño])
    elif tokens[0][1] == "isZero?":
        return isZero(tokens[0:tamaño])
    
    else:
        return False
    
def recorrer_llamado_condicionales(tokens: list)-> bool:
    tamaño = len(tokens)
    if tokens[0][1] == "if":
        return if_cond(tokens[0: tamaño])
    elif tokens[0][1] == "loop":
        return repeate(tokens[0:tamaño])
    elif tokens[0][1] == "repeat":
        return repeate_times(tokens[0:tamaño])
    else: 
        return False
        

def funcion_bien_definida(tokens: list)->bool:
    if tokens[1][0] == "fun":
        if tokens[2][0] == "(":
            variables = set()
            centinela = (tokens[3][0] == "var")
            i = 4
            if centinela:
                variables.add(tokens[3][1])
                variables_globales.add(tokens[3][1])
                while centinela: 
                    if tokens[i][0] == ")":
                        centinela = False
                    elif tokens[i][0] == "var":
                        variables.add(tokens[i][1])
                        variables_globales.add(tokens[i][1])
                    else:
                        return False
                    i+=1
            if (tokens[i-1][0] == ")"):
                if i< len(tokens):
                    if tokens[i][0] == "(":
                        i+=1
                        centinela_fun = tokens[i][0]=="fun"
                        if centinela_fun:
                            while centinela_fun:
                                final = delimitador(tokens[i:len(tokens)-1])
                                nuevo_limite=i+final
                                if not recorrer_llamado_funcion(tokens[i:nuevo_limite]):
                                    return False
                                if nuevo_limite+1<len(tokens): 
                                    i=nuevo_limite+1
                                else:
                                    centinela_fun = False
                        if tokens[nuevo_limite][0]==")":
                            funciones[tokens[1][1]]=len(variables)    
                if i< len(tokens):
                    if tokens[i][0] == "(":
                        i+=1
                        centinela_cond = tokens[i][0]=="cond"
                        if centinela_cond:
                            while centinela_cond:
                                final = delimitador(tokens[i:len(tokens)-1])
                                nuevo_limite=i+final
                                if not recorrer_llamado_condicionales(tokens[i:nuevo_limite]):
                                    return False
                                if nuevo_limite+1<len(tokens): 
                                    i=nuevo_limite+1
                                else:
                                    centinela_fun = False
                        if tokens[nuevo_limite][0]==")":
                            funciones[tokens[1][1]]=len(variables)                     
                            if len(variables) != 0:
                                for i in variables:
                                    variables_globales.remove(i)
                                return True
            else:
                return False    
        else:
            return False
    else: 
        return False


def identificador_llamado(tokens:list)->bool:
    tamaño=len(tokens)
    if tokens[0][0]=="defvar":
        return defvar(tokens[0:tamaño])
    if tokens[0][0]=="defun":
        return funcion_bien_definida(tokens[0:tamaño])
    if tokens[0][0]=="cond":
        return recorrer_llamado_condicionales(tokens[0:tamaño])
    if tokens[0][0]=="fun":
        return recorrer_llamado_funcion(tokens[0:tamaño])
    else:
        return False
        
def analizador(tokens:list)->bool:
    if "defectuoso" not in tokens:
        resultado=True
        i=0
        while i<len(tokens) and resultado:            
            if parentesis_okay(tokens[i]):
                resultado=identificador_llamado(tokens[i][1:len(tokens[i])])
            i+=1
        return resultado    
    else:
        return False
    
