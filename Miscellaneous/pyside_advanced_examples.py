# https://wiki.freecadweb.org/Scripting_examples
# https://wiki.freecadweb.org/PySide_Advanced_Examples

import sys
from PySide import QtGui ,QtCore 
app = QtGui.qApp
mw = FreeCADGui.getMainWindow()

for child in mw.children():
   print('widget name = ', child.objectName(), ', widget type = ', child)

myWidget = QtGui.QDockWidget()
mw.addDockWidget(QtCore.Qt.RightDockWidgetArea,myWidget)

myWidget.setObjectName("my Nice New Widget")
myWidget.resize(QtCore.QSize(300,100)) # sets size of the widget
label = QtGui.QLabel("Hello World", myWidget) # creates a label
label.setGeometry(QtCore.QRect(2,50,200,24))  # sets its size
label.setObjectName("myLabel") # sets its name, so it can be found by name

class myWidget_Ui(object):
  def setupUi(self, myWidget):
    myWidget.setObjectName("my Nice New Widget")
    myWidget.resize(QtCore.QSize(300,100).expandedTo(myWidget.minimumSizeHint())) # sets size of the widget

    self.label = QtGui.QLabel(myWidget) # creates a label
    self.label.setGeometry(QtCore.QRect(50,50,200,24)) # sets its size
    self.label.setObjectName("label") # sets its name, so it can be found by name

  def retranslateUi(self, draftToolbar): # built-in QT function that manages translations of widgets
    myWidget.setWindowTitle(QtGui.QApplication.translate("myWidget", "My Widget", None, QtGui.QApplication.UnicodeUTF8))
    self.label.setText(QtGui.QApplication.translate("myWidget", "Welcome to my new widget!", None, QtGui.QApplication.UnicodeUTF8))

app = QtGui.qApp
FCmw = app.activeWindow()
myNewFreeCADWidget = QtGui.QDockWidget() # create a new dckwidget
myNewFreeCADWidget.ui = myWidget_Ui() # load the Ui script
myNewFreeCADWidget.ui.setupUi(myNewFreeCADWidget) # setup the ui
FCmw.addDockWidget(QtCore.Qt.RightDockWidgetArea,myNewFreeCADWidget) # add the widget to the main window
