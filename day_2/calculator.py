num1=float(input("enter 1st number :"))
char=input("enter operator like('+','-','*','/','%') :")
num2=float(input("enter 2nd number :"))
if char=='+':
    print("addition is : ",num1+num2)
elif char=='-':
        print("substraction is : ",num1-num2)
elif char=='*':
        print("multiplication is : ",num1*num2)
elif char=='/':
        print("division is : ",num1/num2)
elif char=='%':
        print("remainder is : ",num1%num2)

else:
       print("please enter valid operation")