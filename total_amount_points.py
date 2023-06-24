def win_strat(x, y):
    if x > y:
        return 3

    return 0

def tie_strat(x, y):
    if x == y:
        return 1

    return 0


def points(games):
    strats = [win_strat, tie_strat]

    points = 0

    for game in games:
        x, y = game.split(':')
        
        for strat in strats:
            points += strat(x, y)
    
    return points
