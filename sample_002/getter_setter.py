#!/usr/bin/env python
# -*- coding: utf-8 -*-

class User:
    def __init__(self):
        self.name = ""
        self.email = ""
        self.pswd = ""

a = User()

# MAL
# a.name = "John Doe"
# a.email = "john.doe@domain.org"
# a.pswd = "FAKE :)"

# Mejor
new_info = {
    'name': "John Doe",
    'email': "john.doe@domain.org",
    'pswd': "FAKE :)"
}

for k, v in new_info.items():
    if k not in vars(a):
        continue
    setattr(a, k, v)
    a = getattr(a, k, None)

print(print("%r" % a))
