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
import message
from data_stream import InputStream

def create_msg(urn, byte_array):
    urns = message.all_msg_urns()
    if urn in urns:
        class_name = urns[urn]
        module_ = __import__('message')
        class_ = getattr(module_, class_name)
        msg_instance = class_()
        msg_instance.read(InputStream(byte_array))
        return msg_instance
    else:
        return None
