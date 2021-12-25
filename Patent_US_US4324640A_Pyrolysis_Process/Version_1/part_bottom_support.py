import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_bottom_support"


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

# part_bottom_support
part_bottom_support = Part.makeCylinder((diametre_maximal_of_the_chamber + 10*2 + 10*2 + 10*2)/2, 5)

# holes for fixing the bottom support
degre = 90
for i in range(int(360/degre)):
    radius = (diametre_maximal_of_the_chamber)/2 + 10 + 5
    alpha=(i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(5, 5)
    hole.translate(hole_vector)
    part_bottom_support = part_bottom_support.cut(hole)

Part.show(part_bottom_support)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_bottom_support").getObject("Shape"))

stl_file = u"part_bottom_support.stl"

Mesh.export(__objs__, stl_file)

setview()
