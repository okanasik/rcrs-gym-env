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
command.py
v1.0 - 9/April/2018
Kevin Rodriguez Siu

This module mimics the function of the following classes:
rescuecore2.messages.Command

"""

from message import Message
from world_model import EntityID

class Command(Message):
     
    def __init__(self, nid = 0, ntime = 0):
        self.agent_id = EntityID(nid)
        self.time = ntime
    
    def get_agent_id(self):
        return self.agent_id
    
    def get_time(self):
        return self.time