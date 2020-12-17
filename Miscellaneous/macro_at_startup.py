# https://wiki.freecadweb.org/Scripting_examples
# https://wiki.freecadweb.org/Macro_at_Startup

## Import section ##
from PySide import QtGui

## Definition section (classes, functions, ...)
class MyMsgBox(QtGui.QMessageBox):

    def __init__(self):
        super(MyMsgBox, self).information(None, "MyTitle", "MyText")

##Main instruction section
MyMsgBox()

from PySide import QtGui
##The 2 below lines shall be added if not already present to ensure FreeCAD modules are imported
import FreeCAD as App
import FreeCADGui as Gui

class MyMsgBox(QtGui.QMessageBox):

    def __init__(self):
        super(MyMsgBox, self).information(None, "MyTitle", "MyText")

##Enclose the main instructions in a function
def run():
    MyMsgBox()

##Ensure main instructions are still called in case of manal run
if __name__ == '__main__':
    run()

def runMacroStartup(name):
    #Do not run when NoneWorkbench is activated because UI isn't yet completely there
    if name != "NoneWorkbench":
        #Run macro only once by disconnecting the signal at first call
        FreeCADGui.getMainWindow().workbenchActivated.disconnect(runMacroStartup)
        ##Following 2 lines shall be duplicated for each macro to run
        import MySuperMacro
        MySuperMacro.run()
        ##Eg. if a second macro shall be launched at startup
        #import MyWonderfulMacro
        #MyWonderfulMacro.run()

##The following 2 lines are important because InitGui.py files are passed to the exec() function...
##...and the runMacro wouldn't be visible outside. So explicitly add it to __main__
import __main__
__main__.runMacro = runMacro

##Connect the function that runs the macro to the appropriate signal
FreeCADGui.getMainWindow().workbenchActivated.connect(runMacro)
