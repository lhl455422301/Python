#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  confirmed_users.py
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


#���ȣ�����һ������֤�û��б�
#��һ�����ڴ洢����֤�û��Ŀ��б�
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

#��֤ÿ���û���ֱ��û��δ��֤�û�Ϊֹ
#��ÿ��������֤���б��Ƶ�����֤�û��б���
while unconfirmed_users:
	current_user = unconfirmed_users.pop()
	
	print("Verifying user: " + current_user.title())
	confirmed_users.append(current_user)

#��ʾ��������֤���û�
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
	print(confirmed_user.title())
