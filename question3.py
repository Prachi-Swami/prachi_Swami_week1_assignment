# Write a script that accepts user input and
# displays it in reverse order.
user_input = input("Enter a string: ")
reverse = ""
for char in user_input:
    reversed_input = char + reverse
print("Reversed string:", reversed_input)