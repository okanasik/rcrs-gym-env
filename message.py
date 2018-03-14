from message_component import IntComp
from message_component import StringComp
from message_component import StringListComp


urns = {}


def all_msg_urns():
    if len(urns) == 0:
        urns[AKConnect.urn] = 'AKConnect'
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
