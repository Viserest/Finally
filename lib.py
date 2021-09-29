class Players:
  def addPlayer(self, options):
    self.players.append()
  def editPlayer(self, index, options):
    for k,v in options.items():
      self.players[index][k] = v
  def removePlayer(self, index):
    self.players.pop(index)

# Minecraft Class
class Minecraft:
  def __init__(self, options):
    for k,v in options.items():
      self.__dict__[k] = v
  def addPlayer(self, options):
    self.players.append(Minecraft.Player(options))
  def editPlayer(self, index, options):
    for k,v in options.items():
      self.players[index][k] = v
  def removePlayer(self, index):
    self.players.pop(index)
game = Minecraft({'name':'LastLife','players':[]})
game.players.append({'name':'Viserest','hearts':20})
