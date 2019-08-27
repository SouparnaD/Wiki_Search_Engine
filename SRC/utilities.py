# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 19:36:55 2019

@author: USER
"""
import pickle


def save_object(doc_list, file_name):
    file = open(file_name, "wb")
    pickle.dump(doc_list, file)
    file.close()
def get_saved_object(file_name):
    pickle_in = open(file_name, "rb")
    return pickle.load(pickle_in)