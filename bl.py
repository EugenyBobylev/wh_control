
resolution_dct = {
    '1h': '60',
    '2h': '120',
    '4h': '240',
    '6h': '360',
    '12h':'720',
    '1d': '1d',
    '1w': '1w',
}

cohort_dct = {
    '0': 'a) 1 - 100',
    '1': 'b) 100 - 1000',
    '2': 'c) 1000 - 10000',
    '3': 'd) 10000 - 100000',
    '4': 'e) > 100000'
}

label_dct = {
    'anylabel': 'all',
    'nolabel': 'nolabel'
}

endpoint_dct = {
    'btc balance': '/wc/btc',
    'usd_balance': '/wc/usd',
    'profit': '/wc/profit',
    'cummulative profit': '/wc/accumulatedprofit',
    'count of wallets': '/wc/countwallets'
}

success_lst = ['any', '0%', '25%', '50%', '75%', '100%']