import socket
from my_data_encoding import int_to_byte_array

TCP_IP = '127.0.0.1'
TCP_PORT = 7000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))


# send connection message
# requestId
urn = 'urn:rescuecore2:messages.control:ak_connect'
request_id = 20
version = 1
agent_name = 'rescuecore2.components.AbstractComponent'
requested_entities = ['urn:rescuecore2.standard:entity:firebrigade']

my_data = ''
my_data += int_to_byte_array(request_id)
my_data += int_to_byte_array(version)
my_data += int_to_byte_array(len(agent_name))
my_data += agent_name.encode()
my_data += int_to_byte_array(len(requested_entities))
for req_entity in requested_entities:
    my_data += int_to_byte_array(len(req_entity))
    my_data += req_entity.encode()

all_size = 4 + len(urn) + 4 + len(my_data) + 4
all_data = int_to_byte_array(all_size) + int_to_byte_array(len(urn)) + urn.encode() + int_to_byte_array(len(my_data)) + my_data + int_to_byte_array(0)
s.send(all_data)

# receive data

buffsize = 4096
received_data = s.recv(buffsize)
print received_data

# version
# agentName
# requestedEntities
# urn
# byte length
# 0 to indicate the end of the message

# todo: do something
s.close()