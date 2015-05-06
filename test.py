import nltk

sentence = """At eight o'clock on Thursday morning, Arthur didn't feel good."""

tokens = nltk.word_tokenize(sentence)
print("Tokens:")
print(tokens)
print("\n")

tagged = nltk.pos_tag(tokens)
print("Tags:")
print(tagged[0:len(tokens)])
sentence_tags = tagged[0:len(tokens)]
'''
for i in sentence_tags:
    for j in i:
        print(j + ',')
'''
print("\n")
'''
nltk_tagset = ['CC','CD','DT','EX','EX','FW','IN','JJ','JJR','JJS','LS','MD',
               'NN','NNP','NNPS','NNS','PDT','POS','PRP','PRP$','RB','RBR',
               'RBS','RP','SYM','TO','UH','VB','VBD','VBG','VBN','VBP','VBZ',
               'WDT','WP','WP$','WRB']
'''
entities = nltk.chunk.ne_chunk(tagged)
print("Entities:")
print(entities)
