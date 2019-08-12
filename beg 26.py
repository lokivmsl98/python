m=[]
d=int(input())
l=list(map(int,input().strip().split()))[:d]
g=sorted(l)
for i in g:
  print(i,end=" ")
