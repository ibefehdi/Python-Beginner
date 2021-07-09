def menu():
    print(f"Enter 1 for sum of {var1} and {var2}\n"
    f"Enter 2 for sub of {var1} and {var2}\n"
    f"Enter 3 for mul of {var1} and {var2}\n"
    f"Enter 4 for div of {var1} and {var2}\n"
    "Enter 5 to Choose different numbers\n"
    "Enter 0 to end the program\n"
    "\n")
def calculator(num1,num2,sign):
    if sign=="+":
        return (num1+num2)
    elif sign == "-":
        return(num1-num2)
    elif sign == "/":
        return (num1/num2)
    elif sign == "*":
        return(num1*num2)
try:
    var1 = eval(input("Enter the first number: "))
    var2 = eval(input("Enter the second number: "))
    bool = True
    menu()
    while bool:        
        choice = eval(input("Enter your choice: "))
        if (choice==1):
            print(f"The sum of the numbers {var1} and {var2} =",calculator(var1,var2,"+"))
            menu()
        elif(choice==2):
            print(f"The difference of the numbers {var1} and {var2} =",calculator(var1,var2,"-"))
            menu()
        elif(choice==3):
            print(f"The multiple of the numbers {var1} and {var2} =",calculator(var1,var2,"*"))
            menu()
        elif(choice==4):
            print(f"The division of the numbers {var1} and {var2} =",calculator(var1,var2,"/"))
            menu()
        elif(choice==5):
            print("\n")
            var1 = eval(input("Enter the first number: "))
            var2 = eval(input("Enter the second number: "))
        elif(choice==0):
            bool=False
        else:
            print("Invalid Choice Please Choose From the Following")
            menu()
except(NameError):
    print("you might have entered a wrong input")