from core.facade.TestFacade import *
from core.dto.Test import *

class TestController():  

	def insertar(self, nombre, intentos):
		test_facade = TestFacade()
		test = Test()
		test.nombre = nombre
		test.intentos = intentos
		return test_facade.insert(test)

	def listarTodo(self):
		test_facade = TestFacade()
		return test_facade.listAll()
		
