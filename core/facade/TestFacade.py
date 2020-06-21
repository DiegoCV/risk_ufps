from core.dao.factory.FactoryDao import *

class TestFacade():
  
  def insert(self, test):
    testDao = FactoryDao.getTestDao()
    return testDao.insert(test)
    
  
  def listAll(self):
    testDao = FactoryDao.getTestDao()
    return testDao.listAll()
    

 