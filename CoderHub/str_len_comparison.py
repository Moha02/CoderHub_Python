from typing import List
def str_len_comparison(words: List[str]) -> bool:
    # write your code here ^_^
    l = []
    for x in words:
        l.append(len(x))
        if len(words) == 1:
            return False
    mi = min(l)
    ma = max(l)
    if mi == ma:
        return True
    else:
        return False

words = ['A','B']
print(str_len_comparison(words))
words = ['Khalid','Sultan','AlDana','Johrah','Ghadah']

print(str_len_comparison(words))

words = ['Satr','CoderHub']
print(str_len_comparison(words))

words = ['123','456','789']
print(str_len_comparison(words))

words = ['123']
print(str_len_comparison(words))
                   
                   
