import requests

def winner(args):
	winner = args[0] + "\n"
	with open('log.txt', 'r') as inp:
		for line in inp:
			if line == "bets started":
				return "Bets not ended!"
	with open('bets.txt','r') as input_f:
		for line in input_f:
			if line.split(' ')[1] == winner:
				return line.split(' ')[0] + " is the winner!"
	return "No winners"