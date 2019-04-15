# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 20:33:58 2019

@author: ttc
Compare the implementation of inherited versus delegated class
"""

class List:
#    aList = []
    
    def __init__(self):
        self.aList = []
        
    def add(self, item=None):
        self.aList.insert(0,item)
        
    def remove(self, item=None):
        self.aList.remove(item)
        
    def top(self):
        return(self.aList[0])
        
    def whole(self):
        return(self.aList)
        
class StackInh(List):
    
    def __init__(self):
        super().__init__()
        
    def push(self, item=None):
        super().add(item)

    def pop(self):
        item = super().top()
        super().remove(item)
        return(item)

    def top(self):
        return(super().top())
        
class StackInc():
    __alist = List()
    
    def push(self, item=None):
        self.__alist.add(item)

    def pop(self):
        item = self.__alist.top()
        self.__alist.remove(item)
        return(item)

    def top(self):
        return(self.__alist.top())
        
    def whole(self):
        return(self.__alist)        
              
def main():

#Original list Class
#%%    
    alist = List()
    alist.add(1)
    alist.add(2)
    alist.add(3)
    print(dir(alist))
    print(alist.whole())

#Inherited Class
#%%    
    stackinh = StackInh()
    stackinh.push(7)
    stackinh.push(8)
    stackinh.push(9)    

    print(stackinh.top())
    stackinh.pop()
    print(dir(stackinh))    
    print(stackinh.whole())

#Delegated Class
#%%
    stackinc = StackInc()
    stackinc.push(4)
    stackinc.push(5)
    stackinc.push(6)
    stackinc.pop()
    print(dir(stackinc))
    print(stackinc.whole())

if __name__ == "__main__":
    main()