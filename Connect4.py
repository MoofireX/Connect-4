# Python Class 3825
# Lesson 12 Problem 1
# Author: Moofire (1085156)

column1 = ['.','.','.','.','.','.']
column2 = ['.','.','.','.','.','.']
column3 = ['.','.','.','.','.','.']
column4 = ['.','.','.','.','.','.'] #Initialize the empty 6 columns
column5 = ['.','.','.','.','.','.']
column6 = ['.','.','.','.','.','.']

columnList = [column1,column2,column3,column4,column5,column6] #Create a list of those columns

numbers = "1       2      3     4     5     6" #The labels
    
winnerX = False 
winnerO = False
#Intitialize the winnerX and winnerO variables
checkStrX = ""
checkStrO = ""
#Strings to check for diagonal winners

def player_setup(): #Get the player names and return them
    
    X = input("Who is Player X? ")
    O = input("Who is Player O? ")
    
    return X,O


def game_intro(): #Tell the game rules to the players
    print("\n")
    print("Welcome to Connect 4!")
    print("The rules are simple:")
    print("Drop your pieces into one of the 6 columns...")
    print("Whoever connects 4 of them in a row first wins!")
    print("You can win vertically, horizontally, and even diagonally!")
    print("Good luck! :-)")
    print("\n")
    start = ""

    while start != "yes": #Let the players read the rules, and enter yes to start the game
        start = input("Are both players ready to start? Enter yes to start the game. ")
        if start == "no":
            print("\n")
            print("Okay, we'll start later.")
            print("\n")
        elif start == "yes":
            print("\n")
            print("Ready? Then, let's go!")
            print("\n")
        else:
            print("\n")
            pass


def print_board():
    
    
    print(numbers) #Print the number labels
    print("\n")
          
    columnIndx = 0
    
    for column in columnList:
       print(column1[columnIndx],"     ",column2[columnIndx],"     ",column3[columnIndx],"     ",column4[columnIndx],
             "     ",column5[columnIndx],"     ",column6[columnIndx])
       print("\n")
       #Print all the columns 1 index at a time
        
       columnIndx += 1


def diagonal_winner():
    global winnerX,winnerO
    
    for c in range(3):
        for r in range(3):
            
            if columnList[c][r] == "X" and columnList[c+1][r+1] == "X" and columnList[c+2][r+2] == "X" and columnList[c+3][r+3] == "X":
                winnerX = True

            elif columnList[c][r] == "O" and columnList[c+1][r+1] == "O" and columnList[c+2][r+2] == "O" and columnList[c+3][r+3] == "O":
                winnerO = True

    for c in range(3):
        for r in range(3,6):
            
            if columnList[c][r] == "X" and columnList[c+1][r-1] == "X" and columnList[c+2][r-2] == "X" and columnList[c+3][r-3] == "X":
                winnerX = True

            elif columnList[c][r] == "O" and columnList[c+1][r-1] == "O" and columnList[c+2][r-2] == "O" and columnList[c+3][r-3] == "O":
                winnerO = True
        
def horizontal_vertical_winner():
    global winnerX,winnerO #Use the global variables instead of using new ones
    for column in columnList:
        #Check each column in columnList if 4 indexes in a row are equal to X
        if column[5:1:-1] == ['X','X','X','X'] or column[4:0:-1] == ['X','X','X','X'] or column[3:-1:-1] == ['X','X','X','X']:
            winnerX = True
            break
        #Check each column in columnList if 4 indexes in a row are equal to O
        elif column[5:1:-1] == ['O','O','O','O'] or column[4:0:-1] == ['O','O','O','O'] or column[3:-1:-1] == ['O','O','O','O']:
            winnerO = True
            break


        else: #If there are now 4-in-a-row horizontally, check vertically

            rowIndx = 0 

            for x in range(len(columnList)):
                #Check all the possible ways Xs and Os can appear 4-in-a-row accross columns at rowIndx
                if column1[rowIndx] == 'X' and column2[rowIndx] == 'X' and column3[rowIndx] == 'X' and column4[rowIndx] == 'X':
                    winnerX = True
                    break

                elif column1[rowIndx] == 'O' and column2[rowIndx] == 'O' and column3[rowIndx] == 'O' and column4[rowIndx] == 'O':
                    
                    winnerO = True
                    break

                elif  column6[rowIndx] == 'X' and column5[rowIndx] == 'X' and column4[rowIndx] == 'X' and column3[rowIndx] == 'X':

                    winnerX = True
                    break

                elif column6[rowIndx] == 'O' and column5[rowIndx] == 'O' and column4[rowIndx] == 'O' and column3[rowIndx] == 'O':

                    winnerO = True
                    break

                elif column2[rowIndx] == 'X' and column3[rowIndx] == 'X' and column4[rowIndx] == 'X' and column5[rowIndx] == 'X':
                    
                    winnerX = True
                    break

                elif column2[rowIndx] == 'O' and column3[rowIndx] == 'O' and column4[rowIndx] == 'O' and column5[rowIndx] == 'O':
                    
                    winnerO = True
                    break

                rowIndx += 1
                
def connect4():
    X,O = player_setup() #Get the player names
    game_intro() #Print the intro
    Xcounter = 18
    Ocounter = 18
    #Initialize the number of pieces each player has
     
    currentPlayer = input("Is " + str(X) + " going first, or is " + str(O) +" going first? ") #Asks which player is going first
    print_board() #Print the board
    turn = ""
    columnIndx = len(columnList[0]) - 1
    #Intintialize the columnIndx and the turn variables
    
    while True:
        
        if Xcounter == 0 and Ocounter == 0: #At the time each loop starts, check if X and O has used all their pieces
            print("\n")
            print("\n")
            print("After a long battle...")
            print("The game has ended in a draw!!!")
            print("\n")
            print("\n")
            break
        
        if currentPlayer == X: #If it's X's turn
            turn = int(input(str(X) + " it's your turn. What column do you want to play in? ")) #Ask X what column they want to play in
            turnColumn = columnList[turn - 1]
            
            for x in range(len(turnColumn)):
                
                if turnColumn[0] == "X" or turnColumn[0] == "O" :
                    #If the top index is filled, tell X that that column is full
                    print("Column " , columnList.index(turnColumn) + 1 , " is full.")
                    currentPlayer = X
                    columnIndx = len(columnList[0]) - 1
                    break
                
                if turnColumn[columnIndx] == ".":
                    #If the space is not filled, put X's piece there and move on to O's turn
                    turnColumn[columnIndx] = "X"
                    print_board()
                    currentPlayer = O
                    columnIndx =  len(columnList[0]) - 1
                    break
                    
                elif turnColumn[columnIndx] == "O":
                    #If the space is filled by O, check the next column
                    columnIndx -= 1
                    
                else:
                    #Check the next column
                    columnIndx -= 1

        horizontal_vertical_winner()
        diagonal_winner()
        #Check for 4-in-a-row vertically, horizontally, and diagonally
      
        if winnerX == True or winnerO == True:
            break

                
        if currentPlayer == O:
            turn = int(input(str(O) + " it's your turn. What column do you want to play in? "))
            turnColumn = columnList[turn - 1]
        
            for x in range(len(turnColumn)):
                
                
                if turnColumn[0] == "X" or turnColumn[0] == "O" :
                    #If the top index is filled, tell X that that column is full
                    print("Column " , columnList.index(turnColumn) + 1 , " is full.")
                    currentPlayer = O
                    columnIndx = len(columnList[0]) - 1
                    break
       
                if turnColumn[columnIndx] == ".":
                    #If the space is not filled, put O's piece there and move on to X's turn
                    turnColumn[columnIndx] = "O"
                    print_board()
                    currentPlayer = X
                    columnIndx =  len(columnList[0]) - 1
                    break
                    
                elif turnColumn[columnIndx] == "X":
                    #If the space is filled by X, check the next column
                    columnIndx -= 1
                    
                else:
                    #Check the next column
                    columnIndx -= 1

        horizontal_vertical_winner()
        diagonal_winner()
        #Check for 4-in-a-row vertically, horizontally, and diagonally

        Xcounter -= 1
        Ocounter -= 1
        #Decrease the number of pieces X and O have by 1 after both of their turns are over

        if winnerX == True or winnerO == True:
            break
            
    #The lines below print congratulation statements depending on which player has won

    if winnerX == True:
        print("\n")
        print("\n")
        print("Dun dun dun!")
        print(X , ", AKA Player X, has won!!!")
        print("\n")
        print("\n")

            
    elif winnerO == True:
        print("\n")
        print("\n")
        print("Dun dun dun!")
        print(O , ", AKA Player O, has won!!!")
        print("\n")
        print("\n")

        
connect4()
