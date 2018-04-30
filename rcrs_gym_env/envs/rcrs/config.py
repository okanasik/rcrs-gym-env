#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
config.py
v1.0 - 2/April/2018
Kevin Rodriguez Siu

This module mimics the function of the following classes:
rescuecore2.config.*

"""


#TO-DO Complete class Config based on rescuecore2.config.Config;

class Config:
    
    data = None # dict string,string
    no_cache = None #set string
    int_data = None #dict string, integer
    float_data = None #dict string, float
    boolean_data = None #dict string,boolean
    array_data = None #dict string, [string]
    
    constraints = None #set ConfigConstraint
    violated_constraints = None #set ConfigConstraint
    
    seed_generator = None #seedgnerator
    random = None #random
    
    def __init__(self):
        self.data = {}
        self.no_cache = []
        self.int_data = {}
        self.float_data = {}
        self.boolean_data = {}
        self.array_data = {}
        pass
    
    def get_all_keys(self):
        return self.data.keys()
    
    def get_value(self,key):
        if key is None:
            return "Key cannot be None"
        elif self.data.get(key) is None:
            return "NoSuch Config Exception"
            #raise exception
        else:
            return self.data.get(key)
        #processDollarNotation(key,data.get(key))