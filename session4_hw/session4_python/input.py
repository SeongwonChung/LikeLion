# 과제 5

#문제 1. 전화번호 받기
numbers=[]
for i in range(10):
  numbers.append(str(i))

phone_num = input("전화번호 입력: ")

for c in phone_num:
  if c not in numbers:
    phone_num = phone_num.replace(c,'')
print("저장된 전화번호: ",phone_num)


#문제 2. 영어이름 받기
first_name, last_name = input("영어이름 입력: ").split()
print(f"first name : {first_name.capitalize()}, last name: {last_name.capitalize()} ")