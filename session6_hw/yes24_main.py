import requests
from bs4 import BeautifulSoup
import csv
from yes24_functions import get_info

file = open("yes24.csv", mode="w", newline="")
writer = csv.writer(file)
writer.writerow(["title","img_src", "author", "publisher", "price", "abstract"])
final_result=[]
for p in range(20):
    try:
        print(f"Crawling page{p+1}...")
        yes_html = requests.get(f"http://www.yes24.com/24/category/bestseller?CategoryNumber=001&sumgb=03&PageNumber={p+1}")
        yes_soup = BeautifulSoup(yes_html.text, "html.parser")

        yes_table = yes_soup.find("table", {"id" : "category_layout"})
        yes_list = yes_table.find_all("tr")

        book_list=[]
        abstract_list=[]

        for i in range(len(yes_list)):
            if i%2 == 0:
                book_list.append(yes_list[i])
            else: 
                abstract_list.append(yes_list[i])

        final_result.append(get_info(book_list,abstract_list))
    except: 
        print(f"{p+1}page crawling error")
        break
for result in final_result:
    for book_info in result:
        row = []
        row.append(book_info["title"])
        row.append(book_info["img_src"])
        row.append(book_info["author"])
        row.append(book_info["publisher"])
        row.append(book_info["price"])
        row.append(book_info["abstract"])

        writer.writerow(row)

print("Crawling END")
