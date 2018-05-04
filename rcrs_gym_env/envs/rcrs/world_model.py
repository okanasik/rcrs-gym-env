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
from property import IntProperty
from property import IntArrayProperty
from property import EntityIDProperty
from property import EdgeListProperty
from property import EntityIDListProperty

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
    def __init__(self, _entity_id):
        self.entity_id = _entity_id
        self.properties = {}
    
    def add_entity_listener(self,l):
        pass
    
    def remove_entity_listener(self,l):
        pass
    
    def get_id(self):
        return self.entity_id
    
    def get_properties(self):
        return self.properties
    
    def get_property(self, prop_urn):
        return self.properties[prop_urn]

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
    urn = world_urn

    def __init__(self, entity_id):
        Entity.__init__(self, entity_id)
        self.start_time = IntProperty(start_time_urn)
        self.longitude = IntProperty(longitude_urn)
        self.latitude = IntProperty(latitude_urn)
        self.wind_force = IntProperty(wind_force_urn)
        self.wind_direction = IntProperty(wind_direction_urn)
        self.register_properties([self.start_time, self.longitude, self.latitude, self.wind_force, self.wind_direction])


class Area(Entity):
    def __init__(self, entity_id):
        Entity.__init__(self, entity_id)
        self.x = IntProperty(x_urn)
        self.y = IntProperty(y_urn)
        self.edges = EdgeListProperty(edges_urn)
        self.blockades = EntityIDListProperty(blockades_urn)
        self.register_properties([self.x, self.y, self.edges, self.blockades])


class Building(Area):
    urn = building_urn

    def __init__(self, entity_id):
        Area.__init__(self, entity_id)
        self.floors = IntProperty(floors_urn)
        self.ignition = IntProperty(ignition_urn)
        self.fieryness = IntProperty(fieryness_urn)
        self.brokenness = IntProperty(brokenness_urn)
        self.building_code = IntProperty(building_code_urn)
        self.attributes = IntProperty(building_attributes_urn)
        self.ground_area = IntProperty(ground_area_urn)
        self.total_area = IntProperty(total_area_urn)
        self.temperature = IntProperty(temperature_urn)
        self.importance = IntProperty(importance_urn)
        self.register_properties([self.floors, self.ignition, self.fieryness, self.brokenness, self.building_code])
        self.register_properties([self.attributes, self.ground_area, self.total_area, self.temperature, self.importance])


class Road(Area):
    urn = road_urn

    def __init__(self, entity_id):
        Area.__init__(self, entity_id)


class Blockade(Entity):
    urn = blockade_urn

    def __init__(self, entity_id):
        Entity.__init__(self, entity_id)
        self.x = IntProperty(x_urn)
        self.y = IntProperty(y_urn)
        self.position = EntityIDProperty(position_urn)
        self.apexes = IntArrayProperty(apexes_urn)
        self.repair_cost = IntProperty(repair_cost_urn)
        self.register_properties([self.x, self.y, self.position, self.apexes, self.repair_cost])


class Refuge(Building):
    urn = refuge_urn

    def __init__(self, entity_id):
        Building.__init__(self, entity_id)


class Hydrant(Road):
    urn = hydrant_urn

    def __init__(self, entity_id):
        Road.__init__(self, entity_id)


class GasStation(Building):
    urn = gas_station_urn

    def __init__(self, entity_id):
        Building.__init__(self, entity_id)


class FireStationEntity(Building):
    urn = fire_station_urn

    def __init__(self, entity_id):
        Building.__init__(self, entity_id)


class AmbulanceCentreEntity(Building):
    urn = ambulance_centre_urn

    def __init__(self, entity_id):
        Building.__init__(self, entity_id)


class PoliceOfficeEntity(Building):
    urn = police_office_urn

    def __init__(self, entity_id):
        Building.__init__(self, entity_id)


class Human(Entity):
    def __init__(self, entity_id):
        Entity.__init__(self, entity_id)
        self.x = IntProperty(x_urn)
        self.y = IntProperty(y_urn)
        self.travel_distance = IntProperty(travel_distance_urn)
        self.position = EntityIDProperty(position_urn)
        self.position_history = IntArrayProperty(position_history_urn)
        self.direction = IntProperty(direction_urn)
        self.stamina = IntProperty(stamina_urn)
        self.hp = IntProperty(hp_urn)
        self.damage = IntProperty(damage_urn)
        self.buriedness = IntProperty(buriedness_urn)
        self.register_properties([self.x, self.y, self.travel_distance, self.position, self.position_history])
        self.register_properties([self.direction, self.stamina, self.hp, self.damage, self.buriedness])


class Civilian(Human):
    urn = civilian_urn

    def __init__(self, entity_id):
        Human.__init__(self, entity_id)


class FireBrigadeEntity(Human):
    urn = fire_brigade_urn

    def __init__(self, entity_id):
        Human.__init__(self, entity_id)
        self.water = IntProperty(water_urn)
        self.register_properties([self.water])


class AmbulanceTeamEntity(Human):
    urn = ambulance_team_urn

    def __init__(self, entity_id):
        Human.__init__(self, entity_id)


class PoliceForceEntity(Human):
    urn = police_force_urn

    def __init__(self, entity_id):
        Human.__init__(self, entity_id)