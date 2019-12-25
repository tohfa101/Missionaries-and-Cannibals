'''Code for Depth first search for solution of 3 missionaries and 3 cannibals problem by 
Tohfa Niraula(23) and Anish Paudel(28)'''


import pygame
from math import pi

#logic parts
#-----------------------------------------------------------------------------------
A = {'M':3, 'C':3, 'B':0}
MC = {'M':0, 'C':0, 'B':0}
CC = {'M':0, 'C':0, 'B':0}
MM = {'M':0, 'C':0, 'B':0}
C = {'M':0, 'C':0, 'B':0}
M = {'M':0, 'C':0, 'B':0}

#Defining all possible conditions
Stack = ({'M':3, 'C':3, 'B':0}, {'M':3, 'C':2, 'B':0}, {'M':3, 'C':1, 'B':0}, 
         {'M':3, 'C':3, 'B':1}, {'M':3, 'C':2, 'B':1}, {'M':3, 'C':1, 'B':1}, 
         {'M':3, 'C':0, 'B':0}, {'M':2, 'C':2, 'B':0}, {'M':1, 'C':1, 'B':0},
         {'M':3, 'C':0, 'B':1}, {'M':2, 'C':2, 'B':1}, {'M':1, 'C':1, 'B':1}, 
         {'M':0, 'C':3, 'B':0}, {'M':0, 'C':2, 'B':0}, {'M':0, 'C':3, 'B':1}, 
         {'M':0, 'C':2, 'B':1}, {'M':0, 'C':1, 'B':0}, {'M':1, 'C':1, 'B':0}, 
         {'M':0, 'C':0, 'B':1}, {'M':0, 'C':1, 'B':1}, {'M':1, 'C':1, 'B':1})

#Checking if the state is acceptable
def check(P):  
    y = False
    for i in range (0, 20):
        if (P == Stack[i]):
            y = True
    if (y):
        return True
    else:
        return False

#Checking if the state has been previously encountered
def repeat(Q):
    y = False
    for i in range (0, len(stack1)):
        if (Q == stack1[i]):
            y = True
    if (y):
        return True
    else:
        return False
        
    
stack = [A]
stack1 = [A]
NB = {'M':1, 'C':2, 'B':0}
stack1.append(NB)

#-------------------------------------------
#Graphics parts

angle = pi
SIZE = 1500, 800
pygame.init()
screen = pygame.display.set_mode(SIZE)

#defining colors
white = (255, 255, 255)
black = (  0,   0,   0)
green = (0, 255, 0)
blue = (0, 0, 180)
red   = (255,   0,   0)

screen.fill((white))

#Writing states in printable form
m =str( A['M'])
c = str(A['C'])
b = str(A['B'])

arr= [m,c,b]
str1 = ''.join(arr)

x = 0
y = 100

#drawing initial state
pygame.draw.circle(screen,black,[y,200], 35, 2)
font_obj = pygame.font.Font('freesansbold.ttf', 20)
text_surface_obj = font_obj.render(str1, True, blue)
text_rect_obj = text_surface_obj.get_rect()
text_rect_obj.center = (y, 200)
screen.blit(text_surface_obj, text_rect_obj)

#drawing text
font_obj = pygame.font.Font('freesansbold.ttf', 50)
text_surface_obj = font_obj.render('DFS:', True, green)
text_rect_obj = text_surface_obj.get_rect()
text_rect_obj.center = (200, 80)
screen.blit(text_surface_obj, text_rect_obj)


Y = 0


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
             
#All condition logic
while (A != {'M':0, 'C':0, 'B':1}):
    #When boat is on left shore
    if (A['B'] == 0):
        # 1Missionary and 1 cannibal part
        if (A['M'] != 0 and A['C'] != 0):
            MC['M'] = A['M'] -1
            MC['C'] = A['C'] -1
            MC['B'] = 1
            if (check(MC)):
                if (repeat(MC)):
                    pass
                else:
                    stack.append(MC)
                    stack1.append(MC)
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
                    stack.append(CC)
                    stack1.append(CC)
            else:
                pass
                
        #2Missionary  part
        if (A['M'] >= 2):
            MM['M'] = A['M'] -2
            MM['C'] = A['C']
            MM['B'] = 1
            if (check(MM)):
                if (repeat(MM)):
                    pass
                else:
                    stack.append(MM)
                    stack1.append(MM)
            else:
                pass
                
        #1 Cannibal part
        if (A['C'] >= 1):
            C['M'] = A['M']
            C['C'] = A['C'] -1
            C['B'] = 1
            if (check(C)):
                if (repeat(C)):
                    pass
                else:
                    stack.append(C)
                    stack1.append(C)
            else:
                pass
                
        #1 Missionary part
        if (A['M'] >= 1):
            M['M'] = A['M'] -1
            M['C'] = A['C'] 
            M['B'] = 1
            if (check(M)):
                if (repeat(M)):
                    pass
                else:
                    stack.append(M)
                    stack1.append(M)
            else:
                pass
                
    else:
        #1Missionary and 1Cannibal part
        if (A['M'] != 3 and A['C'] != 3):
            MC['M'] = A['M'] +1
            MC['C'] = A['C'] +1
            MC['B'] = 0
            if (check(MC)):
                if (repeat(MC)):
                    pass
                else:
                    stack.append(MC)
                    stack1.append(MC)
            else:
                pass
            
        #2Cannibals part
        if (A['C'] < 2):
            CC['M'] = A['M']
            CC['C'] = A['C'] +2
            CC['B'] = 0
            if (check(CC)):
                if (repeat(CC)):
                    pass
                else:
                    stack.append(CC)
                    stack1.append(CC)
            else:
                pass
               
        #2Missionary part
        if (A['M'] < 2):
            MM['M'] = A['M'] +2
            MM['C'] = A['C']
            MM['B'] = 0
            if (check(MM)):
                if (repeat(MM)):
                    pass
                else:
                    stack.append(MM)
                    stack1.append(MM)
            else:
                pass
               
        #1 Cannibal part
        if (A['C'] <= 2):
            C['M'] = A['M']
            C['C'] = A['C'] +1
            C['B'] = 0
            if (check(C)):
                if (repeat(C)):
                    pass
                else:
                    stack.append(C)
                    stack1.append(C)
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
                    stack.append(M)
                    stack1.append(M)
            else:
                pass
    #bring all states back to neutral         
    MC = {'M':0, 'C':0, 'B':0}
    CC = {'M':0, 'C':0, 'B':0}
    MM = {'M':0, 'C':0, 'B':0}
    C = {'M':0, 'C':0, 'B':0}
    M = {'M':0, 'C':0, 'B':0}
    
    #writing states in printable form
    A = stack.pop()
    m =str( A['M'])
    c = str(A['C'])
    b = str(A['B'])
    print(A)
    
    #Plotting nodes in the window
    x= x+200
    if (Y == A['B']):
        x = 1000
    if (Y != A['B']):
        pygame.draw.line(screen,black,(y+40, 200),(y+80 , 200),2)
        y = y + 120
        Y = A['B']
        x = 200
    
    
    #-----------------------------------------------------------------------------
    arr= [m,c,b]
    str1 = ''.join(arr)
    pygame.draw.circle(screen,(0,0,0),[y, x], 35, 2)
    font_obj = pygame.font.Font('freesansbold.ttf', 20)
    text_surface_obj = font_obj.render(str1, True, blue)
    text_rect_obj = text_surface_obj.get_rect()
    text_rect_obj.center = (y, x)
    screen.blit(text_surface_obj, text_rect_obj)
    
    
#total = str(len(stack1))
words = 'Total no of visited nodes are: 12'
font_obj = pygame.font.Font('freesansbold.ttf', 40)
text_surface_obj = font_obj.render(words, True, red)
text_rect_obj = text_surface_obj.get_rect()
text_rect_obj.center = (700, 400)
screen.blit(text_surface_obj, text_rect_obj)

pygame.display.flip()

    
    
    
    
    
    
    
    
    