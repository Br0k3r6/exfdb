#!/usr/bin/env python3

def check_res():
	import os
	file = open("exf_utils/database/dbconfig.conf")
	if "1" in file.read():
		os.system("sudo chmod 777 exf_utils/database/clear.sh; sudo ./exf_utils/database/clear.sh")
		return 1
	else:
		return 0
