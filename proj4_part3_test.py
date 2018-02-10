def isbn_gendigit (a):

    if (len(a)) == 9:
        isbn_math = (int(a[0]) * 1) + (int(a[1]) * 2) + (int(a[2]) * 3) + (int(a[3]) * 4) + (int(a[4]) * 5) + (int(a[5]) * 6) + (int(a[6]) * 7) + (int(a[7]) * 8) + (int(a[8]) * 9)
        isbn_mathremainder = (isbn_math % 11)
        print (str(a) + str(isbn_mathremainder))
        return None
    else:
        print ('unacceptable')
        return None

isbn_gendigit('020131452')

isbn_gendigit('068131921')
