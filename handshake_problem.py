'''Johnny is a farmer and he annually holds a beet farmers convention "Drop the beet".
Every year he takes photos of farmers handshaking. Johnny knows that no two farmers handshake more than once. He also knows that
 some of the possible handshake combinations may not happen.
However, Johnny would like to know the minimal amount of people that participated this year just by counting all the handshakes.
Help Johnny by writing a function, that takes the amount of handshakes and returns the minimal amount of people needed to perform 
these handshakes (a pair of farmers handshake only once).'''


def get_participants(handshakes):
    if handshakes ==0:
        return 0
    delta = 1+8*(int(handshakes))
    squere_root = delta**0.5
    answer = (1+squere_root)/2
    rounded_up_answer = int(-(-answer // 1))
    return rounded_up_answer


print(get_participants(8))



'''this I found as one of answers after submiting. It is preatty cool solution so I copied it:

def get_participants(handshakes):
    participants = 0
    while handshakes > 0:
        handshakes -= participants
        participants += 1
    return participants
    
    or this one:
    
    def get_participants(handshakes):
    # ...
    n=0
    while n*(n-1)/2 < handshakes:
        n+=1
    return n'''