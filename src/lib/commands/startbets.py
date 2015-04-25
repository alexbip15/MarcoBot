# coding: utf8


def startbets(args):
    usage = 'Usage: !startbets <username>'
    f = open('bets.txt', 'r+')
    f.truncate()
    with open('log.txt', 'r') as input_f:
        for line in input_f:
            if line == "bets started":
                return "Bets Already Started!"
    with open('log.txt', 'w') as output:
        output.write('bets started')
    string = "Bets Started!"
    return string