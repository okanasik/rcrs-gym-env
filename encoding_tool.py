from data_stream import OutputStream
import message_factory
import registry
from world_model import Entity,EntityID,Property

reg = registry.Registry()


def write_int32(value, output_stream):
    output_stream.write(chr((value >> 24) & 0xFF))
    output_stream.write(chr((value >> 16) & 0xFF))
    output_stream.write(chr((value >> 8) & 0xFF))
    output_stream.write(chr(value & 0xFF))


def read_int32(input_stream):
    byte_array = input_stream.read(4)
    return read_int32_from_byte_arr(byte_array)


def read_int32_from_byte_arr(byte_array):
    value = int((ord(byte_array[0]) << 24) + (ord(byte_array[1]) << 18) + (ord(byte_array[2]) << 8) + ord(byte_array[3]))
    return value


def write_str(value, output_stream):
    write_int32(len(value), output_stream)
    output_stream.write(value)


def read_str(input_stream):
    str_len = read_int32(input_stream)
    return input_stream.read(str_len)


def write_msg(msg, output_stream):
    tmp_output_stream = OutputStream()
    msg.write(tmp_output_stream)
    msg_data = tmp_output_stream.getvalue()

    write_str(msg.urn, output_stream)
    write_int32(len(msg_data), output_stream)
    output_stream.write(msg_data)


def read_msg(input_stream):
    urn = read_str(input_stream)
    if urn:
        data_size = read_int32(input_stream)
        if data_size > 0:
            msg_data = input_stream.read(data_size)
            msg = message_factory.create_msg(urn, msg_data)
            return msg

    return None

def read_bytes(size,input_stream):
    buff = []
    for i in range(size):
        buff.append(None)
    input_stream.read(buff) #ToDo check difference between "read" and "readfully"
    return buff
        

def read_boolean(input_stream):
    b = input_stream.read()
    return b==1
    
def write_boolean(b, output_stream):
    output_stream.write(b)

def read_property(input_stream):
    urn = read_str(input_stream)
    if urn == "" or urn is None:
        return None
    defined = read_boolean(input_stream)
    result = reg.getCurrentRegistry().createProperty(urn)
    if defined:
        size = read_int32(input_stream)
        content = read_bytes(size,input_stream)
        if not(result is None):
            result.read(content)
    return result
        
        
        
def write_property(p, output_stream):
    if p.instanceof(Property):
        write_str(p.getURN(), output_stream)
        write_boolean(p.isDefined(), output_stream)
        if p.isDefined():
            gather = [] #TO-DO CHECK THE BYTE ARRAY OUTPUTSTEAM
            p.write(gather)
            byts = gather.toByteArray()
            write_int32(len(byts), output_stream)
            output_stream.write(byts)
            
    return 
            
def read_entity(input_stream):
    urn = read_str(input_stream)
    if urn == "" or urn is None:
        return None
    eid = read_int32(input_stream)
    size = read_int32(input_stream)
    content = read_bytes(size,input_stream)
    result = reg.getCurrentRegistry().createEntity(urn,EntityID(eid))
    if not(result is None):
        result.read(content)
    return result
            
def write_entity(e,output_stream):
    if e.instanceof(Entity):
        gather = [] #TO-DO CHECK THEY BYTE ARRAY OUTPUT STREAM
        e.write(gather)
        byts = gather.toByteArray()
        write_str(e.getURN(),output_stream)
        write_int32(e.getID().getValue(),output_stream)
        write_int32(len(byts), output_stream)
        output_stream.write(byts)
        
        
    