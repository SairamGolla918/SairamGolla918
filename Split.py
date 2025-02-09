def Split(str):

    l = []

    temp = ""
    for char in str:
        if char == ' ':
            l.append(temp)
            temp = ""
        else:
            temp += char
    return l

input_text = "As the gold standard data provider to the world’s largest industries, we continuously collect and analyze terabytes of data to create the most comprehensive, authoritative, and granular market intelligence."

print(Split(input_text))