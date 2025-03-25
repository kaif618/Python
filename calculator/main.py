import art
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1-n2

def multiple(n1, n2):
    return n1*n2

def divide(n1,n2):
    if n2==0:
        print("♾️")
    return n1/n2

def mod(n1, n2):
    if n2==0:
        print("Error Modulo by 0 is not possible")
    return n1%n2

operations_dic = {
    "+" : add,
    "-" : subtract,
    "*" : multiple,
    "/" : divide,
    "%" : mod,
}

def calculator():
    calculating = True
    print(art.logo)
    user_num1 = float(input("Enter the first number: "))
    while calculating:
        for keys in operations_dic:
            print(keys)

        user_operator = input("What type of operation you want to perform: ")
        if user_operator not in operations_dic:
            print("Please enter a valid operation")
            continue

        user_num2 = float(input("Enter the second number: "))

        result = operations_dic[user_operator](user_num1, user_num2)
        print(f"{user_num1} {user_operator} {user_num2} = {result}")

        user_continue = input(f"Type Y to continue calculating with {result} or type 'n' to start new calculation: ").lower()

        if user_continue == "n":
            calculating = False
            print("\n" * 100)
            calculator()
        else:
            user_num1 = result

calculator()






