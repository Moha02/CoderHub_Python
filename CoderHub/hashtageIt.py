

# def hash(array):
#     state = ""
#     for x in array:
#         state = state + "#" + x
#     print(type(state))
#     return f'{state}'

my_array = ['stay_home','coronavirus','Saudi_Arabia']
my_array1 = ['Vibes','SAFCSP','entrepreneur']
my_array2 = ['Programming','Code']
my_array3 = ['SAFCSP','SAUDI_ARABIA','Riyadh']
# # print(hash(my_array))
# # print(hash(my_array1))
# # print(hash(my_array2))
# '#stay_home #coronavirus #Saudi_Arabia'
# '#SAFCSP #SAUDI_ARABIA #Riyadh'
'#Programming #Code'

def hashtag_it(my_array):
    # write your code here ^_^
    state = ""
    for idx ,x in enumerate( my_array):
        
        my_array[idx] = "#" + my_array[idx]
    for x in my_array:
        state = state + x
    newstate = state[1:]
    new =newstate.replace("#", " #")
    new = "#" + new
    return new
    # state = state.replace("#", " #")
    # return state

    #     if leng == 0:
    #         state = "#" + x 
    #         num += 1
    #     #     num += 1
    #     elif leng >= num :
    #     state = state + "#" + x
    # state = state.replace("#", " #") 
    #state = str(state)
    # return state
# '#SAFCSP #SAUDI_ARABIA

print(hashtag_it(my_array))
# print(hashtag_it(my_array1))
# print(hashtag_it(my_array2))
# print(hashtag_it(my_array3))