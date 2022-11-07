from typing import List
def namesSort(namesArray: List[str], order: str) -> List[str]:
    # write your code here ^_^

    if order == 'ASC':
        sorted_list = sorted(namesArray)
        return sorted_list
    elif order == 'DESC':
        sorted_list = sorted(namesArray, reverse=True)
        return sorted_list





namesArray = ['Ahmed Omar','Yousef Abdullah']
order = 'ASC'
print(namesSort(namesArray, order))

namesArray = ['Khaled Bader','Khaled Bader','Mohammed Yahya']
order = 'DESC'
print(namesSort(namesArray, order))