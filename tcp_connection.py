import socket
import threading
from encoding_tool import read_int32
from cStringIO import StringIO

class TCPConnection:
    """The TCP/IP implementation connection"""

    def __init__(self, address, port):
        self.socket = None
        self.agent = None

    def connect(self, address, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.settimeout(10) # 10 seconds to wait for connection
        try:
            self.socket.connect((address, port))
        except socket.error, exception:
            # return without creating tcp reading loop
            print(exception)
            return
        finally:
            self.socket.close()

        read_thread = threading.Thread(target=self.read_loop)
        read_thread.start()

    def set_agent(self, _agent):
        self.agent = _agent

    def bytes_received(self, byte_array):
        # convert byte_array to a message as defined by message.py
        msg = None
        self.agent.message_received(msg)
        pass

    def read_loop(self):
        buffer_size = 4096
        while True:
            try:
                # the first 4 byte is the length of message,
                data_array = self.socket.recv(buffer_size)
                if data_array:
                    # if it is not empty string
                    msg_size = read_int32(data_array[:4])
                    if msg_size == 0:
                        # marks the end of the message
                        continue
                    else:
                        self.recv_by_size(data_array[4:], msg_size, buffer_size)
                else:
                    raise IOError('tcp client is disconnected')
            except:
                self.socket.close()
                break

    def recv_by_size(self, data_array, msg_size, buffer_size):
        if msg_size <= buffer_size:
            self.bytes_received(data_array)
        else:
            data_size_so_far = len(data_array)
            while data_size_so_far < msg_size:
                new_data_array = self.socket.recv(buffer_size)
                if new_data_array:
                    data_size_so_far += len(new_data_array)
                    data_array += new_data_array
                else:
                    raise IOError('tcp client is disconnected')
            if data_size_so_far == msg_size:
                self.bytes_received(data_array)
            else:
                raise IOError('tcp client msg size error')

    def send_message(self, msg):
        pass

    def send_bytes(self, byte_array):
        self.socket.send(byte_array)

    def shutdown(self):
        self.socket.close()
