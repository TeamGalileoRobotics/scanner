import scanner
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
		x, y = scanner.get_x(), scanner.get_y()
		set(x, y, scanner.get_light())
		pygame.display.flip()

p = multiprocessing.Process(target=test, args=(), kwargs={})
p.start()

# ---------------------

print "%f / %f" % (scanner.get_x(), scanner.get_y())
scanner.move(10)
print "%f / %f" % (scanner.get_x(), scanner.get_y())
scanner.rotate(30)
print "%f / %f" % (scanner.get_x(), scanner.get_y())