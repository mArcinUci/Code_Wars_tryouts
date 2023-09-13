'''Imagine a lively dice game where four friends, affectionately known as p1, p2, p3, and p4, come together for an exciting gaming session. Here's how it unfolds: in each round, all players roll a pair of standard six-sided dice.
The player with the lowest total score is promptly eliminated from the game. But what if two or more players happen to share this dubious honor of the lowest score? In such cases, we introduce a tiebreaker: the player among them with the lowest score from their first dice roll gets the boot.
If, despite these measures, we still have players with identical rolls in the exact same order, all players should go for another round of rolls. This electrifying process of elimination keeps going until only one player emerges victorious as the undisputed winner.
Given a list of scores, documented meticulously in the order of each player's participation in every round, determine and declare the name of the triumphant player who stands as the last one standing.'''


def dice_game(scores):
    winner = ['p1','p2', 'p3', 'p4']
    overtime_1 = []
    overtime_2 = []
    overtime_3 = []

    round_1 = scores[:4]

    round_1_score = [sum(x) for x in round_1]
    for i in  round_1_score:
        if min(round_1_score) == i:
            overtime_1.append(i)
    if len(overtime_1) == 1:
        loosing_score = min(round_1)
        del winner[round_1.index(loosing_score)]
    if len(overtime_1) == 2:
        loosing_score = [x for x in round_1 if sum(x) == overtime_1[0]]
        if loosing_score[0][0] > loosing_score[1][0]:
            del winner[round_1.index(loosing_score[1])]
        if loosing_score[0][0] < loosing_score[1][0]:
            del winner[round_1.index(loosing_score[0])]


    print(winner)    
    
dice_game([(6, 2), (4, 5), (3, 4), (4, 3), (5, 4), (5, 5), (1, 5), (4, 3), (1, 5), (1, 5), (5, 6), (2, 2)])



    