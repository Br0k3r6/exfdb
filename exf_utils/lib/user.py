#!/usr/bin/env python3

def use(command):
	if command.lower() == "use modules/exploits/http/php/php_8.1.0_dev_code_injection":
		import os
		os.system("python3 modules/exploits/http/php/PHP_8_1_0_dev_code_injection/index.py")
	elif command.lower() == "use modules/auxiliaries/http/php/vulnerability_checker":
		import os
		os.system("python3 modules/auxiliaries/http/php/vulnerability_checker/index.py")
