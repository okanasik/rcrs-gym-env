from data_stream import OutputStream, InputStream
import message_factory
import entity_factory
import property_factory

#import registry
import world_model
import struct

#reg = registry.Registry()


def write_int32(value, output_stream):
    output_stream.write(chr((value >> 24) & 0xFF))
    output_stream.write(chr((value >> 16) & 0xFF))
    output_stream.write(chr((value >> 8) & 0xFF))
    output_stream.write(chr(value & 0xFF))


def read_int32_from_byte_arr(byte_array):
    value = int((ord(byte_array[0]) << 24) + (ord(byte_array[1]) << 18) + (ord(byte_array[2]) << 8) + ord(byte_array[3]))
    return value


def read_int32(input_stream):
    byte_array = input_stream.read(4)
    return read_int32_from_byte_arr(byte_array)


def write_double(value, output_stream):
    packed = struct.pack('!d', value)
    output_stream.write(packed)


def read_double(input_stream):
    byte_array = input_stream.read(8)
    return struct.unpack('!d', byte_array)


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
    b = ord(input_stream.read(1))
    return b==1


def write_boolean(b, output_stream):
    if b:
        output_stream.write(chr(1))
    else:
        output_stream.write(chr(0))


def read_property(input_stream):
    # TODO: check this property reading method
    result = None
    urn = read_str(input_stream)
    if urn == "" or urn is None:
        return None
    defined = read_boolean(input_stream)
    if defined:
        size = read_int32(input_stream)
        content = read_bytes(size,input_stream)
        result = property_factory.create_property(urn, content)
        if not(result is None):
            result.read(content)
    return result
        

def write_property(p, output_stream):
    write_str(p.get_urn(), output_stream)
    write_boolean(p.is_defined(), output_stream)
    if p.is_defined():
        tmp_output = OutputStream()
        p.write(tmp_output)
        write_int32(len(tmp_output.getvalue()), output_stream)
        output_stream.write(tmp_output.getvalue())


def read_entity(input_stream):
    urn = read_str(input_stream)
    if urn == "" or urn is None:
        return None
    eid = read_int32(input_stream)
    entity_size = read_int32(input_stream)
    entity = entity_factory.create_entity(eid, urn)
    byte_array_data = input_stream.read(entity_size)
    entity_input_stream = InputStream(byte_array_data)
    entity.read(entity_input_stream)
    return entity


def write_entity(e, output_stream):
    tmp_output_stream = OutputStream()
    e.write(tmp_output_stream)
    write_str(e.get_urn(), output_stream)
    write_int32(e.get_id().get_value(), output_stream)
    write_int32(len(tmp_output_stream.getvalue()), output_stream)
    output_stream.write(tmp_output_stream.getvalue())


def read_float32(input_stream):
    byte_array = input_stream.read(4)
    return read_float32_from_byte_arr(byte_array)


def read_float32_from_byte_arr(byte_array):
    value = float((ord(byte_array[0]) << 24) + (ord(byte_array[1]) << 18) + (ord(byte_array[2]) << 8) + ord(byte_array[3]))
    return value


def write_float32(value,output_stream):
    output_stream.write(chr((value >> 24) & 0xFF))
    output_stream.write(chr((value >> 16) & 0xFF))
    output_stream.write(chr((value >> 8) & 0xFF))
    output_stream.write(chr(value & 0xFF))
    return