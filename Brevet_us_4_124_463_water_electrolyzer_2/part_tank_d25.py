import FreeCAD, Part, Mesh, math

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_tank_d25"


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

# Diametre maximal du tank
diametre_maximal = 250

cylinder_1 = Part.makeCylinder(diametre_maximal/2, diametre_maximal)

cylinder_2 = Part.makeCylinder(diametre_maximal/2 - 3 - 5 - 3 - 2 - 3 - 2, diametre_maximal)

# cylinder_1 cut by cylinder_2
cylinder_1 = cylinder_1.cut(cylinder_2)

cylinder_3 = Part.makeCylinder(diametre_maximal/2, diametre_maximal - 3*2)

cylinder_4 = Part.makeCylinder(diametre_maximal/2 - 3 - 5 - 3, diametre_maximal - 3*2)

# cylinder_3 cut by cylinder_4
cylinder_3 = cylinder_3.cut(cylinder_4)

# cylinder_1 cut by cylinder_3
cylinder_3_vector = FreeCAD.Vector(0, 0, 3)
cylinder_3.translate(cylinder_3_vector)
cylinder_1 = cylinder_1.cut(cylinder_3)

# holes for fixing the bottom support and the top support
degree = 10
for i in range(int(360/degree)):
    radius = diametre_maximal/2 - 3 - 2.5
    alpha=(i*degree*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(2.5, diametre_maximal)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

cylinder_5 = Part.makeCylinder(diametre_maximal/2 - 3 - 5 - 3 - 2, 3)

cylinder_6 = Part.makeCylinder(diametre_maximal/2 - 3 - 5 - 3 - 2 - 3, 3)

# cylinder_5 cut by cylinder_6
cylinder_5 = cylinder_5.cut(cylinder_6)

# cylinder_1 cut by cylinder_5
cylinder_1 = cylinder_1.cut(cylinder_5)

cylinder_5_vector = FreeCAD.Vector(0, 0, diametre_maximal - 3)
cylinder_5.translate(cylinder_5_vector)
cylinder_1 = cylinder_1.cut(cylinder_5)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_tank_d25").getObject("Shape"))

stl_file = u"part_tank_d25.stl"

Mesh.export(__objs__, stl_file)

setview()
        