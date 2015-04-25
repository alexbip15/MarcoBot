import os
from src import command_runtime

def bet(args, asking_user, channel):
    if not command_runtime.bets_started:
        return channel + "Bets not started"

    try:
        asked_bet = int(args[0])
        if asked_bet < 0 or asked_bet > 99 : raise ValueError()
    except ValueError:
        return "Bet must be a number between 0 and 99"

    if asking_user in command_runtime.bets_subscriptions.values():
        return asking_user + " has already voted"
    elif command_runtime.bets_subscriptions.has_key(asked_bet):
        return str(bet) + " has already been voted for"
    else:
        command_runtime.bets_subscriptions[asked_bet] = asking_user
