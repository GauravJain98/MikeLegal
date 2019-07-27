import nltk

def htmlTokenize(message):
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    text = nltk.pos_tag(nltk.word_tokenize(message))
    return str(text)

# print(fun("this is real"))