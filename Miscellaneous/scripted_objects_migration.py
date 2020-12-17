# https://wiki.freecadweb.org/Scripting_examples
# https://wiki.freecadweb.org/Scripted_objects_migration

<Document SchemaVersion="4" ProgramVersion="0.19R20959 (Git)" FileVersion="1">
    <Properties Count="15" TransientCount="3">
    </Properties>
    <Objects Count="1" Dependencies="1">
        <ObjectDeps Name="Custom" Count="0"/>
        <Object type="Part::FeaturePython" name="Custom" id="2715" Touched="1" />
    </Objects>
    <ObjectData Count="1">
        <Object name="Custom">
            <Properties Count="9" TransientCount="0">
                <Property name="Proxy" type="App::PropertyPythonObject" status="1">
                    <Python value="eyJUeXBlIjogIkN1c3RvbSJ9" encoded="yes" module="old_module" class="OldObject"/>
                </Property>
            </Properties>
        </Object>
    </ObjectData>
</Document>

# old_module.py
class OldObject:
    def __init__(self, obj):
        obj.addProperty("App::PropertyLength", "Length")
        obj.addProperty("App::PropertyArea", "Area")
        obj.Length = 15
        obj.Area = 300
        obj.Proxy = self
        self.Type = "Custom"

    def execute(self, obj):
        pass

import FreeCAD as App
import old_module

doc = App.newDocument()
doc.FileName = "my_document.FCStd"

obj = doc.addObject("Part::FeaturePython", "Custom")
old_module.OldObject(obj)

if App.GuiUp:
    obj.ViewObject.Proxy = 1

doc.recompute()
doc.save()

obj = App.ActiveDocument.Custom

print(obj.PropertiesList)

print(obj.Proxy)

# objects/new_module.py
class NewObject:
    def __init__(self, obj):
        obj.addProperty("App::PropertyLength", "Length")
        obj.addProperty("App::PropertyArea", "GeneralArea")
        obj.addProperty("App::PropertyInteger", "Divisions")
        obj.Length = 30
        obj.GeneralArea = 600
        obj.Divisions = 4
        obj.Proxy = self
        self.Type = "Custom"

    def execute(self, obj):
        pass

obj2 = App.ActiveDocument.Custom2

print(obj2.PropertiesList)

print(obj2.Proxy)

# old_module.py
import objects.new_module as new_module

OldObject = new_module.NewObject

obj = App.ActiveDocument.Custom

print(obj.PropertiesList)

print(obj.Proxy)

# old_module.py
import FreeCAD as App
import objects.new_module as new_module
import viewp.new_view as new_view
_wrn = App.Console.PrintWarning

class OldObject:
    def onDocumentRestored(self, obj):
        new_module.NewObject(obj)
        _wrn("New proxy class used\n")

        if App.GuiUp:
            new_view.ViewProviderNew(obj.ViewObject)
            _wrn("New viewprovider class used\n")

class OldObject:
    def onDocumentRestored(self, obj):
        if hasattr(obj, "Proxy") and obj.Proxy.Type == "Custom":
            _module = str(obj.Proxy.__class__)
            _module = _module.lstrip("<class '").rstrip("'>")

            if _module == "old_module.OldObject":
                self._migrate(obj)

    def _migrate(self, obj):
        _wrn("New proxy class used\n")
        new_module.NewObject(obj)

        if App.GuiUp:
            new_view.ViewProviderNew(obj.ViewObject)
            _wrn("New viewprovider class used\n")

obj = App.ActiveDocument.Custom

print(obj.PropertiesList)

print(obj.Proxy)

# old_module.py
import FreeCAD as App
import objects.new_module as new_module
import viewp.new_view as new_view
_wrn = App.Console.PrintWarning

class OldObject:
    def onDocumentRestored(self, obj):
        old = dict()
        old["Area"] = obj.Area
        old["Length"] = obj.Length
        obj.removeProperty("Area")
        obj.removeProperty("Length")

        new_module.NewObject(obj)

        obj.GeneralArea = 3 * old["Area"]
        obj.Length = old["Length"]
        _wrn("New proxy class used; properties migrated\n")

        if App.GuiUp:
            vobj = obj.ViewObject
            old = dict()

            old["LineScale"] = vobj.LineScale
            vobj.removeProperty("LineScale")

            new_view.ViewProviderNew(vobj)

            vobj.LineScale = 1.05 * old["LineScale"]
            _wrn("New viewprovider class used; view properties migrated\n")

obj.removeProperty("Visibility")

obj = App.ActiveDocument.Custom

print(obj.PropertiesList)

print(obj.Proxy)

# objects/new_module.py
class NewObject:
    def __init__(self, obj):
        if not hasattr(obj, "Length"):
            obj.addProperty("App::PropertyLength", "Length")
            obj.Length = 30
        if not hasattr(obj, "GeneralArea"):
            obj.addProperty("App::PropertyArea", "GeneralArea")
            obj.GeneralArea = 600
        if not hasattr(obj, "Divisions"):
            obj.addProperty("App::PropertyInteger", "Divisions")
            obj.Divisions = 4

        obj.Proxy = self
        self.Type = "Custom"

    def execute(self, obj):
        pass

obj = App.ActiveDocument.Custom

print(obj.PropertiesList)

print(obj.Proxy)

# old_module.py
class OldObject:
    def __init__(self, obj):
        obj.addProperty("App::PropertyLength", "Length")
        obj.addProperty("App::PropertyArea", "Area")
        obj.addProperty("App::PropertyString", "Version")
        obj.setEditorMode("Version", 1)
        obj.Length = 15
        obj.Area = 300
        obj.Version = "0.18"
        obj.Proxy = self
        self.Type = "Custom"

    def execute(self, obj):
        pass

# old_module.py
import FreeCAD as App
import objects.new_module as new_module
_wrn = App.Console.PrintWarning

class OldObject:
    def onDocumentRestored(self, obj):
        if hasattr(obj, "Version") and obj.Version:
            if obj.Version == "0.18":
                _migrate_from_018(obj)
            elif obj.Version == "0.19":
                _migrate_from_019(obj)

def _migrate_from_018(obj):
    old = dict()
    old["Area"] = obj.Area
    old["Length"] = obj.Length
    obj.removeProperty("Area")
    obj.removeProperty("Length")
    obj.removeProperty("Version")

    new_module.NewObject(obj)

    obj.GeneralArea = 3 * old["Area"]
    obj.Length = old["Length"]
    obj.Version = "0.20"
    _wrn("New proxy class used; properties migrated\n")

# old_module.py
class OldObject:
    def __init__(self, obj):
        obj.addProperty("App::PropertyLength", "Length")
        obj.addProperty("App::PropertyArea", "Area")
        obj.Length = 15
        obj.Area = 300
        obj.Proxy = self

        self.Type = "Custom"
        self.ver = "0.18"

    def execute(self, obj):
        pass

obj = App.ActiveDocument.Custom

print(obj.Proxy.ver)

# old_module.py
import FreeCAD as App
import objects.new_module as new_module
_wrn = App.Console.PrintWarning

class OldObject:
    def onDocumentRestored(self, obj):
        if hasattr(obj.Proxy, "ver") and obj.Proxy.ver:
            if obj.Proxy.ver == "0.18":
                _migrate_from_018(obj)

def _migrate_from_018(obj):
    old = dict()
    old["Area"] = obj.Area
    old["Length"] = obj.Length
    obj.removeProperty("Area")
    obj.removeProperty("Length")

    new_module.NewObject(obj)

    obj.GeneralArea = 3 * old["Area"]
    obj.Length = old["Length"]
    _wrn("New proxy class used; properties migrated\n")

# old_module.py
import FreeCAD as App
import objects.new_module as new_module
_wrn = App.Console.PrintWarning

class OldObject:
    def onDocumentRestored(self, obj):
        if hasattr(obj, "Version") and obj.Version:
            if obj.Version == "0.18":
                _migrate_from_018(obj)

def _migrate_from_018(obj):
    old = dict()
    old["Area"] = obj.Area
    obj.removeProperty("Area")

    new_module.NewObject(obj)

    obj.GeneralArea = 3 * old["Area"]
    obj.Version = "0.20"
    _wrn("New proxy class used; properties migrated\n")



