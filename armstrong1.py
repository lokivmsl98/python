l=int(input())
m=list(map(int,str(l)))
n=list(map(lambda x:x**3,m))
if(sum(n)==l):
  print("yes")
else:
  print("no")
