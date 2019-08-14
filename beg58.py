    
a,b=map(int,input().split())
count=list(map(int,input().split()))[:a]
if b in count:
  print("yes")
else:
  print("no")
