from core.dao.conexion.Conexion import *
from core.dao.entities.TestDao import *


class FactoryDao():
    
    @staticmethod    
    def getTestDao():
        conexion = Conexion()
        return TestDao(conexion.obtenerConexion())

 