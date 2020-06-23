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
import gym
from gym import error, spaces, utils
from gym.utils import seeding

class RCRSEnv(gym.Env):
	metadata={'render.modes': ['human']}
	
	def __init__(self):
		pass
	
	def step(self,action):
		"""
		Parameters
		----------
		action :

		Returns
		-------
		ob, reward, episode_over, info: tuple
		ob(object): an environment-specific object represeting the observation of the environment. 
		reward(float): amount of reward achieved by the previous action. The goal is always to increase the total reward. 
		episode_over(bool): whether it's time to reset the environment again. Most (but not all) tasks are divided up into well-defined episodes, and this being True indicates that the episode has terminated. 
		info(dict): diagnostic information useful for debugging. It can sometimes be useful for learning (for example, it might contain the raw probabilities behind the environment's last state change). However, official evaluations of the agent are not allowed to use this for learning. 
		"""
		self._take_action(action)
		self.status = self.env.step()
		reward = self._get_reward()
		ob = self.env.getState()
		episode_over = self.status != hfo_py.IN_GAME
		return ob, reward, episode_over, {}

	def _reset(self):
		pass

	def _render(self,mode='human',close=False):
		pass

	def _take_action(self,action):
		pass

	def _get_rewards(self):
		"""Reward is given for XY."""
		if self.status == FOOBAR:
			return 1
		elif self.status == ABC:
			return self.somestate ** 2
		else:
			return 0
		


