import FreeCAD, Part, Mesh, math

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly"


def clear_doc():
    # Clear the active document deleting all the objects
    for obj in DOC.Objects:
        DOC.removeObject(obj.Name)


def setview():
    # Rearrange View
    FreeCAD.Gui.SendMsgToActiveView("ViewFit")
    FreeCAD.Gui.activeDocument().activeView().viewAxometric()


if DOC is None:
    FreeCAD.newDocument(DOC_NAME)
    FreeCAD.setActiveDocument(DOC_NAME)
    DOC = FreeCAD.activeDocument()
else:
    clear_doc()

# EPS= tolerance to use to cut the parts
EPS = 0.10
EPS_C = EPS * (-0.5)

# insertion part_top_support
Mesh.insert(u"part_top_support.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_top_support").Placement = App.Placement(App.Vector(0, 0, 1000), App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly").getObject("part_top_support").ShapeColor = (0.10,0.10,0.10)

# insertion part_chamber
Mesh.insert(u"part_chamber.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_chamber").Placement = App.Placement(App.Vector(0, 0, 0), App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly").getObject("part_chamber").ShapeColor = (0.30,0.20,0.10)
FreeCADGui.getDocument("assembly").getObject("part_chamber").Transparency = 70

# insertion part_bottom_support
Mesh.insert(u"part_bottom_support.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_bottom_support").Placement = App.Placement(App.Vector(0, 0, -5), App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly").getObject("part_bottom_support").ShapeColor = (0.90,0.80,0.70)

setview()

__objs__ = []
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_chamber"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_bottom_support"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_top_support"))

stl_file = u"assembly.stl"

Mesh.export(__objs__, stl_file)

del __objs__
            