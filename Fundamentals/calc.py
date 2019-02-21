a='y'
while a=='y' or a=='Y':
    def add():
        res=num1+num2
        print("Addition Result=",res)
        a=input("Do you want to run once more")

    def sub():
        res=num1-num2
        print("Subtraction Result=",res)
        a=input("Do you want to run once more")
    def multiply():
        res=num1*num2
        print("Multiply Result=",res)
        a=input("Do you want to run once more")
    def div():
        res=num1/num2
        print("Division Result=",res)
        a=input("Do you want to run once more")



    print("**************Calculator************")
    print("-------------------------------------")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiply")
    print("4.Divide")

    print("********************")
    print("Enter two number")
    num1=input("Enter First Name:")
    num2=input("Enter Second Number:")
    num1=int(num1)
    num2=int(num2)

    print("--------------------------")
    print("Enter the number to choose the operation from the above menu:",end="")
    ch=input()
    ch=int(ch)

    if ch==1:
        add()
    else:
        if ch==2:
            sub()
        else:
            if ch==3:
                multiply()
            else:
                div()

