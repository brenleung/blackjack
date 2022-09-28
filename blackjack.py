import random

print("Welcome to Blackjack!")
print("Let's start by giving you two cards..")

color = ["black", "red"]
suit = ["spades", "clubs", "hearts", "diamonds"]
num = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
cards = []

def giveCard():
    cardColor = color[random.randint(0,1)]
    cardSuit = suit[random.randint(0,3)]
    cardNum = num[random.randint(0,12)]
    cards.append(convertCard(cardColor, cardSuit, cardNum))

def convertCard(color, suit, num):
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

    for i in cards:  # checks if this card already exists in hand
        if (i == card):
            giveCard()
    return card

def findValue(cards):
    total = 0
    aces = 0
    for i in cards:
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

def checkWin(cards):
    if findValue(cards) == 21:
        displayCards(cards)
        print("Congrats! Blackjack! You win!")
        return True
    return False

def checkLoss(cards):
    if findValue(cards) > 21:
        displayCards(cards)
        print("Bust!")
        return True
    return False

def displayCards(cards):
    print("Your cards are: ")
    for i in cards:
        print(str(i) + " ")
    print("for a total value of: " + str(findValue(cards)))
 
tut = input("Would you like a tutorial? Y/N ")
if (tut == "Y"):
    print("Your goal is to get as close to 21 as you can without going over.")
    print("Cards will be represented in a string format with COLOR + SUIT + VALUE.")
    print("Example: RS7 = Red Spades 7")
    print("Let's play!" + "\n\n")
giveCard()
giveCard()

while (not checkLoss(cards) and not checkWin(cards)):
    displayCards(cards)
    if input("Stand or hit? S/H ") == "H":
        giveCard()
    else:
        print("Thanks for playing! Your final card value was: " + str(findValue(cards)))
        break
