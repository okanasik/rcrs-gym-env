from message_component import IntComp
from message_component import StringComp
from message_component import StringListComp

from message_component import EntityIDComp
from message_component import EntityListComp
from message_component import ConfigComp

urns = {}


def all_msg_urns():
    if len(urns) == 0:
        urns[AKConnect.urn] = 'AKConnect'
        urns[KAConnectOK.urn] = 'KAConnectOK'
        return urns
    else:
        return urns


class Message:
    def __init__(self):
        self.components = []

    def add_component(self, comp):
        self.components.append(comp)

    def write(self, output_stream):
        for comp in self.components:
            comp.write(output_stream)

    def read(self, input_stream):
        for comp in self.components:
            comp.read(input_stream)


class AKConnect(Message):
    urn = 'urn:rescuecore2:messages.control:ak_connect'

    def __init__(self):
        Message.__init__(self)
        self.request_id_comp = IntComp()
        self.version_comp = IntComp()
        self.agent_name_comp = StringComp()
        self.requested_entities_comp = StringListComp()

        self.add_component(self.request_id_comp)
        self.add_component(self.version_comp)
        self.add_component(self.agent_name_comp)
        self.add_component(self.requested_entities_comp)

    def set_message(self, request_id, version, agent_name, requested_entity_types):
        self.request_id_comp.set_value(request_id)
        self.version_comp.set_value(version)
        self.agent_name_comp.set_value(agent_name)
        self.requested_entities_comp.set_value(requested_entity_types)


class KAConnectOK(Message):
    urn = 'urn:rescuecore2:messages.control:ka_connect_ok'

    def __init__(self):
        Message.__init__(self)
        self.request_id_comp = IntComp()
        self.agent_id_comp = EntityIDComp()
        self.world_comp = EntityListComp()
        self.config_comp = ConfigComp()

        self.add_component(self.request_id_comp)
        self.add_component(self.agent_id_comp)
        self.add_component(self.world_comp)
        self.add_component(self.config_comp)

    def set_message(self, request_id, agent_id, entities, config):
        self.request_id_comp.set_value(request_id)
        self.agent_id_comp.set_value(agent_id)
        self.world_comp.set_entities(entities)
        self.config_comp.set_config(config)


class KAConnectError(Message):
    urn = 'urn:rescuecore2:messages.control:ka_connect_error'

    def __init__(self):
        Message.__init__(self)
        self.request_id_comp = IntComp()
        self.reason_comp = StringComp()

        self.add_component(self.request_id_comp)
        self.add_component(self.reason_comp)

    def set_message(self, request_id, reason):
        self.request_id_comp.set_value(request_id)
        self.reason_comp.set_value(reason)


class AKAcknowledge(Message):
    urn = 'urn:rescuecore2:messages.control:ak_acknowledge'

    def __init__(self, request_id, agent_id):
        Message.__init__(self)
        self.request_id_comp = IntComp()
        self.agent_id_comp = EntityIDComp()

        self.add_component(self.request_id_comp)
        self.add_component(self.agent_id_comp)

        self.set_message(request_id, agent_id)

    def set_message(self, request_id, agent_id):
        self.request_id_comp.set_value(request_id)
        self.agent_id_comp.set_value(agent_id)
