import nltk

def htmlTokenize(message):
    text = nltk.pos_tag(nltk.word_tokenize(message))
    return str(text)

# print(fun("this is real"))