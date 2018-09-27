gather: gather.py
	@python gather.py -f config.ini
init: gather.py
	@python gather.py -f config.ini --init
