m=int(input())
n=(input().split())[0:m]
o=m//2
if m>3:
  if(o%2==0):
    print("yes")
  else:
    print("no")
else:
  if(m==3):
    print("yes")
  else:
    print("no")
