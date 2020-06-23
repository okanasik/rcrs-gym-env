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
entity_prefix = 'urn:rescuecore2.standard:entity:'
property_prefix = 'urn:rescuecore2.standard:property:'
message_prefix = 'urn:rescuecore2.standard:message:'

# entity urn definitions
fire_brigade_urn = entity_prefix + 'firebrigade'
police_force_urn = entity_prefix + 'policeforce'
ambulance_team_urn = entity_prefix + 'ambulanceteam'
world_urn = entity_prefix + 'world'
building_urn = entity_prefix + 'building'
road_urn = entity_prefix + 'road'
blockade_urn = entity_prefix + 'blockade'
refuge_urn = entity_prefix + 'refuge'
hydrant_urn = entity_prefix + 'hydrant'
gas_station_urn = entity_prefix + 'gasstation'
fire_station_urn = entity_prefix + 'firestation'
ambulance_centre_urn = entity_prefix + 'ambulancecentre'
police_office_urn = entity_prefix + 'policeOffice'
civilian_urn = entity_prefix + 'civilian'

x_urn = property_prefix + 'x'
y_urn = property_prefix + 'y'

edges_urn = property_prefix + 'edges'
blockades_urn = property_prefix + 'blockades'

start_time_urn = property_prefix + 'starttime'
longitude_urn = property_prefix + 'longitude'
latitude_urn = property_prefix + 'latitude'
wind_force_urn = property_prefix + 'windforce'
wind_direction_urn = property_prefix + 'winddirection'

floors_urn = property_prefix + 'floors'
ignition_urn = property_prefix + 'ignition'
fieryness_urn = property_prefix + 'fieryness'
brokenness_urn = property_prefix + 'brokenness'
building_code_urn = property_prefix + 'buildingcode'
building_attributes_urn = property_prefix + 'buildingattributes'
ground_area_urn = property_prefix + 'buildingareaground'
total_area_urn = property_prefix + 'buildingareatotal'
temperature_urn = property_prefix + 'temperature'
importance_urn = property_prefix + 'importance'
position_urn = property_prefix + 'position'
apexes_urn = property_prefix + 'apexes'
repair_cost_urn = property_prefix + 'repaircost'
travel_distance_urn = property_prefix + 'traveldistance'
water_urn = property_prefix + 'waterquantity'
position_history_urn = property_prefix + 'positionhistory'
direction_urn = property_prefix + 'direction'
stamina_urn = property_prefix + 'stamina'
hp_urn = property_prefix + 'hp'
damage_urn = property_prefix + 'damage'
buriedness_urn = property_prefix + 'buriedness'

