from clasePersona import Persona
class ManejadorPersonas:
    __personas=None
    def __init__(self):
        self.__personas = []
        
    def agregarPersona(self, persona):
        '''agrega a la colección un objeto persona que recibe como parámetro'''
        if(type(persona) == Persona):
            self.__personas.append(persona)

    def getCantidadIntegrantes(self):
        '''devuelve la cantidad de objetos que tiene la colección'''
        if self.__personas != None:
            return int(len(self.__personas))
        else:
            return "No se han agregado objetos a la coleccion"

    def getPersona(self, indice):
        '''recibe un indice de la lista, y devuelve un objeto Persona que está en esa posición'''
        return self.__personas[indice]