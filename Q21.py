#
class home:
  def room(self):
    width = 100
    breadth = 100
    area = width*breadth
    print("Area of Room = ",area)

  def kitchen(self):
    width = 1222
    breadth = 4888
    area =  width * breadth
    print("Area of Kitchen = ",area)

  def hall(self):
    width = 400
    breadth = 300
    area =  width * breadth
    print("Area of hall = ",area)

class firsthome(home):
  def study_room(self):
    width = 250
    breadth = 200
    area =  width * breadth
    print("Area of bathroom = ",area)

class secondhome(home):
  def work_area(self):
    width = 300
    breadth = 180
    area =  width * breadth
    print("Area of work area = ",area)

def main():
  print("FIRST HOME")
  f = firsthome()
  f.room()
  f.kitchen()
  f.hall()
  f.study_room()

  print("\nSECOND HOME")
  s = secondhome()
  s.room()
  s.kitchen()
  s.hall()
  s.work_area()

main()