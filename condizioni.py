eta = input('dammi la tua eta: ')
eta = int(eta)

if eta < 18:
    print('sei minorenne.')
elif eta >= 18 and eta < 65:
    print('sei adulto.')
else :
    print('sei anziano')