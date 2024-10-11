from core import checkFile,addTarjetas,addTablas,eliminarTabla,verTarjetas
from ui.messages import tarjetas,elejir
from ui.util import clear
data ={
    'tablas':{}
}
checkFile(data)

elegir = None
while elegir  != 5 :
    elegir = input(elejir['msg'])
    clear()
    match elegir :
        case '1':
            addTablas()
        case  '2':
            addTarjetas()
        case '3':
            eliminarTabla()
        case '4':
            pass
        case '5':
            elegir = 5
            clear()

def gestionTable(): # gestionar tablas
    elegir = None
    while elegir  != 5 :
        elegir = input()
        clear()
        match elegir :
            case '1':
                addTablas()
            case  '2':
                addTarjetas()
            case '3':
                eliminarTabla()
            case '4':
                pass
            case '5':
                elegir = 5
                clear()
