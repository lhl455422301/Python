#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  test_name_function.py
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


import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
	"""测试name_function.py"""
	
	def test_first_last_name(self):
		"""能够正确地处理像Janis Joplin这样的姓名吗？"""
		formatted_name = get_formatted_name('janis', 'joplin')
		self.assertEqual(formatted_name, 'Janis Joplin')
		
	def test_first_last_middle_name(self):
		"""能够正确地处理像Wolfgang Amadeus Mozart这样的名字吗？"""
		formatted_name = get_formatted_name(
		    'wolfgang', 'mozart', 'amadeous')
		self.assertEqual(formatted_name, 'Wolfgang Amadeous Mozart')

unittest.main()
