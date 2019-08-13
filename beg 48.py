l=int(input())
m=list(map(int,input().split()))[:l]
n=0
for i in range(l):
    n+=m[i]
d=n//l
print(d)
