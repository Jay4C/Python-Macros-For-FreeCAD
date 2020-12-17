# https://wiki.freecadweb.org/Scripting_examples
# https://wiki.freecadweb.org/Scripted_objects_saving_attributes

# various_states.py
class VariousStates:
    def __init__(self, obj):
        obj.addProperty("App::PropertyLength", "Length")
        obj.addProperty("App::PropertyArea", "Area")
        obj.Length = 15
        obj.Area = 300
        obj.Proxy = self

        Type = dict()
        Type["Version"] = "Custom"
        Type["Release"] = "production"
        self.Type = Type
        self.Type = "Custom"
        self.ver = "0.18"
        self.color = (0, 0, 1)
        self.width = 2.5

    def execute(self, obj):
        pass

import FreeCAD as App
import various_states

doc = App.newDocument()
doc.FileName = "my_document.FCStd"

obj = doc.addObject("Part::FeaturePython", "Custom")
various_states.VariousStates(obj)

if App.GuiUp:
    obj.ViewObject.Proxy = 1

doc.recompute()
doc.save()

obj = App.ActiveDocument.Custom

print(obj.Proxy)

print(obj.Proxy.__dict__)

# various_states.py
class CustomStates:
    def __init__(self, obj):
        obj.addProperty("App::PropertyLength", "Length")
        obj.addProperty("App::PropertyArea", "Area")
        obj.Length = 15
        obj.Area = 300
        obj.Proxy = self

        Type = dict()
        Type["Version"] = "Custom"
        Type["Release"] = "production"
        self.Type = Type
        self.ver = "0.18"
        self.color = (0, 0, 1)
        self.width = 2.5

    def execute(self, obj):
        pass

    def __getstate__(self):
        return self.color, self.width

    def __setstate__(self, state):
        self.color = state[0]
        self.width = state[1]

state = (self.color, self.width)
state = ((0, 0, 1), 2.5)

obj2 = App.ActiveDocument.Custom2

print(obj2.Proxy)

print(obj2.Proxy.__dict__)

class DraftObject:
    def __init__(self, obj, _type):
        self.Type = _type

    def __getstate__(self):
        return self.Type

    def __setstate__(self, state):
        if state:
            self.Type = state

class CustomObject:
    def __init__(self, obj, _type):
        self.Type = _type
        self.version = "0.18"

    def __getstate__(self):
        return self.Type, self.version

    def __setstate__(self, state):
        if state:
            self.Type = state[0]
            self.version = state[1]

class CustomObject:
    def onDocumentRestored(self, obj):
        if hasattr(obj.Proxy, "version") and obj.Proxy.version:
            if obj.Proxy.version == "0.18":
                self.migrate_from_018(obj)

