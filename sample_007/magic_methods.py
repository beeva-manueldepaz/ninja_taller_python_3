#!/usr/bin/env python
# -*- coding: utf-8 -*-

class A:

    # Nos permite reducir código en memoria con cosas que no utilizamos -> ojo frameworks
    __slots__ = ["saludo"]

    def __init__(self, saludo):
        self.saludo = saludo

    def __str__(self):
        return "Clase A"

    def __repr__(self):
        return "<A - [saludo=%s] >" % self.saludo

a = A(saludo="Ola")
print("%r" %a)
print(a.saludo)
print(A.__dict__)