score=0

# reading the difficulty level and game mode
dif=open('difficulty_level','r')
md=open('game_mode','r')
difficulty_level=dif.read()
game_mode=md.read()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#importing the stuff
import pygame_sdl2 as pygame
from random import randint
from math import ceil,floor
from time import sleep



#initialising
pygame.init()
font=pygame.font.SysFont(None,60)
#setting up display
mydisplay=pygame.display.set_mode((720,1280))

# variables
	#lists
snake_length=1
if int(difficulty_level)<6:	
	snk_len_incr=12
else:
	snk_len_incr=8
snake_list=[]


	
	
	
	
	
	
	
	#colors
nokia_green=(220,200,0)
nokia_yello=(220,220,0)
black=(0,0,0)
light_black=(60,60,60)

	#booleans
playing=True

	#velocity
snk_velx=0
snk_vely=0

snk_x=20
snk_y=300

food_y=ceil(randint(300,960)/20)*20
food_x=ceil(randint(20,680)/20)*20

#function
def plot_snake(list):
	for i,j in list:
		pygame.draw.rect(mydisplay,light_black,(i,j,20,20))









#game main loop
while playing:
	scr=font.render('SCORE :'+str(score),None,light_black)
		
		# displaying the score
	
		
		
		#buttons
	
	
	
	
	
	
	
	
	#filling the display
	mydisplay.fill(nokia_green)
	
	
	#getting the events
	for ev in pygame.event.get():
		if ev.type==pygame.MOUSEBUTTONDOWN:
			print(food_x,food_y)
			
			if ev.pos[0]in range(530,630)and ev.pos[1]in range(1000,1100):
				move_up=True
				if snk_velx>0:
					snk_x=ceil(snk_x/20)*20
				else:
					snk_x=floor(snk_x/20)*20
				
				snk_vely=-int(difficulty_level)/2
				snk_velx=0
				
			
			if ev.pos[0]in range(530,630)and ev.pos[1]in range(1180,1280):
				move_down=True
				if snk_velx>0:
					snk_x=ceil(snk_x/20)*20
				else: 
					snk_x=floor(snk_x/20)*20
				
				
				snk_vely=int(difficulty_level)/2
				snk_velx=0
			
			if ev.pos[0]in range(440,540)and ev.pos[1]in range(1090,1190):
				move_left=True
				if snk_vely>0:
					snk_y=ceil(snk_y/20)*20
				else: 
					snk_y=floor(snk_y/20)*20
				
				
				
			
				snk_velx=-int(difficulty_level)/2
				snk_vely=0
			
			if ev.pos[0]in range(610,710)and ev.pos[1]in range(1090,1190):
				move_right=True
				if snk_vely>0:
					snk_y=ceil(snk_y/20)*20
				else: 
					snk_y=floor(snk_y/20)*20
				
				snk_velx=int(difficulty_level)/2
				snk_vely=0
			
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	#displaying the stuff
		#play area
	pygame.draw.rect(mydisplay,black,(0,280,720,720))
	pygame.draw.rect(mydisplay,nokia_green,(10,290,700,700))
	
	
	
	
	
	head=[]
	head.append(snk_x)
	head.append(snk_y)
	snake_list.append(head)
	
	if len(snake_list)>snake_length:
		snake_list.pop(0)
	
		#snake
	plot_snake(snake_list)
		#food
	pygame.draw.rect(mydisplay,light_black,(food_x,food_y,20,20))
	
	
		#BUTTONS
		
	pygame.draw.rect(mydisplay,light_black,(550,1020,60,60))	#U

	pygame.draw.rect(mydisplay,light_black,(550,1200,60,60))	#D
	pygame.draw.rect(mydisplay,light_black,(460,1110,60,60))	#L
	pygame.draw.rect(mydisplay,light_black,(630,1110,60,60))	#R
	
	
	
	snk_x+=snk_velx
	snk_y+=snk_vely
	
	
	
	# checking for food eaten
	
	if abs(snk_x-food_x)<5 and abs(snk_y-food_y)<5:
		food_y=ceil(randint(300,960)/20)*20
		food_x=ceil(randint(20,680)/20)*20
		snake_length+=snk_len_incr
		
		score+=10
		
		
		
	# checking crash
	
	for i,j in snake_list[1:]:
		if snk_x==i and snk_y==j:
			
			sleep(1)
			snk_velx=0
			snk_vely=0

			snk_x=20
			snk_y=300

			food_y=ceil(randint(300,960)/20)*20
			food_x=ceil(randint(20,680)/20)*20
			
			snake_length=1
			
			snake_list=[]
			score=0
			
			
			
	# checking crash for classic mode
	
	if game_mode=='classic':
		if snk_x<5 or snk_x>695 or snk_y<285 or snk_y>975:
			sleep(1)
			snk_velx=0
			snk_vely=0

			snk_x=20
			snk_y=300

			food_y=ceil(randint(300,960)/20)*20
			food_x=ceil(randint(20,680)/20)*20
			
			snake_length=1
			
			snake_list=[]
			score=0
	else:
		if snk_x<5:
			snk_x=695
		elif snk_x>695:
			snk_x=5
		if snk_y<285:
			snk_y=975
		elif snk_y>975:
			snk_y=285
		
		
	
	
	
	mydisplay.blit(scr,(50,50))
	#updating the display
	pygame.display.update()
	
	

	
	
	
	