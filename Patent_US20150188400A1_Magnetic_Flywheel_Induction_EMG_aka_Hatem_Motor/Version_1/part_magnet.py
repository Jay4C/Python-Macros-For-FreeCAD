import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_magnet"


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

maximal_diameter = 15

maximal_heigth = 3

# part_magnet
part_magnet = Part.makeCylinder(maximal_diameter/2, maximal_heigth)

# part_magnet cut by cylinder_1
cylinder_1 = Part.makeCylinder(2.5, maximal_heigth)
part_magnet = part_magnet.cut(cylinder_1)

Part.show(part_magnet)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_magnet").getObject("Shape"))

stl_file = u"part_magnet.stl"

Mesh.export(__objs__, stl_file)

setview()
