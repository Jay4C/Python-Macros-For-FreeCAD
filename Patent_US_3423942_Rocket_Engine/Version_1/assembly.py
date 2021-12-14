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

# insertion part_gas_entry
Mesh.insert(u"part_gas_entry.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_gas_entry").Placement = App.Placement(App.Vector(0, 0, 0), App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly").getObject("part_gas_entry").ShapeColor = (0.50,0.40,0.30)

# insertion part_nozzle
Mesh.insert(u"part_nozzle.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_nozzle").Placement = App.Placement(App.Vector(0, 0, 3), App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly").getObject("part_nozzle").ShapeColor = (0.10,0.20,0.30)
FreeCADGui.getDocument("assembly").getObject("part_nozzle").Transparency = 70

# insertion part_element_64
Mesh.insert(u"part_element_64.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_element_64").Placement = App.Placement(App.Vector(0, 0, 3), App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly").getObject("part_element_64").ShapeColor = (0.90,0.80,0.70)

# insertion part_element_32
Mesh.insert(u"part_element_32.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_element_32").Placement = App.Placement(App.Vector(0, 0, -11), App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly").getObject("part_element_32").ShapeColor = (0.70,0.80,0.90)

setview()

__objs__ = []
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_gas_entry"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_nozzle"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_element_64"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_element_32"))

stl_file = u"assembly.stl"

Mesh.export(__objs__, stl_file)

del __objs__
            