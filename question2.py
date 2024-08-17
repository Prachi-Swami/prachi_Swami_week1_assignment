


# Create a program that uses conditional
# statements to determine if a number is positive,
# negative, or zero.

while True:
  try:
   number=int(input("enter your number: "))
   if number>0:
      print("Number is POSITIVE ")
   elif number<0:
      print("number is NEGATIVE")
   elif number==0:
      print("number is ZERO")  
  except:
    print("Invalid input. Please enter a valid number.")




