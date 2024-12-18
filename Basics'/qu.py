# a = [1, 2, 3, 4]
# print(len(a))

# fruit = ["apple", "cherry", "orange"]
# fruit.append("strawberry")
# print(fruit)

# def calculate(num1, num2, operator):
#     if operator == '+':
#         result = num1 + num2
#     elif operator == '-':
#         result = num1 - num2
#     elif operator == '*':
#         result = num1 * num2
#     elif operator == '/':
#         if num2 != 0:
#             result = num1 / num2  
#         else: 
#             return "Error: Division by zero is not allowed"
#     else:
#         return "Error: Invalid operator"
#     return f"The result is: {result}"

# # num1 = float(input("Enter the first number: "))
# # num2 = float(input("Enter the second number: "))
# # operator = input("Enter the operator (+,-,*,/): ")

# print(calculate(10, 5, "+"))
# print(calculate(15, 5, "+"))

# print(calculate(100, 5, "+"))

# def greet(name):
#     print("Hello!", name)
#     print(f"Hello! {name}")
    
# greet("Tarun")
# greet("Pasang")


# a = [1, 2, 2, 3]
# for e in a:
#     print(e)

# if 5 in a and 3 in a:
#     print(True)
    
# if 3 in a or 5 in a:
#     print(True)

   
# # remove duplicate element
# a = [1, 2, 2, 3]
# b = []
# for e in a: # traversing all elements from list a
#     if e not in b: # checking if the element is already present or not in list b 
#         b.append(e) # if not in b, adds the element in list b 
# print(b)

# reverse
# a = [1, 2, 2, 3]
# a.sort(reverse=True)
# print(a)


# # multiply the second element with the first element   
# a = [1, 2, 5, 3]
# b = []
# for i in a:
#     b.append(i * 2)
# print(b)

# a = [1, 2, 5, 3]
# for x in range(0, len(a)):
#   print(a[x])
 
 
# name = ["ram", "rita", "sita"]
# age = [20, 21, 22]
# for i in range(len(name)):
#     print(f"My name is {name[i]}. My age is {age[i]}")

# # calculator..
# def calculate(num1, num2, operator):
#     if operator == "+":
#         return  num1 + num2
#     elif operator == "-":
#         return  num1 - num2
#     elif operator == "*":
#         return num1 * num2
#     elif operator == "/":
#         return num2!= 0
#     else:
#         return "Not valid operator"
    
# num1 = 3
# num2 = 4
# operator = "*"
# print(calculate(num1, num2, operator))
            
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "cherry":
    break   