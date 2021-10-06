import json

class Data:
  def save(self, file):
    with open(file, 'w') as f:
      json.dump(self.__dict__[], f, indent=4)
  def load(self, file):
    with open(file) as f:
      self.__dict__[] = f

class Minecraft(Data):
  def createGame(self, options):
    self.players = []
    for k,v in options.items():
      self.__dict__[k] = v
  def addPlayer(self, options):
    self.players.append(options)
  def getPlayer(self, index):
    print(self.player[index])
  def editPlayer(self, index, options):
    for k,v in options.items():
      if v == None: self.players[index].pop(k)
      else: self.players[index][k] = v
  def removePlayer(self, index):
    print(self.players[index])
    if (input('Are you sure you want to delete this? (y,n)> ') == 'n'): return
    self.players.pop(index)
class Calendar(Data):
  events = []
  def addEvent(options):
    Calendar.events.append(options)
  def getEvents(time):
    print(e for e in Calendar.events if time in e['time'])
  def editEvent(index, options):
    for k,v in options.items():
      if v == None: Calendar.events[index].pop(k)
      else: Calendar.events[index][k] = v
  def removeEvent(index):
    print(Calendar.events[index])
    if (input('Are you sure you want to delete this? (y,n)> ') == 'n'): return
    Calendar.events.pop(index)
class School(Data):
  courses = {}
  def addCourse(name.toLower(), teacher, semester):
    School.courses[name] = {'teacher':teacher, 'semester':semester, 'assignments':[]}
  def getCourses():
    print(c for c in School.courses)
  def removeCourse(name.toLower()):
    print(School.courses[name])
    if (input('Are you sure you want to delete this? (y,n)> ') == 'n'): return
    School.courses.pop(name)
  def addAssignment(course.toLower(), options):
    School.courses[course]['assignments'].append(options)
  def getAssignements(course):
    if (course == None): print(a for a in School.courses)
    else: print(a for a in School.courses[course])
  def editAssignment(course.toLower(), index, options):
    for k,v in options.items():
      School.courses[course]['assignments'][index][k] = v
  def removeAssignment(course.toLower(), index):
    print(School.courses[course])
    if (input('Are you sure you want to delete this? (y,n)> ') == 'n'): return
    School.courses[course].pop(index)
