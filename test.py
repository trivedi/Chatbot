import nltk

sentence = """At eight o'clock on Thursday morning, Arthur didn't feel good."""

tokens = nltk.word_tokenize(sentence)
print("Tokens:")
print(tokens)
print("\n")

tagged = nltk.pos_tag(tokens)
print("Tags:")
print(tagged[0:len(tokens)])
print("\n")

entities = nltk.chunk.ne_chunk(tagged)
print("Entities:")
print(entities)
