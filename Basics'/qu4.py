def info(names, ages):
    return dict(zip(names, ages)) # zip() combines the two list into a dictionary

def get_age(name, people_dict):
    if name in people_dict:
        return f"{name} is {people_dict[name]} years old."
    else:
        return f"{name} is not in the list."

# Lists of names and ages
names = ["Pasang", "Tarun", "Yug", "Sabin"]
ages = ["21", "24", "24", "23"]

people_dict = info(names, ages) # Creating the dictionary
person_name = input("Enter a name: ")
print(get_age(person_name, people_dict))