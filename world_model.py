#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
world_model.py
v1.0 - 19/March/2018
Kevin Rodriguez Siu

This module mimics the function of the following classes:
rescuecore2.worldmodel.Entity
rescuecore2.worldmodel.EntityID
rescuecore2.worldmodel.Property

"""

class EntityID:
    e_id = None
    
    def __init__(self, n_id):
        self.e_id = int(n_id)
        
    def equals(self, o):
        if isinstance(o,EntityID):
            return self.e_id == o.e_id
        return False
    
    def hashCode(self):
        return self.e_id
    
    def getValue(self):
        return self.e_id
    
    def toString(self):
        return str(self.e_id)
    
    


class Property:
    #Interface for the properties that make up an entity
    
    def getURN(self):
        #Get the URN of this property. 
        #return The urn of this property    
        pass
    
    def isDefined(self):
        #Does this property have a defined value? 
        #@return True if a value has been set for this property, False otherwise
        pass
    
    def undefine(self):
        #Undefine the value of this property. Future calls to isDefined() will return false.
        pass
    
    def takeValue (self,other):
        #Take on the value of another property
        #@param other - The other property to inspect
        #@throws IllegalArgumentException if the other property is the wrong type.
        pass
    
    def write(self, out):
        #Write this property to a stream
        #@param out - The Stream to write to.
        #@throws IOException If the write fails. 
        pass
    
    def read(self, inp):
        #Read this property from a stream.
        #@param inp - The Stream to read from.
        #@throws IOException if the read fails.
        pass
    
    def getValue(self):
        #Get the value of this property. If the property is undefined, then the return value should be None.
        #@return The Value of this property
        pass
    
    def copy(self):
        #Create a copy of this property
        #@return A copy of this property
        pass
        


class Entity:
    
    def addEntityListener(self,l):
        pass
    
    def removeEntityListener(self,l):
        pass
    
    def getID(self):
        pass

    def getURN(self):
        pass
    
    def getProperties(self):
        pass
    
    def getProperty(self, urn):
        pass
    
    def write(self, out):
        pass
    
    def read(self, inp):
        pass
    
    def copy(self):
        pass