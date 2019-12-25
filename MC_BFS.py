'''Code for breadth first search for solution of 3 missionaries and 3 cannibals problem by 
Tohfa Niraula(23) and Anish Paudel(28)'''


import pygame
from math import pi

#logic parts
#-----------------------------------------------------------------------------------
from collections import deque 

#Defining conditional states
A = {'M':3, 'C':3, 'B':0}
MC = {'M':0, 'C':0, 'B':0}
CC = {'M':0, 'C':0, 'B':0}
MM = {'M':0, 'C':0, 'B':0}
C = {'M':0, 'C':0, 'B':0}
M = {'M':0, 'C':0, 'B':0}

#Writing all possible states
stack = ({'M':3, 'C':3, 'B':0}, {'M':3, 'C':2, 'B':0}, {'M':3, 'C':1, 'B':0}, 
         {'M':3, 'C':3, 'B':1}, {'M':3, 'C':2, 'B':1}, {'M':3, 'C':1, 'B':1}, 
         {'M':3, 'C':0, 'B':0}, {'M':2, 'C':2, 'B':0}, {'M':1, 'C':1, 'B':0},
         {'M':3, 'C':0, 'B':1}, {'M':2, 'C':2, 'B':1}, {'M':1, 'C':1, 'B':1}, 
         {'M':0, 'C':3, 'B':0}, {'M':0, 'C':2, 'B':0}, {'M':0, 'C':3, 'B':1}, 
         {'M':0, 'C':2, 'B':1}, {'M':0, 'C':1, 'B':0}, {'M':1, 'C':1, 'B':0}, 
         {'M':0, 'C':0, 'B':1}, {'M':0, 'C':1, 'B':1}, {'M':1, 'C':1, 'B':1})


#Checking if the state is possible
def check(P):  
    y = False
    for i in range (0, 20):
        if (P == stack[i]):
            y = True
    if (y):
        return True
    else:
        return False
    
#checking to see if the state have been repeated    
def repeat(Q):
    y = False
    for i in range (0, len(queue1)):
        if (Q == queue1[i]):
            y = True
    if (y):
        return True
    else:
        return False
        
    
queue = deque([A])
queue1 = deque([A])
NB = {'M':1, 'C':2, 'B':0}
queue1.append(NB)
A = queue.popleft()

#----------------------------------------------------
#Graphics parts
angle = pi
SIZE = 1500, 800
pygame.init()
screen = pygame.display.set_mode(SIZE)

#defininf color
white = (255, 255, 255)
black = (  0,   0,   0)
green = (0, 255, 0)
blue = (0, 0, 180)
red   = (255,   0,   0)

screen.fill((white))

#breaking down states in a printable form
m =str( A['M'])
c = str(A['C'])
b = str(A['B'])

arr= [m,c,b]
str1 = ''.join(arr)

x = 0
y = 100

#Drawing initial condition
pygame.draw.circle(screen,black,[y,200], 35, 2)
font_obj = pygame.font.Font('freesansbold.ttf', 20)
text_surface_obj = font_obj.render(str1, True, blue)
text_rect_obj = text_surface_obj.get_rect()
text_rect_obj.center = (y, 200)
screen.blit(text_surface_obj, text_rect_obj)

#Drawing text
font_obj = pygame.font.Font('freesansbold.ttf', 50)
text_surface_obj = font_obj.render('BFS:', True, red)
text_rect_obj = text_surface_obj.get_rect()
text_rect_obj.center = (200, 80)
screen.blit(text_surface_obj, text_rect_obj)


Y = 0
#pygame.display.flip()
#-------------------------------------------------------
clock = pygame.time.Clock()

def game_intro():

  intro = True

  while intro:
     for event in pygame.event.get():
         print(event)
         if event.type == pygame.QUIT:
             pygame.quit()
             quit()
             
#-----------------------------------------------------------------------------
#Logic Part: Checking all conditions             
while (A != {'M':0, 'C':0, 'B':1}):
    #when boat is on the left shore
    if (A['B'] == 0):
        # 1missionary and 1cannibal part
        if (A['M'] != 0 and A['C'] != 0):
            MC['M'] = A['M'] -1
            MC['C'] = A['C'] -1
            MC['B'] = 1
            if (check(MC)):
                if (repeat(MC)):
                    pass
                else:
                    queue.append(MC)
                    queue1.append(MC)
            else:
                pass
            
        #2Cannibals part
        if (A['C'] >= 2):
            CC['M'] = A['M']
            CC['C'] = A['C'] -2
            CC['B'] = 1
            if (check(CC)):
                if (repeat(CC)):
                    pass
                else:
                    queue.append(CC)
                    queue1.append(CC)
            else:
                pass
                
        #2Missionary part
        if (A['M'] >= 2):
            MM['M'] = A['M'] -2
            MM['C'] = A['C']
            MM['B'] = 1
            if (check(MM)):
                if (repeat(MM)):
                    pass
                else:
                    queue.append(MM)
                    queue1.append(MM)
            else:
                pass
                
        #1Cannibal part
        if (A['C'] >= 1):
            C['M'] = A['M']
            C['C'] = A['C'] -1
            C['B'] = 1
            if (check(C)):
                if (repeat(C)):
                    pass
                else:
                    queue.append(C)
                    queue1.append(C)
            else:
                pass
                
        #1Missionary part
        if (A['M'] >= 1):
            M['M'] = A['M'] -1
            M['C'] = A['C'] 
            M['B'] = 1
            if (check(M)):
                if (repeat(M)):
                    pass
                else:
                    queue.append(M)
                    queue1.append(M)
            else:
                pass
    #when boat is on the right shore            
    else:
        #1missionary and 1cannibal part part
        if (A['M'] != 3 and A['C'] != 3):
            MC['M'] = A['M'] +1
            MC['C'] = A['C'] +1
            MC['B'] = 0
            if (check(MC)):
                if (repeat(MC)):
                    pass
                else:
                    queue.append(MC)
                    queue1.append(MC)
            else:
                pass
            
        #2cannibals part
        if (A['C'] < 2):
            CC['M'] = A['M']
            CC['C'] = A['C'] +2
            CC['B'] = 0
            if (check(CC)):
                if (repeat(CC)):
                    pass
                else:
                    queue.append(CC)
                    queue1.append(CC)
            else:
                pass
               
        #2missionaries part
        if (A['M'] < 2):
            MM['M'] = A['M'] +2
            MM['C'] = A['C']
            MM['B'] = 0
            if (check(MM)):
                if (repeat(MM)):
                    pass
                else:
                    queue.append(MM)
                    queue1.append(MM)
            else:
                pass
               
        #1Cannibal part
        if (A['C'] <= 2):
            C['M'] = A['M']
            C['C'] = A['C'] +1
            C['B'] = 0
            if (check(C)):
                if (repeat(C)):
                    pass
                else:
                    queue.append(C)
                    queue1.append(C)
            else:
                pass
               
        #1Missionary part
        if (A['M'] <= 2):
            M['M'] = A['M'] +1
            M['C'] = A['C'] 
            M['B'] = 0
            if (check(C)):
                if (repeat(M)):
                    pass
                else:
                    queue.append(M)
                    queue1.append(M)
            else:
                pass
    #-------------------------------------------------------------------------------------------
    #bringing all states back to neutral         
    MC = {'M':0, 'C':0, 'B':0}
    CC = {'M':0, 'C':0, 'B':0}
    MM = {'M':0, 'C':0, 'B':0}
    C = {'M':0, 'C':0, 'B':0}
    M = {'M':0, 'C':0, 'B':0}
    
    #writing states in a printable form
    A = queue.popleft()
    m =str( A['M'])
    c = str(A['C'])
    b = str(A['B'])
    print(A)
    
    #Plotting nodes in the window
    x= x+200
    if (Y == A['B']):
        pygame.draw.line(screen,black,(y , x-90),(y-120 , 240),2)
        x = x - 50
    if (Y != A['B']):
        pygame.draw.line(screen,black,(y+40, 200),(y+80 , 200),2)
        y = y + 120
        Y = A['B']
        x = 200
    
    
    arr= [m,c,b]
    str1 = ''.join(arr)
    
    pygame.draw.circle(screen,(0,0,0),[y, x], 35, 2)
    font_obj = pygame.font.Font('freesansbold.ttf', 20)
    text_surface_obj = font_obj.render(str1, True, blue)
    text_rect_obj = text_surface_obj.get_rect()
    text_rect_obj.center = (y, x)
    screen.blit(text_surface_obj, text_rect_obj)
    pygame.display.flip()
   
    
words = 'Total no of visited nodes are: 15'
font_obj = pygame.font.Font('freesansbold.ttf', 40)
text_surface_obj = font_obj.render(words, True, green)
text_rect_obj = text_surface_obj.get_rect()
text_rect_obj.center = (700, 400)
screen.blit(text_surface_obj, text_rect_obj)

pygame.display.flip()
