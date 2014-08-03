import Image,sys,os,math
#open
im = Image.open("grid.png")
#setup
x = 3
y = 3
xx = 0
yy = 0
x_max = 700
y_max = 700
list = []

while (x < x_max):
	while (y < y_max):
		list.append([xx,yy,im.getpixel((x,y))])
		y+=7
		yy+=1
	x+=7
	xx+=1
	y=3
	yy=0
os.remove('grid.csv')
os.remove('results.csv')
appender = open('grid.csv','ab')
appender2 = open('results.csv','ab')
appender.write('pin,r,g,b,total\r\n')
appender2.write('pin,frequency\r\n')
result = []
for each in list:
	x = str(each[0]).zfill(2)
	y = str((each[1]*-1)+99).zfill(2)
	rgb = str(each[2]).split(",")
	r = rgb[0].replace("(","")
	g = rgb[1].replace(" ","")
	b = rgb[2].replace(" ","").replace(")","")
	xy = str(x+y)
	result.append([xy,r,g,b])
result = sorted(result)

for each in result:
	total = str(int(each[1])+int(each[2])+int(each[3]))
	writeme = str(each[0]+','+each[1]+','+each[2]+','+each[3]+','+total+'\r\n')
	writeme2 = str(each[0]+','+total+'\r\n')
	appender.write(writeme)
	appender2.write(writeme2)