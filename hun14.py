def permutation(a,b,c):
    if b==c:
      print(''.join(a))
    else:
      for j in range(b,c):
        a[b],a[j]=a[j],a[b]
        permutation(a,b+1,c)
        a[b],a[j]=a[j],a[b]
string=input()
n=len(string)
data=list(string)
permutation(data,0,n)
