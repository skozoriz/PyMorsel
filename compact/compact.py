
def compact(p):
    if len(p)<2:
        return p[:]
    else:
        return [ p[0] ] + [ p[i] for i in range(1, len(p)) if p[i-1] != p[i] ]
            

if __name__ == '__main__':

    p1 = [1, 1, 1]
    c = compact(p1)
    print(p1, c, p1==c, id(p1), id(c))

    p1 = [1, 1, 2, 2, 3, 2]
    c = compact(p1)
    print(p1, c, p1==c, id(p1), id(c))

    p1 = []
    c = compact(p1)
    print(p1, c, p1==c, id(p1), id(c))
    
    p1 = [7]
    c = compact(p1)
    print(p1, c, p1==c, id(p1), id(c))
    
    print('-----')


    

