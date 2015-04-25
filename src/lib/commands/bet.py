import os

def bet(args, asking_user, channelRuntime):
    if not channelRuntime.bets_started:
        return "Bets not started"

    try:
        asked_bet = int(args[0])
        if asked_bet < 0 or asked_bet > 99 : raise ValueError()
    except ValueError:
        return "Bet must be a number between 0 and 99"

    if asking_user in channelRuntime.bets_subscriptions.values():
        return asking_user + " has already voted"
    elif channelRuntime.bets_subscriptions.has_key(asked_bet):
        return str(asked_bet) + " has already been voted for"
    else:
        channelRuntime.bets_subscriptions[asked_bet] = asking_user
