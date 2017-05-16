#!/usr/bin/env python
# -*- coding: utf-8 -*-

l = (1,2,14, 99, 100)

# res = []
# for x in l:
#    res.append(x*x)

# Alternativa
map(list(map(lambda x: x*x, l)))