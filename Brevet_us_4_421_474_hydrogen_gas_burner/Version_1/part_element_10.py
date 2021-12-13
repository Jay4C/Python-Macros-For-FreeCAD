import FreeCAD, Part, Mesh, math

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_element_10"


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

cylinder_1 = Part.makeCylinder(rayon_maximal, 70)

cylinder_2 = Part.makeCylinder(11 + 5, 70)

cylinder_1 = cylinder_1.cut(cylinder_2)

cylinder_3 = Part.makeCylinder(rayon_maximal, 70)

cylinder_4 = Part.makeCylinder(11 + 5 + 1.5, 70)

cylinder_3 = cylinder_3.cut(cylinder_4)

cylinder_3_vector = FreeCAD.Vector(0, 0, 4)
cylinder_3.translate(cylinder_3_vector)
cylinder_1 = cylinder_1.cut(cylinder_3)

# holes for fixing the gas burner
degre = 60
for i in range(int(360/degre)):
    radius = 11 + 5 + 1.5 + 2.5 + 3.5 + 2.5
    alpha=(i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(2.5, 5)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

cylinder_5 = Part.makeCylinder(11 + 5 + 1.5 + 3.5, 2)

cylinder_6 = Part.makeCylinder(11 + 5 + 1.5 + 2, 2)

cylinder_5 = cylinder_5.cut(cylinder_6)

cylinder_1 = cylinder_1.cut(cylinder_5)

# Cut the holes for fixing the air
degre = 30
for i in range(int(360/degre)):
    axe_y = FreeCAD.Vector(0, 1, 0)
    axe_z = FreeCAD.Vector(0, 0, 1)
    radius_hole = 11 + 3.5
    alpha=(i*degre*math.pi)/180
    cylinder_vector = FreeCAD.Vector(radius_hole*math.cos(alpha), radius_hole*math.sin(alpha), 4 + 7.5)
    cylinder = Part.makeCylinder(2.5, 10, cylinder_vector, axe_y)
    cylinder.rotate(cylinder_vector, axe_z, alpha*(360/(2*math.pi)) - 90)
    cylinder_1 = cylinder_1.cut(cylinder)

# Cut the holes for fixing the air
degre = 30
for i in range(int(360/degre)):
    axe_y = FreeCAD.Vector(0, 1, 0)
    axe_z = FreeCAD.Vector(0, 0, 1)
    radius_hole = 11 + 3.5
    alpha=(i*degre*math.pi)/180
    cylinder_vector = FreeCAD.Vector(radius_hole*math.cos(alpha), radius_hole*math.sin(alpha), 70 - 7.5)
    cylinder = Part.makeCylinder(2.5, 10, cylinder_vector, axe_y)
    cylinder.rotate(cylinder_vector, axe_z, alpha*(360/(2*math.pi)) - 90)
    cylinder_1 = cylinder_1.cut(cylinder)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_element_10").getObject("Shape"))

stl_file = u"part_element_10.stl"

Mesh.export(__objs__, stl_file)

setview()
        