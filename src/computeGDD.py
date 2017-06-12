def computeGDD(Data, baseTemp):  # Checking GDD values and Computing it.
    key = 0
    GDD = []
    Data['GDD'] = ((Data['Max Temp'] + Data['Min Temp']) / 2) - baseTemp
    for item in Data['GDD']:
        if item >= 0:
            key += item
        GDD.append(key)
    Data['GDD'] = GDD
    return Data
