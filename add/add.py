# week 20190415 task 
# Python Morsels problem: add
# sergii.kozoriezov@gmail.com

# not used in the solution
def add_simple(m1, m2):
    m = []
    for r in m1:      # row = list
        m.append([])  
        for c in r:   # value
            d =c + m2[m1.index(r)][r.index(c)]  
            m[m1.index(r)].append(d)
    return m

def add2(m1, m2):
    # dimensions test
    m1n = len(m1)
    m2n = len(m2)
    if m1n != m2n : 
        raise ValueError('Given matrices are not the same size.')
    m1m = len(m1[0])
    for i in range(0, m1n): 
        if len(m1[i]) != m1m or len(m2[i]) != m1m :
            raise ValueError('Given matrices are not the same size.')
    # matrix elements addition
    m = [ [ m1[i][j] + m2[i][j] for j in range(0, m1m) ] for i in range(0, m1n) ]  
    # result matrix
    return m

def add(m1, m2, *mm):
    m = add2(m1, m2)
    for matr in mm:
        m = add2(m, matr)
    return m

if __name__ == '__main__':

    res = add(
        [[1,2], [3,4]],
        [[1,1], [1,1]]
        )
    print("2*2 matrix, 2 matrixes\n", res)  

    res = add(
        [[1,2], [3,4]],
        [[1,1], [1,1]],
        [[-1,-1], [-1,-1]],
        [[1,1], [1,1]]
    )
    print("2*2 , 4 matrixes\n", res)  

    res = add2(
        [[], []],
        [[], []]
        )
    print("0*0 empty matrix\n", res)
        
    res = add2(
        [[1, 2], [3, 4, 5]],
        [[1, 1], [1, 1, 1]]
        )
    print("bad matrixes\n", res)