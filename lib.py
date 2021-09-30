class Context:
  storage = self.__dict__[self.__dict__['storage']]
  def addEntity(self, options):
    self[storage].append({k:v for k,v in options.items()})
  def editEntity(self, index, options):
    for k,v in options.items():
      if (v == None) self.entities[index].pop(k)
      self.entities[index][k] = v
  def removeEntity(self, index):
    self.entities.pop(index)

class Minecraft(Context):
  def game(self, options):
    self.entities = []
    for k,v in options.items():
      self.__dict__[k] = v
class Calendar:
  events = []
  def addEvent(self, options):
    Calendar.events.append({k:v for k,v in options.items()})
  def editEvent(self, index, options):
    for k,v in options.items():
      Calendar.events[index][k] = v
  def removeEvent(self, index):
    Calendar.events.pop(index)
# test
game = Minecraft.game({'name':'LastLife'})
game.addEntity({'name':'MumboJumbo', 'lives':3, 'boogieMan':False})
game.editEntity({'boogieMan':None, 'boogeyMan':False})

Calendar.addEvent()
