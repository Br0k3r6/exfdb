#!/usr/bin/env python3
import exf_utils.database.config as database
import exf_utils.lib.banner as banner
import time
import os
import sys

if os.geteuid() != 0:
	exit("Run it as root")

print("[+] Starting exfdb database...")
time.sleep(2)

if database.init_config() == 0:
	print("[i] Database already configured!")
else:
	print("[+] Database successfully configured!")
time.sleep(0.5)

for x in range(26):
	print("[+] Starting the exfdb(EXPLOITATION-FRAMEWORK-DATABASE) console... |       ", end="\r")
	import os
	import sys
	time.sleep(0.1)
	print("[+] Starting the exfdb(EXPLOITATION-FRAMEWORK-DATABASE) console... /       ", end="\r")
	time.sleep(0.1)
	print("[+] Starting the exfdb(EXPLOITATION-FRAMEWORK-DATABASE) console... |       ", end="\r")
	time.sleep(0.1)
	print("[+] Starting the exfdb(EXPLOITATION-FRAMEWORK-DATABASE) console... \\       ", end="\r")
	time.sleep(0.1)

# OUTPUT
print("[+] The exfdb(EXPLOITATION-FRAMEWORK-DATABASE) console started without errors!")
global exploits
global auxiliaries
exploits = 1
auxiliaries = 1
exploits = str(exploits)
auxiliaries = str(auxiliaries)
print("[i] (EXPLOITATION-FRAMEWORK-DATABASE) [ EXFDB ] [ EXPLOITS: " + exploits + " ]")
print("[i] (EXPLOITATION-FRAMEWORK-DATABASE) [ EXFDB ] [ AUXILIARIES: " + auxiliaries + " ]")
banner_result = banner.get_banner()
print(banner_result)
# OUTPUT

import exf_utils.lib.framework as framework
framework.start()
