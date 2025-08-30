#
def sum_no(*args):
  sum = 0
  for i in args:
    sum = sum + i
  return sum

def main():
  n = int(input("Enter the no. of values : "))
  val = []
  print("Enter values : ")
  for i in range(n):
    v = float(input())
    val.append(v)
  
  r = sum_no(*val)
  print("Result = ", r)

main()