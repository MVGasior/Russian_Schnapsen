# This program is simulating a card game "Tysiac"
# Author : Mateusz Gąsior

def shuffle_and_handing_out():
    """


    :return:
    """
    global player1, player2, player3, musik
    import random
    colors = ['Kier', 'Karo', 'Pik', 'Trefl']
    figures = [
        {'Figures': 'As', 'Power': 11},
        {'Figures': 'Krol', 'Power': 4},
        {'Figures': 'Dama', 'Power': 3},
        {'Figures': 'Walet', 'Power': 2},
        {'Figures': '10', 'Power': 10},
        {'Figures': '9', 'Power': 0}]
    allCards = []
    for c in colors:
        for f in figures:
            aCard = f.copy()
            aCard['Color'] = c
            allCards.append(aCard)
    random.shuffle(allCards)
    player1 = []
    player2 = []
    player3 = []
    for i in range(len(allCards) - 3):
        if i % 3 == 0:
            player1.append(allCards[i])
        elif i % 3 == 1:
            player2.append(allCards[i])
        else:
            player3.append(allCards[i])
    musik = allCards[21:]
    return musik, player1, player2, player3


print(shuffle_and_handing_out())


def cards_on_hand(gamer, nazwa):
    """
    This function sort cards 'on hand' in color/power order
    and counting possible points from cards including 'meldunek'
    :param gamer: player's cards in Dir, Type : Dictionary
    :param nazwa: name of the player, Type : Char
    :return: Amount of points, Type : Int
    """
    pula = 0
    gamer.sort(key=lambda k: (k['Color'], k['Power']), reverse=True)
    print('----------', nazwa, '----------')
    for j in range(len(gamer)):
        print(gamer[j]['Color'], '\t', gamer[j]['Figures'])
        pula += gamer[j]['Power']
        if gamer[j]['Figures'] == 'Dama' and j != 0:

            if gamer[j - 1]['Figures'] == 'Krol' and gamer[j]['Color'] == gamer[j - 1]['Color']:
                print('Meldunek')
                if gamer[j]['Color']== 'Pik':
                    pula += 40
                elif gamer[j]['Color']== 'Trefl':
                    pula += 60
                elif gamer[j]['Color']== 'Karo':
                    pula += 80
                else:
                    pula+=100
    print('Ilosc punktow na rece:',pula)
    ret

"""
if __name__ == "__main__":
    Points_1 = cards_on_hand(player1, 'PLAYER 1')
    Points_2 = cards_on_hand(player2, 'PLAYER 2')
    Points_3 = cards_on_hand(player3, 'PLAYER 3')

    if Points_1 > Points_2 and Points_1 > Points_3:
        player1.extend(musik)
    elif Points_2 > Points_1 and Points_2 > Points_3:
        player2.extend(musik)
    else:
        player3.extend(musik)

    Points_1 = cards_on_hand(player1, 'PLAYER 1')
    Points_2 = cards_on_hand(player2, 'PLAYER 2')
    Points_3 = cards_on_hand(player3, 'PLAYER 3')
"""
