from claseManejadorProyectos import ManejadorProyectos
from claseProyecto import Proyecto
from clasePersona import Persona
import csv
def item1(manejador):
    archi = open('proyectos.csv')
    reader =  csv.reader(archi, delimiter = ';')
    for li in reader:

        if(li[0] == 'idProyecto'):
            pass
        else:
            proye = Proyecto(li[0], li[1], li[2])
            manejadorProyectos.agregarProyecto(proye)
    archi.close()

def item2(manejador):
    archi = open('integrantesProyecto.csv')
    reader =  csv.reader(archi, delimiter = ';')
    for li in reader:
        if(li[0] == 'idProyecto'):
            pass
        else:
            integ = Persona(li[2], li[1], li[3], li[4])
            manejadorProyectos.agregarPersonaProyecto(li[0],integ)
    archi.close()

def item3(manejador): 
    '''calcular el puntaje de los proyectos'''
    '''ordenar los proyectos por puntaje'''
    '''mostrar el rankin de proyectos, ordenados por puntaje'''
    print('Listado de Proyectos (rankin por puntaje)')
    print('--------------------')
    manejadorProyectos.calcularPuntajeProyectos()
    manejadorProyectos.ordenarProyectosPorPuntaje()
    manejadorProyectos.mostrarProyectos()

if __name__=='__main__':
    manejadorProyectos = ManejadorProyectos()
    item1(manejadorProyectos)
    item2(manejadorProyectos)
    item3(manejadorProyectos)
