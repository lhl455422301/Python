#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  cut_image.py
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

'''
将一张图片填充为正方形后切成9张图
'''

from PIL import Image
import sys

#将图片填充为正方形
def fill_image(image):
	width, height = image.size
	#选取长和宽中较大值作为新图片的长
	new_image_length = width if width > height else height
	#生成新图片
	new_image = Image.new(image.mode, (new_image_length, new_image_length), 
	    color='white')
	#将之前的图粘贴在新图中,居中
	if width > height:
		new_image.paste(image, (0,int((new_image_length - height)/2)))
	else:
		new_image.paste(image, (int((new_image_length - width)/2),0))
	return new_image

#切图
def cut_image(image):
	width, height = image.size
	item_width = int(width / 3)
	box_list = []
	for i in range(0,3):
		for j in range(0,3):
			box = (j*item_width, i*item_width, (j+1)*item_width, (i+1)*item_width)
			box_list.append(box)
	
	image_list = [image.crop(box) for box in box_list]
	
	return image_list

#保存
def save_image(image_list):
	index = 1
	for image in image_list:
		image.save('./result/longmao'+str(index)+'.png', 'PNG')
		index += 1

if __name__ == '__main__':
	file_path = 'longmao.jpg'
	image = Image.open(file_path)
	image = fill_image(image)
	image_list = cut_image(image)
	save_image(image_list)
