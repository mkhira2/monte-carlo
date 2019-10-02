import random

# the die can take values from 1 to 100. If the number is between 1 and 51, the house wins. 
# if the number is between 52 and 100, the player wins.

def rolldice():
    
    dice = random.randint(1,100)
    
    if dice <=51:
        return False
    elif dice >51 & dice <=100:
        return True

def play(total_funds, wager_amount, total_plays):
    
    play_num = []
    funds = []

    play = 1

    while play <= total_plays:
        # if we win
        if rolldice():
            total_funds = total_funds + wager_amount
            play_num.append(play)
            funds.append(total_funds)
        # if the house wins
        else:
            total_funds = total_funds - wager_amount 
            play_num.append(play)
            funds.append(total_funds)
            
        play = play + 1
        
    final_funds.append(Funds[-1])
    return(final_funds)

final_funds= []

def makeBets(total_plays):
    x=1
    final_funds= []

    while x<=100:
        ending_fund = play(10000,100,total_plays)
        x=x+1

    print(f"Making {total_plays} bets, the player ends with $" + str(int(sum(ending_fund)/len(ending_fund))))

print("\nThe player starts the game with $10,000 and...\n")

makeBets(5)
makeBets(10)
makeBets(50)
makeBets(100)
makeBets(500)
makeBets(1000)
makeBets(10000)
print()
