a=int(input())
b=list(map(int,str(a)))
v=list(map(lambda x:x**3,b))
if(sum(v)==a):
  print("yes")
else:
  print("no")
