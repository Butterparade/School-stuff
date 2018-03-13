def vectorAdd():
    vector_one_i = [(input("Enter vector one's I value: ")), (input("Enter vector one's J value: "))]
    vector_two = [(input("Enter vector two's I value: ")), (input("Enter vector two's J value: "))]





    
    factor_one = float(input("Enter multiplication factor of Vector 1: "))
    one_i = float(input("Enter ui: "))
    one_j = float(input("Enter uj: "))
    factor_two = float(input("Enter multiplication factor of Vector 2: "))
    two_i = float(input("Enter vi: "))
    two_j = float(input("Enter vj: "))
    vector = (factor_one*(one_i + two_i)), (factor_two*(one_j + two_j))
    print (vector)
    return vector

def vectorSub():
    factor_one = float(input("Enter multiplication factor of Vector 1: "))
    one_i = float(input("Enter ui: "))
    one_j = float(input("Enter uj: "))
    factor_two = float(input("Enter multiplication factor of Vector 2: "))
    two_i = float(input("Enter vi: "))
    two_j = float(input("Enter vj: "))
    vector = (factor_one*(one_i - two_i)), (factor_two*(one_j - two_j))
    print (vector)
    return vector



"""
ui = -9
uj = 6
vi = 10
vj = -4
wi = 8
wj = -4

"""
