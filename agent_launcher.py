import sys
import argparse
from rescue_agent import FireBrigade
from rescue_agent import PoliceForce
from rescue_agent import AmbulanceTeam
from tcp_connection import TCPConnection

class AgentLauncher:
    """The base class to launch agents using tcp/ip communication"""

    def __init__(self, _port, _hostname, _numfb, _numpf, _numat):
        self.port = _port
        self.hostname = _hostname
        self.numfb = _numfb
        self.numpf = _numpf
        self.numat = _numat
        self.connect_agents()

    def connect_agents(self):
        try:
            while self.numfb != 0:
                self.connect(FireBrigade())
                self.numfb -= 1
        except IOError:
            pass

        try:
            while self.numpf != 0:
                self.connect(PoliceForce())
                self.numpf -= 1
        except IOError:
            pass

        try:
            while self.numat != 0:
                self.connect(AmbulanceTeam())
                self.numat -= 1
        except IOError:
            pass


    def connect(self, agent):
        connection = TCPConnection()
        connection.connect(self.hostname, self.port)
        agent.connect(connection)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('-p', '--port', action='store')
    parser.add_argument('-h', '--hostname', action='store')
    parser.add_argument('-fb', '--firebrigade', action='store')
    parser.add_argument('-pf', '--policeforce', action='store')
    parser.add_argument('-at', '--ambulanceteam', action='store')

    args = parser.parse_args()
    print(args.port)
    print(args.hostname)
    print(args.firebrigade)
    print(args.policeforce)
    print(args.ambulanceteam)


