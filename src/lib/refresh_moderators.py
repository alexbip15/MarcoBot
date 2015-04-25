from functions_general import *
from src.config import config
from src.lib import channel_runtime

try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
import json

class refresh_moderators:
    def __init__(self, channel=''):
        self.interval = config.config['cron'][channel]['refresh_moderators_interval']
        self.channel = channel
        if channel.startswith('#'):
            self.url = 'https://tmi.twitch.tv/group/user/' + channel[1:] + '/chatters'
        else:
            self.url = 'https://tmi.twitch.tv/group/user/' + channel + '/chatters'

    def run(self):
        while True:
            try:
                response = urlopen(self.url)
                data = str(response.read())
                data = json.loads(data)
                channel_runtime.of(self.channel).moderators = data['chatters']['moderators']
            except:
                pass
            time.sleep(self.interval)