"""
TOKEN  CONTROLLLER
"""



producciones = {
    "I" : ["(defun name (PAR) I_funcion) I"," ", "(if(bool)I)"], #ES POSIBLE GUARDAR EN UN MISMO TOKEN EL NOMBRE DE LAS FUNCIONES Y LAS VARIABLES 
    "PAR" : ["(var PAR)" , " " ],
    "I_funcion" : [" "], 
    "bool" : [" "]
       
}
lst = []

for i in producciones:
    cada = producciones[i]
    producciones
