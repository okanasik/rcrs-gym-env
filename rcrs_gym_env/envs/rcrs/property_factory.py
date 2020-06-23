#    RoboCup RCF 2018 RoboCup Rescue Agent Simulation OpenAI Gym Integration
#    Copyright (C) 2018 Okan Asik, Kevin Christian Rodriguez Siu
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
import data_stream as ds
import property as p
from urn import *

int_property_types = {start_time_urn,
    longitude_urn,
    latitude_urn,
    wind_force_urn,
    wind_direction_urn,
    x_urn,
    y_urn,
    floors_urn,
    ignition_urn,
    fieryness_urn,
    brokenness_urn,
    building_code_urn,
    building_attributes_urn,
    ground_area_urn,
    total_area_urn,
    temperature_urn,
    importance_urn,
    repair_cost_urn,
    travel_distance_urn,
    direction_urn,
    stamina_urn,
    hp_urn,
    damage_urn,
    buriedness_urn,
    water_urn }
int_list_property_types = {apexes_urn, position_history_urn}
edgelist_property_types = {edges_urn}
entityid_property_types = {position_urn}
entityid_list_property_types = {blockades_urn}


def create_property(urn, byte_array):
    prop = None
    if urn in int_property_types:
        prop = p.IntProperty(urn)
        prop.read(ds.InputStream(byte_array))
    elif urn in int_list_property_types:
        prop = p.IntArrayProperty(urn)
        prop.read(ds.InputStream(byte_array))
    elif urn in entityid_property_types:
        prop = p.EntityIDProperty(urn)
        prop.read(ds.InputStream(byte_array))
    elif urn in entityid_list_property_types:
        prop = p.EntityIDListProperty(urn)
        prop.read(ds.InputStream(byte_array))
    elif urn in edgelist_property_types:
        prop = p.EdgeListProperty(urn)
        prop.read(ds.InputStream(byte_array))

    if prop is None:
        print 'prop:'+urn+' is None'

    return prop


