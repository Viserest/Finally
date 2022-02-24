import json
from dateth import Date

class Task:
  def __init__(self, title:str, reps:int=1, amount:int=1):
    self.title = title
    self.reps = reps
    self.amount = amount
    self.total = reps * amount

class Event:
  def __init__(self, title:str, condition, contents:list, description:str=''):
    self.title = title
    self.contents = contents
    self.desc = description
  def save(self):
    file = list(json.load(open('bin/events.json')))
    file.append({
      'title':self.title,
      'condition':self.condition,
      'contents':[{} for _ in self.contents]
    })
    json.dump(file, 'bin/events.json', indent=4)
  @staticmethod
  def load(index):
    
