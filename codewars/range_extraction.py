"""
A format for expressing an ordered list of integers is to use a comma separated list of either

individual integers
or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. 
The range includes all integers in the interval including both endpoints. 
It is not considered a range unless it spans at least 3 numbers. For example "12,13,15-17"
Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string in the range format.

Example:

solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-6,-3-1,3-5,7-11,14,15,17-20"
Courtesy of rosettacode.org
"""

def solution(args):
    response = []

    sub_array = []

    add_last_in_final = False

    for i in range(len(args)):
        n = args[i]

        if not sub_array:
            sub_array.append(n)
            continue
        
        if n == sub_array[-1] + 1 and i + 1 != len(args):
            sub_array.append(n)

        else:
            if i + 1 == len(args) and n == sub_array[-1] + 1:
                sub_array.append(n)
            elif i + 1 == len(args):
                add_last_in_final = True

            if len(sub_array) <= 2:
                response.extend([str(k) for k in sub_array])
            else:
                response.append('%s-%s' % (sub_array[0], sub_array[-1]))

            sub_array = [n]
    
    if add_last_in_final:
        response.append(str(args[-1]))
        
    return ','.join(response)


if __name__ == '__main__':
    print(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]), '-6,-3-1,3-5,7-11,14,15,17-20')
    print(solution([-3,-2,-1,2,10,15,16,18,19,20]), '-3--1,2,10,15,16,18-20')