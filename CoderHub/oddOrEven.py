


def odd(num:int) -> str:
    numstr = str(num)
    even = []
    odd = []
    for x in range(0, len(numstr)):
        if int(numstr[x]) % 2 == 0 :
            
            even.append(int(numstr[x]))
            print(f"even :{numstr[x]}")
        else:
            odd.append(int(numstr[x]))
            print(f"odd :{numstr[x]}")
    total_even = sum(even)
    print(total_even)
    total_odd = sum(odd)
    print(total_odd)
    if total_even > total_odd:
        return "even"
    elif total_even < total_odd:
        return "odd"
    else:
        return "equal"

print(odd(54870))