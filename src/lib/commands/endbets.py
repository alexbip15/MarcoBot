from src import command_runtime


def endbets(args, asking_user, channel):
    if not command_runtime.bets_started:
        return "Bets never started"
    else:
        command_runtime.bets_started = False
        return "Bets ended! Awaiting !winner"