from core.dao.conexion.conexiones.ConexionPyMySql import *
from core.dao.properties.Propiedades import *

class Conexion(object):

  __instance = None
  mi_conexion = None
  p = Propiedades()

  def obtenerConexion(self):
    print(self.p.get_db_password())
    if self.mi_conexion is None:
      self.mi_conexion = ConexionPyMySql().obtener_conector(self.p.get_db_host(), int(self.p.get_db_port()), self.p.get_db_user(), self.p.get_db_password(), self.p.get_db_name())
    return self.mi_conexion

  def __new__(cls):
    if Conexion.__instance is None:
      Conexion.__instance = object.__new__(cls)
    return Conexion.__instance
			