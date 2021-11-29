import FreeCAD, Part, Mesh, math

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_capacitor_plate"


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
diametre_maximal_tank = 250

# Diametre maximal du capacitor plate
diametre_maximal_capacitor_plate = diametre_maximal_tank - 3*2 - 5*2 - 3*2 - 2*2 - 3*2 - 2*2 - 2*2

cylinder_1 = Part.makeCylinder(diametre_maximal_capacitor_plate/2, 1)

cylinder_2 = Part.makeCylinder(5, 1)

cylinder_1 = cylinder_1.cut(cylinder_2)

# holes for fixing the anodes
degre = 120
for i in range(int(360/degre)):
    radius = diametre_maximal_capacitor_plate/2 - 4 - 5
    alpha=(i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(5, 1)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

# holes for fixing the cathodes
degres = [60, 180, 300]
for degre in degres:
    radius = diametre_maximal_capacitor_plate/2
    alpha=(degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(15.5, 1)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

# holes for letting the gas mixture to go out
degre = 10
for i in range(int(360/degre)):
    radius = diametre_maximal_capacitor_plate/2 - 4 - 5
    alpha=(i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(2.5, 1)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

# holes for letting the gas mixture to go out
degre = 90
for i in range(int(360/degre)):
    radius = 20
    alpha=(i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(5, 1)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

# holes for letting the gas mixture to go out
degre = 30
for i in range(int(360/degre)):
    for i_1 in range(2, 5):
        radius = 20 * i_1
        alpha=(i*degre*math.pi)/180
        hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
        hole = Part.makeCylinder(5, 1)
        hole.translate(hole_vector)
        cylinder_1 = cylinder_1.cut(hole)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_capacitor_plate").getObject("Shape"))

stl_file = u"part_capacitor_plate.stl"

Mesh.export(__objs__, stl_file)

setview()
        