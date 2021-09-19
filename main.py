from logic import *
import pygame
import sys
from database import best, cur

gamers_db = best()

def best_gamers():
	font_top = pygame.font.SysFont("terminal", 30)
	font_gamer = pygame.font.SysFont("terminal", 24)
	text_head = font_top.render("Best tries: ", True, scorecolor)
	screen.blit(text_head, (250, 5))
	for index, gamer in enumerate(gamers_db):
		name, score = gamer
		s = f"{index + 1}. {name} - {score}"
		text_gamer = font_top.render(s, True, scorecolor)
		screen.blit(text_gamer, (250, 30 + 27 * index))
		

def draw_interface(score, rez = 0):
	pygame.draw.rect(screen, white, TITLE_REC)
	font = pygame.font.SysFont("terminal", 70)
	fontscore = pygame.font.SysFont("terminal", 48)
	fontrez = pygame.font.SysFont("terminal", 32)
	textscore = fontscore.render("Score: ", True, scorecolor)
	textscorevalue = fontscore.render(f"{score}", True, scorecolor)
	textrez = fontrez.render(f"+{rez}", True, scorecolor)
	screen.blit(textscore, (20, 35))
	screen.blit(textscorevalue, (145, 35))
	screen.blit(textrez, (136, 65))
	pprint(mas)
	best_gamers()
	for row in range(BLOCKS):
		for column in range(BLOCKS):
			value = mas[row][column]
			text = font.render(f"{value}", True, black)
			x = column*BLOCK_SIZE + (column + 1)*TUN
			y = row*BLOCK_SIZE + (row + 1)*TUN + BLOCK_SIZE
			pygame.draw.rect(screen, colors[value], (x,y,BLOCK_SIZE,BLOCK_SIZE))
			if value != 0:
				font_x, font_y = text.get_size()
				text_x = int(x + (BLOCK_SIZE - font_x) / 2)
				text_y = int(y + (BLOCK_SIZE - font_y) / 2)
				screen.blit(text, (text_x, text_y))

mas = [[0]*4 for i in range(4)]

colors = {
	0: (130,130,130),
	2: (255,255,255),
	4: (255,255,128),
	8: (255,255,0),
	16: (140,210,246),
	32: (255,24,45),
	64: (52,255,50),
	128: (251,25,158),
	256: (12,140,20),
	512: (20,20,75),
	1024: (87,26,190),
	2048: (14,14,17),
}

white = (255,255,255)
grey = (130,130,130)
black = (0,0,0)
scorecolor = (150,70,89)

BLOCKS = 4
BLOCK_SIZE = 110
TUN = 10
WIDTH = BLOCKS*BLOCK_SIZE + (BLOCKS + 1)*TUN
HEIGHT = WIDTH + BLOCK_SIZE
TITLE_REC = pygame.Rect(0,0, WIDTH, BLOCK_SIZE)
score = 0

mas[1][2] = 2 
mas[3][0] = 4
pprint(mas)
print(get_empty_list(mas))

 
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("влево вправо цифры")

draw_interface(score)
pygame.display.update()	
while iszero(mas) or can_move(mas) or can_move_extended(mas):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit(0)
		elif event.type == pygame.KEYDOWN:
			rez = 0
			if event.key == pygame.K_LEFT:
				mas, rez = left(mas)
			if event.key == pygame.K_RIGHT:
				mas, rez = right(mas)
			if event.key == pygame.K_UP:
				mas, rez = up(mas)
			if event.key == pygame.K_DOWN:
				mas, rez = down(mas)
			score += rez				
			empty = get_empty_list(mas)
			random.shuffle(empty)
			random_num = empty.pop()
			x, y = get_index_from_number(random_num)
			mas = insert2or4(mas, x, y)		
			draw_interface(score, rez)
			pygame.display.update()
			if iszero(mas) == False and can_move(mas) == False and can_move_extended(mas) == False:
				pygame.quit()
				sys.exit(0)			
	


