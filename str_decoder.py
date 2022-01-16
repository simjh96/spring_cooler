import re

st = input()
word_dict = {"ZERO": '0',
             "ONE": '1',
             "TWO": '2',
             "THREE": '3',
             "FOUR": '4',
             "FIVE": '5',
             "SIX": '6',
             "SEVEN": '7',
             "EIGHT": '8',
             "NINE": '9',
             '+': '+',
             '-': '-',
             'x': '*',
             '/': '/',
             '=': '=',
             }
op_dict = {'+': '+',
           '-': '-',
           '*': '*',
           '/': '/',
           '=': '=',
           }


def parser(arr: str):
    # return (validity, '123+45')
    validity = True
    results = []

    # parse string
    _i = 0
    i = _i
    while _i < len(arr):
        while i < len(arr):
            i += 1
            result = word_dict.get(arr[_i:i])
            if result:   # is a word: add to results and head follow tail
                results.append(result)
                _i = i
                break

        else:   # if no match
            validity = False
            print("no match")
            return False, None

    # merge num
    i = 1
    blocks = []
    block = results[0]
    for i in range(1, len(results)):
        if op_dict.get(results[i-1]) == op_dict.get(results[i]):
            block += results[i]
        else:
            blocks.append(block)
            block = results[i]
    blocks.append(block)

    # check valid rotation
    # check valid elements
    for i in range(len(blocks)):
        if i % 2:
            if re.findall(r'[0-9]+', blocks[i]) or len(blocks[i]) != 1:
                print("is not op")
                print(blocks)
                return False, None
        else:
            if not re.findall(r'[0-9]+', blocks[i]) or not num_eval(blocks[i]):
                print("is not num")
                print(blocks)
                return False, None

    return validity, eval(''.join(blocks)[:-1])


def num_eval(arr: str):
    if re.findall(r'^0[0-9]+', arr):
        return False
    else:
        return True


print(parser(st))
