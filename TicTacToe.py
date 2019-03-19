#Simple Python program for Tic-Tac-Toe Game
import sys

theBoard={'TopL':'','TopM':'','TopR':'',
          'MidL':'','MidM':'','MidR':'',
          'BotL':'','BotM':'','BotR':''
          }

def wonOrNot(player):
    if theBoard['TopL']==theBoard[player] and theBoard['TopM']==theBoard[player] and theBoard['TopR']==theBoard[player]:
        return True
    elif theBoard['MidL']==theBoard[player] and theBoard['MidM']==theBoard[player] and theBoard['MidR']==theBoard[player]:
        return True
    elif theBoard['BotL']==theBoard[player] and theBoard['BotM']==theBoard[player] and theBoard['BotR']==theBoard[player]:
        return True
    elif theBoard['TopL']==theBoard[player] and theBoard['MidL']==theBoard[player] and theBoard['BotL']==theBoard[player]:
        return True
    elif theBoard['TopM']==theBoard[player] and theBoard['MidM']==theBoard[player] and theBoard['BotM']==theBoard[player]:
        return True
    elif theBoard['TopR']==theBoard[player] and theBoard['MidR']==theBoard[player] and theBoard['BotR']==theBoard[player]:
        return True
    elif theBoard['TopL']==theBoard[player] and theBoard['MidM']==theBoard[player] and theBoard['BotR']==theBoard[player]:
        return True
    elif theBoard['TopR']==theBoard[player] and theBoard['MidM']==theBoard[player] and theBoard['BotL']==theBoard[player]:
        return True
    else:
        return False


def printBoard():
    print(theBoard['TopL']+' | '+theBoard['TopM']+' | '+theBoard['TopR'])
    print(' *  * ')
    print(theBoard['MidL']+' | '+theBoard['MidM']+' | '+theBoard['MidR'])
    print(' *  * ')
    print(theBoard['BotL']+' | '+theBoard['BotM']+' | '+theBoard['BotR'])
    print(' *  * ')

def playerTurn(player):
    move=''
    if player=='X':
        print('It is O turn. what is your move?')
        move=input()
        theBoard[move]='O'
    else:
        print('It is X turn. what is your move?')
        move=input()
        theBoard[move]='X'
    printBoard()
    if wonOrNot(move):
        print('Congratulations! '+theBoard[move] + ' has Won')
        sys.exit()
    else:
        if player=='X':
            playerTurn('O')
        else:
            playerTurn('X')
        
printBoard()
print('Enter \n TopR for TopRight \n TopM for Top Middle \n TopL for Top Left\n MidR for Middle Right \n MidM for Middle Mid \n MidL for Middle Left\n BotR for Bottom Right \n BotM for Bottom Middle \n BotL for Bottom Left\n')
FirstInput=input('X goes First.What is your move?')
theBoard[FirstInput]='X'
printBoard()
playerTurn(theBoard[FirstInput])

