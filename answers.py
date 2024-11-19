

# define the function
def calculator():
  
  # Tell the user to enter 1st number
  num1 = float(input("Enter first Number: "))

  # Tell the user to enter the second number
  num2 = float(input("Enter second number: "))

  # Prompt the user to enter the arithmetic operation she/he wants to perform
  operation = input("Enter the operation (+, -, *, /)")

  if operation == '+':
    answer = num1 + num2
    print(answer)
  
  elif operation == '-':
    answer = num1 - num2
    print(answer)

  elif operation == '*':
    answer = num1 * num2
    print(answer)
  
  elif operation == '/':

    # handles division by zero
    if num2 == 0:
      print("Error! float division by zero")
    else:
      answer = num1 / num2
      print(answer)

  else :
    print("Invalid operation!")

if __name__ == "__main__":
    calculator()




  