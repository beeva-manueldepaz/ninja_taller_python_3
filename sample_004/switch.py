#!/usr/bin/env python
# -*- coding: utf-8 -*-

# swap manual
a = 1
b = 2
print ("a=%d b=%d" % (a, b))

c = a
a = b
b = c

print ("Tras el swap")
print ("a=%d b=%d" % (a, b))

# Alternativa de python :)
a, b = b, a

print ("Tras el swap automágico")
print ("a=%d b=%d" % (a, b))