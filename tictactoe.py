"""
Tic Tac Toe Player
"""

import math
import copy
X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    number_of_Xs = 0
    number_of_Os = 0
    number_of_EMPTYs = 0
    
    #iterate over the board identifying the states of each box
    for row in board:
        for box in row:
            if box == X:
                number_of_Xs += 1
            elif box == O:
                number_of_Os += 1
            else:
                number_of_EMPTYs += 1
    
    
    if (number_of_Os == 0 and number_of_Xs == 0) or (number_of_Xs == number_of_Os):
        return X
    elif number_of_EMPTYs == 0:
        return "The game is over"
    else:
        return O
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == EMPTY:
                actions.add((i,j))
    return actions
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # create a deep copy of the board
    deep_copy_board = copy.deepcopy(board)
    
    #get player's turn 
    turn = player(deep_copy_board)
    
    #get the move
    i,j = action
    
    #make the move
    if  i <= 2 and j <= 2:
        if deep_copy_board[i][j] == EMPTY:
            deep_copy_board[i][j] = turn
            return deep_copy_board
    
    # if the move is invalid 
    raise Exception("Invalid action: "+str(action), "nyehh", deep_copy_board)
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    #check winner for horizontal if any
    for i in range(len(board)):
        if board[i][0] == board[i][1] and board[i][0] == board[i][2]:
            #print("horizontal",board[i][0], board[i][1], board[i][2])
            return board[i][0]
    
    
    #check winner for vertical if any
    for j in range(len(board)):
        if board[0][j] == board[1][j] and board[0][j] == board[2][j]:
            #print("vertical",board[0][j], board[1][j], board[2][j])
            return board[0][j]
        
        
    #check winner for diagonal if any
    #Left to right
    if board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        #print("diagonal LR",board[0][0], board[1][1], board[2][2])
        return board[0][0]
    
    #right to left
    if board[0][2] == board[1][1] and board[0][2] == board[2][0]:
        #print("diagonal RL",board[0][2], board[1][1], board[2][0])
        return board[0][2]

    return None
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    number_of_EMPTYs = 0
    #check if there is a winner, if no winner return True
    for row in board:
        for box in row:
            if box == EMPTY:
                number_of_EMPTYs += 1
    
    if winner(board) != None or number_of_EMPTYs == 0:
        return True
    
    return False
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    player_winner = winner(board)
    
    if player_winner == X:
        return 1
    elif player_winner == O:
        return -1
    
    return 0  
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    #get the current player
    start = player(board)
    
    #best move
    bestMove = None
    
    #initialize the best score
    if start == O:
        bestScore = math.inf
    else:
        bestScore = -math.inf
    
    
    #iterate over the the possible actions for a given board (state)
    for action in actions(board):
        if start == O:
            score = max_value(result(board,action))
            #print("score = ", score, action)
            if score <= bestScore:
                bestScore = score
                bestMove = action
                
        if start == X:
            score = min_value(result(board,action))
            #print("score = ", score, action)
            if score >= bestScore:
                bestScore = score
                bestMove = action
                
    return bestMove        
    raise NotImplementedError


def max_value(board):
    v = -math.inf
    
    #if the board is in terminal state return the value.
    if terminal(board):
        return utility(board)
    
    #search for the maximum value for a given action
    for action in actions(board):
        v = max(v, min_value(result(board,action)))

    return v

def min_value(board):
    v = math.inf
    
    #if the board is in terminal state return the value.
    if terminal(board):
        return utility(board)
    
    #search for the minimum value for a given action
    for action in actions(board):
        v = min(v, max_value(result(board,action)))
    return v
    
