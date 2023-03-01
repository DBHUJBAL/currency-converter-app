import sys


def return_exchanage_rate(cn):
    if cn.casefold() == 'aud/usd':
        return 0.8371
    elif cn.casefold() == 'cad/usd':
        return 0.8711
    elif cn.casefold() == 'usd/cny':
        return 6.1715
    elif cn.casefold() == 'eur/usd':
        return 1.2315
    elif cn.casefold() == 'gbp/usd':
        return 1.5683
    elif cn.casefold() == 'nzd/usd':
        return 0.7750
    elif cn.casefold() == 'usd/jpy':
        return 119.95
    elif cn.casefold() == 'eur/czk':
        return 27.6028
    elif cn.casefold() == 'eur/dkk':
        return 7.4450
    elif cn.casefold() == 'eur/nok':
        return 8.6651


def calculation(rate, amt):
    converted_amt = float(amt) * rate
    return converted_amt


rows = 11
cols = 11
base = sys.argv[1]
terms = sys.argv[3]
mat = [[0 for _ in range(cols)] for _ in range(rows)]

country_list = ["AUD", "CAD", "CNY", "CZK", "DKK", "EUR", "GBP", "JPY", "NOK", "NZD", "USD"]


mat[0][0], mat[0][1], mat[0][2], mat[0][3], mat[0][4], mat[0][5], mat[0][6], mat[0][7], mat[0][8], mat[0][9], mat[0][10] = "1:1", "USD", "USD", "USD", "USD", "USD", "USD", "USD", "USD", "USD", "D"
mat[1][0], mat[1][1], mat[1][2], mat[1][3], mat[1][4], mat[1][5], mat[1][6], mat[1][7], mat[1][8], mat[1][9], mat[1][10] = "USD", "1:1", "USD", "USD", "USD", "USD", "USD", "USD", "USD", "USD", "D"
mat[2][0], mat[2][1], mat[2][2], mat[2][3], mat[2][4], mat[2][5], mat[2][6], mat[2][7], mat[2][8], mat[2][9], mat[2][10] = "USD", "USD", "1:1", "USD", "USD", "USD", "USD", "USD", "USD", "USD", "D"
mat[3][0], mat[3][1], mat[3][2], mat[3][3], mat[3][4], mat[3][5], mat[3][6], mat[3][7], mat[3][8], mat[3][9], mat[3][10] = "USD", "USD", "USD", "1:1", "EUR", "Inv", "USD", "USD", "EUR", "USD", "EUR"
mat[4][0], mat[4][1], mat[4][2], mat[4][3], mat[4][4], mat[4][5], mat[4][6], mat[4][7], mat[4][8], mat[4][9], mat[4][10] = "USD", "USD", "USD", "EUR", "1:1", "Inv", "USD", "USD", "EUR", "USD", "EUR"
mat[5][0], mat[5][1], mat[5][2], mat[5][3], mat[5][4], mat[5][5], mat[5][6], mat[5][7], mat[5][8], mat[5][9], mat[5][10] = "USD", "USD", "USD", "D", "D", "1:1", "USD", "USD", "USD", "USD", "USD"
mat[6][0], mat[6][1], mat[6][2], mat[6][3], mat[6][4], mat[6][5], mat[6][6], mat[6][7], mat[6][8], mat[6][9], mat[6][10] = "USD", "USD", "USD", "USD", "USD", "USD", "1:1", "USD", "USD", "USD", "D"
mat[7][0], mat[7][1], mat[7][2], mat[7][3], mat[7][4], mat[7][5], mat[7][6], mat[7][7], mat[7][8], mat[7][9], mat[7][10] = "USD", "USD", "USD", "USD", "USD", "USD", "USD", "1:1", "USD", "USD", "Inv"
mat[8][0], mat[8][1], mat[8][2], mat[8][3], mat[8][4], mat[8][5], mat[8][6], mat[8][7], mat[8][8], mat[8][9], mat[8][10] = "USD", "USD", "USD", "EUR", "EUR", "Inv", "USD", "USD", "1:1", "USD", "EUR"
mat[9][0], mat[9][1], mat[9][2], mat[9][3], mat[9][4], mat[9][5], mat[9][6], mat[9][7], mat[9][8], mat[9][9], mat[9][10] = "USD", "USD", "USD", "USD", "USD", "USD", "USD", "USD", "USD", "1:1", "D"
mat[10][0], mat[10][1], mat[10][2], mat[10][3], mat[10][4], mat[10][5], mat[10][6], mat[10][7], mat[10][8], mat[10][9], mat[10][10] = "Inv", "Inv", "Inv", "EUR", "EUR", "Inv", "Inv", "D", "EUR", "Inv", "1:1"


base_index = country_list.index(base, 0, 11)

terms_index = country_list.index(terms, 0, 11)

x1 = mat[base_index][terms_index]
new_index = country_list.index(x1, 0, 11)

x2 = mat[base_index][new_index]

if x2 == "D":
    c_name = base+"/"+x1
    ex_rate = return_exchanage_rate(c_name)

    y = sys.argv[2]
    ans = calculation(ex_rate, y)

    c_name = x1+"/"+sys.argv[3]

    conv_amt = return_exchanage_rate(c_name)
    final_ans = calculation(conv_amt, ans)

    print("\n From: {0}, {1} ".format(sys.argv[1].upper(), sys.argv[2]))
    print("\n To: ", sys.argv[3].upper())
    if sys.argv[3].casefold() == 'jpy':
        print("\n = {0} {1}".format(sys.argv[3].upper(), int(final_ans)))
    print("\n = {0} {1}".format(sys.argv[3].upper(), round(final_ans, 2)))
