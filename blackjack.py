import random

print("Welcome to Blackjack!")
print("Let's start by giving you two cards..")

color = ["black", "red"]
suit = ["spades", "clubs", "hearts", "diamonds"]
num = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
player = []
AIhand= []

def giveCard(hand):  # generates card for player
    cardColor = color[random.randint(0,1)]
    cardSuit = suit[random.randint(0,3)]
    cardNum = num[random.randint(0,12)]
    hand.append(convertCard(cardColor, cardSuit, cardNum))

def convertCard(color, suit, num):  # converts card attributes to string
    card = ""
    if color == "black":
        card += "B"
    else:
        card += "R"

    if suit == "spades":
        card += "S"
    elif suit == "clubs":
        card += "C"
    elif suit == "hearts":
        card += "H"
    else:
        card += "D"
    
    card += str(num)

    for i in player:  # checks if this card already exists in hand
        if (i == card):
            giveCard()
    for i in AIhand:  # checks if this card already exists in AI
        if (i == card):
            giveCard()
    return card

def findValue(hand):  # finds total value of hand
    total = 0
    aces = 0
    for i in hand:
        if i[2] == "A":
            total += 11
            aces += 1
        elif i[2] == "J" or i[2] == "Q" or i[2] == "K" or len(i) == 4:
            total += 10
        else:
            total += int(i[2])
    while total > 21 and aces > 0:
        total -= 10
        aces -= 1
    return total

def checkWin(hand):  # win condition
    if findValue(hand) == 21 and findValue(AIhand) == 21:
        displayCards(hand)
        print("\nDraw!")
        return True
    elif findValue(hand) == 21:
        displayCards(hand)
        print("\nCongrats! Blackjack! You win!")
        return True
    return False

def checkLoss(hand):  # lose condition
    if findValue(hand) > 21:
        displayCards(hand)
        print("\nBust! You lose!")
        return True
    return False

def displayCards(hand):  # prints cards
    print("Your cards are: ")
    for i in hand:
        print(str(i) + " ")
    print("for a total value of " + str(findValue(hand)))
    print("Known dealer card: " + AIhand[0])
 
tut = input("Would you like a tutorial? Y/N ")
if (tut == "Y" or tut == "y"):
    print("Your goal is to get as close to 21 as you can without going over.")
    print("Cards will be represented in a string format with COLOR + SUIT + VALUE.")
    print("Example: RS7 = Red Spades 7")
    print("Let's play!" + "\n\n")
giveCard(player)
giveCard(player)

while (findValue(AIhand) < 17):  # AI play conditions
    giveCard(AIhand)

while (not checkLoss(player) and not checkWin(player)):  # check for bust/blackjack
    displayCards(player)
    sh = input("Stand or hit? S/H ")
    if sh == "H" or sh == "h":  # hit
        giveCard(player)
    else:  # stand
        print("Thanks for playing! Your final card value was: " + str(findValue(player)) + "\n")
        print("The dealer's cards were ")
        for i in AIhand: # display AI hand
            print(i+" ")
        print("for a value of: " + str(findValue(AIhand)) + "\n")
        if findValue(AIhand) > findValue(player) and findValue(AIhand) <= 21: # lose condition
            print("YOU LOSE!")
        elif findValue(AIhand) < findValue(player) or findValue(AIhand) > 21: # win condition
            print("YOU WIN!")
        else: print("DRAW!")
        break
