import art
import random

print(art.logo)


def add_cards(cards, p, c, resume):
    index = random.randint(0, 12)
    val = cards[index]
    p.append(val)

    index = random.randint(0, 12)
    val = cards[index]
    c.append(val)
    print("Your cards: ", p)
    length = len(c)
    print("Dealer's cards: ")
    print("[", end="")
    for i in range(0, length):

        if (i == length - 1):
            print("x", end="")
        else:
            print(str(c[i]), ",", end="")
    print("]")
    resume = input("Do you want to draw a card? (yes/no)")
    if (resume == "yes"):
        add_cards(cards, player, computer, resume)
    else:
        return 0


def winner(p, c):
    psum = 0
    csum = 0
    #calculating sum of players
    for i in p:
        psum += i
    for i in c:
        csum += i

    if psum > 21 and 11 in p:
        psum = psum - 10

    if csum > 21 and 11 in c:
        psum = psum - 10
    index = len(c) - 1
    print("your sum: ", psum)
    print("Dealer's last card was: ", c[index])
    print("Dealer's sum: ", csum)

    if psum > 21:
        print("You lose!")

    elif csum > 21:
        print("You win!")

    if (psum <= 21 and csum <= 21):
        pdif = 21 - psum
        cdif = 21 - csum
        if (pdif < cdif):
            print("You win!")
        elif (pdif > cdif):
            print("You lose!")
        elif (pdif == cdif):
            print("Game ends in a draw")

    ip = input("Do you want to play again?(yes/no)")
    return ip


play = input("Do you want to play black jack? (yes/no)")
play = play.lower()
#print(play)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player = []
computer = []
while (play == "yes"):
    #starting with two random cards for the player
    for i in range(0, 2):
        index = random.randint(0, 12)
        val = cards[index]
        player.append(val)

    #starting with one random card for the computer
    index = random.randint(0, 12)
    val = cards[index]
    computer.append(val)

    #displaying cards
    print("Your cards: ", player)
    print("Dealer's cards: ", computer)

    #asking if the user wants to add cards
    resume = input("Do you want to draw a card? (yes/no)")
    resume = resume.lower()
    if (resume == "yes"):
        add_cards(cards, player, computer, resume)
    play = winner(player, computer)

#print(player)
#print(computer)
