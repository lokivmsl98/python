l=[]
n=int(input())
l=list(map(int,input().strip().split()))[:n]
k=sorted(l)
for i in k:
  print(i,end=" ")
