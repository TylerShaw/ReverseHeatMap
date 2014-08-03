#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys,os,math
from PIL import Image

# open the image and determine size.
im = Image.open("heatmap.png")
x = 0
y = 0
size = im.size
x_max = size[0]
y_max = size[1]
print x_max
print y_max
list = []

while (x < x_max):
	while (y < y_max):
		list.append([x,y,im.getpixel((x,y))])
		y+=1
	x+=1
	y=1
os.remove('results.csv’)
appender = open('results.csv','ab')
appender.write("x,y,r,g,b,rgbtotal\r\n")
result = []
for each in list:
	x = str(each[0]).zfill(2)
	y = str((each[1]*-1)+99).zfill(2)
	rgb = str(each[2]).split(",")
	r = rgb[0].replace("(","")
	g = rgb[1].replace(" ","")
	b = rgb[2].replace(" ","").replace(")","")
	result.append([x,y,r,g,b])
result = sorted(result)

for each in result:
	total = str(int(each[1])+int(each[2])+int(each[3]))
	writeme = str(each[0]+','+each[1]+','+each[2]+','+each[3]+','+total+'\r\n')
	appender.write(writeme)