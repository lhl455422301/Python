#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  mountain_poll.py
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


responses = {}

#设置一个标志，指出调查是否继续
polling_active = True

while polling_active:
	#提示输入被调查者的名字和回答
	name = input("\nWhat is your name?")
	response = input("Which mountain would you like to climb someday?")
	
	#将答卷存储在字典中
	responses[name] = response
	
	#看看是否还有人要参与调查
	repeat = input("Would you like to let another person respond?(yes/no)")
	if repeat == 'no':·	
		polling_active = False

#调查结束，显示结果
print("\n--- Poll Results ---")
for name, response in responses.items():
	print(name + " would like to climb " + response + ".")	
