global config

config = {  # details required to login to twitch IRC server
            'server': 'irc.twitch.tv',
            'port': 6667,
            #'channels': ['#marco8641', '#alexbip15'],  # if set to true will display any data received
            'channels': ['#loadlow'],  # if set to true will display any data received
            'debug': False,  # if set to true will log all messages from all channels  # todo
            'cron': {
                '#marco8641': {
                    'run_cron': False,
                    # set this to false if you want don't want to run the cronjob but you want to preserve the messages etc
                    'run_time': 5,  # time in seconds
                    'cron_messages': [
                        'This is channel_one cron message one.',
                        'This is channel_one cron message two.'
                    ]
                }
            },  # if set to true will display any data received
            'log_messages': True,
            'socket_buffer_size': 2048  # maximum amount of bytes to receive from socket - 1024-4096 recommended
            }

