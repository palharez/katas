def longest_consec(strarr, k):
    if k <= 0 or k > len(strarr):
        return ""
    longest = ""
    length = 0
    pos = 0
    for n in range(len(strarr)):
        if len(strarr[n]) > len(longest):
            longest = strarr[n]            
            length = len(longest)
        if n < len(strarr) - 1:
            if length > len(strarr[n + 1]) and length != len(strarr[n + 1]):
                longest = strarr[n]
                pos = strarr.index(longest)
                break
    kAux = 0
    for n in range((pos + 1), len(strarr)):
        kAux += 1
        if kAux == k:
            break
        longest += strarr[n]
    return longest


    

print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2))
print(longest_consec([], 3))
print(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 0))
print(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3))
print(longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1))