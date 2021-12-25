import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_chamber"


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

diametre_maximal_of_the_chamber = 500

height_maximal_of_the_chamber = 1000

# part_chamber
part_chamber = Part.makeCylinder(diametre_maximal_of_the_chamber/2, height_maximal_of_the_chamber)

cylinder_1 = Part.makeCylinder(diametre_maximal_of_the_chamber/2 - 3, height_maximal_of_the_chamber)

# part_chamber cut by cylinder_1
part_chamber = part_chamber.cut(cylinder_1)

Part.show(part_chamber)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_chamber").getObject("Shape"))

stl_file = u"part_chamber.stl"

Mesh.export(__objs__, stl_file)

setview()
