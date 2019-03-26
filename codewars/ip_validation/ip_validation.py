from string import ascii_letters as ascii

def is_valid_IP(strng):
    arrayIp = strng.split('.')

    if not (len(arrayIp) > 3 and len(arrayIp) < 5):
        return False

    for n in arrayIp:

        if n in ascii:
            return False

        if len(n) > 1 and n[0] == '0':
            return False

        if ' ' in n:
            return False

        if int(n) < 0 or int(n) > 255:
            return False
        
    return True
        

if __name__ == "__main__":
    assert is_valid_IP('12.255.56.1') == True
    assert is_valid_IP('abc.def.ghi.jkl') == False
    assert is_valid_IP('123.045.067.089') == False
    assert is_valid_IP('0.0.0.0') == True
    assert is_valid_IP('12.34.56 .1') == False
    assert is_valid_IP('12.34.56.-1') == False
    assert is_valid_IP('') == False
    assert is_valid_IP('130.90.113.0') == True