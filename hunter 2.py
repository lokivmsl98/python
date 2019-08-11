    
a=int(input())
b=(int(c) for c in input().split())
g=sorted(b,reverse=True)
c=0
while c<a:
  print(g[c],end="")
  c+=1
