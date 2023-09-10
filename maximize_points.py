'''Two teams are playing a game of tennis. The team sizes are the same and each player from the first team plays against the
 corresponding player from the second team.
proper description on ----->   https://www.codewars.com/kata/58fec262184b6dc30800000d
'''

def maximize_points(team1, team2):
    count = 0
    count_possibilities = []
    team1.sort()
    team2.sort()
    
    for i in range(len(team1)):
        team1.append(team1.pop(team1.index(team1[0])))
        power_poind_difference = [x1 - x2 for (x1, x2) in zip(team1,team2)]
        for i in power_poind_difference:
            if i > 0:
                count +=1
        count_possibilities.append(count)
        count = 0 
    return max(count_possibilities)

print(maximize_points([7, 19, 23, 18, 38, 37, 38, 40], [21, 12, 1, 0, 13, 38, 25, 49]))


'''def maximize_points(a,b):
    a,b = map(sorted,(a,b))
    return max(sum(x>y for x,y in zip(a[i:],b)) for i in range(len(a)))'''

'''def maximize_points(*teams):
    a,b = map(sorted,teams)
    j = 0
    for p in a:
        j += p>b[j]
    return j'''