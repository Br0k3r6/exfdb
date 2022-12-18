#!/usr/bin/env python3

import os
import exf_utils.lib.banner as banner
import exf_utils.lib.tool_shower as show
import exf_utils.lib.user as user

global helpfile
helpfile = """-HELP-----------------------------------------
search <word>       | Searches for a word in exploits, Example: ssh
use <module>        | Use a module Example: use example/example_rce
show options        | Display the options in a module
show exploits       | Display all exploits
show auxiliaries    | Display all auxiliaries
show all            | Display all exploits and auxiliaries
num exploits        | Display how much exploits in exfdb
num auxiliaries     | Display how much auxiliaries in exfdb
set <option> <dest> | Set a option in a module to a destination value
clear               | Clear the framework console
banner              | Display a random exfdb banner
exit / quit         | Exit the framework
-HELP-----------------------------------------"""

def start():
	exploits = str(open("modules/exploits.txt").read()).replace("\n", "")
	auxiliaries = str(open("modules/auxiliaries.txt").read()).replace("\n", "")
	try:
		while True:
			cmd_input = input(f"Exfdb (-)>")
			cmd = str(cmd_input).lower()
			if cmd == "exit" or cmd == "quit" or cmd == "exit()" or cmd == "quit()":
				exit()
			elif cmd == "help":
				print(helpfile)
			elif "search " in cmd:
				cmd1 = cmd.split("search ")
				cmd = cmd1
				print("-SEARCH-EXPLOIT-------------------------")
				try:
					if cmd[0] == "" or cmd[0] == " ":
						cmd = cmd[1]
					else:
						cmd = cmd[0]
				except:
					print("[-] Search command takes a argument to search!")
				else:
					file = str(open("modules/exploit_list.txt").read())
					file = file.split("\n")
				found = 0
				for search_query in file:
					if search_query == "" or search_query == " " or search_query == "\n":
						continue
					if cmd.lower() in search_query.lower():
						print("  "+search_query)
						found += 1
				if found == 0:
					print("[-] No exploits found!")
				print("-SEARCH-EXPLOIT-------------------------")
				print()
				cmd = cmd1
				print("-SEARCH-AUXILIARY-----------------------")
				try:
					if cmd[0] == "" or cmd[0] == " ":
						cmd = cmd[1]
					else:
						cmd = cmd[0]
				except:
					print("[-] Search command takes a argument to search!")
				else:
					file = str(open("modules/auxiliary_list.txt").read())
					file = file.split("\n")
				found = 0
				for search_query in file:
					if search_query == "" or search_query == " " or search_query == "\n":
						continue
					if cmd.lower() in search_query.lower():
						print("  "+search_query)
						found += 1
				if found == 0:
					print("[-] No auxiliaries found!")
				print("-SEARCH-AUXILIARY-----------------------")
			elif cmd == "clear":
				os.system("clear")
			elif cmd == "num exploits":
				print("[i] (EXPLOITATION-FRAMEWORK-DATABASE) [ EXFDB ] [ EXPLOITS: " + exploits + " ]")
			elif cmd == "num auxiliaries":
				print("[i] (EXPLOITATION-FRAMEWORK-DATABASE) [ EXFDB ] [ AUXILIARIES: " + auxiliaries + " ]")
			elif cmd == "show exploits":
				exploits_read = str(open("modules/exploit_list.txt").read())
				exploit_list = exploits_read.split("\n")
				print("-EXPLOITS----------------------------\n")
				for exploit in exploit_list:
					if exploit == "" or exploit == " " or exploit == "\n":
						continue
					print("  "+exploit)
				print("\n-EXPLOITS----------------------------")
			elif cmd == "show all":
				exploits_read = str(open("modules/exploit_list.txt").read())
				exploit_list = exploits_read.split("\n")
				print("-EXPLOITS----------------------------\n")
				for exploit in exploit_list:
					if exploit == "" or exploit == " " or exploit == "\n":
						continue
					print("  "+exploit)
				print("\n-EXPLOITS----------------------------")
				print()
				auxiliaries_read = str(open("modules/auxiliary_list.txt").read())
				auxiliary_list = auxiliaries_read.split("\n")
				print("-AUXILIARIES----------------------------\n")
				for auxiliary in auxiliary_list:
					if auxiliary == "" or auxiliary == " " or auxiliary == "\n":
						continue
					print("  "+auxiliary)
				print("\n-AUXILIARIES----------------------------")
			elif cmd == "show auxiliaries":
				auxiliaries_read = str(open("modules/auxiliary_list.txt").read())
				auxiliary_list = auxiliaries_read.split("\n")
				print("-AUXILIARIES----------------------------\n")
				for auxiliary in auxiliary_list:
					if auxiliary == "" or auxiliary == " " or auxiliary == "\n":
						continue
					print("  "+auxiliary)
				print("\n-AUXILIARIES----------------------------")
			elif cmd == "banner":
				banner_result = banner.get_banner()
				print(banner_result)
			elif "use " in cmd:
				user.use(cmd)
			elif cmd == "show options":
				print("[-] You are not in a module!")
			elif "set " in cmd:
				print("[-] You are not in a module!")
			else:
				print("[-] Unknown command: \""+str(cmd_input)+"\"")
	except KeyboardInterrupt:
		exit("\nInterrupted by user")
