#과제 1
class FourCal():
  def __init__(self, name, age, school):
    self.name = name
    self.age = age
    self.school = school
    
    self.add_cnt = 0
    self.sub_cnt = 0
    self.div_cnt = 0
    self.mul_cnt = 0

  def add(self, n1, n2):
    self.add_cnt+=1
    return n1 + n2
  def sub(self, n1, n2):
    self.sub_cnt+=1
    return n1 - n2
  def div(self, n1, n2):
    if n2 == 0:
      print('ZeroDevisionError')
      return None
    self.div_cnt+=1
    return n1 / n2
  def mul(self, n1, n2):
    self.mul_cnt+=1
    return n1 * n2
  
  def ShowCount(self):
    print("덧셈: ", self.add_cnt)
    print("뺄셈: ", self.sub_cnt)
    print("곱셈: ", self.mul_cnt)
    print("나눗셈: ", self.div_cnt)

  
calculator= FourCal("정성원", 24, "고려대학교")
print("속성: ", calculator.name, calculator.age, calculator.school)

print(calculator.add(3,4))
print(calculator.sub(3,4))
print(calculator.div(3,4))
print(calculator.mul(3,4))
print(calculator.mul(2,5))

calculator.ShowCount()
