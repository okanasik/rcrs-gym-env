import encoding_tool as et
from world_model import *


class Property:
    # Interface for the properties that make up an entity
    def __init__(self, _urn):
        self.urn = _urn
        self.value = None

    def get_urn(self):
        return self.urn

    def is_defined(self):
        # Does this property have a defined value?
        # @return True if a value has been set for this property, False otherwise
        pass

    def undefine(self):
        # Undefine the value of this property. Future calls to isDefined() will return false.
        pass

    def take_value(self, other):
        self.value = other.value

    def write(self, out):
        # Write this property to a stream
        # @param out - The Stream to write to.
        # @throws IOException If the write fails.
        pass

    def read(self, inp):
        # Read this property from a stream.
        # @param inp - The Stream to read from.
        # @throws IOException if the read fails.
        pass

    def get_value(self):
        # Get the value of this property. If the property is undefined, then the return value should be None.
        # @return The Value of this property
        pass

    def copy(self):
        # Create a copy of this property
        # @return A copy of this property
        pass


class EntityIDProp(Property):
    def __init__(self, urn):
        Property.__init__(self, urn)

    def write(self, output_stream):
        et.write_int32(self.value.get_value(), output_stream)

    def read(self, input_stream):
        self.value = EntityID(et.read_int32(input_stream))

    def __hash__(self):
        return self.value.get_value()


class EntityIDListProp(Property):
    def __init__(self, urn):
        Property.__init__(self, urn)
        self.value = []

    def write(self, output_stream):
        et.write_int32(len(self.value), output_stream)
        for id in self.value:
            et.write_int32(id.get_value(), output_stream)

    def read(self, input_stream):
        count = et.read_int32(input_stream)
        for i in range(count):
            e_id = EntityID(et.read_int32(input_stream))
            self.value.append(e_id)


class DoubleProp(Property):
    def __init__(self, urn):
        Property.__init__(self, urn)

    def write(self, output_stream):
        et.write_double(self.value, output_stream)

    def read(self, input_stream):
        self.value = et.read_double(input_stream)


class BooleanProp(Property):
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


class IntProp(Property):
    def __init__(self, urn):
        Property.__init__(self, urn)

    def write(self, output_stream):
        et.write_int32(self.value, output_stream)

    def read(self, input_stream):
        self.value = et.read_int32(input_stream)


class IntArrayProp(Property):
    def __hash__(self, urn):
        Property.__init__(self, urn)


class EdgeListProp(Property):
    def __init__(self, urn):
        Property.__init__(self, urn)

    def write(self, output_stream):
        et.write_int32(len(self.value), output_stream)
        for edge in self.value:
            et.write_int32(edge.get_start_x(), output_stream)
            et.write_int32(edge.get_start_y(), output_stream)
            et.write_int32(edge.get_end_x(), output_stream)
            et.write_int32(edge.get_end_y(), output_stream)
            if edge.is_passable():
                et.write_int32(edge.get_neighbor().get_value(), output_stream)
            else:
                et.write_int32(0, output_stream)

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
                neighbor = EntityID(n_id)
            self.value.append(Edge(start_x, start_y, end_x, end_y, neighbor))
