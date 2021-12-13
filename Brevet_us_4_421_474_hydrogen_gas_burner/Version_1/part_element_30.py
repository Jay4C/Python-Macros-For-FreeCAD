import FreeCAD, Part, Mesh, math

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_element_30"


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

rayon_maximal = 11 + 5 + 1.5 + 2.5 + 3.5 + 5 + 3.5 + 2.5

cylinder_1 = Part.makeCylinder(rayon_maximal, 7)

cylinder_2 = Part.makeCylinder(16/2, 7)

cylinder_1 = cylinder_1.cut(cylinder_2)

cylinder_3 = Part.makeCylinder(11 + 5 + 1.5 + 2, 3)

cylinder_3_vector = FreeCAD.Vector(0, 0, 4)
cylinder_3.translate(cylinder_3_vector)
cylinder_1 = cylinder_1.cut(cylinder_3)

cylinder_4 = Part.makeCylinder(rayon_maximal, 3)

cylinder_5 = Part.makeCylinder(11 + 5 + 1.5 + 3.5, 3)

cylinder_4 = cylinder_4.cut(cylinder_5)

cylinder_4_vector = FreeCAD.Vector(0, 0, 4)
cylinder_4.translate(cylinder_4_vector)
cylinder_1 = cylinder_1.cut(cylinder_4)

# holes for fixing the gas burner
degre = 60
for i in range(int(360/degre)):
    radius = 11 + 5 + 1.5 + 2.5 + 3.5 + 2.5
    alpha=(i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(2.5, 5)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_element_30").getObject("Shape"))

stl_file = u"part_element_30.stl"

Mesh.export(__objs__, stl_file)

setview()
    