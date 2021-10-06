from datetime import date

Calendar.addEvent('School Days', {'2021/10':'10,11,12,13'}, {})
Calendar.addSchedule('School Normal Schedule', 'Monday,Tuesday,Thursday,Friday', {})
Calendar.addSchedule('School Wednesday Schedule', {}, {})
class Calendar:
  events = []
  schedules = []
  def addEvent(name, time, options):
    options['name'] = name
    options['time'] = time
    Calendar.events.append(options)
  def editEvent(index, options):
    pass
  def removeEvent(index):
    pass
  def addSchedule(name, time, options):
    options['name'] = name
    options['time'] = time
    Calendar.schedules.append(options)
  def editSchedule(index, options):
    pass
  def removeSchedule(index):
    pass
