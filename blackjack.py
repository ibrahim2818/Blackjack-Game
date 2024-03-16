
import random
import os

def dealCard():
    cards = [11 , 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10]
    x=random.randint(0,len(cards)-1)
    return cards[x]
design= '''.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
'-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_!
      |  \/ K|                            _/ |                
      '------'                           |__/ '''

want_to_play = True
while want_to_play:
    wannaPlay = input("Do you want to play a Blackjack card? Tyoe 'y' or 'n'").lower()
    if wannaPlay== 'y':
        os.system("cls")
        print(design)


        end_game= True
        while end_game:
            usercards = []
            computercards = []


            usercards.append(dealCard())
            usercards.append(dealCard())
            computercards.append(dealCard())
            computercards.append(dealCard()) 


            userTotal= sum(usercards)
            computerTotal= sum(computercards)


            
            if 11 in usercards and 10 in usercards:
                print("you win you has a blackjack")
                end_game = False
            if 11 in computercards and computerTotal > 20:
                print("you lose comuter has a blackjack")
                end_game = False



            

            print("Computer's first card:")
            print(computercards[0])
            print("Your cards:")
            print(usercards)
            print("your total")
            print(userTotal)


            if userTotal==20:
                print("you win")
                end_game = False


            while True:
                p= input("you want to take another card 'y' or 'n'?\n").lower()

                if p == 'y':
                    usercards.append(dealCard())
                    userTotal =sum(usercards)
                    if 11 in usercards and userTotal > 20:
                        usercards[usercards.index(11)] = 1
                        userTotal = userTotal-10
                    print("Your cards:")
                    print(usercards)
                    print("your total")
                    print(userTotal)
                    
                    if userTotal > 20:
                        print("your total")
                        print(userTotal)
                        print("you lose")
                        end_game = False
                    break
                elif p == 'n':
                    break



            while computerTotal<17:
                computercards.append(dealCard())
                computerTotal = sum(computercards)
                if 11 in computercards and computerTotal > 20:
                    computercards[computercards.index(11)] = 1
                    computerTotal = computerTotal-10




            print("computers cards")
            print(computercards)
            print("computers total")
            print(computerTotal)
            print("Your cards:")
            print(usercards)
            print("your total")
            print(userTotal)


            if computerTotal>20:
                print("you win")
                end_game = False
            elif userTotal > 20:
                print("You lose")
                end_game = False
            else:
                if computerTotal==userTotal:
                    print("It's a tie")
                    end_game= False
                elif computerTotal>=userTotal:
                    print("you lose")
                    end_game= False
                else:
                    print("you win")
                    end_game= False
        
    else:
        print("Thanks ")
        wannaPlay = False



