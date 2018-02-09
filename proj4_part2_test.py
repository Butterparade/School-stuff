def max_trans1 (a,b,c):

    print(min(a,b,c))
    return None

def max_trans2 (a,b,c,d,e):

    if (min(a,b,c))>(min(d,e)):
        print(min(a,b,c))
    elif (min(a,b,c))<(min(d,e)):
        print(min(d,e))
    else:
        print(min(a,b,c,d,e))
    return None

    
max_trans1(1,2,3)
max_trans1(9,6,3)
max_trans1(0,0,0)

max_trans2(1,2,3,4,5)
max_trans2(222,110,411,54,73)
max_trans2(0,0,0,0,0)
