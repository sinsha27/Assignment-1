#
wt = int(input("Enter score of written test : "))
le = int(input("Enter score of lab exams : "))
a = int(input("Enter score of assignments : "))
tot = ((wt*70)/100) + ((le*20)/100) + ((a*10)/100)
print("Overall score = ", tot)