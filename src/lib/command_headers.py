from src.config.config import *

commands = {
	'!test': {
		'limit': 30,
		'return': 'This is a test!'
	},

	'!randomemote': {
		'limit': 180,
		'argc': 0,
		'return': 'command'
	},

	'!wow': {
		'limit': 30,
		'argc': 3,
		'return': 'command'
	},

	'!startbets': {
		'limit': 0,
		'argc': 0,
		'return': 'command'
	},

	'!bet': {
		'limit': 0,
		'argc': 1,
		'return': 'command'
	},

	'!endbets': {
		'limit': 0,
		'argc': 0,
		'return': 'command'
	},

	'!winner': {
		'limit': 0,
		'argc': 1,
		'return': 'command'
	}
}










for channel in config['channels']:
	for command in commands:
		commands[command][channel] = {}
		commands[command][channel]['last_used'] = 0
