"""
Kyu Rank: 5
Write a function that takes a string of parentheses, and determines
if the order of the parentheses is valid. The function should return
 true if the string is valid, and false if it's invalid.

Examples
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
Constraints
0 <= input.length <= 100

Along with opening (() and closing ()) parenthesis, 
input may contain any valid ASCII characters. Furthermore, 
the input string may be empty and/or not contain any parentheses at all. 
Do not treat other forms of brackets as parentheses (e.g. [], {}, <>).
"""

def valid_parentheses(string):
    count = 0

    for char in string:
        if char == '(': 
            count += 1

        if char == ')': 
            count -= 1

        if count < 0:
            return False

    return True if count == 0 else False

if __name__ == '__main__':
    assert valid_parentheses("  (") == False
    assert valid_parentheses(")test") == False
    assert valid_parentheses("") == True
    assert valid_parentheses("hi())(") == False 
    assert valid_parentheses("hi(hi)()") == True
