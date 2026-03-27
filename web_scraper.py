import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

books = []

for book in soup.find_all("article", class_="product_pod"):
    name = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    rating = book.p["class"][1]

    books.append([name, price, rating])

# Convert to DataFrame
df = pd.DataFrame(books, columns=["Name", "Price", "Rating"])

# Save to CSV
df.to_csv("books.csv", index=False)

print("Data scraped and saved to books.csv")