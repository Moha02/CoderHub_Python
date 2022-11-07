

def compare(w1, w2):
    if w1[-2:] == w2[-2:]:
        return True
    else:
        return False

s1 = 'abc'
s2 = 'abc'

print(s1[-2:])
print(s2[-2:])
print(compare(s1, s2))

s1 = 'abc'
s2 = 'abcc'
print(s1[:-2])
print(s2[:-2])
print(compare(s1, s2))

s1 = 'there'
s2 = 'their'
print(s1[:-2])
print(s2[:-2])
print(compare(s1, s2))