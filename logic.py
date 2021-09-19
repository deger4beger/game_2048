import random

def pprint(mas):
	print("-"*7)
	for i in mas:
		print(*i)
	print("-"*7)	

def get_number_from_index(i,j):
	return i*4 + j + 1

def get_index_from_number(num):
	num -= 1
	x, y = num//4, num%4
	return x, y	

def insert2or4(mas,x,y):
	if random.random()<=0.75:
		mas[x][y] = 2
	else:
		mas[x][y] = 4
	return mas		

def get_empty_list(mas):
	empty = []
	for i in range(4):
		for j in range(4):
			if mas[i][j] == 0:
				num = get_number_from_index(i,j)
				empty.append(num)
	return empty

def iszero(mas):
	for i in mas:
		if 0 in i:
			return True
	return False

def transpon(mas):
	return [[*col] for col in zip(*mas)]

def left(mas):
	rez = 0
	for row in mas:
		while 0 in row:
			row.remove(0)
		while len(row) != 4:
			row.append(0)
	for i in range(4):
		for j in range(3):
			if mas[i][j] == mas[i][j+1] and mas[i][j] != 0:
				mas[i][j] *= 2
				rez += mas[i][j]
				mas[i].pop(j+1)
				mas[i].append(0)
	return mas, rez	

def right(mas):
	rez = 0
	for row in mas:
		while 0 in row:
			row.remove(0)
		while len(row) != 4:
			row.insert(0, 0)
	for i in range(4):
		for j in range(3,0,-1):
			if mas[i][j] == mas[i][j-1] and mas[i][j] != 0:
				mas[i][j] *= 2
				rez += mas[i][j]
				mas[i].pop(j-1)
				mas[i].insert(0, 0)
	return mas, rez

def up(mas):
	rez = 0
	mas = [[*col] for col in zip(*mas)]
	for row in mas:
		while 0 in row:
			row.remove(0)
		while len(row) != 4:
			row.append(0)
	for i in range(4):
		for j in range(3):
			if mas[i][j] == mas[i][j+1] and mas[i][j] != 0:
				mas[i][j] *= 2
				rez += mas[i][j]
				mas[i].pop(j+1)
				mas[i].append(0)
	return [[*col] for col in zip(*mas)], rez

def down(mas):
	rez = 0
	mas = [[*col] for col in zip(*mas)]
	for row in mas:
		while 0 in row:
			row.remove(0)
		while len(row) != 4:
			row.insert(0, 0)
	for i in range(4):
		for j in range(3,0,-1):
			if mas[i][j] == mas[i][j-1] and mas[i][j] != 0:
				mas[i][j] *= 2
				rez += mas[i][j]
				mas[i].pop(j-1)
				mas[i].insert(0, 0)
	return [[*col] for col in zip(*mas)], rez

def can_move(mas):
	for i in range(3):
		for j in range(3):
			if mas[i][j] == mas[i][j+1] or mas[i][j] == mas [i+1][j]:
				return True
	return False
	
def can_move_extended(mas):
	for i in range(3):
		if mas[i][3] == mas[i+1][3] or mas[3][i] == mas[3][i+1]:
			return True
	return False								

