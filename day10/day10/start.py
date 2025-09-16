from art import logo

print(logo)


#Add
def Add(n1, n2):
    return n1 + n2


#substract

def Substract(n1, n2):
    return n1 - n2


#multiply

def Multiply(n1, n2):
    return n1 * n2


#divide

def Divide(n1, n2):
    return n1 / n2


operations = {
    "+": Add,
    "-": Substract,
    "*": Multiply,
    "/": Divide
}


def calculator():
    print(logo)
    num1 = float(input("Whats the first number? : "))

    for op in operations:
        print(op)

    should_continuo = True
    while should_continuo:
        op_sybmol = input("Pick an operation from the line above : ")
        num2 = float(input("Whats the next number? : "))
        function = operations[op_sybmol]
        answer = function(num1, num2)
        print(f"{num1} {op_sybmol} {num2} = {answer}")
        if input(f"type 'y' to continuo calculating with {answer} or 'n' to start new calculate : ") == "y":
            num1 = answer
        else:
            should_continuo = False
            calculator()