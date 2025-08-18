 
import requests

# # my_url = 'https://picsum.photos/'

# # response = requests.get(my_url)
# # print(response.status_code)

# my_url = 'https://picsum.photos/id/13/2500/1667'
# response = requests.get(my_url)
      


# with open('m_image.png', 'wb') as f:
#     f.write(response.content)



# city = 'Tashkent'
# my_api_key = 'c0f0658cf2fb8c082a50768721962ea0'
# my_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={my_api_key}&units=metric'

# response = requests.get(my_url)

# print(response.json())

my_title = input("Kino nomidagi biror so'zni kiriting")
my_url = f'https://www.omdbapi.com/?s={my_title}8&apikey=32d93822'
response = requests.get(my_url)
my_data = response.json()


for dict in my_data['Search']:
    print(dict['Title'])



    import json

def load_books():
    try:
        with open('books.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_books(books):
    with open('books.json', 'w') as file:
        json.dump(books, file, indent=4)

books = load_books()

while True:
    action = input("Choose action: add, update, delete, view, exit: ").lower()
    
    if action == "add":
        title = input("Book title: ")
        author = input("Author: ")
        books.append({"title": title, "author": author})
        save_books(books)
        print("Book added.")

    elif action == "update":
        title = input("Title of the book to update: ")
        for book in books:
            if book['title'].lower() == title.lower():
                book['title'] = input("New title: ")
                book['author'] = input("New author: ")
                save_books(books)
                print("Book updated.")
                break
        else:
            print("Book not found.")

    elif action == "delete":
        title = input("Title of the book to delete: ")
        books = [book for book in books if book['title'].lower() != title.lower()]
        save_books(books)
        print("Book deleted.")

    elif action == "view":
        for book in books:
            print(f"Title: {book['title']}, Author: {book['author']}")
    
    elif action == "exit":
        break
    else:
        print("Invalid action")
