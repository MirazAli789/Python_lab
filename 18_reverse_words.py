def reverse_word(sentence):
    words = sentence.split()
    rev = " ".join(reversed(words))

    return rev


sentence = "hello world"
print(reverse_word(sentence))
