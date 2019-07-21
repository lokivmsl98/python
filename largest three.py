l1=(input("enter first number"))
l2=(input("enter second number"))
l3=(input("enter third number"))
if(l1>l2) and (l1>l3):
  Largest=l1
elif(l2>l1) and (l2>l3):
  Largest=l2
else:
  Largest =l3
  print("the Largest number is",Largest)
