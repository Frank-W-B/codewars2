def to_alternating_case(string):
    return_string = [] 
    for letter in string:
        if letter.isalpha():
            if letter.islower():
                return_string.append(letter.upper())
            else:
                return_string.append(letter.lower())
        else:
            return_string.append(letter)

    return ''.join(return_string)    

#best practice code
def to_alternating_case_bp(string):
    return string.swapcase()

def to_alternating_case_int(string):
    return ''.join([c.upper() if c.islower() else c.lower() for c in string])

if __name__ == '__main__':
    #assert_equals(to_alternating_case("HELLO WORLD"), "hello world")
    #Test.assert_equals(to_alternating_case("hello WORLD"), "HELLO world")
    #Test.assert_equals(to_alternating_case("HeLLo WoRLD"), "hEllO wOrld")
    #Test.assert_equals(to_alternating_case("12345"), "12345")
    #Test.assert_equals(to_alternating_case("1a2b3c4d5e"), "1A2B3C4D5E")
    string = '1a2b3c4d5e'
    return_string = [] 
    for letter in string:
        if letter.isalpha():
            if letter.islower():
                return_string.append(letter.upper())
            else:
                return_string.append(letter.lower())
        else:
            return_string.append(letter)

    alt_case = ''.join(return_string)    
    alt_case2 = to_alternating_case(string)
    alt_case3 = to_alternating_case_bp(string)
    alt_case4 = to_alternating_case_int(string)
