"""
Given n as input. Print 'Trisect' if n is odd. Print 'Institute' otherwise.
n = 14
-> Institute
n = 17
-> Trisect
"""

print("Enter number 14 or 17")
n = int(input("Enter Number: "))
if (n==14):
  print("Institute")
elif (n==17):
  print("Trisect")
else:
  print("Worng Input")