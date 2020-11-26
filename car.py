score=0
import pygame
from random import randint
from pygame import mixer
from math import floor
file=open('hi','r')
hiscore=file.read()
pygame.init()
ds=pygame.display.set_mode((720,1280))
#img1=pygame.image.load('home.jpg')
car=pygame.image.load('mycar.png')
clock=pygame.time.Clock()
fps=90

gameover=False
aa=randint(1,4)
if aa==1:	
	enm1=pygame.image.load('car1.png')
elif aa==2:
	enm1=pygame.image.load('car2.png')
elif aa==3:
	enm1=pygame.image.load('car3.png')
elif aa==4:
	enm1=pygame.image.load('car4.png')

aa=randint(1,4)
if aa==1:	
	enm2=pygame.image.load('car1.png')
elif aa==2:
	enm2=pygame.image.load('car2.png')
elif aa==3:
	enm2=pygame.image.load('car3.png')
elif aa==4:
	enm2=pygame.image.load('car4.png')

aa=randint(1,4)
if aa==1:	
	enm3=pygame.image.load('car1.png')
elif aa==2:
	enm3=pygame.image.load('car2.png')
elif aa==3:
	enm3=pygame.image.load('car3.png')
elif aa==4:
	enm3=pygame.image.load('car4.png')

aa=randint(1,4)
if aa==1:	
	enm4=pygame.image.load('car1.png')
elif aa==2:
	enm4=pygame.image.load('car2.png')
elif aa==3:
	enm4=pygame.image.load('car3.png')
elif aa==4:
	enm4=pygame.image.load('car4.png')

aa=randint(1,4)
if aa==1:	
	enm5=pygame.image.load('car1.png')
elif aa==2:
	enm5=pygame.image.load('car2.png')
elif aa==3:
	enm5=pygame.image.load('car3.png')
elif aa==4:
	enm5=pygame.image.load('car4.png')


aa=randint(1,4)
if aa==1:	
	enm6=pygame.image.load('car1.png')
elif aa==2:
	enm6=pygame.image.load('car2.png')
elif aa==3:
	enm6=pygame.image.load('car3.png')
elif aa==4:
	enm6=pygame.image.load('car4.png')











go=pygame.image.load('gameover.png')
up=False
down=False
left=False

right=False
font=pygame.font.SysFont(None,45)
x=480
y=760
vel=5
velx=11

vel1=2
vel2=vel1+10
fps=60
x1=randint(150,480)
y1=-200
x2=randint(150,480)
y2=randint(-1500,-100)
x3=randint(150,480)
y3=randint(-1500,-100)
x4=randint(150,480)
y4=randint(-1500,-100)
x5=randint(150,480)
y5=randint(-1500,-100)
x6=randint(150,480)
y6=randint(-1500,-100)
pause=False
ya=0
yb=150
yc=300
yd=450
ye=600
yf=750




play=False
spd1=True
spd2=True
spd3=True
spd4=True
spd5=True
spd6=True
spd7=True


pt=0




while True:
	for event in pygame.event.get():
		if event.type==pygame.MOUSEBUTTONDOWN:
			if pause==False and event.pos[0]in range(0,100) and event.pos[1]in range(0,50):
				vel=0
				vel1=0
				vel2=0
				velx=0
				pause=True
			elif pause==True:
				pause=False
				vel=5
				velx=11

				vel1=2
				vel2=vel1+10
			
		
		
		
		
		
		if event.type==pygame.MOUSEBUTTONDOWN:
			if event.pos[0]in range(10,120)and event.pos[1]in range(1190,1280):
				raise SystemExit
			if event.pos[0]in range(10,200)and event.pos[1]in range(1050,1120):
				
				#****************restarting all the variables*********************
				aa=randint(1,4)
				if aa==1:	
					enm1=pygame.image.load('car1.png')
				elif aa==2:
					enm1=pygame.image.load('car2.png')
				elif aa==3:
					enm1=pygame.image.load('car3.png')
				elif aa==4:
					enm1=pygame.image.load('car4.png')

				aa=randint(1,4)
				if aa==1:	
					enm2=pygame.image.load('car1.png')
				elif aa==2:
					enm2=pygame.image.load('car2.png')
				elif aa==3:
					enm2=pygame.image.load('car3.png')
				elif aa==4:
					enm2=pygame.image.load('car4.png')

				aa=ralndint(1,4)
				if aa==1:	
					enm3=pygame.image.load('car1.png')
				elif aa==2:
					enm3=pygame.image.load('car2.png')
				elif aa==3:
					enm3=pygame.image.load('car3.png')
				elif aa==4:
					enm3=pygame.image.load('car4.png')
					
				aa=randint(1,4)
				if aa==1:	
					enm4=pygame.image.load('car1.png')
				elif aa==2:
					enm4=pygame.image.load('car2.png')
				elif aa==3:
					enm4=pygame.image.load('car3.png')
				elif aa==4:
					enm4=pygame.image.load('car4.png')
					
				aa=randint(1,4)
				if aa==1:	
					enm5=pygame.image.load('car1.png')
				elif aa==2:
					enm5=pygame.image.load('car2.png')
				elif aa==3:
					enm5=pygame.image.load('car3.png')
				elif aa==4:
					enm5=pygame.image.load('car4.png')
					
				aa=randint(1,4)
				if aa==1:	
					enm6=pygame.image.load('car1.png')
				elif aa==2:
					enm6=pygame.image.load('car2.png')
				elif aa==3:
					enm6=pygame.image.load('car3.png')
				elif aa==4:
					enm6=pygame.image.load('car4.png')
					
					
					
					
					
					
					
					
					
				#*******************resetting all variable ends*****************




				
	
				#font=pygame.font.SysFont(None,40)
				x=480
				y=760
				vel=5
				vel1=5
				vel2=vel1+10
			
				x1=randint(150,480)
				y1=-200
				x2=randint(150,480)
				y2=randint(-1500,-100)
				x3=randint(150,480)
				y3=randint(-1500,-100)
				x4=randint(150,480)
				y4=randint(-1500,-100)
				x5=randint(150,480)
				y5=randint(-1500,-100)
				x6=randint(150,480)
				y6=randint(-1500,-100)
				spd1=True
				spd2=True
				spd3=True
				spd4=True
				spd5=True
				spd6=True
				spd7=True
				play=False
				pt=0
				gameover=False
				score=0
				velx=11
				vel1=2
		
		
		
		if event.type==pygame.MOUSEBUTTONDOWN:
			#if not x<150 and not x>480 and not y<20 and not y>760: 
				
				
				if event.pos[0]in range(540,630) and event.pos[1]in range(880,965):
					up=True
				if event.pos[0]in range(550,630) and event.pos[1]in range(1080,1160):
					down=True
				
				if event.pos[0]in range(440,540) and event.pos[1]in range(970,1060):
					left=True
				if event.pos[0]in range(620,720) and event.pos[1]in range(940,1060):
					right=True
		
		
		
		
		if event.type==pygame.MOUSEBUTTONUP:
			up=False
			down=False
			left=False
			right=False
			
	# diplaying the main window in the screen***************************
	
	#ds.blit(img1,(0,0))
	pygame.draw.rect(ds,(255,255,255),(0,0,720,1280))
	pygame.draw.rect(ds,(255,0,0),(520,890,112,70))
	pygame.draw.rect(ds,(255,0,0),(520,1050,112,70))
	pygame.draw.rect(ds,(255,0,0),(450,970,130,70))
	pygame.draw.rect(ds,(255,0,0),(570,970,130,70))
	pygame.draw.rect(ds,(0,0,255),(10,1050,190,70))
	
	black=(0,0,0)
	#drawing boundaries
	pygame.draw.rect(ds,black,(150,0,10,850))
	pygame.draw.rect(ds,black,(480+110,0,10,850))
	#drawing divider
	pygame.draw.rect(ds,black,(365,ya,20,100))
	#pygame.draw.rect(ds,black,(650,yd,50,100))
	#pygame.draw.rect(ds,black,(20,yd,50,100))
	
	pygame.draw.rect(ds,black,(365,yb,20,100))
	pygame.draw.rect(ds,black,(365,yc,20,100))
	pygame.draw.rect(ds,black,(365,yd,20,100))
	#pygame.draw.rect(ds,black,(650,yd,50,100))
	#pygame.draw.rect(ds,black,(20,yd,50,100))
	
	pygame.draw.rect(ds,black,(365,ye,20,100))
	pygame.draw.rect(ds,black,(365,yf,20,90))
	
	pygame.draw.rect(ds,black,(150,ya,20,100))
	pygame.draw.rect(ds,black,(150,yb,20,100))
	pygame.draw.rect(ds,black,(150,yc,20,100))
	pygame.draw.rect(ds,black,(150,yd,20,100))
	pygame.draw.rect(ds,black,(150,ye,20,100))
	pygame.draw.rect(ds,black,(150,yf,20,90))

	pygame.draw.rect(ds,black,(580,ya,20,100))
	pygame.draw.rect(ds,black,(580,yb,20,100))
	pygame.draw.rect(ds,black,(580,yc,20,100))
	pygame.draw.rect(ds,black,(580,yd,20,100))
	pygame.draw.rect(ds,black,(580,ye,20,100))
	pygame.draw.rect(ds,black,(580,yf,20,90))
	
	
	
	ya+=vel2
	yb+=vel2
	yc+=vel2
	yd+=vel2
	ye+=vel2
	yf+=vel2
	if ya>760:
		ya=-100
	if yb>760:
		yb=-100
	if yc>760:
		yc=-100
	if yd>760:
		yd=-100
	if ye>760:
		ye=-100
	if yf > 760:
		yf=-100
	
		
			
					
	if up==True and y>20:
		y-=vel
	if down==True and y<760:
		y+=velx
		
	if left==True and x>170:
		x-=velx
	if right==True and x<480:
		x+=velx
	y1+=vel1
	y2+=vel1
	y3+=vel1
	y4+=vel1
	y5+=vel1
	y6+=vel1
	
	
	
	
	
	
	ds.blit(car,(x,y))
	if y1<800:	
		ds.blit(enm1,(x1,y1))
		
		
	else:
		score+=1
		mixer.music.load('scor.ogg')
		mixer.music.play()
		y1=randint(-1500,-100)
		x1=randint(150,480)
		aa=randint(1,4)
		if aa==1:	
			enm1=pygame.image.load('car1.png')
		elif aa==2:
			enm1=pygame.image.load('car2.png')
		elif aa==3:
			enm1=pygame.image.load('car3.png')
		elif aa==4:
			enm1=pygame.image.load('car4.png')
	if y2<800:
		ds.blit(enm2,(x2,y2))
	else:
		score+=1
		mixer.music.load('scor.ogg')
		mixer.music.play()
		y2=randint(-1500,-100)
		x2=randint(150,480)
		aa=randint(1,4)
		if aa==1:	
			enm2=pygame.image.load('car1.png')
		elif aa==2:
			enm2=pygame.image.load('car2.png')
		elif aa==3:
			enm2=pygame.image.load('car3.png')
		elif aa==4:
			enm2=pygame.image.load('car4.png')
	if y3<800:
		ds.blit(enm3,(x3,y3))
	else:
		score+=1
		mixer.music.load('scor.ogg')
		mixer.music.play()
		y3=randint(-1500,-100)
		x3=randint(150,480)
		aa=randint(1,4)
		if aa==1:	
			enm3=pygame.image.load('car1.png')
		elif aa==2:
			enm3=pygame.image.load('car2.png')
		elif aa==3:
			enm3=pygame.image.load('car3.png')
		elif aa==4:
			enm3=pygame.image.load('car4.png')
			
	if score>25:	
		
		if y4<800:
			ds.blit(enm4,(x4,y4))
		else:
			score+=1
			mixer.music.load('scor.ogg')
			mixer.music.play()
			y4=randint(-1500,-100)
			x4=randint(150,480)
			aa=randint(1,4)
			if aa==1:	
				enm4=pygame.image.load('car1.png')
			elif aa==2:
				enm4=pygame.image.load('car2.png')
			elif aa==3:
				enm4=pygame.image.load('car3.png')
			elif aa==4:
				enm4=pygame.image.load('car4.png')
		
		if y5<800:
			ds.blit(enm5,(x5,y5))
		else:
			score+=1
			mixer.music.load('scor.ogg')
			mixer.music.play()
			y5=randint(-1500,-100)
			x5=randint(150,480)
			aa=randint(1,4)
			if aa==1:	
				enm5=pygame.image.load('car1.png')
			elif aa==2:
				enm5=pygame.image.load('car2.png')
			elif aa==3:
				enm5=pygame.image.load('car3.png')
			elif aa==4:
				enm5=pygame.image.load('car4.png')
		if score>40:		
			if y6<800:
				ds.blit(enm6,(x6,y6))
			else:
				score+=1
				mixer.music.load('scor.ogg')
				mixer.music.play()
				y6=randint(-1500,-100)
				x6=randint(150,480)
				aa=randint(1,4)
				if aa==1:	
					enm6=pygame.image.load('car1.png')
				elif aa==2:
					enm6=pygame.image.load('car2.png')
				elif aa==3:
					enm6=pygame.image.load('car3.png')
				elif aa==4:
					enm6=pygame.image.load('car4.png')
		
			
			
		

		
				
						
								
										
												
														
																
																		
																				
																								
	if score>int(hiscore):
		hiscore=score
		with open('hi','w') as file:
			file.write(str(score))
		
		

		
		
	if abs(x1-x)<45 and abs(y1-y)<85:
		ds.blit(go,(0,0))
		gameover=True
		play=True
		vel1=0
		vel=0
		velx=0
	if abs(x2-x)<45 and abs(y2-y)<85:
		ds.blit(go,(0,0))
		gameover=True
		play=True
		vel1=0
		vel=0
		velx=0
	if abs(x3-x)<45 and abs(y3-y)<85:
		ds.blit(go,(0,0))
		gameover=True
		play=True
		vel1=0
		vel=0
		velx=0
	if score>25:
		if abs(x4-x)<45 and abs(y4-y)<85:
			ds.blit(go,(0,0))
			gameover=True
			play=True
			vel1=0
			vel=0
			velx=0
		if abs(x5-x)<45 and abs(y5-y)<85:
			ds.blit(go,(0,0))
			gameover=True
			play=True
			vel1=0
			vel=0
			velx=0
		if score>40:
			if abs(x6-x)<45 and abs(y6-y)<85:
				ds.blit(go,(0,0))
				gameover=True
				play=True
				vel1=0
				vel=0
				velx=0
	if play==True:
		mixer.music.load('sound_hit.ogg')
		mixer.music.play()
		
	if score>10 and spd1==True:
		vel1+=2
		vel2+=4
		spd1=False
	if score>20 and spd2==True:
		vel1+=2
		vel2+=4
		spd2=False
	if score>30 and spd3==True:
		vel1+=2
		vel2+=4
		spd3=False
	if score and spd4==True:
		vel1+=2
		vel2+=4
		spd4=False
	if score>50 and spd5==True:
		vel1+=2
		vel2+=4
		spd5=False
	if score>70 and spd6==True:
		vel1+=2
		vel2+=4
		spd6=False
	if score>80 and spd7==True:
		vel1+=2
		vel2+=4
		spd7=False
	
	
	
	txt=font.render('score:'+str(floor(pt))+' CT:'+str(score) +' record:'+str(hiscore),True,(0,255,0))
	if gameover==False:	
		if pause==False:
	
		
			if score>60:
				pt+=1
			elif score>40:
				pt+=0.5
			elif score>30:
				pt+=0.4
			elif score>20:
				pt+=0.3
			elif score>10:
				pt+=0.2
			elif score>-1:
				pt+=0.1
		
		
		
		
		
		
	ds.blit(txt,(0,0))
	
	
	pygame.draw.rect(ds,(0,0,0),(0,1220,100,60))
	txt=font.render('exit',True,(255,255,255))
	ds.blit(txt,(0,1220))
	txt=font.render('Reset',True,(255,255,255))
	ds.blit(txt,(35,1060))
	
	pygame.display.update()
	clock.tick(fps)