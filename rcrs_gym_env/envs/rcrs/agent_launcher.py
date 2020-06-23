#    RoboCup RCF 2018 RoboCup Rescue Agent Simulation OpenAI Gym Integration
#    Copyright (C) 2018 Okan Asik, Kevin Christian Rodriguez Siu
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
import argparse
from rescue_agent import FireBrigadeAgent
from rescue_agent import PoliceForceAgent
from rescue_agent import AmbulanceTeamAgent
from tcp_connection import TCPConnection
import sys
import time
import world_model as wm


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
                self.connect(FireBrigadeAgent())
                self.numfb -= 1
        except IOError:
            pass

        try:
            while self.numpf != 0:
                self.connect(PoliceForceAgent())
                self.numpf -= 1
        except IOError:
            pass

        try:
            while self.numat != 0:
                self.connect(AmbulanceTeamAgent())
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
    parser.add_argument('-fb', '--firebrigade', action='store', default=-1)
    parser.add_argument('-pf', '--policeforce', action='store', default=-1)
    parser.add_argument('-at', '--ambulanceteam', action='store', default=-1)

    args = parser.parse_args()
    launcher = AgentLauncher(int(args.port), args.hostname, int(args.firebrigade), int(args.policeforce), int(args.ambulanceteam))

    while True:
        try:
            time.sleep(100)
        except KeyboardInterrupt:
            #todo: make sure that message reading threads will clean up before exit
            sys.exit(1)



