# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 18:03:38 2019

@author: ttc
"""

#%%
class Person():
    firstName = ''
    lastName = ''
    birthDay = ''
    
    def __init__(self,firstName='',lastName='',birthDay=''):
        self.firstName = firstName
        self.lastName = lastName
        self.birthDay = birthDay
        
    def printPersonalInformation(self):
        print(self.firstName,self.lastName,self.birthDay)

# Define Student Class
class Student(Person):
    majorSubject = ''
    minorSubject = ''
    CourseList = []
    
    def __init__(self, firstName='',lastName='',birthDate='',Major='MIS',Minor=''):
        super().__init__(firstName, lastName, birthDate)
        self.majorSubject = Major
    
    def joinCourse(self, Course):
        self.CourseList.append(Course)
        
    def dropCourse(self, Course):
        self.CourseList.remove(Course)
        
    def printPersonalInformation(self):
        print(self.firstName,self.lastName,self.birthDay,self.majorSubject)       
        
# Initiate a student object s1
#%%
p1 = Person('Amy','Chang','10/20/2001')
p1.printPersonalInformation()   
        
#%%
s1 = Student('Betty','Wang','10/28/2001')
s1.printPersonalInformation()

#%%
# s1 join three courses
s1.joinCourse('Software_Engineering') 
s1.joinCourse('Data_Mining')
s1.joinCourse('AI')

print(s1.majorSubject)
print(s1.CourseList)

#s1 drop one course
s1.dropCourse('AI')
print(s1.CourseList)

# Declare s2's major as EE
s2 = Student('EE')
print(s2.majorSubject)
