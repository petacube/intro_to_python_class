class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

class Student(Person):
    specialization="Computer Science"
    college = "Benin University"
  pass

class Professor(Person):
    degree="Phd"
    specialization="Computer science"
    college = "Boston University"

class Dean(Professor):
    position ="Assistant Dean"

class CollegePresident(Dean):
    years_on_the_job = 10



