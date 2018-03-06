
#coding : utf-8

from Tkinter import *
from turtle import *
import time

class buiding:
	"""My buiding"""
	floors = [0,0,0,0,0,0]
	

class lift:
	"""6 floors"""
	now_lift = 1
	up_or_down_or_static = 0

color = "red"

Build = buiding()
Lift = lift()

root = Tk()

def drawCircle(self, x, y, r, **kwargs):
	return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)

def sleeptime(hour, minite, second):
	return 3600*hour + minite*60 + second

work = []

root.title('Lift')



buiding = Canvas(root, width = 120, height = 600)
buiding.grid(rowspan = 44, column = 0)
buiding.create_rectangle(30,10,100,470, outline = "red", dash = 10)


ball1 = drawCircle(buiding, 66, 425, 20, fill = color)
#ball2 = drawCircle(buiding, 66, 349, 20, fill = "white")
#ball3 = drawCircle(buiding, 66, 273, 20, fill = "white")
#ball4 = drawCircle(buiding, 66, 197, 20, fill = "white")
#ball5 = drawCircle(buiding, 66, 121, 20, fill = "white")
#ball6 = drawCircle(buiding, 66, 45, 20, fill = "white")


def Down6():
	Build.floors[5] = -1
	if Lift.up_or_down_or_static == 0 and Lift.now_lift < 6:
		Up()



def Up5():
	Build.floors[4] = 1
	if Lift.up_or_down_or_static == 0 and Lift.now_lift > 5:
		Down()
	elif Lift.up_or_down_or_static == 0 and Lift.now_lift < 5:
		Up()


def Down5():
	Build.floors[4] = -1
	if Lift.up_or_down_or_static == 0 and Lift.now_lift > 5:
		Down()
	elif Lift.up_or_down_or_static == 0 and Lift.now_lift < 5:
		Up()


def Up4():
	Build.floors[3] = 1
	if Lift.up_or_down_or_static == 0 and Lift.now_lift > 4:
		Down()
	elif Lift.up_or_down_or_static == 0 and Lift.now_lift < 4:
		Up()


def Down4():
	Build.floors[3] = -1
	if Lift.up_or_down_or_static == 0 and Lift.now_lift > 4:
		Down()
	elif Lift.up_or_down_or_static == 0 and Lift.now_lift < 4:
		Up()


def Up3():
	Build.floors[2] = 1
	if Lift.up_or_down_or_static == 0 and Lift.now_lift > 3:
		Down()
	elif Lift.up_or_down_or_static ==0 and Lift.now_lift < 3:
		Up()

def Down3():
	Build.floors[2] = -1
	if Lift.up_or_down_or_static == 0 and Lift.now_lift > 3:
		Down()
	elif Lift.up_or_down_or_static ==0 and Lift.now_lift < 3:
		Up()


def Up2():
	Build.floors[1] = 1
	if Lift.up_or_down_or_static == 0 and Lift.now_lift > 2:
		Down()
	elif Lift.up_or_down_or_static ==0 and Lift.now_lift < 2:
		Up()

def Down2():
	Build.floors[1] = -1
	if Lift.up_or_down_or_static == 0 and Lift.now_lift >2:
		Down()
	elif Lift.up_or_down_or_static ==0 and Lift.now_lift < 2:
		Up()

def Up1():
	Build.floors[0] = 1
	if Lift.up_or_down_or_static == 0 and Lift.now_lift != 1:
		Down()

def Floor6():
	Build.floors[5] = 2
	if Lift.up_or_down_or_static == 0:
		Up()

def Floor5():
	Build.floors[4] = 2
	if Lift.up_or_down_or_static == 0 and Lift.now_lift > 5:
		Down()
	elif Lift.up_or_down_or_static == 0 and Lift.now_lift < 5:
		Up()

def Floor4():
	Build.floors[3] = 2
	if Lift.up_or_down_or_static == 0 and Lift.now_lift > 4:
		Down()
	elif Lift.up_or_down_or_static == 0 and Lift.now_lift < 4:
		Up()

def Floor3():
	Build.floors[2] = 2
	if Lift.up_or_down_or_static == 0 and Lift.now_lift > 3:
		Down()
	elif Lift.up_or_down_or_static == 0 and Lift.now_lift < 3:
		Up()

def Floor2():
	Build.floors[1] = 2
	if Lift.up_or_down_or_static == 0 and Lift.now_lift > 2:
		Down()
	elif Lift.up_or_down_or_static == 0 and Lift.now_lift < 2:
		Up()
def Floor1():
	Build.floors[0] = 2
	if Lift.up_or_down_or_static == 0 and Lift.now_lift > 1:
		Down()

def Up():
	keep = 0
	for i in range(Lift.now_lift,6):
		if Build.floors[i] != 0:
			Lift.up_or_down_or_static = 1
			keep = 1
	while (keep):
		for i in range(0,2):
			buiding.move(2,0, -38)
			root.update()
			time.sleep(1.5)
		Lift.now_lift += 1
		keep = 0
		if Build.floors[Lift.now_lift - 1] > 0:
			time.sleep(5)
			Build.floors[Lift.now_lift - 1] = 0
			root.update()
		for i in range(Lift.now_lift,6):
			if Build.floors[i] != 0:
				keep = 1
	if keep == 0:
		if Build.floors[Lift.now_lift - 1] == -1:
			time.sleep(5)
			Build.floors[Lift.now_lift - 1] = 0
			root.update()
		for i in range (0,Lift.now_lift):
			if Build.floors[i] != 0:
				Down()
	
	Lift.up_or_down_or_static = 0
def Down():
	keep = 0
	for i in range(0,Lift.now_lift-1):
		if Build.floors[i] != 0:
			Lift.up_or_down_or_static = -1
			keep = 1
	while (keep):
		for i in range(0,2):
			buiding.move(2,0, 38)
			root.update()
			time.sleep(1.5)
		Lift.now_lift -= 1
		keep = 0
		if Build.floors[Lift.now_lift - 1] == -1 or Build.floors[Lift.now_lift - 1] == 2:
			time.sleep(5)
			Build.floors[Lift.now_lift - 1] = 0
			root.update()
		for i in range(0,Lift.now_lift-1):
			if Build.floors[i] != 0:
				keep = 1
	if keep == 0:
		if Build.floors[Lift.now_lift - 1] == 1:
			time.sleep(5)
			Build.floors[Lift.now_lift - 1] = 0
			root.update()
		for i in range (Lift.now_lift,6):
			if Build.floors[i] != 0:
				Up()
	
	Lift.up_or_down_or_static = 0

up6 = Button(root, text='!')
up6.grid(row = 0, column = 1, sticky = S)
down6 = Button(root, text = 'down', command = Down6)
down6.grid(row = 1, column = 1, sticky = W)

up5 = Button(root, text='up', command = Up5)
up5.grid(row = 3, column = 1, sticky = S)
down5 = Button(root, text = 'down', command = Down5)
down5.grid(row = 4, column = 1, sticky = W)

up4 = Button(root, text='up', command = Up4)
up4.grid(row = 6, column = 1, sticky = S)
down4 = Button(root, text = 'down', command = Down4)
down4.grid(row = 7, column = 1, sticky = W)

up3 = Button(root, text='up', command = Up3)
up3.grid(row = 9, column = 1, sticky = S)
down3 = Button(root, text = 'down', command = Down3)
down3.grid(row = 10, column = 1, sticky = W)

up2 = Button(root, text='up', command = Up2)
up2.grid(row = 12, column = 1, sticky = S)
down2 = Button(root, text = 'down', command = Down2)
down2.grid(row = 13, column = 1, sticky = W)

up1 = Button(root, text='up', command = Up1)
up1.grid(row = 15, column = 1, sticky = S)
down1 = Button(root, text = '!')
down1.grid(row = 16, column = 1, sticky = S)

floor6 = Button(root, text = '6', command = Floor6)
floor6.grid(row = 1, column = 3, sticky = S)

floor5 = Button(root, text = '5', command = Floor5)
floor5.grid(row = 4, column = 3, sticky = S)

floor4 = Button(root, text = '4', command = Floor4)
floor4.grid(row = 7, column = 3, sticky = S)

floor3 = Button(root, text = '3', command = Floor3)
floor3.grid(row = 10, column = 3, sticky = S)

floor2 = Button(root, text = '2', command = Floor2)
floor2.grid(row = 13, column = 3, sticky = S)

floor1 = Button(root, text = '1', command = Floor1)
floor1.grid(row = 16, column = 3, sticky = S)

#up_or_down.pack()

#buiding.pack()



#ok.pack()

root.mainloop()
