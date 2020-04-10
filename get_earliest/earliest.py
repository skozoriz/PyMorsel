# PyMorsels  earliest

def get_earliest(*ss):
    mins = ss[0]
    (mm, dm, ym) = mins.split('/')
    for s in ss[1:]:
        (m, d, y)= s.split('/')
        if (y, m, d) < (ym, mm, dm):
            (ym, mm, dm) = (y, m, d)
            mins = s
    return mins 
    
if __name__ == '__main__':

    print(get_earliest("01/27/1832", "01/27/1756"))

    print(get_earliest("02/29/1972", "12/21/1946"))

    print(get_earliest("02/24/1946", "03/21/1946"))

    print(get_earliest("06/21/1958", "06/24/1958"))

    print(get_earliest("02/40/2006", "03/01/2006"))

    print(get_earliest("02/40/2006", "02/30/2006"))

    print(get_earliest("02/24/1946", "01/29/1946", "03/29/1945"))

    print(get_earliest("02/24/1946"))