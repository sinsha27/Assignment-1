#
class class_exception(Exception):
  def __init__(self, msg = "You Entered"):
    self.msg = msg
    super().__init__(self.msg)

def choice():
  print("1. Enter")
  print("2. Exit")

  try:
    c = int(input("Enter ur choice : "))

    if c == 1:
      raise class_exception()

    elif c == 2:
      print("Exiting")

    else:
      print("Invalid Choice")

  except class_exception as ce:
    print("Custom Exception : ", ce)

choice()