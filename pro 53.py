def pannu(str): 
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet: 
        if char not in str.lower(): 
            return False
    return True
str =input()
if(pannu(str) == True): 
    print("yes") 
else: 
    print("no") 
