# 실습 3.

def gugudan_n(n):
  for i in range(1,n+1):
    for j in range(1,10):
      print("%d * %d = %d" %(i, j, i*j))

print("11입력: ")
gugudan_n(11)