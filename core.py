import json
import  os
from importlib.resources import files
from ui.messages import  tarjetas,elijaTablero
from ui.util import  clear

MY_DATABASE = files('data').joinpath('datos.json')

def newFile(*param):
    with open(MY_DATABASE,"w") as wf:
        json.dump(param[0],wf,indent=4)

def readFile():
    with open(MY_DATABASE,"r") as rf:
        return json.load(rf)

def checkFile(*param): #verificar archivo existente en caso del no crear
    data = list(param)
    if(os.path.isfile(MY_DATABASE)):
        if(len(param)):
            data[0].update(readFile())
    else:
        if(len(param)):
            newFile(data[0])

def addTarjetas():# agregar una tarjeta dentro de un tablero
    with open(MY_DATABASE,"r+") as rwfT:
        data = json.load(rwfT)
        val = True
        while val == True:
            clear()
            tablas=str(len(data['tablas']))
            print(f' hay : {tablas}\n')
            tableroElec = input(str(elijaTablero)) 
            if int(tableroElec) in range(1,int(tablas)+1):
                break
            else:
                input('no hay tablas con este numero')
                val == True
        clear()
        tarjeta = {
            'actividad': input(tarjetas['name']),
            'tipo' : input(tarjetas['tipo'])
            }
        nuevoId = str(len(data['tablas'][tableroElec])+1)
        data['tablas'][tableroElec][nuevoId] = tarjeta
        rwfT.seek(0)
        json.dump(data, rwfT, indent=4)
        rwfT.truncate()
    return print('Tarjeta creada')

def addTablas():#  agregar Tableros 
    with open(MY_DATABASE,"r+") as rwf:
        data = json.load(rwf)
        nombre  = input('ingrese nombre del tablero: ')
        tabla = {
            'nombreTabla': nombre
        }
        nuevoId = str(len(data['tablas']) + 1)
        data['tablas'][nuevoId] = tabla
        rwf.seek(0)
        json.dump(data, rwf, indent=4)
        rwf.truncate()
    return print('Tabla creada')

def eliminarTabla():#elimina tablero pidiendo 
    with open(MY_DATABASE, "r+") as f:
        data = json.load(f)
        tablas=str(len(data['tablas']))
        print(f' hay : {tablas}\n')
        tableroElec = input(str(elijaTablero)) 
        clear()
        if tableroElec in data['tablas']:
            del data['tablas'][tableroElec]
            tablas = data['tablas']
            nuevosTablas = {}
            for i, (idx, jugadorData) in enumerate(tablas.items()):
                nuevosTablas[f"{i+1}"] = jugadorData
            data['tablas'] = nuevosTablas
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
            print('eliminado')
        else:
            print('no se encontro')

def verTarjetas():# ver tarjetas
    with open(MY_DATABASE, "r+") as f:
        data = json.load(f)
        tablas = data['tablas']
        for id,tabla in tablas:
            for tarjeta in tabla:
                print(f'{id} - {tarjeta}-{tarjeta}')