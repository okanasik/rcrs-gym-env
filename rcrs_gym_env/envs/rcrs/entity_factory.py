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
import world_model as wm


def create_entity(entity_id, urn):
    if urn == wm.Building.urn:
        return wm.Building(entity_id)
    elif urn == wm.Road.urn:
        return wm.Road(entity_id)
    elif urn == wm.World.urn:
        return wm.World(entity_id)
    elif urn == wm.Blockade.urn:
        return wm.Blockade(entity_id)
    elif urn == wm.Refuge.urn:
        return wm.Refuge(entity_id)
    elif urn == wm.Hydrant.urn:
        return wm.Hydrant(entity_id)
    elif urn == wm.GasStation.urn:
        return wm.GasStation(entity_id)
    elif urn == wm.FireStationEntity.urn:
        return wm.FireStationEntity(entity_id)
    elif urn == wm.AmbulanceCentreEntity.urn:
        return wm.AmbulanceCentreEntity(entity_id)
    elif urn == wm.PoliceOfficeEntity.urn:
        return wm.PoliceOfficeEntity(entity_id)
    elif urn == wm.Civilian.urn:
        return wm.Civilian(entity_id)
    elif urn == wm.FireBrigadeEntity.urn:
        return wm.FireBrigadeEntity(entity_id)
    elif urn == wm.AmbulanceTeamEntity.urn:
        return wm.AmbulanceTeamEntity(entity_id)
    elif urn == wm.PoliceForceEntity.urn:
        return wm.PoliceForceEntity(entity_id)
    else:
        print('unknown entity urn:' + urn)
        return None
