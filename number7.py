import nltk
input=open('input7.txt')
sentence= input.read()
output=open('output7.txt','w')
tokens= nltk.word_tokenize(sentence)
print('word of sentence: ',str(tokens))
output.write(str(tokens))