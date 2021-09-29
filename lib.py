# Minecraft Class
class Minecraft:
  class Game(PlayerI):
    def __init__(self, options):
      for k,v in options.items():
        self.__dict__[k] = v
    def addPlayer(self, options): self.players.append(Minecraft.Player(options))
    def 
  class Player:
    def __init__(self, options):
      for k,v in options.items():
        self.__dict__[k] = v
game = Minecraft({'name':'LastLife','players':[]})
game.players.append({'name':'Viserest','hearts':20})
