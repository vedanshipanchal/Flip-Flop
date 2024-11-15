def palindrome(x):
    u = len(x)-1
    z = 0
    while z<u:
      if x[z]!= x[u]:
        return False
      z = z+1
      u = u-1
    return True


x = (1,2,3,3,2,1)

if (palindrome(x)):
   print("The tuple is plaindrome")
else:
   print("it is not a palindrome")

