import requests
from bs4 import BeautifulSoup
import pandas as pd


response = requests.get(
    "https://www.goodreads.com/shelf/show/fantasy")


fantasy_books = response.text

soup = BeautifulSoup(fantasy_books, "html.parser")


books = soup.find(name="div", class_="leftContainer")


book_name = []
book_autor = []
book_rating = []


book_list = books.find_all(name="div", class_="elementList")

for i in range(len(book_list)):
    try:
        name = book_list[i].find(name="a", class_="bookTitle").text
        author = book_list[i].find(name="a", class_="authorName").text
        rating = book_list[i].find(
            name="span", class_="smallText").text.split()[2]
        book_name.append(name)
        book_autor.append(author)
        book_rating.append(rating)
        print(name, author, rating)
    except IndexError:
        pass
    except AttributeError:
        pass


header = ["Book Name", "Author", "Rating"]


df = pd.DataFrame(list(zip(*[book_name, book_autor, book_rating])))
df.to_csv("fantasy_books.csv", index=False)
books_csv = pd.read_csv("fantasy_books.csv", names=header, skiprows=1)
books_csv.to_csv("fantasy_books.csv")
