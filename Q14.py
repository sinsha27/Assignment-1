#
def fun():
  print("Hello, World!")

fun()

def fun(n):
  print("Hello,",n)

fun("Python")

def fun(n):
  print(n+"function")

fun("Python")

def OddEven(n):
  if(n%2==0):
    return "EVEN"
  else:
    return "ODD"

print(OddEven(2))
print(OddEven(3))

#default arguments
def fun(x, y=20):
  print("X=",x,"\nY=",y)
fun(10)

#keyword arguments
def fun(x,y):
  print(x,y)
fun(x="Hello", y="World")
fun(y="World", x="Hello")

#positional arguments
def fun(name,age):
  print("my name is",name)
  print("my age is",age)
fun("Camila",7)
fun(7,"Camila")

#arbitary keyword arguments
def fun(*n):   
    for i in n:
        print(i)

fun('hello', 'world')

def fun(**n):   
    for key, value in n.items():
        print(key, ":", value)

fun(first="hello", second="world")

#LAMBDA
x = lambda a : a + 10
print(x(5))

x = lambda a, b : a*b
print(x(2,3))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

def fun(n):
  return lambda a : a*n
x = fun(2)
y = fun(3)
print(x(10))
print(y(10))
