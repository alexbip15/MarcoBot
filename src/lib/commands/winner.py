from src import command_runtime


def winner(args, asking_user):
    if command_runtime.bets_started:
        return "Bets not ended!"

    try:
        winner_bets = int(args[0])
        if winner_bets < 0 or winner_bets > 99 : raise ValueError()
    except ValueError:
        return "Bet must be a number between 0 and 99"

    if command_runtime.bets_subscriptions.has_key(winner_bets):
        return command_runtime.bets_subscriptions[winner_bets] + " is the winner!"
    else:
        return "No winners"