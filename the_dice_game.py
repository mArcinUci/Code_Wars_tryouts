'''Imagine a lively dice game where four friends, affectionately known as p1, p2, p3, and p4, come together for an exciting gaming session. Here's how it unfolds: in each round, all players roll a pair of standard six-sided dice.
The player with the lowest total score is promptly eliminated from the game. But what if two or more players happen to share this dubious honor of the lowest score? In such cases, we introduce a tiebreaker: the player among them with the lowest score from their first dice roll gets the boot.
If, despite these measures, we still have players with identical rolls in the exact same order, all players should go for another round of rolls. This electrifying process of elimination keeps going until only one player emerges victorious as the undisputed winner.
Given a list of scores, documented meticulously in the order of each player's participation in every round, determine and declare the name of the triumphant player who stands as the last one standing.'''


def dice_game(scores, winner=[]):
    overtime_1 = []
    new_scores = []
    stamp = (4-len(winner))
    next_round = scores[:stamp]
    next_round_score = [sum(x) for x in next_round]
    print(next_round_score)
    
    if len(winner)==3:
        return winner 
    
    for i in next_round_score:
        if min(next_round_score) == i:
            overtime_1.append(i)
    if len(overtime_1) == 1:
        loosing_score = min(next_round)
        winner.append(next_round.index(loosing_score))
        new_scores = scores[stamp:]
    if len(overtime_1) == 2:
        loosing_score = [x for x in next_round if sum(x) == overtime_1[0]]
        if loosing_score[0][0] > loosing_score[1][0]:
            winner.append(next_round.index(loosing_score[1]))
            new_scores =  scores[stamp:]           
        if loosing_score[0][0] < loosing_score[1][0]:
            winner.append(next_round.index(loosing_score[0]))
            new_scores =  scores[stamp:]
        if loosing_score[0][0] == loosing_score[1][0]:
            new_scores =  scores[stamp:]
    print(f'----and the looser here is {winner}')
     
    dice_game(new_scores, winner)
    
  
print(dice_game([(6, 2), (4, 3), (3, 4), (5, 4), (3, 5), (1, 5), (43, 3), (1, 5), (1, 5), (5, 6), (2, 2)])) 