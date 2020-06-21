from core.dto.Test import *

class TestDao():

  def __init__(self, conexion):
    self.cn = conexion
    
  def insert(self, test):
    rta = Test()
    try:
      with self.cn.cursor() as cursor:
        sql = "INSERT INTO `user`(`nombre`,`intentos`) VALUES (%s, %s)"
        cursor.execute(sql, (test.nombre, test.intentos))
        rta.id = cursor.lastrowid
        self.cn.commit()
    except Error as e:
      print("Error reading data from MySQL table", e)
    finally:
      self.cn.cursor().close()
      return rta
   
  def  listAll(self):
    try:      
      tests = list()      
      mycursor = self.cn.cursor()
      mycursor.execute("SELECT * FROM user") 
      myresult = mycursor.fetchall()              
      for i in range(0,len(myresult)):                
        aux = Test()
        aux.id = myresult[i][0]
        aux.nombre = myresult[i][1]
        aux.intentos = myresult[i][3]
        tests.append(aux)
    except Exception as inst:
      print(type(inst))    # the exception instance
      print(inst.args)     # arguments stored in .args
      print(inst) 
    finally:
      mycursor.close()
      return tests