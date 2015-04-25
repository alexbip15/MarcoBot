channels = {}

class ChannelRuntime:
    def __init__(self, channel):
        self.channel = channel
        self.bets_started = False
        self.bets_subscribers = dict()
        self.moderators = {}

def of(channel):
    if not channels.has_key(channel):
         channels[channel] = ChannelRuntime(channel)
    return channels[channel]
