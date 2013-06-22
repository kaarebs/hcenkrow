from  core.hcenkrow import *
from  ui.beautiful import *

class HcenkrowFactory:
  @staticmethod
  def createObjectByName(name, arg=[]):
    constructor = globals()[name.title()]
    if len(arg) is 0:
      instance = constructor()
    else:
      instance = constructor(*arg)
    return instance
