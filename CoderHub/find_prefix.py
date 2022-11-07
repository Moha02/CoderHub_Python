

# def find_prefix(words, text):
#     l = []
#     for x in words:
#         cap = text.capitalize()
#         if x[:2] == text or x[:2] == cap:
#             l.append(x)
#         elif x[:2] != text:
#             pass
#             if len(l) == 0:
#                 return ['No matches found']
#     return l




from typing import List
def find_prefix(words: List[str], text: str) -> List[str]:
    # write your code here ^_^
    l = []
    text = text.upper()
    length = len(text)
    for x in words:
        t = x.upper()
        sliced = t[:length]
        if sliced == text:
            l.append(x)
        
    if len(l) == 0:
        return ["No matches found"]
    else:
        return l

# x[:2] == text or
words = ['Nouf','Abdullah']
text = 'Gh'
print(find_prefix(words, text))

words = ['Reassemble','Remainder','Room','Receive']
text = 're'
print(find_prefix(words, text))

words = ['Compared','Coding','Career','Coderhub','Cold','Call']
text = 'co'
print(find_prefix(words, text))

words = ['Save','Saudi','Satr','Send','Salt','Super','Sample']
text = 'sa'
print(find_prefix(words, text))