from message import AKConnect
from urn import *

class RescueAgent:
    """The base class for handling the rescue"""

    request_id = 0

    def __init__(self):
        self.connection = None
        self.name = ''
        pass

    def connect(self, _connection):
        self.connection = _connection
        self.connection.set_agent(self)
        connect_msg = AKConnect()
        connect_msg.set_message(RescueAgent.request_id, 1, self.name, self.get_requested_entities())
        RescueAgent.request_id += 1
        self.connection.send_msg(connect_msg)

    def message_received(self, msg):
        print 'agent msg received' + str(msg)

    def get_requested_entities(self):
        return ''


class FireBrigade(RescueAgent):
    def __init__(self):
        self.name = 'rescue_agent.FireBrigade'

    def get_requested_entities(self):
        return [fire_brigade_urn]


class AmbulanceTeam(RescueAgent):
    def __init__(self):
        self.name = 'rescue_agent.AmbulanceTeam'

    def get_requested_entities(self):
        return [ambulance_team_urn]


class PoliceForce(RescueAgent):
    def __init__(self):
        self.name = 'rescue_agent.PoliceForce'

    def get_requested_entities(self):
        return [police_force_urn]
