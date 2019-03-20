# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 18:03:38 2019

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

# Define Course Class
class Course():
    courseList = []
    
    def __init__(self, courseName=''):
        self.courseList.append([courseName,{}])
        
    @classmethod
    def allCourse(self):
        return([course[0] for course in self.courseList])
        
    @classmethod        
    def joinCourse(self, courseName='', Student=None):
        for sCourse in self.courseList:
            if sCourse[0] == courseName:
                sCourse[1][Student.idStudent] = Student.firstName + ' ' + Student.lastName
 
    @classmethod      
    def dropCourse(self, courseName='',Student=None):
        for sCourse in self.courseList:
            if sCourse[0] == courseName:
                id = sCourse[1].get(Student.idStudent)
                if id != None:
                    del sCourse[1][Student.idStudent]        

    @classmethod      
    def queryCourse(self, Student=None):
        cList = []
        for sCourse in self.courseList:
            id = sCourse[1].get(Student.idStudent)
            if id != None:
                cList.append(sCourse[0])
        return(cList)

    @classmethod      
    def queryStudent(self, courseName=''):
        sList = []
        for sCourse in self.courseList:
            if sCourse[0] == courseName:
                for aStudent in sCourse[1].values():
                    sList.append(aStudent)
        return(sList)
                            
# Define Student Class
class Student(Person):
    majorSubject = ''
    minorSubject = ''
    idStudent = ''
    studentList = {}
    
    def __init__(self, firstName='',lastName='',birthDate='',Major='MIS',Minor='',id='00000'):
        super().__init__(firstName, lastName, birthDate)
        self.majorSubject = Major
        self.minorSubject = Minor
        self.idStudent = id
        self.studentList[id] = firstName + ' ' + lastName
        
    def printPersonalInformation(self):
        print(self.firstName,self.lastName,self.birthDay,self.majorSubject)
    
    @classmethod     
    def allStudent(self):
        return(self.studentList)
        
        
# Initiate three courses
#%%
# Initial four courses
Course('Software_Engieering')
Course('Data_Mining')
Course('AI')
Course('Research_Methodology') 
print(Course.allCourse())    

#%%
p1 = Person('Amy','Chang','10/20/2001')
p1.printPersonalInformation()   
        
#%%
# Initiate students' object
s1 = Student('Betty','Wang','10/28/2001',id='12345')
s2 = Student('Carol','Hsu','08/28/2001',id='12340')
s3 = Student('Diana','Ross','05/28/1971',id='12349')
s1.printPersonalInformation()

#%%
# Student 1 join and drop courses
print(s1.majorSubject)
Course.joinCourse('Software_Engieering',s1)
Course.joinCourse('Data_Mining',s1)
Course.joinCourse('AI',s1)
print (Course.queryCourse(s1))  
Course.dropCourse('AI',s1)
print(Course.queryCourse(s1))

#%%
# Student 2 join courses
Course.joinCourse('Software_Engieering',s2)
Course.joinCourse('Data_Mining',s2)
Course.joinCourse('AI',s2)
print(Course.queryCourse(s2))

#%%
# Qeury who took the Data Mining course and list all students afterward
print(Course.queryStudent('Data_Mining'))
print(Student.allStudent())
