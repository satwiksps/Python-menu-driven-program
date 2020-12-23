while True:
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("1. Program to print Armstrong numbers within an interval")
    print("2. Python program to display prime numbers within an interval.")
    print("3. Mark List of Students.")
    print("4. Caesar Cipher encryption.")
    print("5. Caesar Cipher decryption.")
    print("6. A Number Pattern Program.")
    print("7. Multiplication Table.")
    print("8. Factorial of a number.")
    print("9. Fibonacci Series")
    print("10. Sum of n Natural numbers")
    print("11. A simple calculator.")
    selection=int(input("Enter Choice :"))
    if selection==1:
        # Program to print Armstrong numbers in a certain interval
        lower=int(input("Enter the Lower Value :"))
        upper=int(input("Enter the Upper Value :"))
        for num in range(lower,upper+1):
            order=len(str(num))
            sum=0
            temp=num
            while temp>0:
                digit=temp%10
                sum+=digit**order
                temp//=10
            if num==sum:
                    print(num)
    elif selection==2:
        # Python program to display all the prime numbers within an interval
        lower=int(input("Enter the Lower Value :"))
        upper=int(input("Enter the Upper Value :"))
        print("Prime numbers between", lower, "and", upper, "are:")
        for num in range(lower,upper+1):
            for i in range(2,num):
                    if (num%i)==0:
                        break
            else:
                print(num)
         
    elif selection==3:
        # Mark List of Students.
        nameinput=input("Enter Student's Name :")
        student_name=nameinput
        score={'Peter':94,'Rahul':99,'Tom':87,'Jack':99,'Nischay':94,'Arun':99,'Jerry':20,'Satwik':100}
        for student in score:
            if student==student_name:
                print(score[student])
                break
        else:
            print('No entry with that name was found.')
    elif selection==4:
        #Caesar Cipher encryption
        string=input("Enter the string :")
        shift=int(input("Enter the number of letters to be shifted :"))
        cipher=''
        for char in string:
            if char==' ':
                cipher=cipher+char
            elif char.isupper():
                cipher=cipher+chr((ord(char)+shift-65)%26+65)
            else:
                cipher=cipher+chr((ord(char)+shift-97)%26+97)
        print("Original string :",string)
        print("After encryption :",cipher)
    elif selection==5:
        #Caesar Cipher decryption
        string=input("Enter the string do be depcrypted :")
        shift=int(input("Enter the number of letters shifted for encryption :"))
        cipher=''
        for char in string:
            if char==' ':
                cipher=cipher+char
            elif char.isupper():
                cipher=cipher+chr((ord(char)-shift-65)%26+65)
            else:
                cipher=cipher+chr((ord(char)-shift-97)%26+97)
        print("Original string :",string)
        print("After decryption :",cipher)
    elif selection==6:
        #Pattern Program
        rows=int(input("Enter the number of rows :"))
        for i in range(0,rows):
            for j in range(rows,i,-1):
                print(j,'',end='')
            for l in range(i):
                print('',end='')
            for k in range(i+1,rows+1):
                print(k,'',end='')
            print()
    elif selection==7:
        #Multiplication Table
        n=int(input("Enter a number"))
        for i in range (1,11):
            print(n,"X",i,"=",n*i)
    elif selection==8:
        #Factorial of a number
        def factorial(n):
            if n == 0:
                return 1
            else:
                return n * factorial(n-1)
        n = int(input("enter a number to find factorial"))
        print(factorial(n))
    elif selection==11:
        #A simple calculator
        def add(x, y):
            return x + y
        def subtract(x, y):
            return x - y
        def multiply(x, y):
            return x * y
        def divide(x, y):
            return x / y
        print("Select operation.")
        print("1.Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Divide")
        choice = input("Enter choice(1/2/3/4): ")
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        if choice == '1':
            print(num1,"+",num2,"=", add(num1,num2))
        elif choice == '2':
            print(num1,"-",num2,"=", subtract(num1,num2))
        elif choice == '3':
            print(num1,"*",num2,"=", multiply(num1,num2))
        elif choice == '4':
            print(num1,"/",num2,"=", divide(num1,num2))
        else:
            print("Invalid input")
    elif selection==10:
        #Sum of n natural numbers
        num = int(input("Enter a number: "))
        if num < 0:
            print("Enter a positive number")
        else:
            sum = 0
            while(num > 0):
                sum += num
                num -= 1
            print("The sum is",sum)  

    elif selection==9:
        #Fibonacci series
        x,y = 0,1
        while y<50:
            print(y)
            x,y = y,x+y
