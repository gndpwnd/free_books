#!/usr/bin/python3

from fileinput import filename
from re import L
from colorama import Fore
import os
import subprocess

main_filename = "filenamefixer.py"
Host_Dir = os.path.realpath(__file__).split(main_filename)[0]
Num_Checks = 1

special_chars = [
	"!",
	"@",
	"#",
	"$",
	"%",
	"^",
	"&",
	"*",
	"(",
	")",
	"-",
	"+",
	"=",
]
replace_strs = {
	"(_PDFDrive_)" : " ",
	"Pdf." : " ",
	"pdf." : " ",
	"Pdf" : " ",
	"pdf" : " ",
	"-" : " ", 
	"," : " ", 
	"_.": " ", 
	"__" : " ",
}

def clear_screen():
		if os.name == "nt":
			os.system("cls")
		elif os.name == "posix":
			os.system("clear")

def fancy_print(str, val, ind):
        indent = ""
        for i in range(ind):
            indent += "    "

        if val == "":
            print(indent + Fore.GREEN + "[+] " +  Fore.RESET + str)
        else:
            print(indent + Fore.GREEN + "[+] " + Fore.RESET + str + Fore.YELLOW + val + Fore.RESET)


work_dir = "/Drivearchive1/free_books/docs/books/"
fancy_print("Working directory: " + Fore.YELLOW + work_dir + Fore.RESET, "", 0)
log_file = work_dir + "Filenamefixer.Log"
exclude_files = [".git", "filenamefixer.py", log_file]
default_replace_char = "_"

cmds = []

def scan_file(file):

	# get filename from path
	filename = file.split("/")[-1]
	path = file.split(filename)[0]

	if filename in exclude_files:
		pass
	else:
		new_filename = ""
		
		for char in special_chars:
			if char in filename:
				new_filename = filename.replace(char, default_replace_char)
		for key, value in replace_strs.items():
			if key in filename:
				new_filename = filename.replace(key, value)
		
		new_filename = new_filename.replace("_", " ")
		new_filename = new_filename.title()
		new_filename = new_filename.replace(" ", "_")
		new_filename = new_filename.replace("__", "_")
		new_filename = new_filename.replace("._", ".pdf")

		if new_filename != filename:
			print(Fore.YELLOW + "Changing: " + Fore.RESET + file + Fore.YELLOW + " -> " + Fore.RESET + path + new_filename)
			os.rename(file, path + new_filename)

def ffixer(num_checks):
	num_files = 0
	
	for i in range(num_checks):

		print(Fore.GREEN + "\n\n[+] " + Fore.WHITE + "Running Check " + Fore.RED + str(i+1) + Fore.WHITE + " of " + Fore.RED + str(num_checks) + Fore.WHITE + "...\n\n")

		for root, dirs, files in os.walk(work_dir):
			for file in files:
				num_files += 1
				# send whole path to scan_file
				scan_file(root + "/" + file)

		print(Fore.GREEN + "[+] " + Fore.WHITE + "Processed " + Fore.RED + str(num_files) + Fore.WHITE + " files...")

		clear_screen()

	print(Fore.RED)
	for cmd in cmds:
		subprocess.call(cmd, shell=True, executable='/bin/bash')
    
	fancy_print("Number of files in working directory: " + Fore.YELLOW + str(num_files) + Fore.RESET, "", 0)

	case1 = Fore.YELLOW + "[+] " + Fore.WHITE + """Observe the following:

Check the log file for errors by running the following command: 

(Windows)
notepad.exe {}

(Linux)
cat {}

After exiting this program, the log file will be deleted. 

Press ENTER to Continue...
""".format(os.path.abspath(log_file), os.path.abspath(log_file))


	case2 = Fore.GREEN + "[+] " + Fore.WHITE + """Observe the following:

Press ENTER to Continue...
"""

	if os.path.exists(log_file):
		input(case1)
		os.remove(log_file)
	else:
		input(case2)

	clear_screen()
	print(Fore.GREEN + "\n\n[+] " + Fore.WHITE + "Done!\n\n")