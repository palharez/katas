def accum(s):
    resp = []

    for i, c in enumerate(s):
        temp = []
        for y in range(i+1):
            if y == 0:
                temp.append(c.upper())
            else:
                temp.append(c.lower())
        
        resp.append(''.join(temp))
    
    return '-'.join(resp)
