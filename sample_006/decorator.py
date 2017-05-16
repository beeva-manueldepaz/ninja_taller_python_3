#!/usr/bin/env python
# -*- coding: utf-8 -*-

def my_decorator2(f):

    # *args = cualquier número de argumentos sin nombrar
    # **kargs = cualquier número de argumentos con nombre
    def _my_decorator(*args, **kwargs):
        print("hello")
        resultado = f(*args, **kwargs)
        print("world")
        return resultado

    return _my_decorator

def my_decorator(f):

    # *args = cualquier número de argumentos sin nombrar
    # **kargs = cualquier número de argumentos con nombre
    def _my_decorator(*args, **kwargs):

        print("hola")
        resultado = f(*args, **kwargs)
        print("mundo")

        return resultado

    return _my_decorator

# @my_decorator2 -> son anidados y se ejecutan de arriba hacia abajo
@my_decorator2
@my_decorator
def hola():
    print("soy function hola")

print(hola())