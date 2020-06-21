import json
class Test():

  def __init__(self):
    self.id = -1
    self.nombre = ""
    self.intentos = ""

  def toJSON(self):
    return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)