costs = {'Philadelphia':{'Chicago':227, 'Dallas':289},
         'Chicago':{'Philadelphia':227, 'Dallas':105, 'Las Vegas':56},
         'Dallas':{'Philadelphia':289, 'Houston':173, 'Chicago':105,
                   'Las Vegas':44, 'San Diego':303},
         'Houston':{'Dallas':173},
         'Las Vegas':{'Chicago':56, 'Dallas':44, 'San Diego':74,
                      'Los Angeles':44, 'San Francisco':56},
         'Los Angeles':{'Las Vegas':44, 'San Diego':157,
                        'San Francisco':111},
         'San Diego':{'Las Vegas':44, 'Los Angeles':157, 'Dallas':303},
         'San Francisco':{'Las Vegas':56, 'Los Angeles':111}}

def cheapest(costs, origins, destination):
    cst = float("inf")
    for next in costs[origins]:
        if next == destination:
            cst = costs[origins][next]
        else:
            for other_next  in costs[next]:
                