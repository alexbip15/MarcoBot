def endbets(args):
    with open('log.txt', 'r') as inp:
        for line in inp:
            if line != "bets started":
                return "Bets Never Started"
    with open('log.txt', 'w') as output:
        output.write("")
    return "Bets ended! Awaiting !winner"