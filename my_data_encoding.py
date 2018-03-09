def int_to_byte_array(value):
    byte_array = bytearray([(value >> 24) & 0xFF, (value >> 16) & 0xFF, (value >> 8) & 0xFF, value & 0xFF])
    return byte_array
    
def byte_array_to_int(byte_array):
    value = (ord(byte_array[0]) << 24) + (ord(byte_array[1]) << 18) + (ord(byte_array[2]) << 8) + ord(byte_array[3])
    return value