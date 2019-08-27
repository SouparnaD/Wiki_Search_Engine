# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 19:13:05 2019

@author: Souparna
"""
from main import get_saved_object
index = get_saved_object("../index/index.pickle")
inc = index["title"]
print(inc)

