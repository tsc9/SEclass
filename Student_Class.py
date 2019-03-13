# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 16:45:17 2019

@author: ttc
"""

# Define Student Class
class Student():
    majorSubject = ''
    minorSubject = ''
    CourseList = []
    
    def joinCourse(self, Course):
        self.CourseList.append(Course)
        
    def dropCourse(self, Course):
        self.CourseList.remove(Course)
        
# Initiate a student object s1
s1 = Student()
s2 = Student()
# Declare s1's major as MIS
s1.majorSubject = 'MIS'

s2.majorSubject = 'Law'
s2.minorSubject = 'Commerce'

# s1 join three courses
s1.joinCourse('Software_Engineering') 
s1.joinCourse('Data_Mining')
s1.joinCourse('AI')

print(s1.majorSubject)
print(s1.CourseList)

#s1 drop one course
s1.dropCourse('AI')
print(s1.CourseList)



print(s2.majorSubject)
#s2.joinCourse('Introduction to Law') 
print(s2.CourseList)