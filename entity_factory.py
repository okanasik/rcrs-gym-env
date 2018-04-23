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
    elif urn == wm.FireStation.urn:
        return wm.FireStation(entity_id)
    elif urn == wm.AmbulanceCentre.urn:
        return wm.AmbulanceCentre(entity_id)
    elif urn == wm.PoliceOffice.urn:
        return wm.PoliceOffice(entity_id)
    elif urn == wm.Civilian.urn:
        return wm.Civilian(entity_id)
    elif urn == wm.FireBrigade.urn:
        return wm.FireBrigade(entity_id)
    elif urn == wm.AmbulanceTeam.urn:
        return wm.AmbulanceTeam(entity_id)
    elif urn == wm.PoliceForce.urn:
        return wm.PoliceForce(entity_id)
    else:
        print('unknown entity urn:' + urn)
        return None
