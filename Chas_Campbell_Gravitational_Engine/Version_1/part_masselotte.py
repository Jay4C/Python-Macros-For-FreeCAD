import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_masselotte"


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
EPS_C = EPS * -0.5

length = 200
width = 70
thickness = 20

box_1 = Part.makeBox(length, width, thickness)

Part.show(box_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_masselotte").getObject("Shape"))

stl_file = u"part_masselotte.stl"

Mesh.export(__objs__, stl_file)

setview()
        