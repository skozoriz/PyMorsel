def tail0(l, n):
    return list(l[-n if n>0 else 9999999999::])

def tail(itr, n):
    l = []
    if n>0 : 
        c = 0    
        for i in itr:
            l.append(i)
            c = c + 1
            if c>n :
                l.pop(0)
    return l


if __name__ == "__main__":

    l = [1,2,3,4,5]
    r = tail(l, 3)
    print(f'--  {l}, 5/3, {r}')

    l = [1,2,3,4,5]
    r = tail(l, 0)
    print(f'--  {l}, 5/0, {r}')

    l = []
    r = tail(l, 3)
    print(f'--  {l}, 0/3, {r}')

    l = []
    r = tail(l, -3)
    print(f'--  {l}, 0/-3, {r}')

    l = [1,2,3,4,5]
    r = tail(l, 7)
    print(f'--  {l}, 5/7, {r}')

    l = [1,2,3,4,5]
    r = tail(l, -3)
    print(f'--  {l}, 5/-3, {r}')

    i = (n**2 for n in range(100))
    r = tail(i, 5)
    print(f'--(n**2 for n in range(100)), 100/5, {r}')