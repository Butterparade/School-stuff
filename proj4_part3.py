def isbn_gendigit (str):

    if (len(str)) == 9:
        isbn_math = (int(str[0]) * 1) + (int(str[1]) * 2) + (int(str[2]) * 3) + (int(str[3]) * 4) + (int(str[4]) * 5) + (int(str[5]) * 6) + (int(str[6]) * 7) + (int(str[7]) * 8) + (int(str[8]) * 9)
        isbn_mathremainder = (isbn_math % 11)
        print ((str),isbn_mathremainder)
        return None
    else:
        print ('unacceptable')
        return None

isbn_gendigit('020131452')

isbn_gendigit('068131921')

isbn_gendigit('0123456789')
