import nltk
nltk.download('wordnet')
text = "feet cats wolves talked"

tokenizer = nltk.tokenize.TreebankWordTokenizer()
tokens = tokenizer.tokenize(text)

stemmer = nltk.stem.PorterStemmer()
sentence = " ".join(stemmer.stem(token) for token in tokens)
print(sentence)

stemmer = nltk.stem.WordNetLemmatizer()
sentence = " ".join(stemmer.lemmatize(token) for token in tokens)
print(sentence)
