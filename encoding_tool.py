def write_int32(value, output_stream):
    output_stream.write((value >> 24) & 0xFF)
    output_stream.write((value >> 16) & 0xFF)
    output_stream.write((value >> 8) & 0xFF)
    output_stream.write(value & 0xFF)


def read_int32(byte_array):
    value = int((ord(byte_array[0]) << 24) + (ord(byte_array[1]) << 18) + (ord(byte_array[2]) << 8) + ord(byte_array[3]))
    return value
