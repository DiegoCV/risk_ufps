import pymysql

class ConexionPyMySql:

	@staticmethod
	def obtener_conector(my_host, my_port, my_user, my_password, my_database):
		mydb = pymysql.connect(
  			host = my_host,
  			port = my_port,
  			user = my_user,
			passwd = my_password,
			db = my_database,			
		)
		return mydb