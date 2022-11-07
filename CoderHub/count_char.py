

def count_char(sentence, ch):
    count = 0

    for x in sentence:
        if x == ch:
            count += 1
    return count

sentence = 'day'
ch = 'd'
print(count_char(sentence, ch))