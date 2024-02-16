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
funciones = ["=","MOVE","SKIP","TURN","FACE","PUT","PICK","MOVE-DIR","RUN-DIRS","MOVE-FACE","NULL"]
condiciones= ["FACING?","BLOCKED?","CAN-PUT?","CAN-PICK?","CAN-MOVE?","ISZERO?","NOT"]
definir=["DEFVAR","DEFUN"]
variables=["0","1","2","3","4","5","6","7","8","9",":LEFT",":RIGHT",":AROUND",":NORTH","SOUTH",":EAST",":WEST",":FRONT",":BACK",":BALLOONS",":CHIPS"]

def delimitador_cadenas(cadena: str)->int:
    i=1
    while True:
        if cadena[i]==" " or cadena[i]==")":
            return i-1
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
    nombre = str("Archivo texto\\") + str(nombre_usuario) 
    with open(nombre, 'r') as archivo:
        contenido = archivo.read()
        return contenido
    
def instrucciones(cadena:str)->list:
    cadenas =[]
    cadena_sin_espacios=cadena.replace("\n", "")
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
    while i<tamaño:
        if cadena[i]=="(":
            return ("(","")
        elif cadena[i]==")":
            return (")","")
    
    
    