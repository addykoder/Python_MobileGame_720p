import pygame
from pygame import mixer
from time import sleep

while True:
	score=0

	#importing and initialising
	
	
	from time import sleep
	from random import randint
	pygame.init()
	
	#game variables
	fps=240
	screen_width=600
	screen_height=600
	running=True
	color_series=0
	snakex=300
	snakey=600
	speedx=0
	speedy=0
	gameover=False

	foodx=randint(20,700)
	foody=randint(300,980)
			#obstacles
	obs1x=randint(20,700)
	obs1y=randint(300,980)
	
	obs2x=randint(20,700)
	obs2y=randint(300,980)
	
	obs3x=randint(20,700)
	obs3y=randint(300,980)
	
	obs4x=randint(20,700)
	obs4y=randint(300,980)
	
	#setting up the clock
	clock=pygame.time.Clock()
	
	
	# colors
	
	white=(255,255,255)
	yello=(0,255,255)
	red=(255,0,0)
	green=(0,255,0)
	blue=(0,0,255)
	black=(0,0,0)
	colors=[white,red,green,blue,black]
	#setting up a display as mydisplay
	
	mydisplay=pygame.display.set_mode((screen_width,screen_height))
	
	cross=pygame.image.load('cross.png')
	left=pygame.image.load('arrow_left.png')
	right=pygame.image.load('arrow_right.png')
	up=pygame.image.load('arrow_up.png')
	down=pygame.image.load('arrow_down.png')
	
	
	
	# functions and methods
	
	
		
	
	
	
	def check_exit():
		    if event.type == pygame.MOUSEBUTTONDOWN:
		        if event.button == 1:
		            
		            
		            
		            if event.pos[0] >600 and event.pos[1]<100:
		            	raise SystemExit
		    
		    #pygame.draw.rect(mydisplay,black,[615,0,120,105])
		    #pygame.draw.rect(mydisplay,red,[620,5,95,95])
		    
	
	def changecolorontouch():
			global color_series
			global snakey
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					if event.pos[0] <100 and  event.pos[1]<100:
						snakey+=20
						color_series+=1
			if color_series>4:
				color_series=0
	
	def move_snake():
		global snakex
		global snakey
		global speedx
		global speedy
		
		if event.type==pygame.MOUSEBUTTONDOWN:
				if event.pos[0]in range(120,240)and event.pos[1]in range(1050,1170):
				#	snakex-=10
					speedx=-8
					speedy=0
					
				if event.pos[0]in range(480,600)and event.pos[1]in range(1050,1170):
				#	snakex+=10
					speedx=8
					speedy=0
					
				if event.pos[0]in range(300,420)and event.pos[1]in range(950,1070):
					#snakey-=10
					speedy=-8
					speedx=0
					
				if event.pos[0]in range(300,420)and event.pos[1]in range(1150,1270):
					#snakey+=10
					speedy=8
					speedx=0
					
		if event.type==pygame.MOUSEBUTTONUP:
			pass
	def wall_cross():
		global snakex
		global snakey
		
		if snakex<20:
			snakex=680
		if snakex>680:
			snakex=20
		if snakey<300:
			snakey=960
		if snakey>960:
			snakey=300
	
	
	
	
	
	
	
	################################################
	#*************************************************************
	################################################
	
	
	# game main loop begin
	
	
	
	while running:
		for event in pygame.event.get():
			
				
						
			
			
			
			
			
			#changing color on touch
			changecolorontouch()
			
			
			#exiting when touched on cross
			check_exit()
			
			
			#
			
			
			#moving snake
			move_snake()
			
			
			
			
			
		
				
			
		
		#main window display
			
		mydisplay.fill(colors[color_series])
		#highscore
		x=open('highscore','r')
		hiscore=x.read()
		
		#screen_text=font.render('highscore:'+str(highscore),True,yello)
		#mydisplay.blit(screen_text,(250,100))
		
		
		# displaying the score
		font=pygame.font.SysFont(None,55)
		if score>int(hiscore):
			hiscore=score
		screen_text=font.render('score:'+str(score)+'    hiscore: '+str(hiscore),True,yello)
		mydisplay.blit(screen_text,(5,100))
		
		
		
		# uploading the score
		"""if int(score)>int(highscore):
			x=open('highscore','w')
			x.write(str(score))"""
		
			
		#crossing the wall
		wall_cross()
		#creating game area
		pygame.draw.rect(mydisplay,black,[20,300,680,680])
		
		#displaying buttons
		mydisplay.blit(cross,(620,0))		#cross
	
		#changing food position
		
			
		
		
		if abs(snakex-foodx)<25 and abs(snakey-foody)<25:
			score+=1
			#importing the sounds
			mixer.music.load('sound1.ogg')
			mixer.music.play()
			print(score)
			foodx=randint(20,700)
			foody=randint(300,980)
			
			obs1x=randint(20,700)
			obs1y=randint(300,980)
	
			obs2x=randint(20,700)
			obs2y=randint(300,980)
	
			obs3x=randint(20,700)
			obs3y=randint(300,980)
	
			obs4x=randint(20,700)
			obs4y=randint(300,980)
			
		
		#drawing the food
		pygame.draw.rect(mydisplay,red,[foodx,foody,30,30])
				#drawing the snake
				#my face as player
		#mm=pygame.image.load('my.png')
		#mydisplay.blit(mm,(snakex,snakey))
				#resctangle as player
		pygame.draw.rect(mydisplay,green,[snakex,snakey,20,20])
		#drawing obstacle
		pygame.draw.rect(mydisplay,blue,[obs1x,obs1y,40,40])
		
		if snakex in range(obs1x,obs1x+40) and snakey in range(obs1y,obs1y+40):
			mixer.music.load('sound_hit.ogg')
			mixer.music.play()
			
			
			gameover=True
		
		
		pygame.draw.rect(mydisplay,blue,[obs2x,obs2y,40,40])
		
		if snakex in range(obs2x,obs2x+40) and snakey in range(obs2y,obs2y+40):
			mixer.music.load('sound_hit.ogg')
			mixer.music.play()
			
			
			gameover=True
			
		
		pygame.draw.rect(mydisplay,blue,[obs3x,obs3y,40,40])
		
		if snakex in range(obs3x,obs3x+40) and snakey in range(obs3y,obs3y+40):
			mixer.music.load('sound_hit.ogg')
			mixer.music.play()
			
			gameover=True
			
	
		pygame.draw.rect(mydisplay,blue,[obs4x,obs4y,40,40])
		
		if snakex in range(obs4x,obs4x+40) and snakey in range(obs4y,obs4y+40):
			mixer.music.load('sound_hit.ogg')
			mixer.music.play()
			
			gameover=True
		
		
		
		
		
		
		
		
		
		
		
		#arrow buttons
		mydisplay.blit(left,(120,1050))
		mydisplay.blit(right,(480,1050))
		mydisplay.blit(up,(300,950))
		mydisplay.blit(down,(300,1150))
		
		color=color_series+1
		if color_series==4:
			color=0
			
		#drawing color change button
		pygame.draw.rect(mydisplay,colors[color],[0,0,50,50])
		#auto moving the snake
		
		snakex=snakex+speedx
		snakey=snakey+speedy
		
		# making game over
		if gameover:
			sleep(2)
			
			mydisplay.fill(red)
			font=pygame.font.SysFont(None,100)
			screen_text=font.render('Game Over',True,yello)
			scr=font.render('score:'+str(score),True,yello)
			sc=font.render('Restarting . . .',True,yello)
			mydisplay.blit(screen_text,(100,600))
			mydisplay.blit(scr,(200,800))
			mydisplay.blit(sc,(0,1000))
			with open("highscore","w") as f:
			    f.write(str(hiscore))
			pygame.display.update()
			sleep(2)
			break
			
		
		
		#setting fps
		
		
		
		clock.tick(fps)
		#pygame main loop
		pygame.display.update()
	
	        
	    