from encoding_tool import write_int32
from encoding_tool import read_int32
from encoding_tool import write_str
from encoding_tool import read_str
from encoding_tool import write_entity
from encoding_tool import read_entity
from encoding_tool import write_msg
from encoding_tool import read_msg
from encoding_tool import write_float32
from encoding_tool import read_float32
from encoding_tool import read_bytes


from change_set import ChangeSet
from world_model import Entity,EntityID
from command import Command
from config import Config


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
        
    def __str__(self):
        return str(self.name) + " = " + str(self.value)


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

    def __str__(self):
        return str(self.name) + " = " + str(self.value)

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

    def __str__(self):
        return str(self.name) + " = " + str(self.value_list)


class ChangeSetComp:
    changes = None
    def __init__(self,n_changes=None):
        if n_changes is None:
            self.changes = ChangeSet()
        else:
            self.changes = ChangeSet(n_changes)
            
    def get_change_set(self):
        return self.changes
    
    def set_change_set(self, newChanges):
        self.changes = ChangeSet(newChanges)
    
    def write(self, output_stream):
        self.changes.write(output_stream)
        
    def read(self, input_stream):
        self.changes = ChangeSet()
        self.changes.read(input_stream)
    
    def __str__(self):
        return str(self.name) + " = " + str(len(self.changes.get_changed_entities())) + " entities."
    
class EntityComp:
    entity = None
    
    def __init__(self,n_entity=None):
        if isinstance(n_entity,Entity):
            self.entity = n_entity
        else:
            self.entity = None
        
    def get_entity(self):
        return self.entity
    
    def set_entity(self, e):
        if isinstance(e,Entity):
            self.entity = e
            
    def write(self, output_string):
        write_entity(self.entity,output_string)
        
    def read(self, input_string):
        self.entity = read_entity(input_string)
        
    def __str__(self):
        return str(self.name) + " = " + str(self.entity)
    
class EntityIDComp:
    value = None
    
    def __init__(self, value=None):
        self.value = value
        
    def get_value(self):
        return self.value
    
    def set_value(self, eid):
        if isinstance(eid,EntityID):
            self.value=eid
        return
    
    def write(self, output_stream):
        write_int32(self.value.getValue(),output_stream)
        
    def read(self,input_stream):
        self.value = EntityID(read_int32(input_stream))
        
    def __str__(self):
        return str(self.name) + " = " + str(self.value)
    
class EntityIDListComp:
    ids = None
    
    def __init__(self,nids=None):
        if not (nids is None) and isinstance(nids,list):
            self.ids = nids
        else:
            self.ids = []
    
    def get_ids(self):
        return self.ids
    
    def set_ids(self,nids):
        if not (nids is None) and isinstance(nids,list):
            self.ids = nids
        return
    
    def write(self,output_stream):
        write_int32(len(self.ids), output_stream)
        for eid in self.ids:
            write_int32(eid.getValue(),output_stream)
        return
    
    def read(self,input_stream):
        self.ids.clear()
        count = read_int32(input_stream)
        for i in range(count):
            eid = EntityID(read_int32(input_stream))
            self.ids.append(eid)
        return
    
    def __str__(self):
        return str(self.name) + " = " + str(self.ids)
    
class EntityListComp:
    ents = None
    
    def __init__(self,nents=None):
        if not (nents is None) and isinstance(nents,list):
            self.ents = nents
        else:
            self.ents = []
    
    def get_entities(self):
        return self.ents
    
    def set_entities(self,nents):
        if not (nents is None) and isinstance(nents,list):
            self.ents = nents
        return
    
    def write(self,output_stream):
        write_int32(len(self.ents), output_stream)
        for ent in self.ents:
            write_entity(ent.getValue(),output_stream)
        return
    
    def read(self,input_stream):
        self.ents.clear()
        count = read_int32(input_stream)
        for i in range(count):
            e = Entity(read_entity(input_stream))
            self.ents.append(e)
        return
    
    def __str__(self):
        return str(self.name) + " = " + str(len(self.ents)) + " entities."
        
    
class IntListComp:
    ints = None
    
    def __init__(self,nints=None):
        if not (nints is None) and isinstance(nints,list):
            self.ints = nints
        else:
            self.ints = []
    
    def get_values(self):
        return self.ints
    
    def set_values(self,nints):
        if not (nints is None) and isinstance(nints,list):
            self.ints = nints
        return
    
    def write(self,output_stream):
        write_int32(len(self.ints), output_stream)
        for nt in self.ints:
            write_int32(nt,output_stream)
        return
    
    def read(self,input_stream):
        self.ints.clear()
        count = read_int32(input_stream)
        for i in range(count):
            e = read_int32(input_stream)
            self.ints.append(e)
        return
    
    def __str__(self):
        return str(self.name) + " = " + str(self.ints)

    
class CommandListComp:
    commands = None
    
    def __init__(self, lcommands=None):
        if not(lcommands is None) and isinstance(lcommands,list):
            self.commands = lcommands
        else:
            self.commands = []
            
    def get_commands(self):
        return self.commands
    
    def set_commands(self,lcommands):
        if not(lcommands is None) and isinstance(lcommands,list):
            self.commands = lcommands
        return
    
    def write(self, output_stream):
        write_int32(len(self.commands), output_stream)
        for command in self.commands:
            write_msg(command,output_stream)
        return

    def read(self,input_stream):
        self.commands.clear()
        count = read_int32(input_stream)
        for i in range(count):
            m = read_msg(input_stream)
            if isinstance(m,Command):
                self.commands.append(m)
            else:
                print "Command list stream contained a non-command message:", m, "(", type(m),")"
        return
    
    def __str__(self):
        return str(len(self.commands)) + " commands."
        
class FloatListComp:
    data = None
    def __init__(self, floats=None):
        if not(floats is None) and isinstance(floats,list):
            self.data = floats
        else:
            self.data = []
            
    def get_values(self):
        return self.data
    
    def set_values(self,floats):
        if not(floats is None) and isinstance(floats,list):
            self.data = floats
        return
    
    def write(self,output_stream):
        write_int32(len(self.data), output_stream)
        for f in self.data:
            write_float32(f,output_stream)
        return
    
    def read(self,input_stream):
        self.data.clear()
        count = read_int32(input_stream)
        for i in range(count):
            f = read_float32(input_stream)
            self.data.append(f)
        return
        
    def __str__(self):
        return str(self.name) + " = " + str(self.data)
    
        
class RawDataComp:
    byte_data = None
    
    def __init__(self, bdata=None):
        if not(bdata is None) and isinstance(bdata,list):
            self.byte_data = bdata
        else:
            self.byte_data = []
            
    def get_data(self):
        return self.byte_data
    
    def set_data(self,bdata):
        if not(bdata is None) and isinstance(bdata,list):
            self.byte_data = bdata
        return
    
    def write(self,output_stream):
        write_int32(len(self.byte_data), output_stream)
        for b in self.byte_data:
            output_stream.write(self.b) #CHECK WRITING OF BYTES
        return
    
    def read(self,input_stream):
        self.byte_data = read_bytes(read_int32(input_stream),input_stream) #CHECK READING OF BYTES
        return

    def __str__(self):
        return (self.name) + " = " + str(len(self.byte_data)) + " bytes of raw data."
    

class ConfigComp:
    config = None
    
    def __init__(self,nconfig=None):
        if not(nconfig is None) and isinstance(nconfig,Config):
            self.config = nconfig
        else:
            self.config = Config()
            
    def get_config(self):
        return self.config
    
    def set_config(self,nconfig):
        if not(nconfig is None) and isinstance(nconfig,Config):
            self.config = nconfig
        return
    
    def write(self,output_stream):
        keys = self.config.get_all_keys()
        write_int32(len(keys),output_stream)
        for k in keys:
            write_str(k,output_stream)
            write_str(self.config.get_value(k), output_stream)
        return
    
    def read(self,input_stream):
        count = read_int32(input_stream)
        self.config = Config()
        for i in range(count):
            key = read_str(input_stream)
            value = read_str(input_stream)
            self.config.set_value(key,value)
        return
    
    def __str__(self):
        return str(self.name) + " (" + str(len(self.config.get_all_keys())) + " entries)" 
    
    
        
    
        
        
        

    

    

        
        