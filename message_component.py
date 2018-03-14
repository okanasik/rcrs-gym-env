from encoding_tool import write_int32
from encoding_tool import read_int32
from encoding_tool import write_str
from encoding_tool import read_str


class IntComp:
    def __init__(self):
        self.value = None

    def set_value(self, _value):
        self.value = _value

    def get_value(self):
        return self.value

    def write(self, output_stream):
        write_int32(self.value, output_stream)

    def read(self, input_stream):
        self.value = read_int32(input_stream)


class StringComp:
    def __init__(self):
        self.value = None

    def set_value(self, _value):
        self.value = _value

    def get_value(self):
        return self.value

    def write(self, output_stream):
        write_str(self.value, output_stream)

    def read(self, input_stream):
        self.value = read_str(input_stream)


class StringListComp:
    def __init__(self):
        self.value_list = None

    def set_value(self, _value_list):
        self.value_list = _value_list

    def get_value(self):
        return self.value_list

    def write(self, output_stream):
        write_int32(len(self.value_list), output_stream)
        for value in self.value_list:
            write_str(value, output_stream)

    def read(self, input_stream):
        self.value_list.clear()
        list_len = read_int32(input_stream)
        for i in range(list_len):
            self.value_list.append(read_str(input_stream))
