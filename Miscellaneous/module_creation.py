# https://wiki.freecadweb.org/Scripting_examples
# https://wiki.freecadweb.org/Module_Creation

class MyWorkbench ( Workbench ):
	"My workbench object"
	Icon = """
			/* XPM */
			static const char *test_icon[]={
			"16 16 2 1",
			"a c #000000",
			". c None",
			"................",
			"................",
			"..############..",
			"..############..",
			"..############..",
			"......####......",
			"......####......",
			"......####......",
			"......####......",
			"......####......",
			"......####......",
			"......####......",
			"......####......",
			"......####......",
			"................",
			"................"};
			"""
	MenuText = "My Workbench"
	ToolTip = "This is my extraordinary workbench"

        def GetClassName(self):
               return "Gui::PythonWorkbench"
	
	def Initialize(self):
		import myModule1, myModule2
		self.appendToolbar("My Tools", ["MyCommand1","MyCommand2"])
		self.appendMenu("My Tools", ["MyCommand1","MyCommand2"])
		Log ("Loading MyModule... done\n")

	def Activated(self):
               # do something here if needed...
		Msg ("MyWorkbench.Activated()\n")

	def Deactivated(self):
               # do something here if needed...
		Msg ("MyWorkbench.Deactivated()\n")

FreeCADGui.addWorkbench(MyWorkbench)

import FreeCAD,FreeCADGui

class MyTool:
	"My tool object"

       def GetResources(self):
               return {"MenuText": "My Command",
                       "Accel": "Ctrl+M",
                       "ToolTip": "My extraordinary command",
                       "Pixmap"  : """
			/* XPM */
			static const char *test_icon[]={
			"16 16 2 1",
			"a c #000000",
			". c None",
			"................",
			"................",
			"..############..",
			"..############..",
			"..############..",
			"......####......",
			"......####......",
			"......####......",
			"......####......",
			"......####......",
			"......####......",
			"......####......",
			"......####......",
			"......####......",
			"................",
			"................"};
			"""}

       def IsActive(self):
               if FreeCAD.ActiveDocument == None:
                       return False
               else:
                       return True

	def Activated(self):
               # do something here...

FreeCADGui.addCommand('MyCommand1',MyTool())


