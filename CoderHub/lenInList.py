

def word_length(arr):
    index = 0
    new_list = []
    for x in arr:
        l = len(x)
        new_list.insert(index, l)
        index += 1
    return new_list

arr = ['Code','hub']

print(word_length(arr))
        
