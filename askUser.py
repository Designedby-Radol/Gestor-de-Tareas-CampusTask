from ui.util import clear
def ask(msg):
    pass

def validUser (msg):
    print (msg) 
    opcion = input('elija un una  opcion (s/n): ')
    opcionesV = ['S','s']
    opcionesIN = ['N','n']
    if opcion in opcionesV :
        return True
    elif opcion in opcionesIN:
        return False
    else:
        print('usuario desconocido') 
        validUser()
        clear()