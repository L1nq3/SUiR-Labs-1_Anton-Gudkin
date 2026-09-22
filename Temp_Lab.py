RED = '\u001b[41m'
GREEN = '\u001b[42m'
YELLOW = '\u001b[43m'
BLUE = '\u001b[44m'
PURPLE = '\u001b[45m'
CIAN = '\u001b[46m'
RESET = '\u001b[0m'
WHITE = '\u001b[47m'

import time
import sys
import os
import math

def Benin():
    pixel = ' '
    height = 10
    for i in range(height):
        print(GREEN + pixel*6, end=' ') #зеленая полоса 
        if height//2 > i:
            print(YELLOW + pixel*20 + RESET) #желтая полоса первую половину
        else:
            print(RED + pixel*20 + RESET) #красная полоса вторую половину

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

def Frame_vanila():
    pixel = ' '
    offset = 6
    print(WHITE + offset*pixel + GREEN + 9*pixel + WHITE + offset*pixel + RESET)
    for i in range(1, 3):
        print(WHITE + (offset - i)*pixel + GREEN + 2*pixel + WHITE + (5 + 2*i)*pixel + GREEN + 2*pixel + WHITE + (offset-i)*pixel + RESET)
    for _ in range(3):
        print(WHITE + (offset-2)*pixel + GREEN + 2*pixel + WHITE + 9*pixel + GREEN + 2*pixel + WHITE + (offset-i)*pixel + RESET)
    for i in range(2, 0, -1):
        print(WHITE + (offset - i)*pixel + GREEN + 2*pixel + WHITE + (5 + 2*i)*pixel + GREEN + 2*pixel + WHITE + (offset-i)*pixel + RESET)
    print(WHITE + offset*pixel + GREEN + 9*pixel + WHITE + offset*pixel + RESET)
    for _ in range(2):
        print(WHITE + (offset + 4)*pixel + GREEN + pixel + WHITE + (offset+4)*pixel + RESET)
    print(WHITE + (offset)*pixel + GREEN + pixel*9 + WHITE + (offset)*pixel + RESET)

def Frame_1():
    pixel = ' '
    offset = 6
    print(RESET + offset*pixel + GREEN + 9*pixel + RESET + offset*pixel)
    for i in range(1, 3):
        print((offset - i)*pixel + GREEN + 2*pixel + RESET + (pixel*(2+i) + RED + pixel + RESET + pixel*(2+i)) + GREEN + 2*pixel + RESET + (offset-i)*pixel)
    for n in range(3):
        if n < 1:
            print((offset-2)*pixel + GREEN + 2*pixel + RESET + (pixel*4 + RED + pixel + RESET + pixel*4) + GREEN + 2*pixel + RESET + (offset-2)*pixel)
        elif n == 1:
            print((offset-2)*pixel + GREEN + 2*pixel + RESET + (CIAN + pixel*4 + BLUE + pixel + CIAN + pixel*4) + GREEN + 2*pixel + RESET + (offset-2)*pixel)
        else:
            print((offset-2)*pixel + GREEN + 2*pixel + RESET + (pixel*4 + RED + pixel + RESET + pixel*4) + GREEN + 2*pixel + RESET + (offset-2)*pixel)
    for i in range(2, 0, -1):
        print((offset - i)*pixel + GREEN + 2*pixel + RESET + (pixel*(2+i) + RED + pixel + RESET + pixel*(2+i)) + GREEN + 2*pixel + RESET + (offset-i)*pixel)
    print(offset*pixel + GREEN + 9*pixel + RESET + offset*pixel)
    for _ in range(2):
        print((offset + 4)*pixel + GREEN + pixel + RESET + (offset+4)*pixel)
    print((offset)*pixel + GREEN + pixel*9 + RESET + (offset)*pixel)

def Frame_2():
    pixel = ' '
    offset = 6
    print(RESET + offset*pixel + GREEN + 9*pixel + RESET + offset*pixel)
    for i in range(1, 3):
        print((offset - i)*pixel + GREEN + 2*pixel + RESET + 2*(i-1)*pixel + CIAN + pixel + RESET + pixel*(7-2*i) + RED + pixel + RESET + 2*(i-1)*pixel + GREEN + 2*pixel + RESET + (offset-i)*pixel)
    for n in range(3):
        if n < 1:
            print((offset-2)*pixel + GREEN + 2*pixel + RESET + (pixel*3 + CIAN + pixel + RESET + pixel + RED + pixel + RESET + pixel*3) + GREEN + 2*pixel + RESET + (offset-2)*pixel)
        elif n == 1:
            print((offset-2)*pixel + GREEN + 2*pixel + RESET + (pixel*4 + BLUE + pixel + RESET + pixel*4) + GREEN + 2*pixel + RESET + (offset-2)*pixel)
        else:
            print((offset-2)*pixel + GREEN + 2*pixel + RESET + (pixel*3 + RED + pixel + RESET + pixel + CIAN + pixel + RESET + pixel*3) + GREEN + 2*pixel + RESET + (offset-2)*pixel)
    for i in range(2, 0, -1):
        print((offset - i)*pixel + GREEN + 2*pixel + RESET + 2*(i-1)*pixel + RED + pixel + RESET + pixel*(7-2*i) + CIAN + pixel + RESET + 2*(i-1)*pixel +  GREEN + 2*pixel + RESET + (offset-i)*pixel)
    print(offset*pixel + GREEN + 9*pixel + RESET + offset*pixel)
    for _ in range(2):
        print((offset + 4)*pixel + GREEN + pixel + RESET + (offset+4)*pixel)
    print((offset)*pixel + GREEN + pixel*9 + RESET + (offset)*pixel)

def Frame_3():
    pixel = ' '
    offset = 6
    print(RESET + offset*pixel + GREEN + 9*pixel + RESET + offset*pixel)
    for i in range(1, 3):
        print((offset - i)*pixel + GREEN + 2*pixel + RESET + (pixel*(2+i) + CIAN + pixel + RESET + pixel*(2+i)) + GREEN + 2*pixel + RESET + (offset-i)*pixel)
    for n in range(3):
        if n < 1:
            print((offset-2)*pixel + GREEN + 2*pixel + RESET + (pixel*4 + CIAN + pixel + RESET + pixel*4) + GREEN + 2*pixel + RESET + (offset-2)*pixel)
        elif n == 1:
            print((offset-2)*pixel + GREEN + 2*pixel + RESET + (RED + pixel*4 + BLUE + pixel + RED + pixel*4) + GREEN + 2*pixel + RESET + (offset-2)*pixel)
        else:
            print((offset-2)*pixel + GREEN + 2*pixel + RESET + (pixel*4 + CIAN + pixel + RESET + pixel*4) + GREEN + 2*pixel + RESET + (offset-2)*pixel)
    for i in range(2, 0, -1):
        print((offset - i)*pixel + GREEN + 2*pixel + RESET + (pixel*(2+i) + CIAN + pixel + RESET + pixel*(2+i)) + GREEN + 2*pixel + RESET + (offset-i)*pixel)
    print(offset*pixel + GREEN + 9*pixel + RESET + offset*pixel)
    for _ in range(2):
        print((offset + 4)*pixel + GREEN + pixel + RESET + (offset+4)*pixel)
    print((offset)*pixel + GREEN + pixel*9 + RESET + (offset)*pixel)

def Frame_4():
    pixel = ' '
    offset = 6
    print(RESET + offset*pixel + GREEN + 9*pixel + RESET + offset*pixel)
    for i in range(1, 3):
        print((offset - i)*pixel + GREEN + 2*pixel + RESET + 2*(i-1)*pixel + RED + pixel + RESET + pixel*(7-2*i) + CIAN + pixel + RESET + 2*(i-1)*pixel + GREEN + 2*pixel + RESET + (offset-i)*pixel)
    for n in range(3):
        if n < 1:
            print((offset-2)*pixel + GREEN + 2*pixel + RESET + (pixel*3 + RED + pixel + RESET + pixel + CIAN + pixel + RESET + pixel*3) + GREEN + 2*pixel + RESET + (offset-2)*pixel)
        elif n == 1:
            print((offset-2)*pixel + GREEN + 2*pixel + RESET + (pixel*4 + BLUE + pixel + RESET + pixel*4) + GREEN + 2*pixel + RESET + (offset-2)*pixel)
        else:
            print((offset-2)*pixel + GREEN + 2*pixel + RESET + (pixel*3 + CIAN + pixel + RESET + pixel + RED + pixel + RESET + pixel*3) + GREEN + 2*pixel + RESET + (offset-2)*pixel)
    for i in range(2, 0, -1):
        print((offset - i)*pixel + GREEN + 2*pixel + RESET + 2*(i-1)*pixel + CIAN + pixel + RESET + pixel*(7-2*i) + RED + pixel + RESET + 2*(i-1)*pixel +  GREEN + 2*pixel + RESET + (offset-i)*pixel)
    print(offset*pixel + GREEN + 9*pixel + RESET + offset*pixel)
    for _ in range(2):
        print((offset + 4)*pixel + GREEN + pixel + RESET + (offset+4)*pixel)
    print((offset)*pixel + GREEN + pixel*9 + RESET + (offset)*pixel)

def animation():
    while True:
        Frame_1() 
        time.sleep(0.5)
        os.system("clear")
        Frame_2() 
        time.sleep(0.5)
        os.system("clear")
        Frame_3() 
        time.sleep(0.5)
        os.system("clear")
        Frame_4() 
        time.sleep(0.5)
        os.system("clear")
# Benin()

# n = int(input('color number: '))
# Picture(n) # можно указать цвет

animation()

# Frame_1()
# Frame_2()
# Frame_3()
# Frame_4()

# graphics()