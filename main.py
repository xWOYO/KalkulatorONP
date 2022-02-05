from collections import deque

dane = []

def priority(sign):
        if sign == "(":
            return 0
        if sign == ")":
            return 1
        if sign == "+":
            return 1
        if sign == "-":
            return 1
        if sign == "*":
            return 2
        if sign == "/":
            return 2
        if sign == "^":
            return 3

def translateToONP(equation):
    global place
    place = 0
    length = len(equation)
    pile = create_stack()
    temp = ""
    con = ""

    while place < length:
        # print(dane)
        # print(equation[place])
        if place == 0 and equation[place] == "-":
            temp = temp + "-"
            place = place + 1


        if equation[place].isdigit():
            while place < length and equation[place].isdigit():
                temp = temp + equation[place]
                place = place + 1
            dane.append(temp)
            temp = ""


        elif equation[place] == "(":
            push(pile, "(")
            place = place + 1
            if equation[place] == "-":
                temp = temp + "-"
                place = place + 1


        elif equation[place] == ")":
            while not check_empty(pile) and top(pile) != "(":
                con = con + top(pile)
                dane.append(con)
                pop(pile)
                con = ""
            if not check_empty(pile) and top(pile) == "(":
                pop(pile)
            place = place + 1


        elif equation[place] == "+" or equation[place] == "-" or equation[place] == "*" or equation[place] == "/" or equation[place] == "^":
            if check_empty(pile) or priority(equation[place]) > priority(top(pile)):
                push(pile, equation[place])
                place = place + 1
            else:
                while not check_empty(pile) and priority(equation[place]) <= priority(top(pile)):
                    con = con + top(pile)
                    dane.append(con)
                    pop(pile)
                    con = ""
                push(pile, equation[place])
                place = place + 1
            if equation[place] == "-":
                temp = temp + "-"
                place = place + 1

    while not check_empty(pile):
        con = con + top(pile)
        dane.append(con)
        pop(pile)
        con = ""

def calculate():
    numerki = create_stack()
    x = 0.0
    y = 0.0
    action = 0
    while action < len(dane):
        if dane[action][0].isdigit() or (dane[action][0] == "-" and len(dane[action]) > 1):
            push(numerki, int(dane[action]))
            action = action + 1
        else:
            y = int(top(numerki))
            pop(numerki)
            x = int(top(numerki))
            pop(numerki)
            if dane[action] == "+":
                push(numerki, x + y)
            elif dane[action] == "-":
                push(numerki, x - y)
            elif dane[action] == "/":
                push(numerki, x / y)
            elif dane[action] == "*":
                push(numerki, x * y)
            elif dane[action] == "^":
                push(numerki, pow(x, y))
            action = action + 1
    wynik = top(numerki)
    print("Wynik to: ", wynik)


def create_stack():
    stack = []
    return stack

def check_empty(stack):
    return len(stack) == 0

def push(stack, item):
    stack.append(item)

def pop(stack):
    if (check_empty(stack)):
        return "stack is empty"
    return stack.pop()

def top(stack):
    if (check_empty(stack)):
        return "stack is empty"
    return stack[-1]



input = input("Podaj równanie: ")
translateToONP(input)
print("Twoje równanie w notacji ONP: " + " ".join(dane))
calculate()
