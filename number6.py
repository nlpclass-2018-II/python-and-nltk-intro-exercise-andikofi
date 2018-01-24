import nltk
sentence ='i am going to take the NLP class next semester'
tokens= nltk.word_tokenize(sentence)
for word in tokens:#iterate each word 	
	print(len(word))#print the length of each word	