input_text = "As the gold standard data provider to the world’s largest industries, we continuously collect and analyze terabytes of data to create the most comprehensive, authoritative, and granular market intelligence."

def long(Str):
    longest_word = ""
    word = ""

    for char in input_text:
        if char.isalpha() or char == '’':
            word += char
        else:
            if len(word) > len(longest_word):
                longest_word = word
            word = ""
    return longest_word


list = input_text.split()
LongWord = ""

for word in list:
    if(len(word) > len(LongWord)):
        LongWord = word

print(LongWord)
print(long(input_text))
