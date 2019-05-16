
array = ["mission statement", "a quick bite to eat","a chip off the old block","chocolate bar","mission impossible","a man on a mission","block party",
		"eat my words", "bar of soap"]
res = []
for sentence in array:
	wordList = sentence.split(" ")
	#print(wordList)
	firstWord = wordList[0]
	for word in array:
		lastList = word.split(" ")
		lastWord = lastList[-1]
		#print(firstWord)
		#print("ll", lastWord)
		if firstWord == lastWord:
			print(word + sentence[len(firstWord): ] )
		
