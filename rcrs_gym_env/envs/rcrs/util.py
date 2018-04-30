import sys


def print_bytes(byte_array):
    for val in byte_array:
        sys.stdout.write(str(ord(val)) + ' ')
    sys.stdout.flush()