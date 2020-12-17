# https://wiki.freecadweb.org/Scripting_examples
# https://wiki.freecadweb.org/Property

obj.addProperty("App::PropertyFloat", "Length")
obj.addProperty("App::PropertyFloat", "Width")
obj.addProperty("App::PropertyFloat", "Height")

obj = App.ActiveDocument.addObject("Part::Feature", "CustomObject")

obj.addProperty("App::PropertyFloat", "Velocity", "Parameter", "Body speed")
obj.addProperty("App::PropertyBool", "VelocityEnabled", "Parameter", "Enable body speed")

obj.ViewObject.addProperty("App::PropertyBool", "SuperVisibility", "Base", "Make the object glow")


