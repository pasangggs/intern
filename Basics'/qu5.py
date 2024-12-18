import requests


url = "https://raw.githubusercontent.com/benoitvallon/100-best-books/refs/heads/master/books.json"
data = requests.get(url).json()

output = []

country_books = {}

for book in data:
    country = book['country']
    if country not in country_books:
        country_books[country] = []  # Initializing the list for the country
    country_books[country].append(book)  

# Convert the dictionary into the desired list format
for country, books in country_books.items():
    output.append({country: books})
    
# data = requests.get(url).json()

# country_name = []

# for i in data:
#     if i['country'] not in country_name:
#         country_name.append(i['country'])      
        

# output = [
#   {
#       'Nigeria': [{
#                 "author": "Chinua Achebe",
#                 "imageLink": "images/things-fall-apart.jpg",
#                 "language": "English",
#                 "link": "https://en.wikipedia.org/wiki/Things_Fall_Apart\n",
#                 "pages": 209,
#                 "title": "Things Fall Apart",
#                 "year": 1958
#             },
#             {
#                 "author": "Hans Christian Andersen",
#                 "imageLink": "images/fairy-tales.jpg",
#                 "language": "Danish",
#                 "link": "https://en.wikipedia.org/wiki/Fairy_Tales_Told_for_Children._First_Collection.\n",
#                 "pages": 784,
#                 "title": "Fairy tales",
#                 "year": 1836
#             }]
#   }]