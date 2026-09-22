RED = '\u001b[41m'
GREEN = '\u001b[42m'
YELLOW = '\u001b[43m'
RESET = '\u001b[0m'
WHITE = '\u001b[47m'

import time
import sys
import os

def Benin():
    pixel = ' '
    height = 10
    for i in range(height):
        print(GREEN + pixel*6, end=' ')
        if height//2 > i:
            print(YELLOW + pixel*20 + RESET)
        else:
            print(RED + pixel*20 + RESET)

def Picture(n):
    COLOR = f'\u001b[{n}m'
    pixel = '  '
    axis = 8
    hight = 16
    sector = 8
    mid_sector = 6
    for i in range(hight):
        print(sector*pixel, end='')
        print(COLOR + pixel*(axis-sector) + RESET, end='')
        if mid_sector > 0:
            print(COLOR + pixel*(axis - sector) + RESET + pixel*mid_sector*2 + COLOR + pixel*(2*(axis - sector)) + RESET)
        else:
            print(COLOR + pixel*(axis+axis//2) + pixel*(axis-sector) + RESET)
        if i < hight//2:
            sector -= 1
            mid_sector -= 1
        else:
            sector += 1
            mid_sector += 1

def animation():
    colors = [41, 42, 43, 44] 
    while True:
        for i in range(4):
            Picture(colors[i])
            time.sleep(1)
            os.system("clear")

def file_state():
    file = open('sequence.txt')
    num_1 = 0
    num_2 = 0
    for i in file:
        if 5 >= float(i) >= 0:
            num_1 += 1
        elif -5 <= float(i) <= 0:
            num_2 += 1
    file.close()
    num_1, num_2 = ((num_1 / (num_1 + num_2))*100), ((num_2 / (num_1 + num_2))*100)
    print(f'{RED}{'  ' * int(num_1//5)} {RESET}{round(num_1,2)}%')
    print(f'{GREEN}{'  ' * int(num_2//5)} {RESET}{round(num_2,2)}%')

def graphics():
    hight = 9
    lenght = 9
    for y in range(hight):
        print(f'\t{hight-y}', end='   ')
        for x in range(1, lenght+1):
            if x == 1:
                add = '\t'
            else:
                add = ''
            if hight-y == x+1:
                print(add + GREEN + '  ' + RESET, end='')
            else:
                print(add + WHITE + '  ' + RESET, end='')
        print()
    print('\t0', end='')
    for x in range(1, lenght+1):
        if x == 1:
            add = '\t'
        else:
            add = ''
        print(add + str(x),end=' ')

# Benin()

n = int(input('color number: '))
Picture(n) # можно указать цвет

# animation()

# graphics()