#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import namedtuple

# Ejemplo de clase tradicional (POJO)

class Car:
    def __init__(self):
        self.peso = 1000
        self.modelo = "GTR"
        self.marca = "Nissan"

c = Car()
print(c.modelo)


# Alternativa, tuplas nombradas
CarDos =namedtuple("CarDos", "one, two, three")
CarTres = namedtuple("CarDos", ["one","two","three"])
c= CarDos(one=1, two=2, three=3)
print(c.one)
print(c.three)