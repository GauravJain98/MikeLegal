import nltk

def fun(message):
    colors = {
        "CD":"black",  # Cardinal Number 
        "AT":"black",  # Articles
        "JJ":"black",  # Adjectives
        "NN":"black",  # Nouns
        "RB":"black",  # Adverbs
        "NNS":"black", # Plural Nouns
        "VBG":"black", # Gerunds
        "VBD":"black", # Past Tense Verbs
    }
    html = ""
    text = nltk.pos_tag(nltk.word_tokenize(message))
    print(text)

fun("this is real")