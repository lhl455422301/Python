#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  hn_submissions.py
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


import requests

from operator import itemgetter

#执行API调用并存储响应
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print("Status code:", r.status_code)

#处理有关每篇文章的信息
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
	#对于每篇文章，都执行一个API调用
	url = ('https://hacker-news.firebaseio.com/v0/item' + 
	    str(submission_id) + '.json')
	submission_r = requests.get(url)
	print(submission_r.status_code)
	response_dict = submission_r.json()
	
	submission_dict = {
	    'title': response_dict['title'],
	    'link': 'http://news.ycombinator.com/item?id=' + str(submission_id),
	    'comments': response_dict.get('descendants', 0)
	    }
	submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
	    reverse=True)
	
for submission_dict in submission_dicts:
	print("\nTitle:", submission_dict['title'])
	print("Discussion link:", submission_dict['link'])
	print("Comments:", submission_dict['comments'])
