import FreeCAD, Part, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_core_ferrite"

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

# EPS = tolerance to use to cut the parts
EPS = 0.10
EPS_C = EPS * -0.5

# part_core_ferrite
part_core_ferrite = Part.makeBox(93, 76, 16)

# box_1
box_1 = Part.makeBox(37, 48, 16)
box_1_vector = FreeCAD.Vector(28, 0, 0)
box_1.translate(box_1_vector)

# part_core_ferrite cut by box_1
part_core_ferrite = part_core_ferrite.cut(box_1)

Part.show(part_core_ferrite)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_core_ferrite").getObject("Shape"))

stl_file = u"part_core_ferrite.stl"

Mesh.export(__objs__, stl_file)

setview()
