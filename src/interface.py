#!/usr/bin/env python2
#Works in working dir...
import sys
import os
import shutil
import re
from movie_renamer import rename

def query_yes_no(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is one of "yes" or "no".
    """
    valid = {"yes":True,   "y":True,  "ye":True,
             "no":False,     "n":False}
    if default == None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = raw_input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "\
                             "(or 'y' or 'n').\n")


movieExt = ('.avi','.mpg','.mkv')
for filename in os.listdir('.'):
	#Special case, if there is a movie without a folder, create a folder with moviename
	#and try to rename folder
	if os.path.isdir(filename) == False:
		filename_without_extension, extension = os.path.splitext(filename)
		if extension in movieExt:
			os.mkdir(filename_without_extension)
			shutil.move(filename,filename_without_extension + "/" + filename)
			filename = filename_without_extension
		else:
			continue
	
	new = rename(filename)
	#Ignore stuff that are basically the same.
	newFix = re.sub(r'[^a-zA-Z0-9_]', '', new.lower())
	fFix = re.sub(r'[^a-zA-Z0-9_]', '', filename.lower())
	if newFix ==  fFix:
		continue
	
	if new == "None":
		sys.stdout.write("Fail to rename " + filename + "\n")
		continue
		
	#Query a rename	
	if query_yes_no("Rename\t" + filename + "\nto\t" + new):
		try:
			os.rename(filename, new)
		except:
			sys.stdout.write("Fail to rename " + filename + " to " + new + "\n")
