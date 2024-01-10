firstNum=int(input("Enter your first number:"))
function=str(input("Enter the sum(+,/,*,-):"))
secondNum=int(input("Enter your Second number:"))

if function=='+':
    output=firstNum+secondNum
elif function=='/':
    output=firstNum/secondNum
elif function=='*':
    output=firstNum*secondNum
elif function=='-':
    output=firstNum-secondNum

print("Answer is:",output)