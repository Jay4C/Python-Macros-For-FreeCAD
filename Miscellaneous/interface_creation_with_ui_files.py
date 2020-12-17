# https://wiki.freecadweb.org/Scripting_examples
# https://wiki.freecadweb.org/PySide_usage_snippets

import FreeCADGui as Gui

class SomeTool:
    def __init__(self):
        self.ui_path = "Mod/MyWorkbench/file.ui"
        self.form = Gui.PySideUic.loadUi(self.ui_path)

Gui.Control.showDialog(SomeTool())
