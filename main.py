from factories.factory import *

hcen = HcenkrowFactory.createObjectByName('hcenkrow')
ui = HcenkrowFactory.createObjectByName('beautiful', [hcen])
ui.render()

