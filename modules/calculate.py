def checkValues(*args):
    for arg in args:
        if not arg.replace(',', '').isdigit() or not arg.replace(',', '').isdigit():
            raise TypeError('Os cálculos de finanças podem ser feitas apenas com números')

def relatoryGenerator(*args):
    newDict = [args[0]]
    tempDict = {
        'Total livre de dívidas': args[1],
        'Total reservado para investimentos': args[2],
        'Total livre': args[3],
    }
    newDict.append(tempDict)
    return newDict

def calculateFinances(dict):
    for key, value in dict.items():
        dict[key] = int(value)

    subtractDebits = dict['renda'] - (dict['água'] + dict['energia'] + dict['alimentação'])
    totalInvest = 0
    if isinstance(dict['investimentos'], float) or dict['investimentos'] <= 1:
        totalInvest = subtractDebits * dict['investimentos']
    else:
        totalInvest = subtractDebits * (dict['investimentos'] / 100)
    rest = subtractDebits - totalInvest
    return relatoryGenerator(dict, subtractDebits, totalInvest, rest)