
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

def is_positive(k):
    if k>=1:
        return 'true'
    elif k==0:
       return 'false'

def max_of_two(a,b):
    if a>= b:
        return a


