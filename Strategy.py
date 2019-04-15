# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 15:56:03 2019

@modified from: 
    https://sourcemaking.com/design_patterns/strategy/python/1
"""

"""
Define a family of algorithms, encapsulate each one, and make them
interchangeable. Strategy lets the algorithm vary independently from
clients that use it.
"""

import abc
#from abc import ABC, abstractmethod

class Context:
    """
    Define the interface of interest to clients.
    Maintain a reference to a Strategy object.
    """

    def __init__(self, strategy):
        self._strategy = strategy

    def context_interface(self):
        self._strategy.algorithm_interface()

#Alternatively, 
#class Strategy(metaclass=abc.ABCMeta):        
class Strategy(abc.ABC):

    """
    Declare an interface common to all supported algorithms. Context
    uses this interface to call the algorithm defined by a
    ConcreteStrategy.
    """

    @abc.abstractmethod
    def algorithm_interface(self):
        pass


class ConcreteStrategyA(Strategy):
    """
    Implement the algorithm using the Strategy interface.
    """

    def algorithm_interface(self):
        print('ConcreteStrategyA')


class ConcreteStrategyB(Strategy):
    """
    Implement the algorithm using the Strategy interface.
    """

    def algorithm_interface(self):
        print('ConcreteStrategyB')


def main():
    for i in range(5):
        if (i%2) == 0:
            concrete_strategy= ConcreteStrategyA()
        else:
            concrete_strategy = ConcreteStrategyB()
            
        context = Context(concrete_strategy)
        mycontext = context
        mycontext.context_interface()


if __name__ == "__main__":
    main()