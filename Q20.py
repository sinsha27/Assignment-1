#
from abc import ABC, abstractmethod

class  calculator(ABC):

  @abstractmethod
  def add(self, a, b):
    pass

  @abstractmethod
  def sub(self, a, b):
    pass

  @abstractmethod
  def mul(self, a, b):
    pass

  @abstractmethod
  def div(self, a, b):
    pass

class calc(calculator):
  
  def add(self, a, b):
    return a+b

  def sub(self, a, b):
    return a-b

  def mul(self, a, b):
    return a*b

  def div(self, a, b):
    return a/b

def main():
  c = calc()

  a = float(input("Enter first no. : "))
  b = float(input("Enter second no. : "))

  print("Addition:", c.add(a, b))
  print("Subtraction:", c.sub(a, b))
  print("Multiplication:", c.mul(a, b))
  print("Division:", c.div(a, b))

main()