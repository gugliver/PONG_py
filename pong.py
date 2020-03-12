import pygame
import random

pygame.init()

#constants
display_width = 1000
display_height = 800

pad_width = 16
pad_height = 140

border_h = 80

counter = 0
counter_1 = 0
counter_2 = 0

bouncity = 0.3

ball_pace = 10
pad_pace = 10
fps = 40

pos_ball = [display_width//2, display_height//2] #x, y
ball_rad = 10
dir_ball = [0, 0] #x, y

pad_1_pos_v = (display_height - pad_height)//2
pad_1_pos_h = border_h			#fixed
pad_1_pos_v_c = 0

pad_2_pos_v = (display_height - pad_height)//2
pad_2_pos_h = display_width - border_h - pad_width	#fixed
pad_2_pos_v_c = 0

wall_pos_v = 0
wall_pos_h = display_width - border_h - pad_width

gameDisplay = pygame.display.set_mode((display_width, display_height))
#, pygame.FULLSCREEN
pygame.display.set_caption('PONG')

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()


#define the pad's shape
pad = pygame.Surface((pad_width, pad_height)).convert_alpha()
pad.fill(white)

wall = pygame.Surface((pad_width, display_height)).convert_alpha()
wall.fill(white)

#pad_alt = pygame.draw.rect(gameDisplay, white, (0, 0, 20, 60))

#blit the pads over the background
def pad_1(x,y):
    gameDisplay.blit(pad, (x,y))

def pad_2(x,y):
    gameDisplay.blit(pad, (x,y))

def wally(x,y):
	gameDisplay.blit(wall, (x,y))

dir_ball = [random.randrange(-5,5), random.randrange(-5,5)]
if dir_ball[0] == 0:
	dir_ball[0] = 2

pygame.display.update()
pExit = False
ball_pace_i = ball_pace
while not pExit:
	#checks for exit status
	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			pExit = True

		#controls of pad_1
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				pad_1_pos_v_c = - pad_pace

			elif event.key == pygame.K_DOWN:
					pad_1_pos_v_c = pad_pace

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
				pad_1_pos_v_c = 0




	#limiting the range of pad_1
	if pad_1_pos_v < 0:
		pad_1_pos_v = 0
	elif pad_1_pos_v + pad_height > display_height:
		pad_1_pos_v = display_height - pad_height
	else:
		pad_1_pos_v += pad_1_pos_v_c
	

	if(pos_ball[0] > display_width - display_width//2):
			#limiting the range of pad_2
		if pad_2_pos_v < 0:
			pad_2_pos_v = 0
		elif pad_2_pos_v + pad_height > display_height:
			pad_2_pos_v = display_height - pad_height
		else:
			pad_2_pos_v = int(pad_2_pos_v + (pos_ball[1] - pad_2_pos_v - pad_height//2)*(pos_ball[0]/(5*display_width)))




	#movement of ball
	#vertical
	if (pos_ball[1] - ball_rad <= 0) and dir_ball[1] < 0:
		pos_ball[1] = ball_rad
		dir_ball[1] = ball_pace

	elif (pos_ball[1] + ball_rad >= display_height) and dir_ball[1] > 0:
		pos_ball[1] = display_height - ball_rad
		dir_ball[1] = - ball_pace

	#horizontal vs pad1
	#hit
	if ((pos_ball[0] - ball_rad <= border_h + ball_pace//2) and (pos_ball[0] - ball_rad >= border_h - ball_pace//2))  and (dir_ball[0] < 0) and ((pos_ball[1] >= pad_1_pos_v) and (pos_ball[1] <= pad_1_pos_v + pad_height)):
		pos_ball[0] = ball_rad + border_h
		dir_ball[0] = int(ball_pace - (bouncity*pad_1_pos_v_c))
		dir_ball[1] = int(dir_ball[1] + (bouncity*pad_1_pos_v_c))
		counter_1 += 1

	#point 2
	elif ((pos_ball[0] + ball_rad <= 0)  and (dir_ball[0] < 0)):
		pExit = True

	#horizontal vs pad2
	#hit
	elif ((pos_ball[0] - ball_rad <= display_width + ball_pace//2 - border_h - pad_width) and (pos_ball[0] - ball_rad >= display_width - border_h - pad_width - ball_pace//2) and (pos_ball[1] >= pad_2_pos_v) and (pos_ball[1] <= pad_2_pos_v + pad_height)):
		pos_ball[0] =  display_width - border_h - ball_rad
		dir_ball[0] = int(- ball_pace + (bouncity*pad_2_pos_v_c))
		dir_ball[1] = int(dir_ball[1] + (bouncity*pad_2_pos_v_c))
		counter_2 += 1

	#point 1
	elif ((pos_ball[0] + ball_rad >= display_width)  and (dir_ball[0] > 0)):
		pExit = True

	#horizontal vs wall
	#elif ((pos_ball[0] - ball_rad <= display_width + ball_pace//2 - border_h - pad_width) and (pos_ball[0] - ball_rad >= display_width - border_h - pad_width - ball_pace//2)) and (dir_ball[0] > 0):
	#	pos_ball[0] = display_width - ball_rad - border_h
	#	dir_ball[0] = - ball_pace



	#limiting the velocity of the ball
	if dir_ball[1] >= 2*ball_pace:
			dir_ball[1] = 2*ball_pace
	if dir_ball[1] <= -2*ball_pace:
			dir_ball[1] = -2*ball_pace


	#refresh

	#refresh velocity
	counter = counter_1 + counter_2
	ball_pace = ball_pace_i + (counter)//4

	#refresh position
	pos_ball[0] += dir_ball[0] 
	pos_ball[1] += dir_ball[1] 


	#refresh display
	gameDisplay.fill(black)
	pad_1(pad_1_pos_h,pad_1_pos_v)
	pad_2(pad_2_pos_h,pad_2_pos_v)
	#wally(wall_pos_h, wall_pos_v)
	pygame.draw.circle(gameDisplay, white, pos_ball, ball_rad)
	#pygame.display.update(pad_1(pad_1_pos_h,pad_1_pos_v))
	pygame.display.update()
	clock.tick(fps)

pygame.quit()
quit()



















