# a = [1, 2, 3, 4, 5]
# for i in a:
#     print(i)
#     if i == 3:
#         break

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     continue
#   print(x)    

# for x in range(6):
#   print(x)
# else:
#     print("Finally finished")  
  
# # increment the sequence with 3
# for p in range(2, 20, 3):
#     print(p) 

# i = 1
# while i < 6:
#   print(i)
#   i += 1

# a = "pasang"
# print(a[2:6])
  
# b = [1, 2, 3, 4]
# print(b[0:2])

# c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# a = "pasang"
# print(a[::-1])

a = "112-223-4567-8910"
b = "456-229-111"
# print(a.split("-"))

def converter(data):
  splited_data = data.split("-")
  value = splited_data[:-1]
  last = splited_data[-1]
  pasang = []
  for i in value:
    pasang.append(len(i) * '*')
  final_value = ""
  for i in pasang:
    final_value += i + '-'
  final_value += last   
  return final_value

print(converter(a))
print(converter(b))

