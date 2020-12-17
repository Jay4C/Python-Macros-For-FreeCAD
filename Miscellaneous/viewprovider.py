# https://wiki.freecadweb.org/Scripting_examples
# https://wiki.freecadweb.org/Viewprovider

# views/view_custom.py
class ViewProviderCustom:
    """Viewprovider of the custom object."""

    def __init__(self, vobj):
        self.Object = vobj.Object

        self._set_properties(vobj)
        vobj.Proxy = self

    def _set_properties(self, vobj):
        if not hasattr(vobj, "Pattern"):
            vobj.addProperty("App::PropertyEnumeration",
                             "Pattern",
                             "Custom",
                             "Defines a hatch pattern for this object.")
            vobj.Pattern = ["None", "diagonals", "cross", "brick"]

        if not hasattr(vobj, "PatternSize"):
            vobj.addProperty("App::PropertyFloat",
                             "PatternSize",
                             "Custom",
                             "Defines the size of the hatch pattern.")
            vobj.PatternSize = 1

    def onChanged(self, vobj, prop):
        if prop in "Pattern":
            self._set_pattern(vobj.Pattern)
        if prop in "PatternSize":
            self._set_size(vobj.PatternSize)

import FreeCAD as App
import objects.custom as custom
import views.view_custom as view_custom

doc = App.newDocument()
obj = doc.addObject("Part::FeaturePython", "Custom")

custom.CustomObject(obj)

if App.GuiUp:
    view_custom.ViewProviderCustom(obj.ViewObject)

import os
some_path = "/home/user/.FreeCAD/custom_icons"

class ViewProviderCustom:
    def getIcon(self):
        return os.path.join(some_path, "my_icon.svg")
    
import MyModule_rc.py

class ViewProviderCustom:
    def getIcon(self):
        return ":/icons/my_icon.svg"

import MyModule_rc.py

class ViewProviderCustom:
    def getIcon(self):
        return """
               /* XPM */
               static char *Some_icon_xpm[] = {
               /* columns rows colors chars-per-pixel */
               "16 16 3 1 ",
               "  c None",
               ". c #D71414",
               "+ c #AA1919",
               /* pixels */
               "                ",
               "  +          +  ",
               " +.+        +.+ ",
               "  +.+      +.+  ",
               "   +        +   ",
               "      ++++      ",
               "     +....+     ",
               "     +...++     ",
               "     +..+++     ",
               "     +.++.+     ",
               "      ++++      ",
               "   +        +   ",
               "  +.+      +.+  ",
               " +.+        +.+ ",
               "  +          +  ",
               "                "
               };
               """
