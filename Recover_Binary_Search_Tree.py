a = [3,4,7,2,9,10,11]

def find_swapped(a):
    x = y = None
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            x = a[i+1]
            y = a[i]
        else:
            continue
    return [x,y]

print(find_swapped(a))