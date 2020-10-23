import datetime

date = datetime.datetime.now()
textDefault = 'not found'

class Staff:
  def __init__(self, name=textDefault, pay=textDefault, admissionDate=textDefault):
    self.name = name
    self.pay = pay
    self.admissionDate = admissionDate
  
  def __repr__(self):
    return '(' + str(self.name) + ', ' + str (self.pay) + ', ' + str (self.admissionDate) + ')'

  def setStaff(self, name, pay, admissionDate):
    self.name = name
    self.pay = pay
    self.admissionDate = admissionDate
  
  def getStaff(self):
    return self.name, self.pay, self.admissionDate


class Manager(Staff):
  def setBonus(self, bonus=textDefault):
    self.bonus = bonus

  
staff1 = Staff()
print('Staff:', staff1.getStaff())

staff1.setStaff('Marcelo', 2000, date.strftime("%d/%m/%Y"))
print('Staff:', staff1.getStaff())

manager1 = Manager()
print('Manager:', manager1.getStaff())

manager1.setStaff('Bruno', 20000, date.strftime("%d/%m/%Y"))
manager1.setBonus(int(10))
manager1.pay += int(manager1.pay * manager1.bonus / 100) 
print('Manager:', manager1.getStaff())