#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  survey.py
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


class AnonymousSurvey():
	"""收集匿名调查问卷的答案"""
	
	def __init__(self, question):
		"""存储一个问题，并为存储答案做准备"""
		self.question = question
		self.responses = []
		
	def show_question(self):
		"""显示调查问卷"""
		print(self.question)
	
	def store_response(self, new_response):
		"""存储单份调查答卷"""
		self.responses.append(new_response)
	
	def show_results(self):
		"""显示收集到的所有答卷"""
		print("Survey results:")
		for response in self.responses:
			print('- ' + response)
