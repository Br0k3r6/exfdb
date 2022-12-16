#!/usr/bin/env python3

def init_config():
	import exf_utils.database.dblib as dblib
	if dblib.check_res() == 1:
		pass
	elif dblib.check_res() == 0:
		return 0
