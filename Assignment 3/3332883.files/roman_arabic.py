import sys
import os
import re
import itertools
import time
timeout = time.time() + 28

def error():
    print('The input is not a valid arabic number,\n  or is too large an arabic number,\n  or is not a valid (possibly generalised) roman number,\n  depending  on what is expected.')
    return
def error_2():
    print('The input is not a valid arabic number,\n  or is too large an arabic number,\n  or is not a valid (possibly generalised) roman number,\n  depending  on what is expected.')
    return
def input_error():
    print('I expect one, two or three command line arguments,\n  the second one being "minimally" in case two of those are provided\n  and "using" in case three of those are provided.')
    return
def arab_to_roman(arab):
    value = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    letter = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
    # since we need to recognise the largest number first, we need to reverse the list
    value = list(reversed(value))
    letter = list(reversed(letter))
    # Checked range already:
    roman = ''
    while arab > 0:
        for _ in range(len(value)):
            if arab >= value[_]:
                roman = roman + letter[_]
                arab -= value[_]
                break
    print(roman)
    return roman
def roman_to_arab_customise(roman, value, letter, mode):

    test_string = "^"
    start = 1
    if len(letter) % 2 == 0:
        for _ in range(len(letter)):
            if _ % 2 != 0:
                if start == 1:
                    if _ == 0:
                        test_string = test_string + letter[_] + '{0,3}'
                    else:
                        test_string = test_string +'('+ letter[_] + letter[_-1]+ '|' +letter[_-1] + '?'+letter[_] + '{0,3})'
                    start = 0
                else:
                    test_string = test_string +'('+ letter[_] + letter[_-2] + '|' + letter[_] + letter[_-1]+ '|' +letter[_-1] + '?'+letter[_] + '{0,3})'
            else:
                pass
    else:
        for _ in range(len(letter)):
            if _ % 2 == 0:
                if start == 1:
                    test_string = test_string + letter[_] + '{0,3}'
                    start = 0
                else:
                    test_string = test_string +'('+ letter[_] + letter[_-2] + '|' + letter[_] + letter[_-1]+ '|' +letter[_-1] + '?'+letter[_] + '{0,3})'
            else:
                pass
    test_string = test_string +  "$"
    valid_pattern = re.compile(test_string,re.VERBOSE)  # closing (EOS)
    if valid_pattern.search(roman) is None:
        if mode == 0:
            error_2()
            return None
        else:

            return None

    value = list(reversed(value))
    letter = list(reversed(letter))
    for _ in range(len(value)-1,0,-1):
        if _ % 2 == 0:
            value.insert(_, 9*10**((_-1)//2))
            letter.insert(_, letter[_-2]+letter[_])
        else:
            value.insert(_, 4*10**(_//2))
            letter.insert(_, letter[_-1]+letter[_])
    value = list(reversed(value))
    letter = list(reversed(letter))
    counter = 0
    arabic = 0
    while counter < len(roman):
        for _ in range(len(letter)):
            if roman[counter:(counter + len(letter[_]))] == letter[_]:
                arabic += value[_]
                counter += len(letter[_])
    if mode == 0:
        print(arabic)
    return arabic
def arab_to_roman_customise(arab, value, letter):
    # since we need to recognise the largest number first, we need to reverse the list
    # Checked range already:
    code_length = len(letter)
    if code_length % 2 == 0:
        max = '8'
        for _ in range(1,code_length // 2 ):
            max = max + '9'
    else:
        max = '3'
        for _ in range(code_length // 2 ):
            max = max + '9'
    if arab >  int(max):
        error_2()
        return
    value = list(reversed(value))
    letter = list(reversed(letter))
    for _ in range(len(value)-1,0,-1):
        if _ % 2 == 0:
            value.insert(_, 9*10**((_-1)//2))
            letter.insert(_, letter[_-2]+letter[_])
        else:
            value.insert(_, 4*10**(_//2))
            letter.insert(_, letter[_-1]+letter[_])
    value = list(reversed(value))
    letter = list(reversed(letter))

    roman = ''
    while arab > 0:
        for _ in range(len(value)):
            if arab >= value[_]:
                roman = roman + letter[_]
                arab -= value[_]
                break
    print(roman)
    return roman
def roman_to_arab(roman):
    value = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    letter = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
    result = [0]*13
    for _ in range(len(roman)):
        if roman[_] not in letter:
            error_2()
            return None
    # search for invalid input
    # Eliminate input more than 3 repetitive
    recogniser = ([[k,len(list(g))] for k, g in itertools.groupby(roman)])
    for _ in range(len(recogniser)):
        if recogniser[_][1] > 3:
            error_2()
            return None
        if recogniser[_][0] == 'V' or recogniser[_][0] == 'L' or recogniser[_][0] == 'D':
            if recogniser[_][1] > 1:
                error_2()
                return None
    # define pattern for search purpose
    valid_pattern = re.compile('^'+ # start searching from largest to lowest from the start of the string
                               'M{0,3}' +# only allow 3 repeater for M
                               '(CM|CD|D?C{0,3})' +  # only allow single repetition for CM 900, CD 400, max 3 C's 100, 200, 300
                                                 # or D with zero to three C's, 500 D, 600 DC, 700 DCC, 800 DCCC
                               '(XC|XL|L?X{0,3}) ' + # again only 1 repetition for 90 XC, 40 XL, max 3 X's 10, 20, 30
                                                 # or L with zero to three X's, 50 L, 60 LX, 70 LXX, 80 LXXX
                               '(IX|IV|V?I{0,3})' +  # same logic with IX 9, IV 4, max 3 I's 1, 2, 3
                                                 # or V with zero to three I's, 5 V, VI 6, VII 7, VIII 8.
                               '$',re.VERBOSE)  # closing (EOS)
    if valid_pattern.search(roman) is None:
        error_2()
        return None
    arabic = 0
    counter = 0
    # since we need to recognise the largest number first, we need to reverse the list
    value = list(reversed(value))
    letter = list(reversed(letter))
    while counter < len(roman):
        for _ in range(len(letter)):
            if roman[counter:(counter + len(letter[_]))] == letter[_]:
                arabic += value[_]
                counter += len(letter[_])
    print(arabic)
    return arabic

Argument = []
for _ in range(len(sys.argv)):
    if _ != 0:
        Argument.append(sys.argv[_])

convert = 0
# print( 'Number of arguments:', len(sys.argv), 'arguments.')
# print( 'Argument List:', str(sys.argv))
# print('------\n This is what you put in:')
# print(Argument)
# print('-------')
error = 0
if len(Argument) == 2 :
    if Argument[1] != 'minimally':
        input_error()
        error = 1
    # Check for non alphabetic input
    if error != 1:
        roman = Argument[0]
        if roman.isalpha():
            # print('THIS IS THE INPUTED: {}'.format(roman))
            code = list(set(roman))
            value = []
            for _ in range(len(code)):
                if _ % 2 == 0:
                    value.append(10**(_//2))
                else:
                    value.append(5*10**(_//2))
            value = list(reversed(value))
            base_list = ''
            for _ in range(len(code)):
                base_list = base_list + code[_]
            # print('BASELIST:{}'.format(base_list))
            possible_list = list(itertools.permutations(base_list,len(base_list)))
            # print('possible_list:')
            # print(possible_list)
            # print('Value: {}'.format(value))
            result = []
            result_code = []
            unused_code = []
            for _ in range(len(possible_list)):
                if roman_to_arab_customise(Argument[0],value,possible_list[_],1) is not None:
                    result.append(roman_to_arab_customise(Argument[0],value,possible_list[_],1))
                    result_code.append(list(possible_list[_]))
            if len(result) == 0:
                if len(code) < 26*2:
                    current_code = set(code)
                    unused_code = []
                    for _ in range(ord('A'),ord('Z')+1):
                        unused_code.append(chr(_))
                    for _ in range(ord('a'),ord('z')+1):
                        unused_code.append(chr(_))
                    unused_code = set(unused_code)
                    unused_code = unused_code - current_code
                    try_index = 0
                    upper_bound = len(base_list)
                    while len(result) == 0 and try_index < len(unused_code) and len(base_list) < 2*upper_bound:
                        if error == 1:
                            break
                        base_list = base_list + list(unused_code)[try_index]
                        possible_list = list(itertools.permutations(base_list,len(base_list)))
                        value = []
                        for _ in range(len(possible_list[0])):
                            if _ % 2 == 0:
                                value.append(10**(_//2))
                            else:
                                value.append(5*10**(_//2))
                        value = list(reversed(value))
                        for _ in range(len(possible_list)):
                            if time.time() >= timeout:
                                error_2()
                                error = 1
                                break
                            if roman_to_arab_customise(Argument[0],value,possible_list[_],1) is not None:
                                result.append(roman_to_arab_customise(Argument[0],value,possible_list[_],1))
                                result_code.append(list(possible_list[_]))
                        try_index += 1
                        if error == 1:
                            break
                if len(result) == 0:
                    error_2()
                    error = 1
            final_code = ''
            for _ in range(len(result)):
                if min(result) == result[_]:
                    for i in range(len(result_code[_])):
                        if result_code[_][i] not in unused_code:
                            final_code = final_code + result_code[_][i]
                        else:
                            final_code = final_code + '_'
                    break
            if error != 1:
                print('{} using {}'.format(min(result), final_code))
        else:
            error_2()
            error = 1

if len(Argument) == 3 :
    if Argument[1] != 'using':
        input_error()
        error = 1
    if error != 1:
        code = []
        value = []
        for _ in range(len(Argument[2])):
            code.append(Argument[2][_])
            if _ % 2 == 0:
                value.append(10**(_//2))
            else:
                value.append(5*10**(_//2))
        value = list(reversed(value))

        if Argument[0].isalpha():
            #check generalised roman is valid
            if Argument[2].isalpha() is False or len(code) != len(set(code)):
                print('The provided sequence of so-called gneneralised roman symbols is invalid,\n  either because it does not consist of letters only\n  or because some letters are repeated.')
                error = 1
            if error != 1:
                roman_to_arab_customise(Argument[0],value,code,0)
        else:
            if Argument[2].isalpha() is False or len(code) != len(set(code)):
                print('The provided sequence of so-called gneneralised roman symbols is invalid,\n  either because it does not consist of letters only\n  or because some letters are repeated.')
                error = 1
            if len(Argument[0]) >1:
                if int(Argument[0][0]) == 0:
                    print('The input is not a valid arabic number,\n  or is too large an arabic number,\n  or is not a valid (possibly generalised) roman number,\n  depending  on what is expected.')
                    error = 1
            if error != 1:
                arab_to_roman_customise(int(Argument[0]),value,code)

if len(Argument) > 3 or len(Argument) == 0 :
    input_error()
if len(Argument) == 1 :
    error = 0
    number = Argument[0]
    if number.isalpha():
        convert = roman_to_arab(number)
    else:
        if number[0] == '0':
            print('The input is not a valid arabic number,\n  or is too large an arabic number,\n  or is not a valid (possibly generalised) roman number,\n  depending  on what is expected.')
            error = 1
        if error != 1:
            number = int(number)
            if number >= 4000:
                print('The input is not a valid arabic number,\n  or is too large an arabic number,\n  or is not a valid (possibly generalised) roman number,\n  depending  on what is expected.')
                error = 1
            if error != 1:
                answer = arab_to_roman(number)
            # testing:
            # roman_to_arab(answer)
