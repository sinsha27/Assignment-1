#
M = float(input("Enter total mark percentage : "))
print("Total mark percentage = ",M,"%")
if M>90:
  print("Grade = A")
elif M>=80 and M<=89:
  print("Grade = B")
elif M>=70 and M<=79:
  print("Grade = C")
elif M>=60 and M<=69:
  print("Grade = D")
elif M>=50 and M<=59:
  print("Grade = E")
else:
  print("FAILED")