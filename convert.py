import nltk

def htmlTokentize(message):
    text = nltk.pos_tag(nltk.word_tokenize(message))
    return str(text)

# print(fun("this is real"))