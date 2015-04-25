# coding: utf8
from src import command_runtime


def startbets(args, asking_user, channel):
    if command_runtime.bets_started:
        return "Bets already started!"
    else:
        command_runtime.bets_started = True
        command_runtime.bets_subscriptions = dict()
        return "Bets started!"
