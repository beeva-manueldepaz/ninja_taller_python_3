#!/usr/bin/env python
# -*- coding: utf-8 -*-

class A:
    def __init__(self):
        self.hola = "mundo"
        self._protected = "no deberias verlo"
        self.__private = "ni saberlo"

# A través del debugger los vemos :(
# Es realmente una convención

a = A()
print(a)