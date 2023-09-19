'''Imagine a lively dice game where four friends, affectionately known as p1, p2, p3, and p4, come together for an exciting gaming session. Here's how it unfolds: in each round, all players roll a pair of standard six-sided dice.
The player with the lowest total score is promptly eliminated from the game. But what if two or more players happen to share this dubious honor of the lowest score? In such cases, we introduce a tiebreaker: the player among them with the lowest score from their first dice roll gets the boot.
If, despite these measures, we still have players with identical rolls in the exact same order, all players should go for another round of rolls. This electrifying process of elimination keeps going until only one player emerges victorious as the undisputed winner.
Given a list of scores, documented meticulously in the order of each player's participation in every round, determine and declare the name of the triumphant player who stands as the last one standing.'''


def dice_game(scores, loosing_player=[]):
    overtime_1 = []
    new_scores = []
    first_roll = []
    stamp = (4-len(loosing_player))
    next_round = scores[:stamp]
    next_round_score = [sum(x) for x in next_round]

    for i in next_round_score:
        if i == min(next_round_score):
            overtime_1.append(i)
    if len(overtime_1) == 1:
        loosing_score = min(next_round)
        for i in range(next_round.index(loosing_score), 5):
            if i not in loosing_player:
                loosing_player.append(i)
                break
    
    if len(overtime_1) > 1:
        loosing_score = min(next_round)
        for i in next_round:
            if i == loosing_score:
                first_roll.append(i[0])

        smallest_first_roll = min(first_roll)
        count_smallest_roll = [x for x in first_roll if x == smallest_first_roll]
        if len(count_smallest_roll) == 1:
            for i in range(next_round.index(smallest_first_roll), 5):
                if i not in loosing_player:
                    loosing_player.append(i)
                    break
    
    new_scores = scores[stamp:]
    if len(loosing_player)==3:
        for i in range(1,5):
            if i not in loosing_player:
                and_the_winner_is = 'p'+str(i)
                print(loosing_player)
                return and_the_winner_is
    else:
       return dice_game(new_scores, loosing_player)
    
  
#print(dice_game([(1, 5), (3, 1), (2, 3), (5, 3), (1, 2), (1, 2), (6, 3), (2, 2), (6, 3), (2, 2), (5, 5), (3, 1), (3, 1), (6, 6), (6, 4), (5, 3), (3, 4), (6, 4)]))
#print(dice_game([(5, 2), (2, 5), (5, 5), (2, 5), (6, 4), (6, 5), (6, 2), (6, 2), (3, 5), (6, 4), (4, 2), (5, 2), (3, 2), (6, 4), (1, 2), (5, 4), (5, 5)]))
print(dice_game([(4, 4), (4, 3), (1, 1), (1, 1), (3, 1), (4, 5), (2, 6), (2, 3), (1, 5), (5, 3), (4, 5), (5, 2), (2, 1)]))