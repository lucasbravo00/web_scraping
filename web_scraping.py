import bs4
import requests

base_url = "https://books.toscrape.com/catalogue/page-{}.html"
titles = []
stars = []
page_numbers = []

for n in range(1, 51):
    url = base_url.format(n)
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, 'lxml')
    books = soup.select('.product_pod')

    for book in books:
        if book.select(".star-rating.Four") or book.select(".star-rating.Five"):
            title = book.select_one("h3 a")["title"]
            titles.append(title)
            page_numbers.append(n)
            if book.select(".star-rating.Four"):
                stars.append(4)
            if book.select(".star-rating.Five"):
                stars.append(5)

print("\nThese are the books with 4 or 5 stars:\n")
for title, rating, page in zip(titles, stars, page_numbers):
    print(f"Page {page} | {rating}⭐ | {title}")
