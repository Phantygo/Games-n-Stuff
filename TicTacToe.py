import sys

def display_board(board):
    print(board[1]+'|'+board[2]+'|'+board[3])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[7]+'|'+board[8]+'|'+board[9])

def pick_player():
    marker = "wrong"
    # PICK X OR O
    while marker != "X" and marker != "O":
        marker = input("Player 1, choose X or O to play: ").upper()
        
        if marker != "X" and marker != "O":
            print("Invalid input!")
        
        player1 = marker
        
        if player1 == "X":
            player2 = "O"
        else:
            player2 = "X"
    
    return ("Player 1:", player1, "Player 2:", player2)

def check_win(game_board, player_marker):

        if  game_board[1] == player_marker and game_board[2] == player_marker and game_board[3] == player_marker or \
            game_board[4] == player_marker and game_board[5] == player_marker and game_board[6] == player_marker or \
            game_board[7] == player_marker and game_board[8] == player_marker and game_board[9] == player_marker or \
            game_board[1] == player_marker and game_board[5] == player_marker and game_board[9] == player_marker or \
            game_board[3] == player_marker and game_board[5] == player_marker and game_board[7] == player_marker or \
            game_board[1] == player_marker and game_board[4] == player_marker and game_board[7] == player_marker or \
            game_board[2] == player_marker and game_board[5] == player_marker and game_board[8] == player_marker or \
            game_board[3] == player_marker and game_board[6] == player_marker and game_board[9] == player_marker:

            return True
        
        else:
            return False
       

def choose_position(game_board, player1_marker, player2_marker):

    display_board(game_board)
    player1_turn = True
    gameon = True
    #PLACE USER INPUT ON BOARD
    
    while gameon == True:
        while player1_turn == True:         
            if " " not in game_board:
                gameon = False
                break
            user_input = int(input("Player 1, pick a position (1-9): "))
            
            if user_input in range(1,10):           
                if game_board[user_input] == " ":
                    game_board[user_input] = player1_marker
                    display_board(game_board)
                    if check_win(game_board, player1_marker):
                        print("Player 1 is the Winner!")
                        play_again(gameon)

                        break
                    if " " not in game_board and check_win(game_board,player1_marker) == False:
                        print("Tie Game!")
                        play_again(gameon)
                        break
                    player1_turn = False
                        


                    
                else:
                    print("This position is taken, please choose another.")

            else:
                print("Invalid Input, choose a position from 1-9")
        

        
        while player1_turn == False:
            if " " not in game_board:   
                gameon = False
                break
            user_input = int(input("Player 2, pick a position (1-9): "))

            if user_input in range(1,10):
                if game_board[user_input] == " ":
                    game_board[user_input] = player2_marker
                    display_board(game_board)
                    if check_win(game_board, player2_marker):
                        print("Player 2 is the Winner!")
                        play_again(gameon)
                        break
                    player1_turn = True


                else:
                    print("This position is taken, please choose another.")

            else:
                print("Invalid Input, choose a position from 1-9")

def play_again(gameon):
    
    question = "wrong"
    while question != "Yes" and question != "No":
        question = input("Play again? (Yes or No)").capitalize()
        if question == "Yes":
            game_board = ['*'," "," "," "," "," "," "," "," "," "]
            players = pick_player()
            player1_marker = players[1]
            player2_marker = players[3]
            choose_position(game_board,player1_marker,player2_marker)

        
        elif question == "No":
            print("Thank you for playing, have a great day!")
            sys.exit()

        
        else:
            print("Invalid input")


print("Welcome to Tic Tac Toe")
players = pick_player()
game_board = ['*'," "," "," "," "," "," "," "," "," "]
player1_marker = players[1]
player2_marker = players[3]
choose_position(game_board,player1_marker,player2_marker)







