import pygame
pygame.init()
font=pygame.font.SysFont(None,70)
g1=font.render('1 : EAT THE APPLE',True,(255,0,0))
g2=font.render('2 : TIC TAC TOE ',True,(0,255,0))
g3=font.render('3 : NITRO RACING ',True,(0,0,0))
g4=font.render('4 : SUPER RUNNER',True,(255,255,0))
g5=font.render('5 : SNAKES ',True,(0,0,255))
ds=pygame.display.set_mode((720,1280))
while True:
	ds. fill((255,255,255))
	for ev in pygame.event.get():
		if ev.type==pygame.MOUSEBUTTONDOWN:		
			if ev.pos[0]in range(50,720)and ev.pos[1]in range(200,300):
				import dot
			if ev.pos[0]in range(50,720)and ev.pos[1]in range(400,500):
				import xox
			if ev.pos[0]in range(50,720)and ev.pos[1]in range(600,700):
				import car
			if ev.pos[0]in range(50,720)and ev.pos[1]in range(800,900):
				import jump
			if ev.pos[0]in range(50,720)and ev.pos[1]in range(1000,1100):
				import snakes
	ds.blit(g1,(50,200))
	ds.blit(g2,(50,400))
	ds.blit(g3,(50,600))
	ds.blit(g4,(50,800))
	ds.blit(g5,(50,1000))
	pygame.display.update()