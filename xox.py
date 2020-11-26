# IMPORTING STUFF
import pygame
from pygame import mixer
from random import randint
from time import sleep



#  RESET THE GAME LOOP
while True:

	
		
	
	
	# CREATING ALL THE VARIABLES
		# game main variables
	fps=30
	
	
	playing=True
	reset=False
	chance=1
	win1=False
	
	draw=False
		#creating display
	mydisplay=pygame.display.set_mode((720,1080))
		#creating clock
	clock=pygame.time.Clock()
	
	
	
	
	
	
		# board occupancy variable
	board=[0,0,0,0,0,0,0,0,0]
	
	
	
	
	
	#LOADING ALL THE IMAGES

	img_o=pygame.image.load('O.png')
	img_x=pygame.image.load('X.png')
	background=pygame.image.load('home.jpg')
	won1=pygame.image.load('WON.png')
	won2=pygame.image.load('win.png')
	dr=pygame.image.load('drow.png')
	
	
	
	#LOADING ALL THE SOUNDS
	
	
	
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	
	# DEFINING ALL THE FUNCTIONS
	
	#displaying X or O as per the input
	def display(piece,position):
		pass
		
		
	
	
	
	#checking exit and exitting if true
	def check_exit():
		if event.type==pygame.MOUSEBUTTONDOWN:
			if event.pos[0]in range(0,100)and event.pos[1]in range(1200,1280):
				raise SystemExit
				
				
				
	
	#checking reset and resetting if true
	def check_reset():
		if event.type==pygame.MOUSEBUTTONDOWN:
			if event.pos[0]in range(300,440)and event.pos[1]in range(100,240):
				
				reset=True
		
	
	
	
	
	#checking the input and placing piece acording chance
	
			
				
			
	
#FUNCTIONS OVER	
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	
	
	#     				GAME MAIN LOOP BEGINS
	
	
	
	while playing:
	
		# displaying homewindow as background
		mydisplay.blit(background,(0,0))
		
		
		
		
		
		for event in pygame.event.get():
			if event.type==pygame.MOUSEBUTTONDOWN:
				if event.pos[0]in range(10,250) and event.pos[1]in range(420,670):
					if win1!=True:
						
						if board[0]==0:
							if chance==1:
								board[0]=1
								chance=2
							elif chance==2:
								board[0]=2
								chance=1
				if event.pos[0]in range(245,475) and event.pos[1]in range(420,670):
					if win1!=True:
						if board[1]==0:
							if chance==1:
								board[1]=1
								chance=2
							elif chance==2:
								board[1]=2
								chance=1
				if event.pos[0]in range(475,725) and event.pos[1]in range(420,670):
					if win1!=True:
						if board[2]==0:
							if chance==1:
								board[2]=1
								chance=2
							elif chance==2:
								board[2]=2
								chance=1
				if event.pos[0]in range(10,250) and event.pos[1]in range(670,900):
					if win1!=True:
						if board[3]==0:
							if chance==1:
								board[3]=1
								chance=2
							elif chance==2:
								board[3]=2
								chance=1
				if event.pos[0]in range(245,475) and event.pos[1]in range(670,900):
					if win1!=True:
						if board[4]==0:
							if chance==1:
								board[4]=1
								chance=2
							elif chance==2:
								board[4]=2
								chance=1
				if event.pos[0]in range(475,725) and event.pos[1]in range(670,900):
					if win1!=True:
						if board[5]==0:
							if chance==1:
								board[5]=1
								chance=2
							elif chance==2:
								board[5]=2
								chance=1
				if event.pos[0]in range(10,250) and event.pos[1]in range(900,1130):
					if win1!=True:
						if board[6]==0:
							if chance==1:
								board[6]=1
								chance=2
							elif chance==2:
								board[6]=2
								chance=1
				if event.pos[0]in range(250,475) and event.pos[1]in range(900,1130):
					if win1!=True:
						if board[7]==0:
							if chance==1:
								board[7]=1
								chance=2
							elif chance==2:
								board[7]=2
								chance=1
				if event.pos[0]in range(475,725) and event.pos[1]in range(900,1130):
					if win1!=True:
						if board[8]==0:
							if chance==1:
								board[8]=1
								chance=2
							elif chance==2:
								board[8]=2
								chance=1
			
			
			
			
			
		
			
			
			
			
			
			
			check_exit()
			
			
			
			
			if event.type==pygame.MOUSEBUTTONDOWN:			
				if event.pos[0]in range(300,440)and event.pos[1]in range(100,240):
				
				
		
		
					playing=True
					reset=False
					chance=1
					win1=False
					win2=False
					board=[0,0,0,0,0,0,0,0,0]
	

			
			
			
			
			
			
			
		
		
		
		
		
		
		
		
		
		
		#		DISPLAYING ALL STUFF
		if board[0]==1:
			mydisplay.blit(img_x,(10,420))
		if board[0]==2:
			mydisplay.blit(img_o,(10,420))
		
		if board[1]==1:
			mydisplay.blit(img_x,(245,420))
		if board[1]==2:
			mydisplay.blit(img_o,(245,420))
			
		if board[2]==1:
			mydisplay.blit(img_x,(475,420))
		if board[2]==2:
			mydisplay.blit(img_o,(475,420))
			
		if board[3]==1:
			mydisplay.blit(img_x,(10,670))
		if board[3]==2:
			mydisplay.blit(img_o,(10,679))
			
		if board[4]==1:
			mydisplay.blit(img_x,(245,670))
		if board[4]==2:
			mydisplay.blit(img_o,(245,670))
			
		if board[5]==1:
			mydisplay.blit(img_x,(475,670))
		if board[5]==2:
			mydisplay.blit(img_o,(475,670))
			
		if board[6]==1:
			mydisplay.blit(img_x,(10,900))
		if board[6]==2:
			mydisplay.blit(img_o,(10,900))
			
		if board[7]==1:
			mydisplay.blit(img_x,(245,900))
		if board[7]==2:
			mydisplay.blit(img_o,(245,900))
			
		if board[8]==1:
			mydisplay.blit(img_x,(475,900))
		if board[8]==2:
			mydisplay.blit(img_o,(475,900))
			
			
		if board[0]==1 and board[1]==1 and board[2]==1:
			mydisplay.blit(won1,(0,0))
			win1=True
		if board[3]==1 and board[4]==1 and board[5]==1:
			mydisplay.blit(won1,(0,0))
			win1=True
		if board[6]==1 and board[7]==1 and board[8]==1:
			mydisplay.blit(won1,(0,0))
			win1=True
		if board[0]==1 and board[3]==1 and board[6]==1:
			mydisplay.blit(won1,(0,0))
			win1=True
		if board[1]==1 and board[4]==1 and board[7]==1:
			mydisplay.blit(won1,(0,0))
			win1=True
		if board[2]==1 and board[5]==1 and board[8]==1:
			mydisplay.blit(won1,(0,0))
			win1=True
		if board[0]==1 and board[4]==1 and board[8]==1:
			mydisplay.blit(won1,(0,0))
			win1=True
		if board[2]==1 and board[4]==1 and board[6]==1:
			mydisplay.blit(won1,(0,0))
			win1=True
			
		if board[0]==2 and board[1]==2 and board[2]==2:
			mydisplay.blit(won2,(0,0))
			win1=True
		if board[3]==2 and board[4]==2 and board[5]==2:
			mydisplay.blit(won2,(0,0))
			win1=True
		if board[6]==2 and board[7]==2 and board[8]==2:
			mydisplay.blit(won2,(0,0))
			win1=True
		if board[0]==2 and board[3]==2 and board[6]==2:
			mydisplay.blit(won2,(0,0))
			win1=True
		if board[1]==2 and board[4]==2 and board[7]==2:
			mydisplay.blit(won2,(0,0))
			win1=True
		if board[2]==2 and board[5]==2 and board[8]==2:
			mydisplay.blit(won2,(0,0))
			win1=True
		if board[0]==2 and board[4]==2 and board[8]==2:
			mydisplay.blit(won2,(0,0))
			win1=True
		if board[2]==2 and board[4]==2 and board[6]==2:
			mydisplay.blit(won2,(0,0))
			win1=True
			
		if board[0]!=0 and board[1]!=0 and board[2]!=0 and board[3]!=0 and board[4]!=0 and board[5]!=0 and board[6]!=0 and board[7]!=0 and board[8]!=0 and win1 ==False:
			mydisplay.blit(dr,(0,0))
		
			
		
			
		
		
		
		
		
		
		
		
		
		
		
		
		
		#updating display
		pygame.display.update()
		
		
		
		#updating frames
		clock.tick(fps)
		
		
		
		
		
		
		
		
		
		
		
		
		
		