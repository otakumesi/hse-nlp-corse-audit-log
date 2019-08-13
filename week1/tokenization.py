import nltk
text = "This is Andrew's text, isn't it?"

tokenizer = nltk.tokenize.WhitespaceTokenizer()
print(tokenizer.tokenize(text))

tokenizer = nltk.tokenize.TreebankWordTokenizer()
print(tokenizer.tokenize(text))

tokenizer = nltk.tokenize.WordPunctTokenizer()
print(tokenizer.tokenize(text))
