class Player(object):
    
    def __init__(self,openingBal=100):
        self.openingBal = int(openingBal)
        self.cards = []
        #xyz
        
    def Show(self):
        #show cards
        print("Player's cards are:\n")
        print(self.cards)
    
        
    def Sum(self):
        # sum of the cards   
        total = 0 
        for (val,suit) in self.cards:
            if(val=='King' or val == 'Jack' or val=='Queen'):
                total = total + 10
            elif(val=="Ace"):
                val=input("you want to count it as 1 or 11 ?")
                total=total+int(val)
            else:
                total = total + int(val)
        print("total sum = "+str(total))
        return total

    def eligibleForSplit(Self):
        [(a,b),(c,d)] = self.cards
        if(a==c):
            return True
        
    def Hit(self,card):
        self.cards.append(card)

        
    def balance(self,update=0):
        self.openingBal+=float(update)
        print("balance left = "+str(self.openingBal))
        return self.openingBal
        #how much a player lost or earned

        
        
class Dealer(object):
        
        
    def __init__(self):
        self.cards = []
        
    def ShowACard(self):
        print("Dealer's card is:\n")
        print(self.cards[0])
        
    def Show(self):
        #show cards
        print("Dealer's cards are:\n")
        print(self.cards)
    
        
    def Sum(self):
        # sum of the cards   
        total = 0 
        for (val,suit) in self.cards:
            if(val=='King' or val == 'Jack' or val=='Queen'):
                total = total + 10
            elif(val=="Ace"):
                val=input("you want to count this Ace as 1 or 11 ?")
                total=total+int(val)
            else:
                total = total + int(val)
        print("total sum = "+str(total)) 
        return total

        
    def Hit(self,card):
        self.cards.append(card)


        
import random
import itertools

print(" Welcome to Animesh's Black Jack Game")
playerName = input("Enter your Name ")
print("Hi",playerName)
openingBal = input("Enter the amount you want to play with ? Default is 100 ")



player = Player(openingBal)
dealer = Dealer()

while(input("Hey "+playerName+", you want to play another round ? y/n\n")=='y'):
    
    while(True):
        try:
            bettingAmount=int(input("Hey "+playerName+", How much you want to bet in this round ? Reply with 1, 2, 5, 10\n"))
        except:
            print("Oops. Invalid bet amount selected")
            continue
        else: 
            break
    
    value = ["Ace","Jack","Queen","King",2,3,4,5,6,7,8,9,10]
    suit = ["Spade", "hearts", "clubs", "diamond"]
    card = list(itertools.product(value, suit)) 
    random.shuffle(card)
    
    
#serving cards 
    del player.cards[:]
    del dealer.cards[:]

    #player.cards
    
    player.Hit(card.pop())
    dealer.Hit(card.pop())

    player.Hit(card.pop())
    dealer.Hit(card.pop())

    player.Show()
    
    print("\nHey "+playerName+" , Dealer's card is:")
    dealer.ShowACard()
    

#dealer.Show()

    doubleBet=input("Hey "+playerName+", do you want to double your betting amount ?\n")
    if(doubleBet=='y'):
        bettingAmount*=2
# if(player.eligibleForSplit()):
    #    doubleBet=input("Hey "+playerName+", do you want to split your cards ?")
    gameEnd = "No"
    player.Show()
    currentPlayerTotal = player.Sum()
    while(input("Hey "+playerName+", you want to hit ? y/n\n")=='y'):
        player.Hit(card.pop())
        print("Hey "+playerName+" your cards are:")
        
        player.Show()
        currentPlayerTotal = player.Sum()
        if(currentPlayerTotal > 21):
            print("your Sum ="+str(currentPlayerTotal)+". Exceeded 21 !!!  Round lost")
            bettingAmount*=-1
            player.balance(str(bettingAmount))
            gameEnd = "Yes"
            break
        elif(currentPlayerTotal == 21):
            print("your Sum ="+str(currentPlayerTotal)+" YOU WON the round !! ")
            bettingAmount*=1.5
            player.balance(str(bettingAmount))
            gameEnd = "Yes"
        else: 
            continue
 
    if(gameEnd=="Yes"):
        continue
        
    dealer.Show()
    currentDealerTotal = dealer.Sum()
    while(currentDealerTotal<=16):
        print("Now dealer will hit till he reaches a minimum of 17")
        dealer.Hit(card.pop())
        dealer.Show()
        currentDealerTotal = dealer.Sum()
        if(currentDealerTotal > 21):
            print("Dealer busted ! YOU WON the round ")
            bettingAmount*=1.5
            player.balance(str(bettingAmount))   
    if(currentPlayerTotal > currentDealerTotal):
        print("Player Sum ="+str(currentPlayerTotal)+"and dealer Sum ="+str(currentDealerTotal)+ " YOU WON the round !! ")
        bettingAmount*=1.5
        player.balance(str(bettingAmount))
    elif(currentPlayerTotal == currentDealerTotal):
        print("Player Sum ="+str(currentPlayerTotal)+"and dealer Sum ="+str(currentDealerTotal)+ " No one won !! ")
        player.balance(str(0))
    else:  
        print("Player Sum ="+str(currentPlayerTotal)+"and dealer Sum ="+str(currentDealerTotal)+ " You lost !! ")
        bettingAmount*=-1
        player.balance(str(bettingAmount))
        
    if(player.balance(0)<=0):
        print("Please recharge your account and come back to play")
        break
            
print("Game over")
print("Thanks for playing !! " + playerName)
player.balance(0)
