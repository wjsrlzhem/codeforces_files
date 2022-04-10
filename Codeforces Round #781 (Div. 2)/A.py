iT = int(input())

def gcd(a,b):
    while a:
        b , a = a, b%a
    return b

def lcm(c,d):
    return c*d //gcd(c,d) 

for _ in range(iT):

    iN = int(input())

    lst_temp = [1]*4
    lst_temp[0] = iN -3
    lst_temp.sort(reverse = True)
    [a,b,c,d] = lst_temp
    idx = 0
    while gcd(a,b) != lcm(c,d):
        if lst_temp == 1:
            idx +=1
            if idx >4:
                print('초과')
                break
        lst_temp[idx] -=1
        lst_temp[idx+1] +=1
    
    print(" ".join(map(str,lst_temp)))
