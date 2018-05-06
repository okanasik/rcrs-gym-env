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
import entity_factory as ef
from rtree import index
import sys


class WorldModel():
    def __init__(self):
        self.entities = {}
        self.indexed = False
        self.index = index.Index()
        self.human_rectangles = {}
        self.minx = None
        self.miny = None
        self.maxx = None
        self.maxy = None


    def add_entities(self, _entities):
        for entity in _entities:
            self.entities[entity.get_id()] = entity

    def get_entity(self, entity_id):
        if self.entities.has_key(entity_id):
            return self.entities.get(entity_id)
        else:
            return None

    def add_entity(self, entity):
        self.entities[entity.get_id()] = entity

    def remove_entity(self, entity_id):
        del self.entities[entity_id]

    def merge(self, change_set):
        for entity_id in change_set.get_changed_entities():
            existing_entity = self.get_entity(entity_id)
            added = False
            if existing_entity is None:
                existing_entity = ef.create_entity(entity_id, change_set.get_entity_urn(entity_id))
                if existing_entity is None:
                    print('world model merge existing entity is still None')
                    continue
                added = True

            for property in change_set.get_changed_properties(entity_id):
                existing_property = existing_entity.get_property(property.get_urn())
                existing_property.take_value(property)

            if added:
                self.add_entity(existing_entity)

        for entity_id in change_set.get_deleted_entities():
            self.remove_entity(entity_id)

        #update human rectangles
        new_human_rectangles_to_push = {}
        for human, rectangle in self.human_rectangles.iteritems():
            self.index.delete(human.get_id().get_value(), rectangle)
            left, bottom, right, top = self.make_rectangle(human)
            if left is not None:
                self.index.insert(human.get_id().get_value(), (left, bottom, right, top))
                new_human_rectangles_to_push[human] = (left, bottom, right, top)

        for human, rectangle in new_human_rectangles_to_push:
            self.human_rectangles[human] = rectangle

    def index(self):
        if not self.indexed:
            self.minx = sys.maxint
            self.miny = sys.maxint
            self.maxx = sys.minint
            self.maxy = sys.minint

            self.index = index.Index()
            self.human_rectangles.clear()

            for entity in self.entities.values():
                left, bottom, right, top = self.make_rectangle(entity)
                if left is not None:
                    self.index.insert(entity.get_id().get_value(), (left, bottom, right, top))
                    self.minx = min(self.minx, left, right)
                    self.maxx = max(self.maxx, left, right)
                    self.miny = min(self.miny, bottom, top)
                    self.maxy = max(self.maxy, bottom, top)
                    if isinstance(entity, Human):
                        self.human_rectangles[entity] = (left, bottom, right, top)
            self.indexed = True

    def make_rectangle(self, entity):
        x1 = sys.maxint
        x2 = sys.minint
        y1 = sys.maxint
        y2 = sys.minint
        apexes = None
        if isinstance(entity, Area):
            apexes = entity.get_apexes()
        elif isinstance(entity, Blockade):
            apexes = entity.get_apexes()
        elif isinstance(entity, Human):
            apexes = []
            human_x, human_y = entity.get_location(self)
            apexes.append(human_x)
            apexes.append(human_y)
        else:
            return None, None, None, None

        if len(apexes) == 0:
            print('this area, blockade or human entity does not have apexes!!')
            return None
        for i in range(0, len(apexes), 2):
            x1 = min(x1, apexes[i])
            x2 = max(x2, apexes[i])
            y1 = min(y1, apexes[i+1])
            y2 = max(y2, apexes[i+1])
        return x1, y1, x2, y2















class EntityID:
    def __init__(self, _id):
        self.id = _id
        
    def __eq__(self, other):
        if isinstance(other, EntityID):
            return self.id == other.id
        return False

    def __hash__(self):
        return self.id
    
    def get_value(self):
        return self.id
    
    def to_string(self):
        return str(self.id)
        

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

    def __hash__(self):
        return self.entity_id.get_value()


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
        self.apexes = None

    def get_edges(self):
        return self.edges.get_value()

    def get_apexes(self):
        if self.apexes is None:
            self.apexes = []
            for edge in self.get_edges():
                self.apexes.append(edge.get_start_x())
                self.apexes.append(edge.get_start_y())

        return self.apexes

    def get_location(self, world_model):
        if self.x.is_defined() and self.y.is_defined():
            return self.x.get_value(), self.y.get_value()
        else:
            return None, None


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

    def get_apexes(self):
        return self.apexes.get_value()

    def get_location(self, world_model):
        if self.x.is_defined() and self.y.is_defined():
            return self.x.get_value(), self.y.get_value()
        else:
            return None, None



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

    def get_position(self):
        return self.position.get_value()

    def get_location(self, world_model):
        if self.x.is_defined() and self.y.is_defined():
            return self.x.get_value(), self.y.get_value()
        if self.position.is_defined():
            pos_entity = world_model.get_entity(self.get_position())
            return pos_entity.get_location(world_model)
        return None, None


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