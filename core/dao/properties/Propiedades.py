import os

class Propiedades():

	def __init__(self):
		self.cfg = {
			"DB_HOST" : os.environ["DB_HOST_RIESGO"],
			"DB_PORT" : os.environ["DB_PORT_RIESGO"],			
    		"DB_USER" : os.environ["DB_USER_RIESGO"],
    		"DB_PASS" : os.environ["DB_PASS_RIESGO"],
    		"DB_NAME" : os.environ["DB_NAME_RIESGO"]
		}

	def get_db_host(self):
		return self.cfg['DB_HOST']

	def get_db_user(self):
		return self.cfg['DB_USER']

	def get_db_password(self):
		return self.cfg['DB_PASS']

	def get_db_name(self):
		return self.cfg['DB_NAME']

	def get_db_port(self):
		return self.cfg['DB_PORT']