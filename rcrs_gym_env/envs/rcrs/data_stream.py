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
from collections import deque


class InputStream:
    def __init__(self, data_string):
        self.byte_queue = None
        self.set_data_string(data_string)

    def set_data_string(self, data_string):
        self.byte_queue = deque(list(data_string))

    def read(self, count=-1):
        if count == -1:
            return ''.join(self.byte_queue)
        else:
            if len(self.byte_queue) <= count:
                return ''.join(self.byte_queue)
            else:
                data_list = []
                for i in range(count):
                    data_list.append(self.byte_queue.popleft())
                return ''.join(data_list)
        return ''


class OutputStream:
    def __init__(self):
        self.byte_array = []

    def write(self, data_string):
        self.byte_array.extend(list(data_string))

    def getvalue(self):
        return ''.join(self.byte_array)
