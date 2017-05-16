#!/usr/bin/env python
# -*- coding: utf-8 -*-

l = (1,2,14, 99, 100)

# res = []
# for x in l:
#    res.append(x*x)

# Alternativa
map(list(map(lambda x: x*x, l)))

l=[
"/api/v1",
"/api/v1/index",
"/api/v1/home"
]

def auth(y):
    return "/api/v1" in y

if all(auth(x) for x in l):
    print("ok")

if any(auth(x) for x in l):
    print("ok")

if all(x > 50 for x in l):
    print("entra")
else:
    print("no entra")

sum(l)
max(l)