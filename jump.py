score=0
import pygame
from math import floor
from random import randint
from time import sleep
from pygame import mixer
hi=open('hij','r')
hiscore=hi.read()

pygame.init()
ds=pygame.display.set_mode((720,1280))
p1=pygame.image.load('pic11.jpg')
p2=pygame.image.load('pic22.jpg')
p3=pygame.image.load('pic33.jpg')
p4=pygame.image.load('pic44.jpg')
p5=pygame.image.load('pic55.jpg')
p6=pygame.image.load('pic66.jpg')
p7=pygame.image.load('pic77.jpg')
p8=pygame.image.load('pic88.jpg')
x1=0
x2=110
x3=220
x4=330
x5=440
x6=550
x7=660
x8=770
gameover=False
xa=700
ya=1140

vel_ground=-15

reset=False
vel_obstacle=-15
incr_g=True
incr_g2=True

plus1=True
plus2=True
plus3=True
plus4=True
plus5=True
plus6=True
plus7=True
plus8=True
plus9=True
plus10=True
plus11=True
plus12=True
plus13=True

font=pygame.font.SysFont(None,50)

clock=pygame.time.Clock()
fps=30
sr=1

psr=False
x=40
y=1100
vel_incr=-60
vel=0
gravity=6
while True:
	for event in pygame.event.get():
		if event.type==pygame.MOUSEBUTTONDOWN:
			if event.pos[0]in range(680,720)and event.pos[1]in range(60):
				raise SystemExit
			
			
			
			
			
			if y>=1100:
				if gameover==False:
					vel=vel_incr
	
			
	
	
	
	
	
	ds.fill((255,255,255))
	if sr==1 or psr==True:
		ds.blit(p1,(x,y))
		if gameover==False:
			sr=3
	elif sr==2:
		ds.blit(p2,(x,y))
		if gameover==False:
			
			sr=3
	elif sr==3:
		ds.blit(p3,(x,y))
		if gameover==False:
			sr=4
	elif sr==4:
		ds.blit(p4,(x,y))
		if gameover==False:
			sr=5
	elif sr==5:
		ds.blit(p5,(x,y))
		if gameover==False:
			sr=6
	elif sr==6:
		ds.blit(p6,(x,y))
		if gameover==False:
			sr=7
	elif sr==7:
		ds.blit(p7,(x,y))
		if gameover==False:
			sr=8
	elif sr==8:
		ds.blit(p8,(x,y))
		if gameover==False:
			sr=1
	
	
	
	
	
	y+=vel
	if not y>1100:
		vel+=gravity
	if y>1100:
		vel=0
		psr=False
	if y<1100:
		psr=True
	black=(0,0,0)	
	red=(255,0,0)
	pygame.draw.rect(ds,(0,0,0),(0,1230,720,5))
	pygame.draw.rect(ds,black,(x1,1220,100,10))
	pygame.draw.rect(ds,black,(x2,1220,100,10))
	pygame.draw.rect(ds,black,(x3,1220,100,10))
	pygame.draw.rect(ds,black,(x4,1220,100,10))
	pygame.draw.rect(ds,black,(x5,1220,100,10))
	pygame.draw.rect(ds,black,(x6,1220,100,10))
	pygame.draw.rect(ds,black,(x7,1220,100,10))
	pygame.draw.rect(ds,black,(x8,1220,100,10))
	
	pygame.draw.rect(ds,red,(xa,ya,100,80))
	
	
	x1+=vel_ground
	x2+=vel_ground
	x3+=vel_ground
	x4+=vel_ground
	x5+=vel_ground
	x6+=vel_ground
	x7+=vel_ground
	x8+=vel_ground
	
	
	
	
	
	xa+=vel_obstacle
	
	if xa<-90:
		mixer.music.load('scor.ogg')
		mixer.music.play()
		xa=randint(500,900)
		a=randint(1,3)
		if a==1:
			ya=1140
		elif a==2:
			ya=1050
		elif a==3:
			ya=890
	if abs(x-xa)<80 and abs(y-ya)<65:
		mixer.music.load('sound_hit.ogg')
		mixer.music.play()
		vel_obstacle=0
		vel_ground=0
		vel_incr=0
		gameover=True
	
	
	if x1<-100:
		x1=770
	if x2<-100:
		x2=770
	if x3<-100:
		x3=770
	if x4<-100:
		x4=770
	if x5<-100:
		x5=770
	if x6<-100:
		x6=770
	if x7<-100:
		x7=770
	if x8<-100:
		x8=770
	
	
	
	if gameover==False:
		score+=1
		if score>1000:
			score+=1
			if incr_g==True:
				
				incr_g=False
		if score>3600:
			if incr_g==True:
				
				incr_g=False
			score+=2
			
			
	if score/2>100 and plus1==True:
		vel_ground-=5
		vel_obstacle-=0.5
		plus1=False
	if score>200 and plus2==True:
		vel_ground-=5
		vel_obstacle-=1
		plus2=False
	if score>250 and plus3==True:
		vel_ground-=5
		vel_obstacle-=1
		plus3=False
	if score>300 and plus4==True:
		vel_ground-=5
		vel_obstacle-=1
		plus4=False
	if score>400 and plus5==True:
		vel_ground-=5
		vel_obstacle-=1
		plus5=False
		
		
		
		
		
	if score/2>500 and plus6==True:
		vel_ground-=5
		vel_obstacle-=1
		plus6=False
	if score/2>600 and plus7==True:
		vel_ground-=5
		vel_obstacle-=1
		plus7=False
	if score/2>750 and plus8==True:
		vel_ground-=5
		vel_obstacle-=1
		plus8=False
	if score/2>900 and plus9==True:
		vel_ground-=5
		vel_obstacle-=1
		plus9=False
	if score/2>1000 and plus10==True:
		vel_ground-=5
		vel_obstacle-=2
		plus10=False
	if score/2>1200 and plus11==True:
		vel_ground-=5
		vel_obstacle-=1.5
		plus11=False
	if score/2>1500 and plus12==True:
		vel_ground-=5
		vel_obstacle-=1.5
		plus12=False
	if score/2>1800 and plus13==True:
		vel_ground-=5
		vel_obstacle-=2
		plus13=False
	
	
	
	
	
	
	
	if gameover==True:
		
		sleep(2)
		gameover=False
		xa=700
		ya=1140
		score=0
		vel_ground=-15
		plus1=True
		plus2=True
		plus3=True
		plus4=True
		plus5=True
		plus6=True
		plus7=True
		plus8=True
		plus9=True
		plus10=True
		plus11=True
		plus12=True
		plus13=True
		incr_g=True
		incr_g2=True
		
				
		vel_obstacle=-15
			
			
			
				
				
				
			
		psr=False
		x=40
		y=1100
		vel_incr=-60
		vel=0
		gravity=6
		reset=False
	
	
	
	
	
	
	score_s=floor(score/2)
	if score/2>int(hiscore):
		hiscore=score/2
		new=font.render('New Highscore',True,(0,255,0))
		ds.blit(new,(0,50))
		with open('hij','w') as xx:
			xx.write(str(score_s))
	
	
	
	myscore=font.render('SCORE :'+str(floor(score/2))+'  Hiscore :'+str(floor(int(hiscore))),True,(255,0,0))
	ds.blit(myscore,(0,0))
	pygame.display.update()
	clock.tick(fps)