# Write a Python program to perform basic arithmetic operations (addition, subtraction multiplication, division)
while True:
  try:
    number1=int(input("enter number1:"))
    number2=int(input("enter number2: "))
    operator=input("select operator you want to perform: ")
    if operator=="+":
      print(number1+number2)
    elif operator=="-":
      print(number1-number2)
    elif operator=="*":
      print(number1+number2) 
    elif operator=="/":
      print(number1/number2)
    else:
      print("enter valid operator")  
  except ValueError:
    print("enter valid input ")
  except ZeroDivisionError:
    print("division by zero not allowed")   
