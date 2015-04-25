# coding: utf8


def startbets(args, asking_user, channelRuntime):
    if channelRuntime.bets_started:
        return "Bets already started!"
    else:
        channelRuntime.bets_started = True
        channelRuntime.bets_subscriptions = dict()
        return "Bets started!"
