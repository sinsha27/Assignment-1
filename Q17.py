#
class math:
  def addition(self,a,b):
    return a+b

  def subtraction(self,a,b):
    return a-b
  
  def multiplication(self,a,b):
    return a*b

  def division(self,a,b):
    return a/b

def main():
  m = math()
  print("1. Addition\n","2. Subtraction\n","3. Multiplication\n","4. Division")
  c = int(input("Enter your choice(1-4) : "))

  n1 = float(input("Enter first no. : "))
  n2 = float(input("Enter second no. : "))

  if c == 1:
    print("Result = ", m.addition(n1, n2))

  elif c == 2:
    print("Result = ", m.subtraction(n1, n2))

  elif c == 3:
    print("Result = ", m.multiplication(n1, n2))

  elif c == 4:
    print("Result = ", m.division(n1, n2))

  else:
    print("Invalid Choice")

main()