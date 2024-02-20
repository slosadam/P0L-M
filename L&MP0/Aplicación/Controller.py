"""
TOKEN  CONTROLLLER
"""
import model

""""
producciones = {
    "I" : ["(defun name (PAR) I_funcion) I"," ", "(if(bool)I)", "()"], #ES POSIBLE GUARDAR EN UN MISMO TOKEN EL NOMBRE DE LAS FUNCIONES Y LAS VARIABLES 
    "PAR" : ["(var PAR)" , " " ],
    "I_funcion" : [" "], 
    "bool" : [" "]   
}
"""
estructuras_de_control = ["IF","LOOP","REPEAT"]
funciones = ["=","MOVE","SKIP","TURN","FACE","PUT","PICK","MOVE","MOVE-DIR","RUN-DIRS","MOVE-FACE","NULL"]
condiciones= ["FACING?","BLOCKED?","CAN-PUT?","CAN-PICK?","CAN-MOVE?","ISZERO?","NOT"]
variables=[":LEFT",":RIGHT",":AROUND",":NORTH","SOUTH",":EAST",":WEST",":FRONT",":BACK",":BALLOONS",":CHIPS","DIM","MYXPOS","MYYPOS",
           "MYCHIPS","MYBALLOONS","BALLOONSHERE","CHIPSHERE","SPACES"]
for i in range(0, 100001):
    variables.append(str(i))
def delimitador_cadenas(cadena: str)->int:
    i=1
    while True:
        if cadena[i]==" " or cadena[i]==")" or cadena[i]=="(":
            return i+1
        i+=1
        
def delimitador_instruccion(texto: str)->int:
    i=0
    abiertos=0 
    centinela = True
    if texto[0] == "(":
        while centinela:
            if len(texto)>i:
                if texto[i] == "(":
                    abiertos+=1
                elif texto[i]== ")":
                    abiertos-=1
                if abiertos == 0:
                    centinela = False
                i+=1    
            else:
                return -1
        return i
    else:
        return -1

def abrir_archivo(nombre_usuario: str)->str:
    nombre = str("Archivo texto//") + str(nombre_usuario) 
    with open(nombre, 'r') as archivo:
        contenido = archivo.read()
        return contenido
    
def instrucciones(cadena:str)->list:
    cadenas =[]
    cadena_sin_espacios=cadena.replace("\n", "")
    centinela= cadena_sin_espacios[len(cadena_sin_espacios)-1]==" "
    while centinela:
        cadena_sin_espacios=cadena_sin_espacios[0:len(cadena_sin_espacios)-1]
        if cadena_sin_espacios[len(cadena_sin_espacios)-1]!=" ":
            centinela=False
    tamaño=len(cadena_sin_espacios)
    if cadena_sin_espacios[0]=="(" and cadena_sin_espacios[tamaño-1]==")":
        inicio=0
        while inicio<tamaño-1:
            limite=delimitador_instruccion(cadena_sin_espacios[inicio:tamaño])
            if limite>0:
                final=inicio + limite
                cadenas.append(cadena_sin_espacios[inicio:final])
                inicio=+final
            else:
                cadenas.append("ERROR_PARENTESIS_LLAMEN_A_DIOS")
                inicio=tamaño
    else:
        cadenas.append("ERROR_PARENTESIS_LLAMEN_A_DIOS")
    return cadenas

def tokenizador(cadena : str)->list:
    tamaño = len(cadena)
    i=0
    lst_final = []
    while i<tamaño:
        if cadena[i]=="(":
            lst_final.append(("(",""))
            i+=1
            
        elif cadena[i]==")":
            lst_final.append((")",""))
            i+=1
        elif cadena[i] == " ":
            i+=1
        else: 
            final = delimitador_cadenas(cadena[i:tamaño]) 
            
            if cadena[i:(i + final -1)].upper() in estructuras_de_control:
                lst_final.append(("control", cadena[i:(i + final -1)].lower()))
                i += final - 1
            elif cadena[i:(i + final -1)].upper() in funciones:
                lst_final.append(("fun", cadena[i:(i + final -1)].lower()))
                i += final - 1
            elif cadena[i:(i + final -1)].upper() in condiciones:
                lst_final.append(("cond", cadena[i:(i + final -1)].lower()))
                i +=final - 1
            elif cadena[i:(i + final -1)].upper() in variables:
                lst_final.append(("var", cadena[i:(i + final -1)].lower()))
                i += final - 1
            elif cadena[i:final].upper() == "DEFVAR":
                lst_final.append(("defvar", ""))
                i += final
                if i < tamaño and cadena[i] != " " and cadena[i] != ")":
                    final_falso = delimitador_cadenas(cadena[i:tamaño]) + i
                    lst_final.append(("var", cadena[i:final_falso-1]))
                    variables.append((cadena[i:final_falso-1]).upper())
                    i += (final_falso-i)
            elif cadena[i:final].upper() == "DEFUN":
                lst_final.append(("defun",""))
                i += final
                if i < tamaño and cadena[i] != " " and cadena[i] != ")":
                    final_falso = delimitador_cadenas(cadena[i:tamaño]) + i
                    lst_final.append(("fun", cadena[i:final_falso-1]))
                    funciones.append(cadena[i:final_falso-1].upper())
                    i += (final_falso - i) 
                    if i < tamaño:
                        if cadena[i] == "(":
                            lst_final.append(("(",""))
                            i+=1
                            if cadena[i] == ")":
                                lst_final.append((")", "")) 
                                i += 1
                            else:  
                                final_alt = delimitador_cadenas(cadena[i:tamaño]) +1
                                j = i
                                while i< (j + final_alt):
                                    final_feliz = delimitador_cadenas(cadena[i:i + final_alt])
                                    lst_final.append(("var", cadena[i:final_feliz + i - 1]))
                                    variables.append( cadena[i:final_feliz + i - 1].upper())
                                    i += final_feliz 
                                i -= 1
            else:
                return "defectuoso"       
    
    return lst_final

def tokenizar(instrucciones: list)->list:
    tokens = []
    if "ERROR_PARENTESIS_LLAMEN_A_DIOS" in instrucciones:
        tokens.append("defectuoso")
    else: 
        i=0   
        while i < len(instrucciones) and "defectuoso" not in tokens:
            tokens_ins = tokenizador(instrucciones[i])
            tokens.append(tokens_ins)
            i+=1
    
    return tokens

def analizador(tokens:list)->bool:
    return model.analizador(tokens)

    
    
    