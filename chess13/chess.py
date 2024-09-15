import pygame
import sys
from random import randint
from board import *
from possible import possibleblack

pygame.init()
pygame.font.init()
pygame.mixer.init()

# loading sounds
move_sound = pygame.mixer.Sound('move-self.mp3')

#constants
WIDTH , HIEGHT = 600 , 600
FPS = 24

#display setup
screen = pygame.display.set_mode((WIDTH ,HIEGHT))
pygame.display.set_caption("CHESS")
screen.fill((121,149,132))
#clock setup 
clock = pygame.time.Clock()

def check_checkmate(board):
    pass

def check_for_win(board,moust):
    pieces = [[x,y] for x in range(8) for y in range(8) if board.game[x][y][0] != 0]
    black = [0,0]
    white = [0,0]
    for piece in pieces:
        x1,y1 = piece
        if board.game[x1][y1][0] == p.king and board.game[x1][y1][1] == p.black: 
            black = piece
        if board.game[x1][y1][0] == p.king and board.game[x1][y1][1] == p.white: 
            white = piece
            
    for piece in pieces:
        x1,y1 = piece
        if board.game[x1][y1][1] == p.white and black in validmoves(x1,y1,board):
            x , y = black
            if path_is_clear(x1,y1,x,y,board):
                pygame.draw.rect(screen, (249,66,58), (y*75, x*75 , 75, 75))
                return [True , black , white]
        if board.game[x1][y1][1] == p.black and white in validmoves(x1,y1,board):
            x , y = white
            if path_is_clear(x1,y1,x,y,board):
                pygame.draw.rect(screen, (249,66,58), (y*75, x*75 , 75, 75))
                return [True , black , white]
    return [False]
#Draw Board
def board_display():
    for x in range(8):
        for y in range(8):
            if x == y == 0 or (x+y)%2 == 0: 
                pygame.draw.rect(screen, (255,253,208), (x*75, y*75 , 75, 75))
            else:
                pygame.draw.rect(screen, (121,149,132), (x*75, y*75 , 75, 75))

def highlight_moves(x,y,valid_moves):
    try:
        pygame.draw.rect(screen, (200,150,55), (x * 75, y * 75, 75, 75))
        for move in valid_moves:
            if (move[1] + move[0])%2 == 0:
                pygame.draw.rect(screen, (255*0.7,255*0.7,180*0.7), (move[1] * 75, move[0] * 75, 75, 75))
            else:    
                pygame.draw.rect(screen, (121*0.7,149*0.7,132*0.7), (move[1] * 75, move[0] * 75, 75, 75))
    except (ValueError,TypeError):
        pass
    

#sprites

blackp = pygame.image.load("blackp.png")
whitep = pygame.image.load("whitep.png")
rookb = pygame.image.load("rookb.png")
rookw = pygame.image.load("rookw.png")
knightw = pygame.image.load("knightw.png")
knightb = pygame.image.load("knightb.png")
bishopb = pygame.image.load("bishopb.png")
bishopw = pygame.image.load("bishopw.png")
kingb = pygame.image.load("kingb.png")
kingw = pygame.image.load("kingw.png")
queenb = pygame.image.load("queenb.png")
queenw = pygame.image.load("queenw.png")
options = pygame.image.load("options.png")


#game setup
m = []
bord = board(m)
bord.start()
peec = piece()

mous_pos = pygame.mouse.get_pos()
moust = 1

first_move = True

while True:
    check_checkmate(board)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if moust == 1:
                mous_pos = pygame.mouse.get_pos()
                moust *= -1 
            elif moust == -1:
                x , y = mous_pos
                x2,y2 = pygame.mouse.get_pos()
                x2 = int(x2/75)
                y2 = int (y2/75)
                x = int(x/75)
                y = int(y/75)
                z = bord
                e = bord.move(y,x,y2,x2,z,check_for_win(bord,moust),True)
                pygame.mixer.Sound.play(move_sound)
                for i in range(8):
                    if bord.game[0][i][0] == p.pawn and bord.game[0][i][1] == p.white:
                        while True:
                            mool = False
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    pygame.quit()
                                    sys.exit()
                                if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_1:
                                            bord.game[0][i] = [p.queen,p.white]
                                            mool = True
                                            break
                                    if event.key == pygame.K_2:
                                            bord.game[0][i] = [p.bishop,p.white]
                                            mool = True
                                            break
                                    if event.key == pygame.K_3:
                                            bord.game[0][i] = [p.knight,p.white]
                                            mool = True
                                            break
                                    if event.key == pygame.K_4:
                                            bord.game[0][i] = [p.rook,p.white]
                                            mool = True
                                            break
                            if mool == True:
                                break
                            screen.blit(options , (0,0))
                            pygame.display.update()
                            clock.tick(FPS)
                              
                moust *= -1
                if e != 0:
                    possibleblack(bord, check_for_win(bord,moust) )
                    pygame.mixer.Sound.play(move_sound)
                    for i in range(8):
                        if bord.game[7][i][0] == p.pawn and bord.game[7][i][1] == p.black:
                            bord.game[7][i] = [p.queen,p.black]

                
     
    
    board_display()
    x , y = mous_pos
    x = int(x/75)
    y = int(y/75)
    if moust == -1:
        highlight_moves(x,y,validmoves(y,x,bord)) 
    check_for_win(bord,moust) 
    for x in range(8):
        for y in range(8):
            piec = bord.game[x][y][0]
            color = bord.game[x][y][1]
            if piec == peec.pawn and  color == peec.black:
                screen.blit(blackp , (y*75,x*75))
            elif piec == peec.pawn and color == peec.white:
                screen.blit(whitep , (y*75,x*75))
            elif piec == peec.rook and color == peec.black:
                screen.blit(rookb , (y*75,x*75))  
            elif piec == peec.rook and color == peec.white:
                screen.blit(rookw , (y*75,x*75)) 
            elif piec == peec.knight and color == peec.white:
                screen.blit(knightw , (y*75,x*75))
            elif piec == peec.knight and color == peec.black:
                screen.blit(knightb , (y*75,x*75))
            elif piec == peec.bishop and color == peec.black:
                screen.blit(bishopb , (y*75,x*75))
            elif piec == peec.bishop and color == peec.white:
                screen.blit(bishopw , (y*75,x*75))
            elif piec == peec.king and color == peec.black:
                screen.blit(kingb , (y*75,x*75))
            elif piec == peec.king and color == peec.white:
                screen.blit(kingw , (y*75,x*75))
            elif piec == peec.queen and color == peec.black:
                screen.blit(queenb , (y*75 , x*75 ))
            elif piec == peec.queen and color == peec.white:
                screen.blit(queenw , (y*75 , x*75 ))
    
    pygame.display.update()

    clock.tick(FPS)