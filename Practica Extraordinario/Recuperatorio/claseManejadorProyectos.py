from claseProyecto import Proyecto
class ManejadorProyectos:
    __proyectos=None
    def __init__(self):
        self.__proyectos = []

    def agregarProyecto(self, proyecto):
        '''recibe un objeto proyecto a agregar a la colección'''
        if type(proyecto) == Proyecto:
            self.__proyectos.append(proyecto)

    def mostrarProyectos(self):
        '''recorre la colección de proyectos, muestra los datos de proyecto y personas integrantes'''
        for li in self.__proyectos:
            print(li)

    def buscarProyectoPorId(self, idProyecto):
        '''dado un idProyecto, lo busca en la colección, si lo encuentra devuelve el proyecto, si no lo encuentra, devuelve una referencia None'''
        proy = None
        i = 0
        while i < len(self.__proyectos) and proy == None:
            if self.__proyectos[i].getIdProyecto() == idProyecto:
                proy = self.__proyectos[i]
            i += 1
        return proy

    def agregarPersonaProyecto(self, idProyecto, persona):
        '''recibe un idProyecto, y una persona a agregar a dicho Proyecto'''
        '''hace uso del método buscarProyectoPorId para buscar el Proyecto'''
        proy = self.buscarProyectoPorId(idProyecto)
        if proy != None:
            proy.agregarIntegrante(persona)

    def calcularPuntajeProyectos(self):
        '''para cada Proyecto de la colección, calcula el puntaje según reglas de negocio'''
        for i in self.__proyectos:
            i.calcularPuntaje()
        

    def ordenarProyectosPorPuntaje(self):
        '''invoca a la función sort de las lista, que hace uso del operador sobrecargado en la clase Proyecto __gt__'''
        self.__proyectos.sort()