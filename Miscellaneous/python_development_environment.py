# https://wiki.freecadweb.org/Scripting_examples
# https://wiki.freecadweb.org/Python_Development_Environment

FreeCAD.ParamGet('User parameter:BaseApp/Preferences/Macro').SetString('MacroPath','/me/myself/and/I')

def breakpoint(*args):
	# this routine will print an optional parameter on the console and then stop execution by diving by zero
	# e.g. breakpoint()
	# e.g. breakpoint("summation module")
	#
	if len(args)>0:
		FreeCAD.Console.PrintMessage('Breakpoint: '+str(args[0])+"\n")
	hereWeStop = 12/0

breakpoint('amalgamation routine')

FreeCAD.myVariable = 123

FreeCAD.myVariable

# program A
myListVariable = list()
myListVariable.append(123)
myListVariable.append('abc')
FreeCAD.myVariable = myListVariable

myOtherVariable = FreeCAD.myVariable
# further calculations involving myOtherVariable

FreeCAD.myVariable

def monthCounter():
	# program to calculate the number of months in the year
	signsInTheZodiac = 12
	numberOfSeasons = 3
	numberOfCompassPoints = 5
	#
	temporaryVariable1 = signsInTheZodiac + numberOfSeasons
	numberOfMonths = temporaryVariable1 - numberOfCompassPoints
	#
	FreeCAD.Console.PrintMessage(numberOfMonths)

monthCounter()

def monthCounter():
	# program to calculate the number of months in the year
	signsInTheZodiac = 12
	numberOfSeasons = 3
	numberOfCompassPoints = 5
	#
	temporaryVariable1 = signsInTheZodiac + numberOfSeasons
	FreeCAD.saveMyVariable = temporaryVariable1 # <<<<<<<<<<< first inserted line
	breakpoint('is this assignment faulty?') # <<<<<<<<<<<<<< second inserted line
	numberOfMonths = temporaryVariable1 - numberOfCompassPoints
	#
	FreeCAD.Console.PrintMessage(numberOfMonths)

monthCounter()

FreeCAD.saveMyVariable

numberOfSeasons = 3

numberOfSeasons = 4

def monthCounter():
	# program to calculate the number of months in the year
	signsInTheZodiac = 12
	numberOfSeasons = 4
	numberOfCompassPoints = 5
	#
	temporaryVariable1 = signsInTheZodiac + numberOfSeasons
	FreeCAD.saveMyVariable1 = temporaryVariable1
	#breakpoint('first assignment')
	numberOfMonths = temporaryVariable1 - numberOfCompassPoints
	FreeCAD.saveMyVariable2 = numberOfMonths
	breakpoint('second assignment')
	#
	FreeCAD.Console.PrintMessage(numberOfMonths)

FreeCAD.saveMyVariable1

FreeCAD.saveMyVariable2

#
#			TEST
#			TEST stub to clip any code onto...
#			TEST
#
################################
# routine to <description goes here>
"""
script does <long winded description goes here>
"""

# import statements
import FreeCAD
from FreeCAD import Base
import math, collections
from PySide import QtGui, QtCore

# UI Class definitions

# Class definitions

# Functions definitions

# Constant definitions

# code ***********************************************************************************

QtGui.QMessageBox.information(None,"","Test Stub")

##########################################################################################
##########################################################################################
##########################################################################################
