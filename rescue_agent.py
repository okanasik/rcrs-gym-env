from message import AKConnect
from message import KAConnectOK
from message import KAConnectError
from message import AKAcknowledge
from urn import *
from world_model import WorldModel

class RescueAgent:
    """The base class for handling the rescue"""

    request_id = 0

    def __init__(self):
        self.connection = None
        self.name = ''
        self.connect_request_id = None
        self.world_model = None
        self.config = None
        self.random = None
        self.entity_id = None
        pass

    def connect(self, _connection):
        self.connection = _connection
        self.connection.set_agent(self)
        connect_msg = AKConnect()
        connect_msg.set_message(RescueAgent.request_id, 1, self.name, self.get_requested_entities())
        self.connect_request_id = RescueAgent.request_id
        RescueAgent.request_id += 1
        self.connection.send_msg(connect_msg)

    def message_received(self, msg):
        if isinstance(msg, KAConnectOK):
            self.handle_connect_ok(msg)
        elif isinstance(msg, KAConnectError):
            self.handle_connect_error(msg)


    # that will be overriden by agents
    def get_requested_entities(self):
        return ''

    # that will be overriden by agents
    def post_connect(self, agent_id, entities, config):
        self.entity_id = agent_id
        self.world_model = WorldModel()
        self.world_model.add_entities(entities)
        #todo: check whether we need to merge agent config and the config coming from kernel
        self.config = config
        print('post_connect agent_id:' + str(agent_id.get_value()))

    def handle_connect_ok(self, msg):
        if msg.request_id_comp.get_value() == self.connect_request_id:
            self.post_connect(msg.agent_id_comp.get_value(), msg.world_comp.get_entities(), msg.config_comp.get_config())
            ack_msg = AKAcknowledge(self.connect_request_id, msg.agent_id_comp.get_value())
            self.connection.send_msg(ack_msg)

    def handle_connect_error(self, msg):
        if msg.request_id_comp.get_value() == self.connect_request_id:
            print('KAConnectionError:' + msg.get_reason())



class FireBrigadeAgent(RescueAgent):
    def __init__(self):
        self.name = 'rescue_agent.FireBrigadeAgent'

    def get_requested_entities(self):
        return [fire_brigade_urn]


class AmbulanceTeamAgent(RescueAgent):
    def __init__(self):
        self.name = 'rescue_agent.AmbulanceTeamAgent'

    def get_requested_entities(self):
        return [ambulance_team_urn]


class PoliceForceAgent(RescueAgent):
    def __init__(self):
        self.name = 'rescue_agent.PoliceForceAgent'

    def get_requested_entities(self):
        return [police_force_urn]
