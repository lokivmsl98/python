def reverse(l):
  str=" "
  for i in l:
    str=i+str
  return str
l="aabbcc"
print("input:")
print(l)
print("output")
print(reverse(l))
