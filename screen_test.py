import pygame
import random
import multiprocessing

pygame.init()
size = width, height = 480, 480
black = 0, 0, 0
white = 255, 255, 255

screen = pygame.display.set_mode(size)

def val_to_col(val):
	val *= 255
	return val, val, val

def set(x, y, val):
	col = val_to_col(val)
	pygame.draw.line(screen, col, [x, y], [x, y])

def test():
	while 1:
		screen.fill(white)
		for y in range(0, height):
			for x in range(0, width):
				set(x, y, random.random())
		pygame.display.flip()

p = multiprocessing.Process(target=test, args=(), kwargs={})
p.start()