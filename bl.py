
resolution_dct = {
    '1h': 3600,
    '2h': 3600 * 2,
    '4h': 3600 * 4,
    '6h': 3600 * 6,
    '12h': 3600 * 12,
    '1d': 3600 * 24,
    '1w': 3600 * 24 * 7
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