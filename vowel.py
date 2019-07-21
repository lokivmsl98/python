l=input()
if(l=="a" or l=="A" or l=="e" or l=="E" or l=="i" or l=="I" or l=="o" or l=="O" or l=="u" or l=="U"):
  print("vowel")
elif(l>="a" and l<="z") or (l>="A" and l<="Z"):
  print("constant")
else:
  print("invalid")
