a,b=map(int,input().split())
l=list(map(int,input().split()))[:a]
count=0
for i in l:
    if (i==b):
        count+=1
print(count)
