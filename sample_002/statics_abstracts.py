#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Creamos interfaces abstractos realmente con esta lib
import abc

# Hacemos que a través de una metaclase de Python se ejecute previamente esta comprobación
class MyInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def suma(selfs):
        pass

    def rest(self):
        pass

# c = MyInterface()
# c.suma()

class MyOne(MyInterface):
    def suma(self,a,b):
        return a+b

m = MyOne()
print(m.suma(1,2))