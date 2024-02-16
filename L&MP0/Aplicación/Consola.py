"""""
CONSOLA
"""""
import Controller
import model

def iniciar_menu():
    print("------------------------------------------------------------------\n")
    print("Bienvenido")
    print("------------------------------------------------------------------\n")
    nombre_archivo=pedir_nombre_archivo()
    try: 
        texto=Controller.abrir_archivo(nombre_archivo)
        print("------------------------------------------------------------------\n")
        print("El archivo se abrió y leyó correctamente.")
        print("------------------------------------------------------------------\n")
        print("A continuación, se llevará a cabo el análisis del léxico y la sintáxis del texto ingresado.")
        print("------------------------------------------------------------------\n")
        instrucciones=Controller.instrucciones(texto)
        
        
    except (FileNotFoundError):
        print("------------------------------------------------------------------\n")
        print("Asegurese de que el archivo de texto se encuentre en la carpeta Archivo texto y el nombre esté bien escrito e intente nuevamente.")
        print("------------------------------------------------------------------\n")
    
def pedir_nombre_archivo():
    return str(input("Indique el nombre del archivo en formato .txt que contiene las instrucciones.\n"))

    
iniciar_menu()