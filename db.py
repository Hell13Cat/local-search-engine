#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pickle, os

def load(name):
    file = open(os.getcwd() + "/db/" + name + ".pk", "rb")
    res = pickle.load(file)
    file.close()
    return res

def save(name, setting):
    file = open(os.getcwd() + "/db/" + name + ".pk", "wb")
    pickle.dump(setting, file)
    file.close()