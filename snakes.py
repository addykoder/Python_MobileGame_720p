

#Importimg
import pygame


#initialising
pygame.init()



#setting up display
mydisplay=pygame.display.set_mode((720,1280))


#game variables
	#integer variables
difficulty_level=6
game_mode='classic'
	
	
	
	#boolean
	
	
	#initial variables
font1=pygame.font.SysFont(None,100)	
font2=pygame.font.SysFont(None,55)	
font3=pygame.font.SysFont(None,30)	

	
	
	
	
	#colors
nokia_green=(220,200,0)
black=(0,0,0)
light_black=(40,40,40)
vlight_black=(100,100,100)

	
			
	
	#display texts
nokia_text=font1.render('NOKIA',True,light_black)
snakes_text=font1.render('SNAKES',True,light_black)

start_text=font2.render('START',True,black)
difficulty_text=font3.render('DIFFICULTY LEVEL',True,vlight_black)
mode_text=font3.render('GAME MODE',True,vlight_black)
exit_text=font2.render('EXIT',True,black)






	
	
	




	
	
	
	#points




#methods




#game main loop
while True:
	# assigning in loop variables
	difficulty_switchbutton=font2.render('<  '+str(difficulty_level) +'  >',True,black)
	mode_switchbutton=font2.render('<  '+ game_mode  +'  >',True,black)

	
	
	
	
	
	
	
	
	
	# getting events
	for event in pygame.event.get():
		if event.type==pygame.MOUSEBUTTONDOWN:
			# starting the game
			
			
			
			
			
			
			
			if event.pos[0]in range(270,400)and event.pos[1]in range(550,610):
				
				with open('difficulty_level','w') as lev:
					lev.write(str(difficulty_level))
				with open('game_mode','w') as mod:
					
				
					mod.write(game_mode)
				
				
				
				import game
			
			
			
			
			
			# quitting the game
			
			if event.pos[0]in range(280,400)and event.pos[1]in range(1050,1110):
				raise SystemExit
			
			
			
			
			
			
		
			# changing the difficulty level on touch
			if event.pos[0]in range(200,290)and event.pos[1]in range(680,770):
				if difficulty_level>1:
					difficulty_level-=1
				else:
					difficulty_level=9
			if event.pos[0]in range(390,500)and event.pos[1]in range(680,770):
				if difficulty_level<9:
					difficulty_level+=1
				else:
					difficulty_level=1
			
			
			# changing the game mode
			if event.pos[0]in range(180,270)and event.pos[1]in range(850,910) or event.pos[0]in range(510,560)and event.pos[1]in range(850,950) :
				
				if game_mode=='classic':
					game_mode='arcade'
				elif game_mode=='arcade':
					game_mode='classic'
					

	
	
	
	
	
	
	








	#displaying the stuff
		#filling display
	mydisplay.fill(nokia_green)

		
		
		
		#printing title
		
	mydisplay.blit(nokia_text,(200,200))
	mydisplay.blit(snakes_text,(160,300))
	
	
		#printing start button
	
	mydisplay.blit(start_text,(270,550))
		
		#printing difficulty stuff
		
	mydisplay.blit(difficulty_text,(225,650))
	mydisplay.blit(difficulty_switchbutton,(255,690))
	
		#printing mode stuff
		
	mydisplay.blit(mode_text,(255,800))
	mydisplay.blit(mode_switchbutton,(190,850))
		
		#printing quit button
	
	mydisplay.blit(exit_text,(295,1050))
	
	
	
	
	#updating display
	pygame.display.update()
	
	
	
	
	


