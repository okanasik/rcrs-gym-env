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

from urn import *
from property import IntProp
from property import IntArrayProp
from property import EntityIDProp
from property import EdgeListProp
from property import EntityIDListProp

import encoding_tool as et


class WorldModel():
    def __init__(self):
        self.entities = {}

    def add_entities(self, _entities):
        for entity in _entities:
            self.entities[entity.get_id()] = entity


class EntityID:
    def __init__(self, n_id):
        self.e_id = n_id
        
    def equals(self, o):
        if isinstance(o,EntityID):
            return self.e_id == o.e_id
        return False

    def __hash__(self):
        return self.e_id
    
    def get_value(self):
        return self.e_id
    
    def to_string(self):
        return str(self.e_id)


class Property:
    #Interface for the properties that make up an entity
    
    def get_urn(self):
        #Get the URN of this property. 
        #return The urn of this property    
        pass
    
    def is_defined(self):
        #Does this property have a defined value? 
        #@return True if a value has been set for this property, False otherwise
        pass
    
    def undefine(self):
        #Undefine the value of this property. Future calls to isDefined() will return false.
        pass
    
    def take_value (self,other):
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
    
    def get_value(self):
        #Get the value of this property. If the property is undefined, then the return value should be None.
        #@return The Value of this property
        pass
    
    def copy(self):
        #Create a copy of this property
        #@return A copy of this property
        pass
        

class Edge():

    def __init__(self, start_x, start_y, end_x, end_y, _neighbor):
        self.start = [start_x, start_y]
        self.end = [end_x, end_y]
        self.line = [[start_x, start_y], [end_x, end_y]]
        self.neighbor = _neighbor

    def get_start_x(self):
        return self.start[0]

    def get_start_y(self):
        return self.start[1]

    def get_end_x(self):
        return self.end[0]

    def get_end_y(self):
        return self.end[1]

    def get_neighbor(self):
        return self.neighbor


class Entity:
    def __init__(self, _entity_id, _urn):
        self.entity_id = _entity_id
        self.properties = {}
        self.urn = _urn
    
    def add_entity_listener(self,l):
        pass
    
    def remove_entity_listener(self,l):
        pass
    
    def get_id(self):
        return self.entity_id
    
    def get_properties(self):
        return self.properties
    
    def get_property(self, urn):
        return self.properties[urn]

    def get_location(self, world_model):
        # returns the position of the entity on the world model
        pass

    def register_properties(self, props):
        for p in props:
            self.properties[p.get_urn()] = p

    def write(self, out):
        count = 0
        for p in self.properties:
            if p.is_defined():
                count += 1
        et.write_int32(count, out)
        for p in self.properties:
            if p.is_defined():
                et.write_property(p, out)
    
    def read(self, inp):
        count = et.read_int32(inp)
        for i in range(count):
            p = et.read_property(inp)
            if p is not None:
                existing = self.get_property(p.get_urn())
                existing.take_value(p)
    
    def copy(self):
        pass

    def get_urn(self):
        return self.urn



class World(Entity):
    urn = entity_prefix + 'world'

    def __init__(self, entity_id):
        Entity.__init__(self, entity_id, World.urn)
        self.start_time = IntProp(start_time_urn)
        self.longitude = IntProp(longitude_urn)
        self.latitude = IntProp(latitude_urn)
        self.wind_force = IntProp(wind_force_urn)
        self.wind_direction = IntProp(wind_direction_urn)
        self.register_properties([self.start_time, self.longitude, self.latitude, self.wind_force, self.wind_direction])


class Area(Entity):
    def __init__(self, entity_id, urn):
        Entity.__init__(self, entity_id, urn)
        self.x = IntProp(x_urn)
        self.y = IntProp(y_urn)
        self.edges = EdgeListProp(edges_urn)
        self.blockades = EntityIDListProp(blockades_urn)
        self.register_properties([self.x, self.y, self.edges, self.blockades])


class Building(Area):
    urn = entity_prefix + 'building'

    def __init__(self, entity_id, urn=None):
        if urn is None:
            urn = Building.urn
        Area.__init__(self, entity_id, urn)
        self.floors = IntProp(floors_urn)
        self.ignition = IntProp(ignition_urn)
        self.fieryness = IntProp(fieryness_urn)
        self.brokenness = IntProp(brokenness_urn)
        self.building_code = IntProp(building_code_urn)
        self.attributes = IntProp(attributes_urn)
        self.ground_area = IntProp(ground_area_urn)
        self.total_area = IntProp(area_total_urn)
        self.temperature = IntProp(temperature_urn)
        self.importance = IntProp(importance_urn)
        self.register_properties([self.floors, self.ignition, self.fieryness, self.brokenness, self.building_code])
        self.register_properties([self.attributes, self.ground_area, self.total_area, self.temperature, self.importance])


class Road(Area):
    urn = entity_prefix + 'road'

    def __init__(self, entity_id):
        Area.__init__(self, entity_id, Road.urn)


class Blockade(Entity):
    urn = entity_prefix + 'blockade'

    def __init__(self, entity_id):
        Entity.__init__(self, entity_id, Blockade.urn)
        self.x = IntProp(x_urn)
        self.y = IntProp(y_urn)
        self.position = EntityIDProp(position_urn)
        self.apexes = IntArrayProp(apexes_urn)
        self.repair_cost = IntProp(repair_cost_urn)
        self.register_properties([self.x, self.y, self.position, self.apexes, self.repair_cost])


class Refuge(Building):
    urn = entity_prefix + 'refuge'

    def __init__(self, entity_id):
        Building.__init__(self, entity_id, Refuge.urn)


class Hydrant(Road):
    urn = entity_prefix + 'hydrant'

    def __init__(self, entity_id):
        Road.__init__(self, entity_id, Hydrant.urn)


class GasStation(Building):
    urn = entity_prefix + 'gasstation'

    def __init__(self, entity_id):
        Building.__init__(self, entity_id, GasStation.urn)


class FireStation(Building):
    urn = entity_prefix + 'firestation'

    def __init__(self, entity_id):
        Building.__init__(self, entity_id, FireStation.urn)


class AmbulanceCentre(Building):
    urn = entity_prefix + 'ambulancecentre'

    def __init__(self, entity_id):
        Building.__init__(self, entity_id, AmbulanceCentre.urn)


class PoliceOffice(Building):
    urn = entity_prefix + 'policeoffice'

    def __init__(self, entity_id):
        Building.__init__(self, entity_id, PoliceOffice.urn)


class Human(Entity):
    def __init__(self, entity_id, urn):
        Entity.__init__(self, entity_id, urn)
        self.x = IntProp(x_urn)
        self.y = IntProp(y_urn)
        self.travel_distance = IntProp(travel_distance_urn)
        self.position = EntityIDProp(position_urn)
        self.position_history = IntArrayProp(position_history_urn)
        self.direction = IntProp(direction_urn)
        self.stamina = IntProp(stamina_urn)
        self.hp = IntProp(hp_urn)
        self.damage = IntProp(damage_urn)
        self.buriedness = IntProp(buriedness_urn)
        self.register_properties([self.x, self.y, self.travel_distance, self.position, self.position_history])
        self.register_properties([self.direction, self.stamina, self.hp, self.damage, self.buriedness])


class Civilian(Human):
    urn = entity_prefix + 'civilian'

    def __init__(self, entity_id):
        Human.__init__(self, entity_id, Civilian.urn)


class FireBrigade(Human):
    urn = entity_prefix + 'firebrigade'

    def __init__(self, entity_id):
        Human.__init__(self, entity_id, FireBrigade.urn)
        self.water = IntProp(water_urn)
        self.register_properties([self.water])


class AmbulanceTeam(Human):
    urn = entity_prefix + 'ambulanceteam'

    def __init__(self, entity_id):
        Human.__init__(self, entity_id, AmbulanceTeam.urn)



class PoliceForce(Human):
    urn = entity_prefix + 'policeforce'

    def __init__(self, entity_id):
        Human.__init__(self, entity_id, PoliceForce.urn)