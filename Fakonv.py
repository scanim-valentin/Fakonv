#!/usr/bin/env python3

import time
import sys, os

def readDialog(file):
	
	class Conv:
		conversation = ""
	
	def printConv(string):
		os.system("clear")
		conv.conversation = conv.conversation + string + "\n"
		print(conv.conversation)
			
	conv = Conv()
	
	lineType = True #If False it's a quote, if True it's a delay
	linesList = file.readlines()
	for line in linesList:
		delay = 0
		if lineType :
			lineType = False
			if line[-2] == 'A': #if a reply is required..
				reply = input() #..the script will wait for any input
				os.system('clear')
				printConv("> "+reply+"\n")
				if len(line) != 2:
					delay = int(line[:len(line)-2])
			else:
				delay = int(line)
			time.sleep(delay)
		else :
			lineType = True
			quote = line
			printConv(quote)
			#print("")		

file = open(input("Enter the name of the text file >>"),"r")
readDialog(file)
file.close()

