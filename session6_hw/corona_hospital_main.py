import requests
from bs4 import BeautifulSoup
from corona_hospital_functions import get_info
import csv

file = open("corona_hospital.csv", mode="w", newline="")
writer = csv.writer(file)
writer.writerow(["city", "district", "name", "contact"])

print("Crawling ... ")
hospital_html = requests.get('https://www.mohw.go.kr/react/popup_200128_3.html')
hospital_html.encoding = 'utf-8'

hospital_soup = BeautifulSoup(hospital_html.text, "html.parser")

# 이제부터 시도, 시군구, 선별진료소(이름), 전화번호 크롤링 후 csv 파일에 저장하시면 됩니다!
hospital_table = hospital_soup.find("tbody", {"class" : "tb_center"})
hospital_list = hospital_table.find_all("tr")

final_result = []

final_result += get_info(hospital_list)

for result in final_result:
    row = []
    row.append(result["city"])
    row.append(result["district"])
    row.append(result["name"])
    row.append(result["contact"])

    writer.writerow(row)

print("Crawling END")