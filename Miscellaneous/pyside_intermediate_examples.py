# https://wiki.freecadweb.org/Scripting_examples
# https://wiki.freecadweb.org/PySide_Intermediate_Examples

from PySide import QtGui, QtCore

# import statements
from PySide import QtGui, QtCore

# UI Class definitions

class ExampleModalGuiClass(QtGui.QDialog):
	""""""
	def __init__(self):
		super(ExampleModalGuiClass, self).__init__()
		self.initUI()
	def initUI(self):
		self.result = userCancelled
		# create our window
		# define window		xLoc,yLoc,xDim,yDim
		self.setGeometry(	250, 250, 400, 350)
		self.setWindowTitle("Our Example Modal Program Window")
		self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
		# create some Labels
		self.label1 = QtGui.QLabel("                       ", self)
		self.label1.setFont('Courier') # set to a non-proportional font
		self.label1.move(20, 20)
		self.label2 = QtGui.QLabel("sample string number two", self)
		self.label2.move(20, 70)
		self.label3 = QtGui.QLabel("                        ", self)
		self.label3.setFont('Courier') # set to a non-proportional font
		self.label3.move(20, 120)
		self.label4 = QtGui.QLabel("can you see this?", self)
		self.label4.move(20, 170)
		# checkboxes
		self.checkbox1 = QtGui.QCheckBox("Left side", self)
		self.checkbox1.clicked.connect(self.onCheckbox1)
		#self.checkbox1.toggle() # will set an initial value if executed
		self.checkbox1.move(210,10)
		#
		self.checkbox2 = QtGui.QCheckBox("Right side", self)
		self.checkbox2.clicked.connect(self.onCheckbox2)
		self.checkbox2.move(210,30)
		# radio buttons
		self.radioButton1 = QtGui.QRadioButton("random string one",self)
		self.radioButton1.clicked.connect(self.onRadioButton1)
		self.radioButton1.move(210,60)
		#
		self.radioButton2 = QtGui.QRadioButton("owt gnirts modnar",self)
		self.radioButton2.clicked.connect(self.onRadioButton2)
		self.radioButton2.move(210,80)
		# set up lists for pop-ups
		self.popupItems1 = ("pizza","apples","candy","cake","potatoes")
		# set up pop-up menu
		self.popup1 = QtGui.QComboBox(self)
		self.popup1.addItems(self.popupItems1)
		self.popup1.setCurrentIndex(self.popupItems1.index("candy"))
		self.popup1.activated[str].connect(self.onPopup1)
		self.popup1.move(210, 115)
		# toggle visibility button
		pushButton1 = QtGui.QPushButton('Toggle visibility', self)
		pushButton1.clicked.connect(self.onPushButton1)
		pushButton1.setAutoDefault(False)
		pushButton1.move(210, 165)
		# text input field
		self.textInput = QtGui.QLineEdit(self)
		self.textInput.setText("cats & dogs")
		self.textInput.setFixedWidth(190)
		self.textInput.move(20, 220)
		# set contextual menu options for text editing widget
		# set text field to some dogerel
		popMenuAction1 = QtGui.QAction(self)
		popMenuAction1.setText("load some text")
		popMenuAction1.triggered.connect(self.onPopMenuAction1)
		# make text uppercase
		popMenuAction2 = QtGui.QAction(self)
		popMenuAction2.setText("uppercase")
		popMenuAction2.triggered.connect(self.onPopMenuAction2)
		# menu dividers
		popMenuDivider = QtGui.QAction(self)
		popMenuDivider.setText('---------')
		popMenuDivider.triggered.connect(self.onPopMenuDivider)
		# remove all text
		popMenuAction3 = QtGui.QAction(self)
		popMenuAction3.setText("clear")
		popMenuAction3.triggered.connect(self.onPopMenuAction3)
		# define menu and add options
		self.textInput.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
		self.textInput.addAction(popMenuAction1)
		self.textInput.addAction(popMenuAction2)
		self.textInput.addAction(popMenuDivider)
		self.textInput.addAction(popMenuAction3)
		# numeric input field
		self.numericInput = QtGui.QLineEdit(self)
		self.numericInput.setInputMask("999")
		self.numericInput.setText("000")
		self.numericInput.setFixedWidth(50)
		self.numericInput.move(250, 220)
		# cancel button
		cancelButton = QtGui.QPushButton('Cancel', self)
		cancelButton.clicked.connect(self.onCancel)
		cancelButton.setAutoDefault(True)
		cancelButton.move(150, 280)
		# OK button
		okButton = QtGui.QPushButton('OK', self)
		okButton.clicked.connect(self.onOk)
		okButton.move(260, 280)
		# now make the window visible
		self.show()
		#
	def onCheckbox1(self):
		text = self.label1.text()
		if text[0]==' ':
			self.label1.setText('left'+text[4:])
		else:
			self.label1.setText('    '+text[4:])
	def onCheckbox2(self):
		text = self.label1.text()
		if text[-1]==' ':
			self.label1.setText(text[:-5]+'right')
		else:
			self.label1.setText(text[:-5]+'     ')
	def onRadioButton1(self):
		self.label2.setText(self.radioButton1.text())
	def onRadioButton2(self):
		self.label2.setText(self.radioButton2.text())
	def onPopup1(self, selectedText):
		if self.label3.text().isspace():
			self.label3.setText(selectedText)
		else:
			self.label3.setText(self.label3.text()+","+selectedText)
	def onPushButton1(self):
		if self.label4.isVisible():
			self.label4.hide()
		else:
			self.label4.show()
	def onPopMenuAction1(self):
		# load some text into field
		self.textInput.setText("Lorem ipsum dolor sit amet")
	def onPopMenuAction2(self):
		# set text in field to uppercase
		self.textInput.setText(self.textInput.text().upper())
	def onPopMenuDivider(self):
		# this option is the divider and is really there as a spacer on the menu list
		# consequently it has no functional code to execute if user selects it
		pass
	def onPopMenuAction3(self):
		# clear the text from the field
		self.textInput.setText('')
	def onCancel(self):
		self.result			= userCancelled
		self.close()
	def onOk(self):
		self.result			= userOK
		self.close()
	def mousePressEvent(self, event):
		# print mouse position, X & Y
		print "X = ", event.pos().x()
		print "Y = ", event.pos().y()
		#
		if event.button() == QtCore.Qt.LeftButton:
			print "left mouse button"
		if self.label1.underMouse():
			print "over the text '"+self.label1.text()+"'"
		if self.label2.underMouse():
			print "over the text '"+self.label2.text()+"'"
		if self.label3.underMouse():
			print "over the text '"+self.label3.text()+"'"
		if self.label4.underMouse():
			print "over the text '"+self.label4.text()+"'"
		if self.textInput.underMouse():
			print "over the text '"+self.textInput.text()+"'"
		if event.button() == QtCore.Qt.RightButton:
			print "right mouse button"

# Class definitions

# Function definitions

# Constant definitions
userCancelled		= "Cancelled"
userOK			= "OK"

# code ***********************************************************************************

form = ExampleModalGuiClass()
form.exec_()

if form.result==userCancelled:
	pass # steps to handle user clicking Cancel
if form.result==userOK:
	# steps to handle user clicking OK
	localVariable1 = form.label1.text()
	localVariable2 = form.label2.text()
	localVariable3 = form.label3.text()
	localVariable4 = form.label4.text()
	print localVariable1
	print localVariable2
	print localVariable3
	print localVariable4
#
#OS: Mac OS X
#Word size: 64-bit
#Version: 0.14.3703 (Git)
#Branch: releases/FreeCAD-0-14
#Hash: c6edd47334a3e6f209e493773093db2b9b4f0e40
#Python version: 2.7.5
#Qt version: 4.8.6
#Coin version: 3.1.3
#SoQt version: 1.5.0
#OCC version: 6.7.0
#

from PySide import QtGui, QtCore

# UI Class definitions

class ExampleNonmodalGuiClass(QtGui.QMainWindow):
	""""""
	def __init__(self):
		super(ExampleNonmodalGuiClass, self).__init__()
		self.initUI()
	def initUI(self):
		self.result = userCancelled
		# create our window
		# define window		xLoc,yLoc,xDim,yDim
		self.setGeometry(	250, 250, 400, 150)
		self.setWindowTitle("Our Example Nonmodal Program Window")
		self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
		self.setMouseTracking(True)
		# create Labels
		self.label4 = QtGui.QLabel("can you see this?", self)
		self.label4.move(20, 20)
		self.label5 = QtGui.QLabel("Mouse position:", self)
		self.label5.move(20, 70)
		self.label6 = QtGui.QLabel("               ", self)
		self.label6.move(135, 70)
		# toggle visibility button
		pushButton1 = QtGui.QPushButton('Toggle visibility', self)
		pushButton1.clicked.connect(self.onPushButton1)
		pushButton1.setMinimumWidth(150)
		#pushButton1.setAutoDefault(False)
		pushButton1.move(210, 20)
		# cancel button
		cancelButton = QtGui.QPushButton('Cancel', self)
		cancelButton.clicked.connect(self.onCancel)
		cancelButton.setAutoDefault(True)
		cancelButton.move(150, 110)
		# OK button
		okButton = QtGui.QPushButton('OK', self)
		okButton.clicked.connect(self.onOk)
		okButton.move(260, 110)
		# now make the window visible
		self.show()
		#
	def onPushButton1(self):
		if self.label4.isVisible():
			self.label4.hide()
		else:
			self.label4.show()
	def onCancel(self):
		self.result			= userCancelled
		self.close()
	def onOk(self):
		self.result			= userOK
		self.close()
	def mouseMoveEvent(self,event):
		self.label6.setText("X: "+str(event.x()) + " Y: "+str(event.y()))
# Class definitions

# Function definitions

# Constant definitions
global userCancelled, userOK
userCancelled		= "Cancelled"
userOK			= "OK"

# code ***********************************************************************************

form = ExampleNonmodalGuiClass()
#
#OS: Mac OS X
#Word size: 64-bit
#Version: 0.14.3703 (Git)
#Branch: releases/FreeCAD-0-14
#Hash: c6edd47334a3e6f209e493773093db2b9b4f0e40
#Python version: 2.7.5
#Qt version: 4.8.6
#Coin version: 3.1.3
#SoQt version: 1.5.0
#OCC version: 6.7.0

# get screen dimensions (Available Screen Size)
screenWidth		= QtGui.QDesktopWidget().screenGeometry().width()
screenHeight		= QtGui.QDesktopWidget().screenGeometry().height()
# get dimensions for available space on screen
availableWidth		= QtGui.QDesktopWidget().availableGeometry().width()
availableHeight		= QtGui.QDesktopWidget().availableGeometry().height()

# set up a variable to hold the Main Window to save some typing...
mainWin = FreeCAD.Gui.getMainWindow()

mainWin.showFullScreen() # no menu bars, every last pixel is given over to FreeCAD
mainWin.geometry()
mainWin.frameSize()
mainWin.frameGeometry()

mainWin.showMaximized() # show maximised within the screen, window edges and the menu bar will be displayed
mainWin.geometry()
mainWin.frameSize()
mainWin.frameGeometry()

mainWin.showNormal() # show at the last non-maximised or non-minimised size (and location)
mainWin.geometry()
mainWin.frameSize()
mainWin.frameGeometry()

mainWin.setGeometry(50, 50, 800, 800) # specifically set FreeCAD main window's size and location, this will become the new setting for 'showNormal()'

mainWin.showMinimized() # FreeCAD will disappear from view after this command...
mainWin.geometry()
mainWin.frameSize()
mainWin.frameGeometry()
