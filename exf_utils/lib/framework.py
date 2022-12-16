#!/usr/bin/env python3

import os
import exf_utils.lib.banner as banner

global helpfile
helpfile = """-HELP-----------------------------------------
search <word>       | Searches for a word in exploits, Example: ssh
use <module>        | Use a module Example: use example/example_rce
show options        | Display the options in a module
show exploits       | Display how much exploits in exfdb
show auxiliaries    | Display how much auxiliaries in exfdb
set <option> <dest> | Set a option in a module to a destination value
clear               | Clear the framework console
banner              | Display a random exfdb banner
exit / quit         | Exit the framework
-HELP-----------------------------------------"""

def start():
	try:
		while True:
			cmd_input = input("Exfdb >")
			cmd = str(cmd_input).lower()
			if cmd == "exit" or cmd == "quit" or cmd == "exit()" or cmd == "quit()":
				exit()
			elif cmd == "help":
				print(helpfile)
			elif cmd == "clear":
				os.system("clear")
			elif cmd == "show exploits":
				print("[i] (EXPLOITATION-FRAMEWORK-DATABASE) [ EXFDB ] [ EXPLOITS: " + exploits + " ]")
			elif cmd == "show auxiliaries":
				print("[i] (EXPLOITATION-FRAMEWORK-DATABASE) [ EXFDB ] [ AUXILIARIES: " + auxiliaries + " ]")
			elif cmd == "banner":
				banner_result = banner.get_banner()
				print(banner_result)
			else:
				print("[-] Unknown command: "+str(cmd_input))
	except KeyboardInterrupt:
		exit("\nInterrupted by user")
