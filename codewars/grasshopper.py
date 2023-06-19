def a_strat(score):
    if 90 <= score <= 100:
        return 'A'
    
    return False
    
def b_strat(score):
    if 80 <= score < 90:
        return 'B'
    
    return False

def c_strat(score):
    if 70 <= score < 80:
        return 'C'
    
    return False

def d_strat(score):
    if 60 <= score < 70:
        return 'D'
    
    return False

def f_strat(score):
    return 'F'


def get_grade(s1, s2, s3):
    strats = [
        a_strat,
        b_strat,
        c_strat,
        d_strat,
        f_strat,
    ]
    
    avg = (s1 + s2 + s3) // 3
    
    for strat in strats:
        valid = strat(avg)

        if valid:
            return valid
