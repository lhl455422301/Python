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

#����һ����־��ָ�������Ƿ����
polling_active = True

while polling_active:
	#��ʾ���뱻�����ߵ����ֺͻش�
	name = input("\nWhat is your name?")
	response = input("Which mountain would you like to climb someday?")
	
	#�����洢���ֵ���
	responses[name] = response
	
	#�����Ƿ�����Ҫ�������
	repeat = input("Would you like to let another person respond?(yes/no)")
	if repeat == 'no':��	
		polling_active = False

#�����������ʾ���
print("\n--- Poll Results ---")
for name, response in responses.items():
	print(name + " would like to climb " + response + ".")	
