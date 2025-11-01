
def sub(a,b):
    return a-b
def mul(a,b):
    return  a*b
def sum_list(num):
    if len(num) == 0:
        return 0
    k = 0
    for n in num:
        k +=n
    return k
def is_event(z):
    if z % 2 == 0 :
        return 'true'
    elif  z % 2 != 0 :
        return 'false'
