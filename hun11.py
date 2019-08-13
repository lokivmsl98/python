def rW(Sent): 
	words = Sent.split(" ") 
	newWords = [word[::-1] for word in words] 
	newSentence = " ".join(newWords) 
	return newSentence 

l= input()
print(rW(l)) 
