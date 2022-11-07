from typing import List
def search(word: str, character: str) -> int:
    # write your code here ^_^
    z = word.find(character)
    return z
vales = "cloud"
print(search(vales, "z"))