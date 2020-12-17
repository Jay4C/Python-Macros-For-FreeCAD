# https://wiki.freecadweb.org/Scripting_examples
# https://wiki.freecadweb.org/PySide_Beginner_Examples

from PySide import QtCore
from PySide import QtGui

reply = QtGui.QMessageBox.information(None,"","Houston, we have a problem")

reply = QtGui.QMessageBox.question(None, "", "This is your chance to answer, what do you think?",
         QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
if reply == QtGui.QMessageBox.Yes:
         # this is where the code relevant to a 'Yes' answer goes
         pass
if reply == QtGui.QMessageBox.No:
         # this is where the code relevant to a 'No' answer goes
         pass

reply = QtGui.QInputDialog.getText(None, "Ouija Central","Enter your thoughts for the day:")
if reply[1]:
	# user clicked OK
	replyText = reply[0]
else:
	# user clicked Cancel
	replyText = reply[0] # which will be "" if they clicked Cancel

anInteger = int(userInput) # to convert to an integer from a string representation

aFloat = float(userInput) # to convert to a float from a string representation

from PySide import QtGui, QtCore

class MyButtons(QtGui.QDialog):
	""""""
	def __init__(self):
		super(MyButtons, self).__init__()
		self.initUI()
	def initUI(self):      
		option1Button = QtGui.QPushButton("Option 1")
		option1Button.clicked.connect(self.onOption1)
		option2Button = QtGui.QPushButton("Option 2")
		option2Button.clicked.connect(self.onOption2)
		option3Button = QtGui.QPushButton("Option 3")
		option3Button.clicked.connect(self.onOption3)
		option4Button = QtGui.QPushButton("Option 4")
		option4Button.clicked.connect(self.onOption4)
		option5Button = QtGui.QPushButton("Option 5")
		option5Button.clicked.connect(self.onOption5)
		#
		buttonBox = QtGui.QDialogButtonBox()
		buttonBox = QtGui.QDialogButtonBox(QtCore.Qt.Horizontal)
		buttonBox.addButton(option1Button, QtGui.QDialogButtonBox.ActionRole)
		buttonBox.addButton(option2Button, QtGui.QDialogButtonBox.ActionRole)
		buttonBox.addButton(option3Button, QtGui.QDialogButtonBox.ActionRole)
		buttonBox.addButton(option4Button, QtGui.QDialogButtonBox.ActionRole)
		buttonBox.addButton(option5Button, QtGui.QDialogButtonBox.ActionRole)
		#
		mainLayout = QtGui.QVBoxLayout()
		mainLayout.addWidget(buttonBox)
		self.setLayout(mainLayout)
		# define window		xLoc,yLoc,xDim,yDim
		self.setGeometry(	250, 250, 0, 50)
		self.setWindowTitle("Pick a Button")
		self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
	def onOption1(self):
		self.retStatus = 1
		self.close()
	def onOption2(self):
		self.retStatus = 2
		self.close()
	def onOption3(self):
		self.retStatus = 3
		self.close()
	def onOption4(self):
		self.retStatus = 4
		self.close()
	def onOption5(self):
		self.retStatus = 5
		self.close()

def routine1():
	print 'routine 1'

form = MyButtons()
form.exec_()
if form.retStatus==1:
	routine1()
elif form.retStatus==2:
	routine2()
elif form.retStatus==3:
	routine3()
elif form.retStatus==4:
	routine4()
elif form.retStatus==5:
	routine5()

buttonBox = QtGui.QDialogButtonBox(QtCore.Qt.Horizontal)

buttonBox = QtGui.QDialogButtonBox(QtCore.Qt.Vertical)
