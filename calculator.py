num1=int(input("Enter your Number :"))
num2=int(input("Enter your Number :"))
# num3= num1+num2
print("select you calculator function")
cn=input("Enter your calcution symbol +,-,*,/,% :")
if cn=="+":
    print(num1 + num2)
elif cn=="-":
    print(num1 - num2)
elif cn=="*":
    print(num1 * num2)
elif cn=="/":
    print(num1 / num2)
elif cn=="%":
    print(num1 % num2)