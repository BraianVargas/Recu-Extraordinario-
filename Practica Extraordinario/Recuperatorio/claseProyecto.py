from claseManejadorPersonas import ManejadorPersonas
class Proyecto:
    __idProyecto=None
    __titulo=None
    __palabrasClave=None
    '''__integrantes es una instancia de ManejadorPersonas'''
    __integrantes=None
    __puntaje=None

    def __init__(self, idProyecto, titulo, palabrasClave):
        '''crea un proyecto a partir de los datos recibidos'''
        self.__idProyecto = idProyecto
        self.__titulo = titulo
        self.__palabrasClave = palabrasClave
        self.__integrantes = ManejadorPersonas()
        self.__puntaje = 0

    def getIdProyecto(self):
        '''devuelve el idProyecto'''
        return self.__idProyecto

    def agregarIntegrante(self, persona):
        '''agrega una Persona al manejador de Personas (__integrantes)'''
        self.__integrantes.agregarPersona(persona)

    def setPuntaje(self, puntaje):
        '''establece el valor del puntaje al atributo __puntaje'''
        self.__puntaje = puntaje

    def getPuntaje(self):
        '''devuelve el valor del __puntaje del Proyecto'''
        return int(self.__puntaje)

    def calcularPuntaje(self):
        print('Cálculo de puntajes')
        print('-------------------')
        '''imprimr datos del ¨Proyecto'''
        '''luego realizar cálculo de puntaje'''
        puntaje = 0
        #Verifica Cantidad Integrantes
        if(self.__integrantes.getCantidadIntegrantes() >= 3):
            puntaje += 10
        else:
            puntaje = puntaje - 20
            print("‘El Proyecto debe tener como mínimo 3 integrantes’")
        
        #Regla de negocio DIRECTOR
        banDire = False
        i = 0
        while i < self.__integrantes.getCantidadIntegrantes() and banDire == False:
            if self.__integrantes.getPersona(i).getRol().lower() == 'director':
                banDire = True
                if self.__integrantes.getPersona(i).getCategoria() == 'I' or self.__integrantes.getPersona(i).getCategoria() == 'II':
                    puntaje += 10
                else:
                    puntaje = puntaje - 5
                    print("‘El Director del Proyecto debe tener categoría I o II.’")
            i += 1
        if banDire == False:
            print("‘El Proyecto debe tener un Director.’")
            puntaje = puntaje - 10

        #Regla de negocio CO-DIRECTOR
        banDire = False
        i = 0
        while i < self.__integrantes.getCantidadIntegrantes() and banDire == False:
            if self.__integrantes.getPersona(i).getRol().lower() == 'codirector':
                banDire = True
                if self.__integrantes.getPersona(i).getCategoria() == 'I' or self.__integrantes.getPersona(i).getCategoria() == 'II' \
                    or self.__integrantes.getPersona(i).getCategoria() == 'III':
                    puntaje += 10
                else:
                    puntaje = puntaje - 5
                    print("‘El Codirector del Proyecto debe tener como mínimo categoría III’")
            i += 1
        if banDire == False:
            print("‘El Proyecto debe tener un Codirector.’")
            puntaje = puntaje - 10
        
        self.__puntaje = puntaje


    def __gt__(self, otroProyecto):
        '''utilizado para ordenar de mayor a menor los Proyectos, según el puntaje obtenido'''
        if self.getPuntaje() > otroProyecto.getPuntaje():
            return (self)
        else:
            return (otroProyecto)

    def __str__(self):
        '''devuelve una cadena con los datos del Proyecto y de los integrantes del mismo'''
        s = "\nPuntaje del Proyecto: {} ".format(self.getPuntaje())
        s += "\nId del Proyecto: {} " .format(self.__idProyecto)
        s += "\nTitulo: {}" .format(self.__titulo)  
        s += "\nPalabras Clave: {}" .format(self.__palabrasClave)
        s += "\n**************** INTEGRANTES ****************"
        cant = self.__integrantes.getCantidadIntegrantes()
        for i in range(cant):
            pers = "\n{}" .format(self.__integrantes.getPersona(i))
            s += pers.__str__()
            s += "\n"

        return s