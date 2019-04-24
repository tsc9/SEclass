# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 20:33:58 2019

@author: ttc
referencing https://www.tutorialsteacher.com/ioc/inversion-of-control
Implemented Unit Test and Inversion of Control
"""
import abc
import unittest

class AbstractList():
   
    @abc.abstractmethod
    def __init__(self):
        pass
    
    @abc.abstractmethod
    def add(self):
        pass

    @abc.abstractmethod
    def remove(self):
        pass

    @abc.abstractmethod
    def top(self):
        pass
    
    @abc.abstractmethod
    def whole(self):
        pass

class List(AbstractList):
    
    def __init__(self):
        self.aList = []
        
    def add(self, item=None):
        self.aList.insert(0,item)
        
    def remove(self, item=None):
        if len(self.aList) > 0:
            self.aList.remove(item)
        else:
            raise Exception ('Remove {} from an empty list'.format(item))
        
    def top(self):
        if len(self.aList) > 0:        
            return(self.aList[0])
        else:
            return(None)
        
    def whole(self):
        return(self.aList)
        
class Dict:

    def __init__(self):
        self.aDict = {}        

# a simple factory implementation
class Factory():

    def __init__(self, type):
        self.type = type

    @staticmethod
    def __new__(self,type):
        try:
            MyObj = eval(type)()
        except NameError:
            print('Name Error Exception')
            return(None)
        
        if isinstance(MyObj, object):
            return MyObj
        else:
            raise Exception ('Unsupported Type')               
                  
class Stack():
    __alist = Factory('List')
    
    def push(self, item=None):
        self.__alist.add(item)

    def pop(self):
        item = self.__alist.top()
        if item != None:
            self.__alist.remove(item)
        return(item)

    def top(self):
        return(self.__alist.top())
        
    def whole(self):
        return(self.__alist)

    def size(self):
        return(len(self.__alist.whole()))      
              
class TestStackMethods(unittest.TestCase):
    def test_push(self):
        stack = Stack()
        OneM = 1000
        for i in range(OneM):
            stack.push(i)
        self.assertEqual(OneM,stack.size())
                    
    def test_pop(self):
        stack = Stack()
        for i in range(1000):
            stack.push(i)
            self.assertEqual(i,stack.pop())
        self.assertEqual(0,stack.size())
                               
    def test_top(self):
        stack = Stack()
        item = 8888
        stack.push(item)
        self.assertEqual(item,stack.top())
        
    def test_empty(self):
        stack = Stack()
        self.assertIsNone(stack.pop())

#%%

if __name__ == "__main__":
    unittest.main()