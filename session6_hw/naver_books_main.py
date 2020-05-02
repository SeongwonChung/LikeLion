import requests
from bs4 import BeautifulSoup
import csv
from naver_books_functions import get_info

file = open("naver_books.csv", mode = "w", newline = "")
writer = csv.writer(file)
writer.writerow(["title", "author", "publisher", "pub_date", "price", "link", "img_src"])

final_result = []

for i in range(10):
    print(f"{i+1}page crawling...")
    books_html = requests.get(f"https://book.naver.com/category/index.nhn?cate_code=100&tab=new_book&list_type=list&sort_type=publishday&page={i+1}")

    books_soup = BeautifulSoup(books_html.text, "html.parser")

    books_list_box = books_soup.find("ol", {"class" : "basic"})
    books_list = books_list_box.find_all("li")

    final_result = final_result + get_info(books_list)

for result in final_result:
    row = []
    row.append(result["title"])
    row.append(result["author"])
    row.append(result["publisher"])
    row.append(result["pub_date"])
    row.append(result["price"])
    row.append(result["link"])
    row.append(result["img_src"])

    writer.writerow(row)

print("Crawling END")   
    
    
