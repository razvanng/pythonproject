class Person:
    def __init__(self,nume):
        self.nume = nume


class Student(Person):
    def Study(self):
        return  'Elevul studiaza'
    def mananca(self):
        return 'cartofi'

class Profesor(Person):
    def Preda(self):
        return '{} preda'.format(self.nume)
    def mananca(self):
        return 'paine'
class PrefesorAsistent(Student,Profesor):
    pass


student1 = Student('Liviu')
profesor1 = Profesor('xxx')
profesorassist1 = PrefesorAsistent('yyyy')

import pdb;pdb.set_trace()

