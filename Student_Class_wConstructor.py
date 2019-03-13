# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 17:07:45 2019

@author: ttc
"""

# Define Student Class
class Student():
    majorSubject = ''
    minorSubject = ''
    CourseList = []
    
    def __init__(self, Major='MIS'):
        self.majorSubject = Major
    
    def joinCourse(self, Course):
        self.CourseList.append(Course)
        
    def dropCourse(self, Course):
        self.CourseList.remove(Course)
        
# Initiate a student object s1
s1 = Student()

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
