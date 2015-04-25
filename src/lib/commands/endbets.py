def endbets(args, asking_user, channelRuntime):
    if not channelRuntime.bets_started:
        return "Bets never started"
    else:
        channelRuntime.bets_started = False
        return "Bets ended! Awaiting !winner"