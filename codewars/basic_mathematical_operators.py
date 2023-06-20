def basic_op(operator, value1, value2):
    operators = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
        
    }
    
    return operators[operator](value1, value2)
