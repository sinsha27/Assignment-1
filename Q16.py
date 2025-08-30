#
def decorator(fun):
  def wrapper():
    print("HELLO WORLD")
  return wrapper

@decorator
def main_fun():
  pass
  
main_fun()
