import math

def perpend():
    for d in range (-40, 41):
        x = round(((0.1)*d), 2)
        u = [((2*x) + 1), 1]
        v = [1, (x**2)]
        Dotproduct = round(((u[0]*v[0])+(u[1]*v[1])), 2)
        product = [u*v for u,v in zip(list(u), list(v))]
        if Dotproduct == 0:
            print ()
            print ('D: ', d)
            print ('X: ', x)
            print ('Dot Product: ', round(Dotproduct, 2))
            print ()
        else:
            print ('nope')
    return None

perpend()    
