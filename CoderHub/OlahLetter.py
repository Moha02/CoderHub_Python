


def vowels(phrase, n):
    # r = []
    vo = ""

    v = ["A", "a", "U", "u", "E", "e", "I", "i", "O", "o"]

    for x in phrase:
        if x in v:
            # r.append(x)
            vo = vo + x
    if n > len(vo):
        raise ValueError
    else:
        
        return vo

phrase = 'Queen'
n = 3
print(vowels(phrase, n))
