import pygame

from ship import Player

pygame.init()  
SCREEN = pygame.display.set_mode((1280, 720))  
CLOCK = pygame.time.Clock()  
RUNNING = True  
FRAMERATE = 60


background_color = pygame.Color(19, 57, 135)

x = 640
y = 535
radius = 15
u, v = 0, 0
vel = 7

player = Player()
def coords_update(cx : int, cy : int, ax : int, ay : int) :
	"""
	update coordinates
	"""
	cx += ax
	cy += ay
	return cx, cy


def coords_valid_y(y : int, dec : int) -> bool :
	"""
	verifies if a coordinate is valid (meaning still in the window)
	"""
	if y-dec > 0 and y+dec < 720 :
		return True
	return False



def handle_event(ev: pygame.event.Event) -> None:
	"""
	Handle user inputs.
	"""
	if ev.type == pygame.QUIT:  
		global RUNNING  
		RUNNING = False 
	


while RUNNING:
	

	for event in pygame.event.get():  
		handle_event(event) 
	
	userInput = pygame.key.get_pressed()


	if userInput[pygame.K_LEFT] and x > 0+radius+vel:
		u, v = player.move(-1, 0, vel)
		x, y = coords_update(x, y, u, v)
	if userInput[pygame.K_RIGHT] and x < 1280-radius-vel:
		u, v = player.move(1, 0, vel)
		x, y = coords_update(x, y, u, v)
	if userInput[pygame.K_UP] and y > 0+radius+vel:
		u, v = player.move(0, -1, vel)
		x, y = coords_update(x, y, u, v)
	if userInput[pygame.K_DOWN] and y < 720-radius-vel:
		u, v = player.move(0, 1, vel)
		x, y = coords_update(x, y, u, v)
	print(x, y)


	pygame.Surface.fill(SCREEN, background_color)
	pygame.draw.circle(SCREEN, (255,255,255), (int(x), int(y)), radius)
	pygame.display.update()

	CLOCK.tick(FRAMERATE)

"""
To set coordinates boundaries 
0 < x < 1280     et  0 < y <720
PRBLM : cricle stuck on the sides
"""