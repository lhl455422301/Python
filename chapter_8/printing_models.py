#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  printing_models.py
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


def print_models(unprinted_designs, completed_models):
	"""
	模拟打印每个设计，直到没有未打印的设计为止
	打印每个设计后，都将其移到列表completed_models中
	"""
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		
		#模拟根据设计制作3D打印模型的过程
		print("Printing model: " + current_design)
		completed_models.append(current_design)

def show_completed_models(completed_models):
	"""显示打印好的所有模型"""
	print("\nThe following models have been printed:")
	for completed_model in completed_models:
		print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_designs = []

print_models(unprinted_designs, completed_designs)
show_completed_models(completed_designs)
