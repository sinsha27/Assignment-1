#
s = str(input("Enter a string : "))
s = s.upper()
print(s)
l = len(s)
i,j = 0, l - 1

is_palindrome = True
while i < j:
    if s[i] != s[j]:
        is_palindrome = False
        break
    i += 1
    j -= 1

if is_palindrome:
    print("PALINDROME")
else:
    print("NOT PALINDROME")