from board import *
import random
import sys
import math
import copy

global move_count
move_count = 0

def check_checkmate(board):
    black_pieces = [[x,y] for x in range(8) for y in range(8) if board.game[x][y][1] == piece().black]
    for i in range(0,len(black_pieces)):
        
        piece_to_move = black_pieces[i]
        if not type(validmoves(piece_to_move[0],piece_to_move[1],board)) == int:
            for i in validmoves(piece_to_move[0],piece_to_move[1],board):
                if piece_to_move[0] > -1 and piece_to_move[1] > -1 and  i[0] > -1 and i[1] > -1 and i[0] < 8 and i[1] < 8:
                    if path_is_clear(piece_to_move[0] , piece_to_move[1] , i[0] ,i[1] ,board): 
                        # move implementation
                        tempboard = board.copy_board()
                        tempboard.game[i[0]][i[1]] = tempboard.game[piece_to_move[0]][piece_to_move[1]]
                        tempboard.game[piece_to_move[0]][piece_to_move[1]] = [0,0]
                        if not check_for_check(tempboard,-1)[0]:
                            return False
    return True
                

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
        if board.game[x1][y1][1] == p.black and white in validmoves(x1,y1,board):
            x , y = white
            if path_is_clear(x1,y1,x,y,board):
                return ["yes" , black , white]
        if board.game[x1][y1][1] == p.white and black in validmoves(x1,y1,board):
            x , y = black
            if path_is_clear(x1,y1,x,y,board):
                return ["no" , black , white]
    return [False]

def check_whitecheckmate(board):
    black_pieces = [[x,y] for x in range(8) for y in range(8) if board.game[x][y][1] == piece().white]
    for i in range(0,len(black_pieces)):
        
        piece_to_move = black_pieces[i]
        if not type(validmoves(piece_to_move[0],piece_to_move[1],board)) == int:
            for i in validmoves(piece_to_move[0],piece_to_move[1],board):
                if piece_to_move[0] > -1 and piece_to_move[1] > -1 and  i[0] > -1 and i[1] > -1 and i[0] < 8 and i[1] < 8:
                    if path_is_clear(piece_to_move[0] , piece_to_move[1] , i[0] ,i[1] ,board): 
                        # move implementation
                        tempboard = board.copy_board()
                        tempboard.game[i[0]][i[1]] = tempboard.game[piece_to_move[0]][piece_to_move[1]]
                        tempboard.game[piece_to_move[0]][piece_to_move[1]] = [0,0]
                        if not check_for_check(tempboard,-1)[0]:
                            return False
    return True

def possibleblack(boaard, check):
    global rook1
    global rook2
    global rook3
    global rook4
    
    if check_checkmate(boaard):
            if check_for_check(boaard,-1)[0] == "no":
                print("YOU WON")
                sys.exit(0)
            else:
                print("STALEMATE")
                sys.exit(0)
                # prefrences 
                

    black_pieces = [[x,y] for x in range(8) for y in range(8) if boaard.game[x][y][1] == p.black]
    
    all_possible_moves = dict()
    all_possible_moves = [[k,m] for k in black_pieces for m in validmoves(k[0],k[1],boaard)]
    all_possible_moves = sorted(all_possible_moves, key=lambda move: score_move(move, boaard), reverse=True)
    possible = []
    cool = True        
        # move check
    for move in all_possible_moves:
        piece_to_move = move[0]
        i = move[1]
        if not type(validmoves(piece_to_move[0],piece_to_move[1],boaard)) == int:      
            if piece_to_move[0] > -1 and piece_to_move[1] > -1 and  i[0] > -1 and i[1] > -1 and i[0] < 8 and i[1] < 8:
                if path_is_clear(piece_to_move[0] , piece_to_move[1] , i[0] ,i[1] ,boaard): 
                    # move implementation
                        
                    if boaard.game[piece_to_move[0]][piece_to_move[1]][0] == p.king:
                            pieces_black = [[x,y] for x in range(8) for y in range(8) if boaard.game[x][y][1] == p.black]
                            pieces_white = [[x,y] for x in range(8) for y in range(8) if boaard.game[x][y][1] == p.white]
                            if boaard.game[piece_to_move[0]][piece_to_move[1]][1] == p.white:
                                global white_virgin
                                white_virgin = False
                                if [i[0],i[1]] == [7,6]:
                                    if boaard.game[7][7][0] != p.rook or boaard.game[7][7][1] != p.white:
                                        continue
                                    if boaard.game[7][5] != [0,0]:
                                        continue
                                    if not rook4:
                                        continue
                                    for piece in pieces_black:
                                        x1,y1 = piece
                                        if [7,5] in validmoves(x1,y1,boaard):
                                            x , y = [7,5]
                                            if path_is_clear(x1,y1,x,y,boaard):
                                                cool = False
                                    if cool == False:
                                        continue
                                elif [i[0],i[1]] == [7,2]:
                                    if boaard.game[7][0][0] != p.rook or boaard.game[7][2][1] != p.white:
                                        continue
                                    if boaard.game[7][1] != [0,0]:
                                        continue
                                    if not rook3:
                                        continue
                                    for piece in pieces_black:
                                        x1,y1 = piece
                                        if boaard.game[x1][y1][1] == p.black  and ([7,1] in validmoves(x1,y1,boaard) or [7,3] in validmoves(x1,y1,boaard)):
                                            x , y = [7,1]
                                            if path_is_clear(x1,y1,x,y,boaard):
                                                cool = False
                                            x,y = [7,3]
                                            if path_is_clear(x1,y1,x,y,boaard):
                                                cool =False
                                    if cool == False:
                                        continue
                            if boaard.game[piece_to_move[0]][piece_to_move[1]][1] == p.black:
                                if [i[0],i[1]] == [0,6]:
                                    if boaard.game[0][7][0] != p.rook or boaard.game[0][7][1] != p.black:
                                        continue
                                    if boaard.game[0][5] != [0,0]:
                                        
                                        continue
                                    if not rook2:
                                        
                                        continue
                                    for piece in pieces_white:
                                        x1,y1 = piece
                                        if [0,5] in validmoves(x1,y1,boaard):
                                            x , y = [0,5]
                                            if path_is_clear(x1,y1,x,y,boaard):
                                                cool = False
                                    if cool == False:
                                        
                                        continue
                                elif [i[0],i[1]] == [0,2]:
                                    if boaard.game[0][0][0] != p.rook or boaard.game[0][2][1] != p.black:
                                        
                                        continue
                                    if boaard.game[0][1] != [0,0]:
                                        
                                        continue
                                    if boaard.game[0][3] != [0,0]:
                                        
                                        continue
                                    if not rook1:
                                        
                                        continue
                                    for piece in pieces_white:
                                        x1,y1 = piece
                                        if boaard.game[x1][y1][1] == p.white  and ([0,1] in validmoves(x1,y1,boaard) or [0,3] in validmoves(x1,y1,boaard)):
                                            x , y = [0,1]
                                            if path_is_clear(x1,y1,x,y,boaard):
                                                cool = False
                                            x,y = [0,3]
                                            if path_is_clear(x1,y1,x,y,boaard):
                                                cool = False
                                    if cool == False:
                                        continue
                    #random move with check mate checker
                    possible.append(move)
    for j in possible:
        tempboard = boaard.copy_board()
        color = tempboard.game[j[0][0]][j[0][1]][1]
        tempboard.game[j[1][0]][j[1][1]] = tempboard.game[j[0][0]][j[0][1]]
        tempboard.game[j[0][0]][j[0][1]] = [0,0]
        if color == p.black:
            if check_for_check(tempboard,-1)[0] == "no":
                possible.remove(j)
        if color == p.white:
            if check_for_check(tempboard,-1)[0] == "yes":
                possible.remove(j)
    possible += [[[0,4],[0,6]],[[0,4],[0,2]]]
    while True:
        # check for bot getting checkmated
        if check_checkmate(boaard):
            if check_for_check(boaard,-1)[0]:
                print("YOU WON")
                sys.exit(0)
            else:
                print("STALEMATE")
                sys.exit(0)
        e = 0
        move = best_move_generator(boaard,possible)
        xl = move[0][0]
        yl = move[0][1]
        xl2 = move[1][0]
        yl2 = move[1][1]
        trl = boaard.copy_board()
        trl.move(xl,yl,xl2,yl2,boaard,8,False)
        if not check_for_check(trl,-1)[0] == "no":
            e = boaard.move(xl,yl,xl2,yl2,boaard,8,True)
            global move_count
            move_count += 1
        
        if e != 0:
            if check_whitecheckmate(boaard):
                if check_for_check(boaard,-1)[0] == "yes":
                    print("You lose")
                    sys.exit(0)
                else:
                    print("Stalemate")
                    sys.exit(0)
            return 0
        possible.remove(move)
         

def best_move_generator(board,legal_moves,depth = 2):
    
    best_moves = []
    best_move = legal_moves[0]
    best_eval = -math.inf
    initial = evaluate(board)
    eval_score = evaluate(board)
    
    for move in legal_moves:
        if move[0][0] > -1 and move[0][1] > -1 and  move[1][0] > -1 and move[1][1] > -1 and move[1][0] < 8 and move[1][1] < 8:
            if path_is_clear(move[0][0] , move[0][1],move[1][0],move[1][1],board):
                new_board = board.copy_board()
                new_board.move(move[0][0],move[0][1],move[1][0],move[1][1],new_board,8,False)  # Replace with your function to make a move
                eval_score = min_max(new_board, depth - 1, -math.inf, math.inf, False)
                
        if eval_score > best_eval:
            best_moves = []
            best_moves.append(best_move)
            best_eval = eval_score
            best_move = move
        elif eval_score == best_eval:
            best_moves.append(move)
    best_moves = sorted(best_moves, key=lambda move: score_move(move, board), reverse=True)
    i = 0
    if initial == best_eval:
        while True:
            try:
                new_board = board.copy_board()
                best_move = best_moves[i]
                eval_score = min_max(new_board, depth - 1, -math.inf, math.inf, False)
                if eval_score == initial:
                    break
                i += 1
            except IndexError:
                break
    return best_move

def min_max(board, depth, alpha, beta, maximizing_player):
    global rook1
    global rook2
    global rook3
    global rook4
    if depth == 0:
        return evaluate(board)
    if check_checkmate(board):
        if check_for_check(board,-1)[0] == "no":
            return -100
    if check_whitecheckmate(board):
        if check_for_check(board,-1)[0] == "yes":
            return 100
    
    black_pieces = [[x,y] for x in range(8) for y in range(8) if board.game[x][y][1] != 0]
    
    all_possible_moves = dict()
    all_possible_moves = [[k,m] for k in black_pieces for m in validmoves(k[0],k[1],board)]
    legal_moves = all_possible_moves  # Replace with your function to get valid moves
    possible = []
    cool = True        
        # move check
    for move in all_possible_moves:
        piece_to_move = move[0]
        i = move[1]
        if not type(validmoves(piece_to_move[0],piece_to_move[1],board)) == int:      
            if piece_to_move[0] > -1 and piece_to_move[1] > -1 and  i[0] > -1 and i[1] > -1 and i[0] < 8 and i[1] < 8:
                if path_is_clear(piece_to_move[0] , piece_to_move[1] , i[0] ,i[1] ,board): 
                    # move implementation
                        if board.game[piece_to_move[0]][piece_to_move[1]][0] == p.king:
                                pieces_black = [[x,y] for x in range(8) for y in range(8) if board.game[x][y][1] == p.black]
                                pieces_white = [[x,y] for x in range(8) for y in range(8) if board.game[x][y][1] == p.white]
                                if board.game[piece_to_move[0]][piece_to_move[1]][1] == p.white:
                                    global white_virgin
                                    white_virgin = False
                                    if [i[0],i[1]] == [7,6]:
                                        if board.game[7][7][0] != p.rook or board.game[7][7][1] != p.white:
                                            continue
                                        if board.game[7][5] != [0,0]:
                                            continue

                                        if not rook4:
                                            continue
                                        for piece in pieces_black:
                                            x1,y1 = piece
                                            if [7,5] in validmoves(x1,y1,board):
                                                x , y = [7,5]
                                                if path_is_clear(x1,y1,x,y,board):
                                                    cool = False
                                        if cool == False:
                                            continue
                                    elif [i[0],i[1]] == [7,2]:
                                        if board.game[7][0][0] != p.rook or board.game[7][2][1] != p.white:
                                            continue
                                        if board.game[7][1] != [0,0]:
                                            continue
                                        
                                        if not rook3:
                                            continue
                                        for piece in pieces_black:
                                            x1,y1 = piece
                                            if board.game[x1][y1][1] == p.black  and ([7,1] in validmoves(x1,y1,board) or [7,3] in validmoves(x1,y1,board)):
                                                x , y = [7,1]
                                                if path_is_clear(x1,y1,x,y,board):
                                                    cool = False
                                                x,y = [7,3]
                                                if path_is_clear(x1,y1,x,y,board):
                                                    cool =False
                                        if cool == False:
                                            continue
                                if board.game[piece_to_move[0]][piece_to_move[1]][1] == p.black:
                                    if [i[0],i[1]] == [0,6]:
                                        if board.game[0][7][0] != p.rook or board.game[0][7][1] != p.black:
                                            continue
                                        if board.game[0][5] != [0,0]:
                                            
                                            continue
                                        
                                        if not rook2:
                                            
                                            continue
                                        for piece in pieces_white:
                                            x1,y1 = piece
                                            if [0,5] in validmoves(x1,y1,board):
                                                x , y = [0,5]
                                                if path_is_clear(x1,y1,x,y,board):
                                                    cool = False
                                        if cool == False:
                                            
                                            continue
                                    elif [i[0],i[1]] == [0,2]:
                                        if board.game[0][0][0] != p.rook or board.game[0][2][1] != p.black:
                                            
                                            continue
                                        if board.game[0][1] != [0,0]:
                                            
                                            continue
                                        if board.game[0][3] != [0,0]:
                                            
                                            continue

                                        if not rook1:
                                            
                                            continue
                                        for piece in pieces_white:
                                            x1,y1 = piece
                                            if board.game[x1][y1][1] == p.white  and ([0,1] in validmoves(x1,y1,board) or [0,3] in validmoves(x1,y1,board)):
                                                x , y = [0,1]
                                                if path_is_clear(x1,y1,x,y,board):
                                                    cool = False
                                                x,y = [0,3]
                                                if path_is_clear(x1,y1,x,y,board):
                                                    cool = False
                                        if cool == False:
                                            
                                            continue
                        #random move with check mate checker
                        possible.append(move)
                        
    legal_moves = possible
    for j in legal_moves:
        tempboard = board.copy_board()
        color = tempboard.game[j[0][0]][j[0][1]][1]
        tempboard.game[j[1][0]][j[1][1]] = tempboard.game[j[0][0]][j[0][1]]
        tempboard.game[j[0][0]][j[0][1]] = [0,0]
        if color == p.black:
            if check_for_check(tempboard,-1)[0] == "no":
                legal_moves.remove(j)
        if color == p.white:
            if check_for_check(tempboard,-1)[0] == "yes":
                legal_moves.remove(j)
    if maximizing_player:
        max_eval = -math.inf
        for move in legal_moves:
            new_board = board.copy_board()
            new_board.move(move[0][0],move[0][1],move[1][0],move[1][1],new_board,8,False)   # Replace with your function to make a move
            eval_score = min_max(new_board, depth-1, alpha, beta, False)
            max_eval = max(max_eval, eval_score)
            alpha = max(alpha, eval_score)
            if beta <= alpha:
                break  # Beta cut-off
        return max_eval
    else:
        min_eval = math.inf
        for move in legal_moves:
            new_board = board.copy_board()
            new_board.move(move[0][0],move[0][1],move[1][0],move[1][1],new_board,8,False) # Replace with your function to make a move
            eval_score = min_max(new_board, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval_score)
            beta = min(beta, eval_score)
            if beta <= alpha:
                break  # Alpha cut-off
        return min_eval

def evaluate(board):
    
    score = 0
    if check_checkmate(board):
        return -100
    if check_whitecheckmate(board):
        return 100
    for i in range(8):
        for j in range(8):
            if board.game[i][j][1] == p.white:
                if board.game[i][j][0] == p.pawn:
                    score -= 1
                if board.game[i][j][0] == p.bishop:
                    score -= 3
                if board.game[i][j][0] == p.knight:
                    score -= 3
                if board.game[i][j][0] == p.rook:
                    score -= 5
                if board.game[i][j][0] == p.queen:
                    score -= 9
            if board.game[i][j][1] == p.black:
                if board.game[i][j][0] == p.pawn:
                    score += 1
                if board.game[i][j][0] == p.bishop:
                    score += 3
                if board.game[i][j][0] == p.knight:
                    score += 3
                if board.game[i][j][0] == p.rook:
                    score += 5
                if board.game[i][j][0] == p.queen:
                    score += 9


    return score

def score_move(move, board):
    i, j = move[0]
    x, y = move[1]
    score = 0

    # Example: Prioritize capturing moves
    for s in [i,j,x,y]:
        if s >7:
            return -100
        if s < 0:
            return -100
    if 2<=y<=5:
        score = 2
    if board.game[i][j][0] == p.king:
        score = -1
    if board.game[x][y] != [0, 0]:
        score = 2  # High score for capturing moves
    if board.game[i][j][0] == p.queen:
        score = 1
    if board.game[i][j][0] == p.rook:
        score = 1
    # Example: Prioritize pawn promotion
    if board.game[i][j][0] == p.pawn and x in [0, 7]:
        score = 3  # Highest score for pawn promotion
    if move == [[0,4],[0,6]] or move == [[0,4],[0,2]]:
        score = 5
    lelo = board.copy_board()
    lelo.move(i,j,x,y,lelo,1,False)
    if check_for_check(lelo,-1) == "no":
        score = 5
    if move == [[1,4],[3,4]]:
        score = 10

    # Default score for other moves
    return score