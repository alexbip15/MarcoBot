import requests
import os


def bet(args):
    usage = 'Usage: !bet <bet>'
    true = 0
    bet = args[0]
    username = args[1]
    with open('log.txt', 'r') as input_f:
        for line in input_f:
            if line != "bets started":
                return "Bets not started"
    while True:
        f = open('semaphore.txt', 'r')
        line = f.readline()
        if line.strip() == '':
            break

    f = open('semaphore.txt', 'w')
    f.write("lock")
    with open('bets.txt', 'r') as input_f:
        with open('bets_n.txt', 'w') as output:
            for line in input_f:
                if line.split(' ')[1] == bet:
                    true = 1
                elif line.split(' ')[0] == username:
                    true = 2
                output.write(line)
            if true != 1 and true != 2:
                output.write(username + " " + bet)
                output.write("\n")
    os.remove('bets.txt')
    os.rename('bets_n.txt', 'bets.txt')
    f = open('semaphore.txt', 'r+')
    f.truncate()
    if true == 1:
        return bet + " has already been voted for"
    elif true == 2:
        return username + " has already voted"
    else:
        return "nothing"

	