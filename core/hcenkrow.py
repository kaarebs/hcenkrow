from core.backend import Backend
class Hcenkrow:
  def __init__(self):
    self.name = 'hcenkrow is my name'
    self.backend = Backend()
  def getName(self):
    return self.name

  def list(self):
    str = "SELECT * FROM Writers" ## testing ##
    return self.backend.list(str)

