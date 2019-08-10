a=int(input())
b=list(map(int,input().split()))[:a]
b.sort(reverse=True)
i=0
while i<a:
    print(b[i], end="\n")
    i+=1
