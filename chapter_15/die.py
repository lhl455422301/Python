#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  die.py
#  
#  Copyright 2018 Administrator <Administrator@SKY-20180411HYU>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


from random import randint

class Die():
	"""表示一个骰子的类"""
	
	def __init__(self, num_sides=6):
		"""骰子默认为6面"""
		self.num_sides = num_sides
	
	def roll(self):
		"""返回一个位于1和骰子面数之间的随机数"""
		return randint(1, self.num_sides)
