from urn import *
import encoding_tool as et
import world_model as wm

class Property:
    # Interface for the properties that make up an entity
    def __init__(self, urn_):
        self.urn = urn_
        self.defined = False
        self.value = None

    def get_urn(self):
        return self.urn

    def is_defined(self):
        return self.defined

    def set_defined(self, is_defined_):
        self.defined = is_defined_

    # this method is going to be overriden
    def take_value(self, other):
        self.value = other.value

    # this method is going to be overriden
    def get_value(self):
        self.value

    # this method is going to be overriden
    def write(self, out):
        # Write this property to a stream
        # @param out - The Stream to write to.
        # @throws IOException If the write fails.
        pass

    # this method is going to be overriden
    def read(self, inp):
        # Read this property from a stream.
        # @param inp - The Stream to read from.
        # @throws IOException if the read fails.
        pass

    # this method is going to be overriden
    def copy(self):
        # Create a copy of this property
        # @return A copy of this property
        pass




class EntityIDProperty(Property):
    def __init__(self, urn):
        Property.__init__(self, urn)

    def write(self, output_stream):
        et.write_int32(self.value.get_value(), output_stream)

    def read(self, input_stream):
        self.value = wm.EntityID(et.read_int32(input_stream))

    def __hash__(self):
        return self.value.get_value()


class EntityIDListProperty(Property):
    def __init__(self, urn):
        Property.__init__(self, urn)

    def write(self, output_stream):
        et.write_int32(len(self.value), output_stream)
        for id in self.value:
            et.write_int32(id.get_value(), output_stream)

    def read(self, input_stream):
        self.value = []
        count = et.read_int32(input_stream)
        for i in range(count):
            e_id = wm.EntityID(et.read_int32(input_stream))
            self.value.append(e_id)


# class DoubleProperty(Property):
#     def __init__(self, urn):
#         Property.__init__(self, urn)
#
#     def write(self, output_stream):
#         et.write_double(self.value, output_stream)
#
#     def read(self, input_stream):
#         self.value = et.read_double(input_stream)


class BooleanProperty(Property):
    def __init__(self, urn):
        Property.__init__(self, urn)

    def write(self, output_stream):
        if self.value:
            et.write_int32(1, output_stream)
        else:
            et.write_int32(0, output_stream)

    def read(self, input_stream):
        tmp_value = et.read_int32(input_stream)
        if tmp_value == 0:
            self.value = False
        elif tmp_value == 1:
            self.value = True


class IntProperty(Property):
    def __init__(self, urn):
        Property.__init__(self, urn)

    def write(self, output_stream):
        et.write_int32(self.value, output_stream)

    def read(self, input_stream):
        self.value = et.read_int32(input_stream)


class IntArrayProperty(Property):
    def __hash__(self, urn):
        Property.__init__(self, urn)

    def write(self, output_stream):
        et.write_int32(len(self.value), output_stream)
        for int_val in self.value:
            et.write_int32(int_val, output_stream)

    def read(self, input_stream):
        self.value = []
        count = et.read_int32(input_stream)
        for i in range(count):
            int_val = et.read_int32(input_stream)
            self.value.append(int_val)


class EdgeListProperty(Property):
    def __init__(self, urn):
        Property.__init__(self, urn)

    def write(self, output_stream):
        et.write_int32(len(self.value), output_stream)
        for edge in self.value:
            et.write_int32(edge.get_start_x(), output_stream)
            et.write_int32(edge.get_start_y(), output_stream)
            et.write_int32(edge.get_end_x(), output_stream)
            et.write_int32(edge.get_end_y(), output_stream)
            if edge.get_neighbor() is None:
                et.write_int32(0, output_stream)
            else:
                et.write_int32(edge.get_neighbor().get_value(), output_stream)

    def read(self, input_stream):
        count = et.read_int32(input_stream)
        self.value = []
        for i in range(count):
            start_x = et.read_int32(input_stream)
            start_y = et.read_int32(input_stream)
            end_x = et.read_int32(input_stream)
            end_y = et.read_int32(input_stream)
            n_id = et.read_int32(input_stream)
            neighbor = None
            if n_id != 0:
                neighbor = wm.EntityID(n_id)
            self.value.append(wm.Edge(start_x, start_y, end_x, end_y, neighbor))
