# WAP to not allow children pass through:
#     - If below 18 years shoukd return print Children not allowed
#     - If age is above 60 years, ticket is free.
#     - If age is above 18 years and below 60 years then should return "You can pass name. Ticket price"

# def ticket_pass(name, age):
#     price = 200
#     if age < 18:
#         print("Children not allowed")
#     elif age > 60:
#         print("Ticket is free")
#     else:
#         print(f"You can pass {name}. Ticket price {price}")
        
# name = input("Enter your name:")
# age = int(input("Enter your age:"))
# ticket_pass(name, age)                

# q = "I love football"
# r = "I don't love football"
# common = []
# for i in q.split():
#     if i in r.split():
#         common.append(i)

# print(common)

q = "I love football"
r = "I don't love football"
unique = []
for i in r.split():
    if i in q.split():
        unique.append(i)
print(unique)