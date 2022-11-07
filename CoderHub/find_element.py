

def find_element(elements_array, element):
    if element in elements_array:
        return True
    else:
        return False

elements_array = [3232,1,24,45,335,454]
element = 3554
print(find_element(elements_array, element))

elements_array = [2,12,34,2,3,4,5]
element = 4
print(find_element(elements_array, element))

elements_array = [2,5,6,7,8,2,1]
element = 5
print(find_element(elements_array, element))

elements_array = [1,5,7,3,6,1]
element = 1
print(find_element(elements_array, element))