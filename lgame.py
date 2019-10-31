import pygame
import random
from tkinter import messagebox

pygame.init()


x1=0
y1=0
x=251
y=251
rows=20
w=500
sizebtw=w//rows
win = pygame.display.set_mode((500,500))
snack= pygame.image.load("piza.jpg")
font = pygame.font.SysFont("comicsansms", 30)
text = font.render("SNAKE GAME", True, (0, 128, 0))
snak=pygame.image.load("snak.jpg")
count=0
snakeBody=[]
snakelen=1
rx=random.randrange(26,500-26,25)
ry=random.randrange(26+25,500-26,25)
dx=25
dy=25

def reset():
	x1=0
	y1=0
	x=251
	y=251
	rows=20
	w=500
	sizebtw=w//rows
	win = pygame.display.set_mode((500,500))
	snack= pygame.image.load("piza.jpg")
	font = pygame.font.SysFont("comicsansms", 30)
	text = font.render("SNAKE GAME", True, (0, 128, 0))
	snak=pygame.image.load("snak.jpg")
	count=0
	snakeBody=[]
	snakelen=1
	rx=random.randrange(26,500-26,25)
	ry=random.randrange(26+25,500-26,25)
	dx=25
	dy=25

def randomsnack(rx,ry,win):
	pygame.draw.rect(win,(255,0,255),(rx,ry,24,24))
def griddraw(x1,y1,rows):
	y1=25
	for l in range(rows):
		x1=x1+sizebtw
		y1=y1+sizebtw
		pygame.draw.line(win,(255,255,255),(x1,50),(x1,w))
		pygame.draw.line(win,(255,255,255),(0,y1),(w,y1))

def snake(snakeBody):
	for xy in snakeBody:
		pygame.draw.rect(win,(180,66,0),(xy[0],xy[1],24,24))

flag=True
while flag:
	pygame.time.delay(100)
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			
			flag=False
	keys=pygame.key.get_pressed()
	
	


	#rx=random.randrange(26,500-26,25)
	#ry=random.randrange(26,500-26,25)
	if keys[pygame.K_UP]:
			
			
			dir="UP"
			


	elif keys[pygame.K_DOWN]:
			
			
			dir="DOWN"
			
			
			
	elif keys[pygame.K_LEFT]:
			
			
			dir="LEFT"
			
			
			
	elif keys[pygame.K_RIGHT]:
			

			dir="RIGHT"
			
	if dir=="UP" and y>=50+25:
		y-=25
		win.fill((0,0,0))
		

	elif dir=="DOWN" and y<=500-25:
		y+=25
		win.fill((0,0,0))
		
	elif dir=="RIGHT" and x<=500-25:
		x+=25
		win.fill((0,0,0))
		
		
	elif dir=="LEFT" and x>=25:
		x-=25
		win.fill((0,0,0))
			
	if x==rx and y==ry:
		#pygame.draw.rect(win,(255,0,0),(x-25,y,24,24))
		#pygame.draw.rect(win,(0,255,0),(dx+1,dy+1,22,22))
		count+=1

		snakelen+=1
		
		
		
		
		
		
		

	
	griddraw(x1,y1,rows)
			

	#pygame.draw.rect(win,(255,0,0),(dx,dy,24,24))
	pygame.draw.rect(win,(68,0,115),(rx,ry,24,24))
	
	#pygame.draw.rect(win,(0,255,0),(x+1,y+1,22,22))
	
	snakeHead=[]
	snakeHead.append(x)
	snakeHead.append(y)
	snakeBody.append(snakeHead)
	if len(snakeBody) > snakelen:
		del snakeBody[0]
	snake(snakeBody)
	pygame.draw.rect(win,(255,255,255),(0,0,500,50))
	pygame.draw.line(win,(0,0,0),(0,0),(500,0),6)
	pygame.draw.line(win,(0,0,0),(0,0),(0,50),6)
	pygame.draw.line(win,(0,0,0),(500,0),(500,50),8)
	win.blit(text,(10,5))
	win.blit(snak,(225,5))

	t1=font.render('score:'+str(count),True,(255,0,0))
	win.blit(t1,(380,10))
	pygame.display.update()
	for each in snakeBody[:-1]:

		if snakeHead==each:
			
			
			
			flag=False
	if x==rx and y==ry:
		rx=random.randrange(26,500-26,25)
		ry=random.randrange(26+25,500-26,25)
messagebox.showinfo("sanp Mela","score"+str(count))
pygame.quit()

