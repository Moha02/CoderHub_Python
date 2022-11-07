import re
from typing import List
def stringContains(firstName: str, contains: str) -> bool:

    if contains in firstName:
        return True
    else:
        return False


firstName = 'Ahmad'
contains = 'A'

print(stringContains(firstName, contains))