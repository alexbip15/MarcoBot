import time
import importlib

from command_headers import *


def is_valid_command(command):
    return command in commands

def update_last_used(command, channel):
    commands[command][channel]['last_used'] = time.time()

def get_command_limit(command):
    return commands[command]['limit']

def is_on_cooldown(command, channel):
    return commands[command]['limit'] > 0 \
           and time.time() - commands[command][channel]['last_used'] < commands[command]['limit']

def is_protected(command):
    return commands[command]['protected']

def get_cooldown_remaining(command, channel):
    return round(commands[command]['limit'] - (time.time() - commands[command][channel]['last_used']))

def check_has_return(command):
    return commands[command]['return'] \
           and commands[command]['return'] != 'command'

def get_return(command):
    return commands[command]['return']

def check_has_args(command):
   return 'argc' in commands[command]

def check_has_correct_args(message, command):
    message = message.split(' ')
    return len(message) - 1 == commands[command]['argc']

def check_returns_function(command):
    return commands[command]['return'] == 'command'

def pass_to_function(command, args, asking_user, channel):
    command = command.replace('!', '')

    module = importlib.import_module('src.lib.commands.%s' % command)
    function = getattr(module, command)

    return function(args, asking_user, channel)