e_n = {
    "ZERO": '0',
    "ONE": '1',
    "TWO": '2',
    "THREE": '3',
    "FOUR": '4',
    "FIVE": '5',
    "SIX": '6',
    "SEVEN": '7',
    "EIGHT": '8',
    "NINE": '9'
}
n_e = {
     '0':"ZERO",
     '1':"ONE",
     '2':"TWO",
     '3':"THREE",
     '4':"FOUR",
     '5':"FIVE",
     '6':"SIX",
     '7':"SEVEN",
     '8':"EIGHT",
     '9':"NINE"
}


def operation(n1, n2, oper):
    if oper == "+":
        return n1 + n2
    if oper == "-":
        return n1 - n2
    if oper == "x":
        return n1 * n2
    if oper == "/":
        return n1 // n2

eq = input()
op = []
numbs = []
i = 0
proper = True
numb = ''

while i < len(eq):
    if eq[i] in ["+", "-", "x", "/", "="]:
        op.append(eq[i])
        numbs.append(numb[:])
        numb = ''
        i += 1
        continue
    else:
        for e in e_n.keys():
            if eq[i:].startswith(e):
                numb = numb + e_n[e]
                i = i + len(e)
                break
        else:
            proper = False
            print("Madness!")
            break

if proper and len(numbs) != len(op):
    proper = False
    print("Madness")

if proper:
    line1 = ''
    for i in range(len(numbs)):
        line1 += numbs[i]+op[i]

    _answer = int(numbs[0])
    for i in range(1, len(numbs)):
        _answer = operation(_answer, int(numbs[i]), op[i-1])

    line2 = ''
    if _answer<0:
        line2 = '-'+line2
        for e in str(-1*_answer):
            line2 += n_e[e]
    else:
        for e in str(_answer):
            line2 += n_e[e]

    print(line1)
    print(line2)




