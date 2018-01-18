def reverse_sentence(sentence):
    if not sentence:
        return ""
    index = 0
    while index < len(sentence) and sentence[index] != " ":
        index += 1
    if index == len(sentence):
        return sentence
    return reverse_sentence(sentence[index + 1:]) + " " + sentence[:index]


if __name__ == "__main__":
    s = "this is a sentence"
    print(reverse_sentence(s))
