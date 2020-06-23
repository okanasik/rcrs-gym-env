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
    def __init__(self):
        self.data = {}
        # self.no_cache = {}
        # self.int_data = {}
        # self.float_data = {}
        # self.boolean_data = {}
        # self.array_data = {}

    def get_keys(self):
        return self.data.keys()

    def set_value(self, key, value):
        self.data[key] = value

    def get_value(self, key, default_value = None):
        if key not in self.data:
            return default_value
        else:
            return self.data.get(key)

