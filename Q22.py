#
class bankaccount:
  def __init__(self, name, acc_no):
    self.name = name
    self.acc_no = acc_no

  @property #getter
  def name(self):
    return self._name

  @name.setter
  def name(self, n):
    self._name = n

  @property
  def acc_no(self):
    return self._acc_no

  @acc_no.setter
  def acc_no(self, n):
    self._acc_no = n

def main():
  ba = bankaccount("Rono", 1234)

  print("Name : ",ba.name)
  print("Account No. : ", ba.acc_no)

  ba.name = "Messi"
  ba.acc_no = "4321"

  print("Updated Name : ",ba.name)
  print("Updated Account No. : ",ba.acc_no)

main()