# 실습 2.
def gugudan_odd():
    for i in range(1,10,2):
      for j in range(1,10):
        print("%d * %d = %d" %(i, j, i*j))
      
def gugudan_even():
  for i in range(2,10,2):
      for j in range(1,10):
        print("%d * %d = %d" %(i, j, i*j))
      

def gugudan_odd_or_even (n):
  if n % 2 ==1:
    gugudan_odd()
  else:
    gugudan_even()

print("1 입력: ")
gugudan_odd_or_even(1)
print("2 입력: ")
gugudan_odd_or_even(2)