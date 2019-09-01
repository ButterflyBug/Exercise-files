# jeżeli obaj gracze mają taką samą kartę,
# to karty te wracają do graczy na dół ich talii.

import random

''' aCard = {"Figure":"King", "Power":12}
print(aCard)
print(aCard["Figure"])
print(aCard["Power"])

aCard['Color'] = 'Heart'
print(aCard) '''

colors = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
figures = [
    {'Figure': 'Ace',  'Power': 14},
    {'Figure': 'King', 'Power': 13},
    {'Figure': 'Queen', 'Power': 12},
    {'Figure': 'Jack', 'Power': 11},
    {'Figure': '10',   'Power': 10},
    {'Figure': '9',    'Power': 9}]


allCards = []

for color in colors:
    for figureAndPower in figures:
        aCard = {'Color': color,
                 'Figure': figureAndPower['Figure'],
                 'Power': figureAndPower['Power']}
        allCards.append(aCard)
print(allCards, '\n\n')
# print(len(allCards))

random.shuffle(allCards)
# print(allCards)

player1 = allCards[0:12]
player2 = allCards[12:24]

print('Cards for player1:\n', player1, '\n')
print('Cards for player2:\n', player2, '\n')

# print(len(player1))
# print(len(player2))

usedCards = []

while not (player1 == [] or player2 == []):

    firstMoveCardPlayer1 = player1.pop(0)
    firstMoveCardPlayer2 = player2.pop(0)
    usedCards.extend([firstMoveCardPlayer1, firstMoveCardPlayer2])

    if firstMoveCardPlayer1['Power'] > firstMoveCardPlayer2['Power']:
        print("Player 1 wins.")
        player1.extend([firstMoveCardPlayer1, firstMoveCardPlayer2])
        usedCards = []
        print(len(player1))

    elif firstMoveCardPlayer1['Power'] < firstMoveCardPlayer2['Power']:
        print("Player 2 wins.")
        player2.extend([firstMoveCardPlayer2, firstMoveCardPlayer1])
        usedCards = []
        print(len(player2))

    else:
        print("TIE!")
        if not (player1 == [] or player2 == []):
            tieCardPlayer1 = player1.pop(0)
            tieCardPlayer2 = player2.pop(0)
            usedCards.extend([tieCardPlayer1, tieCardPlayer2])
        else:
            break

print('Game over.\n Player 1 has', len(player1),
      'cards.\n Player 2 has', len(player2), 'cards.')
