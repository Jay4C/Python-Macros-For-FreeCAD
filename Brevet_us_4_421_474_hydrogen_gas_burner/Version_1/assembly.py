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

# insertion part_element_30
Mesh.insert(u"part_element_30.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_element_30").Placement = App.Placement(App.Vector(0, 0, 0), App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly").getObject("part_element_30").ShapeColor = (1.00,1.00,0.00)

# insertion part_element_10
Mesh.insert(u"part_element_10.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_element_10").Placement = App.Placement(App.Vector(0, 0, 5), App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly").getObject("part_element_10").ShapeColor = (0.10,0.10,0.00)
FreeCADGui.getDocument("assembly").getObject("part_element_10").Transparency = 70

# insertion part_element_64
Mesh.insert(u"part_element_64.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_element_64").Placement = App.Placement(App.Vector(0, 0, 4), App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly").getObject("part_element_64").ShapeColor = (0.10,0.20,0.30)

# insertion part_element_32
Mesh.insert(u"part_element_32.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_element_32").Placement = App.Placement(App.Vector(0, 0, -11), App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly").getObject("part_element_32").ShapeColor = (0.20,0.40,0.60)

setview()

__objs__ = []
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_element_10"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_element_30"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_element_64"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_element_32"))

stl_file = u"assembly.stl"

Mesh.export(__objs__, stl_file)

del __objs__
            