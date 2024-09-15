class piece():
    def __init__(self):
        self.none = 0
        self.pawn = 1
        self.bishop = 2
        self.knight = 3
        self.rook = 4
        self.queen = 5
        self.king = 6
        self.white = 8
        self.black = 16
        
global white_virgin
white_virgin = True
global black_virgin
black_virgin = True

global rook1
rook1 = True
global rook2
rook2 = True
global rook3
rook3 = True
global rook4
rook4 = True
        
def check_for_check(board,moust):
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
        if board.game[x1][y1][1] == p.black  and white in validmoves(x1,y1,board):
            x , y = white
            if path_is_clear(x1,y1,x,y,board):
                return [True , black , white]
    return [False]
        
p = piece()
def path_is_clear(x1,y1,x2,y2,board):
    path = True
    peece1 = board.game[x1][y1][0]
    color1 = board.game[x1][y1][1]
    color2 = board.game[x2][y2][1]
    if color1 == color2:
        return False
    
    if peece1 == p.pawn and y2-y1 != 0 and board.game[x2][y2] == [0,0] and color1 != color2:
        return False
    if peece1 == p.pawn and board.game[x2][y2] != [0,0] and y2-y1 == 0:
        return False
    if peece1 == p.pawn and (x1 == x2 + 2 or x1 == x2-2):
        if x2 == x1+2:
             if board.game[x1+1][y1] != [0,0]:
                 return False
             
        if x2 == x1-2:
             if board.game[x1-1][y1] != [0,0]:
                 return False
             
    if peece1 == p.bishop:
        xdif = abs(x1-x2)
        ydif = abs(y1-y2)
        x_dir = 1 if x1 < x2 else -1
        y_dir = 1 if y1 < y2 else -1

        # Check each square in the diagonal path
        for i in range(1, xdif):
            x_check = x1 + i * x_dir
            y_check = y1 + i * y_dir

            # Check if there is a piece in the diagonal path
            if board.game[x_check][y_check] != [0,0]:
                return False
    if peece1 == p.rook:
        xdif = abs(x1-x2)
        ydif = abs(y1-y2)
        # Determine the direction of movement
        x_dir = 1 if x1 < x2 else -1 if x1 > x2 else 0
        y_dir = 1 if y1 < y2 else -1 if y1 > y2 else 0

        # Check each square in the path
        for i in range(1, max(abs(x2 - x1), abs(y2 - y1))):
            x_check = x1 + i * x_dir
            y_check = y1 + i * y_dir

            # Check if there is a piece in the path
            if board.game[x_check][y_check] != [0,0]:
                return False
    if peece1 == p.queen:
        xdif = abs(x1-x2)
        ydif = abs(y1-y2)
        # Determine the direction of movement
        x_dir = 1 if x1 < x2 else -1 if x1 > x2 else 0
        y_dir = 1 if y1 < y2 else -1 if y1 > y2 else 0

        # Check each square in the path
        for i in range(1, max(abs(x2 - x1), abs(y2 - y1))):
            x_check = x1 + i * x_dir
            y_check = y1 + i * y_dir

            # Check if there is a piece in the path
            if board.game[x_check][y_check] != [0,0]:
                return False

        # Check each square in the diagonal path
        for i in range(1, xdif):
            x_check = x1 + i * x_dir
            y_check = y1 + i * y_dir

            # Check if there is a piece in the diagonal path
            if board.game[x_check][y_check] != [0,0]:
                return False
        
        
    return path
def validmoves(x,y,board):
        peece = board.game[x][y][0]
        color = board.game[x][y][1]
        try:
            if  peece == p.pawn and color == p.white:
                valid_moves = [[x-1,y]] + [[x-1,y+1]] +[[x-1,y-1]]
                if x == 6:
                    valid_moves += [[x-2,y]]
            elif peece == p.pawn and color == p.black:
                valid_moves = [[x+1,y]] + [[x+1,y+1]] +[[x+1,y-1]]
                if x == 1:
                    valid_moves += [[x+2,y]]
            elif peece == p.bishop:
                valid_moves = [[x+n,y+n] for n in range(-8,8) ] + [ [x+n,y-n] for n in range(-8,8)]
                while([x,y] in valid_moves):
                    valid_moves.remove([x,y])      
            elif peece == p.rook:
                valid_moves = [[x+n , y] for n in range (-8,8)] + [ [x,y+n] for n in range(-8,8)]
            elif peece == p.knight:
                valid_moves = [[x+2,y-1],[x+2,y+1],[x-2,y+1],[x-2,y-1],[x-1,y+2],[x+1,y+2],[x+1,y-2],[x-1,y-2]]
            elif peece == p.queen:
                valid_moves = [[x+n,y+n] for n in range(-8,8) ] + [ [x+n,y-n] for n in range(-8,8)] + [[x+n , y] for n in range (-8,8)] + [ [x,y+n] for n in range(-8,8)]
                while([x,y] in valid_moves):
                    valid_moves.remove([x,y]) 
            elif peece == p.king:
                valid_moves = [[x+1,y+1],[x-1,y-1],[x+1,y],[x-1,y],[x,y+1],[x,y-1],[x+1,y-1],[x-1,y+1]]
                if white_virgin == True:
                        if color == p.white:
                            valid_moves += [[7,2],[7,6]]
                if black_virgin == True:
                    if color == p.black:
                        valid_moves += [[0,2],[0,6]]
            return valid_moves
        except (UnboundLocalError):
            return 0     
#BOARD
class board():
    def __init__(self, n):
        self.game = n
        
    def reset(self):
        for i in range(8) :
            temp = []
            for _ in range(8):
                temp.append([0,0])
            self.game.append(temp)
            
    def __str__(self):
        return str(self.game)
    
    def move(self , x1 , y1,x2,y2,board,check,original):
        #if (self.game[x1][y1][1] == p.black):
        #   return 0
        global rook1
        global rook2
        global rook3
        global rook4
        if (self.game[x1][y1]) != [0,0]:
            if validmoves(x1,y1,board) != 0:
                if [x2,y2] in validmoves(x1,y1,board):    
                            if x1 > -1 and y1 > -1 and  x2 > -1 and y2 > -1 and x2 < 8 and y2 < 8: 
                                    if path_is_clear(x1 , y1,x2,y2,board):
                                        x3 = x2
                                        y3 = y2
                                        x4 = x1
                                        y4 = y1
                                        tempboard = board.copy_board()
                                        tempboard.game[x2][y2] = tempboard.game[x1][y1]  
                                        tempboard.game[x1][y1] = [0,0]
                                        if not check_for_check(tempboard,-1)[0] or check == 8:
                                            if self.game[x1][y1][0] == p.king:
                                                if self.game[x1][y1][1] == p.white:
                                                    pieces_black = [[x,y] for x in range(8) for y in range(8) if board.game[x][y][1] == p.black]
                                                    pieces_white = [[x,y] for x in range(8) for y in range(8) if board.game[x][y][1] == p.white]
                                                    if [x2,y2] == [7,6]:
                                                        if self.game[7][7][0] != p.rook or self.game[7][7][1] != p.white:
                                                            return 0
                                                        if self.game[7][5] != [0,0]:
                                                            return 0
                                                        if check_for_check(board,-1)[0]:
                                                            return 0
                                                        if not rook4:
                                                            return 0
                                                        for piece in pieces_black:
                                                            x1,y1 = piece
                                                            if [7,5] in validmoves(x1,y1,board):
                                                                x , y = [7,5]
                                                                if path_is_clear(x1,y1,x,y,board):
                                                                    return 0
                                                        self.game[7][5] = self.game[7][7]
                                                        self.game[7][7] = [0,0]
                                                        global white_virgin
                                                        if original == True:
                                                            white_virgin = False
                                                    elif [x2,y2] == [7,2]:
                                                        if self.game[7][0][0] != p.rook or self.game[7][2][1] != p.white:
                                                            return 0
                                                        if self.game[7][1] != [0,0]:
                                                            return 0
                                                        if self.game[7][3] != [0,0]:
                                                            return 0
                                                        if check_for_check(board,-1)[0]:
                                                            return 0
                                                        if not rook3:
                                                            return 0
                                                        for piece in pieces_black:
                                                            x1,y1 = piece
                                                            if board.game[x1][y1][1] == p.black  and ([7,1] in validmoves(x1,y1,board) or [7,3] in validmoves(x1,y1,board)):
                                                                x , y = [7,1]
                                                                if path_is_clear(x1,y1,x,y,board):
                                                                    return 0
                                                                x,y = [7,3]
                                                                if path_is_clear(x1,y1,x,y,board):
                                                                    return 0
                                                        self.game[7][3] = self.game[7][0]
                                                        self.game[7][0] = [0,0]
                                                        if original == True:
                                                            white_virgin = False
                                                if self.game[x1][y1][1] == p.black :
                                                    pieces_black = [[x,y] for x in range(8) for y in range(8) if board.game[x][y][1] == p.black]
                                                    pieces_white = [[x,y] for x in range(8) for y in range(8) if board.game[x][y][1] == p.white]
                                                    if [x2,y2] == [0,6]:
                                                        if self.game[0][7][0] != p.rook or self.game[0][7][1] != p.black:
                                                            return 0
                                                        if self.game[0][5] != [0,0]:
                                                            return 0
                                                        if not rook2:
                                                            return 0
                                                        for piece in pieces_white:
                                                            x1,y1 = piece
                                                            if [0,5] in validmoves(x1,y1,board):
                                                                x , y = [0,5]
                                                                if path_is_clear(x1,y1,x,y,board):
                                                                    return 0
                                                        self.game[0][5] = self.game[0][7]
                                                        self.game[0][7] = [0,0]
                                                        global black_virgin
                                                        if original:
                                                            black_virgin = False
                                                    elif [x2,y2] == [0,2]:
                                                        if self.game[0][0][0] != p.rook or self.game[0][2][1] != p.black:
                                                            return 0
                                                        if not rook1:
                                                            return 0
                                                        if self.game[0][1] != [0,0]:
                                                            return 0
                                                        if self.game[0][3] != [0,0]:
                                                            return 0
                                                        for piece in pieces_white:
                                                            x1,y1 = piece
                                                            if board.game[x1][y1][1] == p.white  and ([0,1] in validmoves(x1,y1,board) or [0,3] in validmoves(x1,y1,board)):
                                                                x , y = [0,1]
                                                                if path_is_clear(x1,y1,x,y,board):
                                                                    return 0
                                                                x,y = [0,3]
                                                                if path_is_clear(x1,y1,x,y,board):
                                                                    return 0
                                                        self.game[0][3] = self.game[0][0]
                                                        self.game[0][0] = [0,0]
                                                        if original:
                                                            black_virgin = False
                                            if original == True:
                                                if [x4,y4] == [0,0]:
                                                    rook1 = False
                                                if [x4,y4] == [0,7]:
                                                    rook2 = False
                                                if [x4,y4] == [7,0]:
                                                    rook3 = False
                                                if [x4,y4] == [7,7]:
                                                    rook4 = False
                                            self.game[x3][y3] = self.game[x4][y4]  
                                            self.game[x4][y4] = [0,0]
                                        else:
                                            return 0
                                    else:
                                        return 0
                            else:
                                return 0
                else:
                    return 0
            else:
                return 0
        else:
            return 0

    
    def start(self):
        self.reset()
        self.game[0] = [[i,16] for i in [4,3,2,5,6,2,3,4]]
        self.game[1] = [[1,16] for _ in range(8)]
        self.game[6] = [[1,8] for _ in range(8)]
        self.game[7] = [[i,8] for i in [4,3,2,5,6,2,3,4]]
        
    def copy_board(self):
        new_board = board([])
        new_board.game = [row[:] for row in self.game]
        return new_board
        

        