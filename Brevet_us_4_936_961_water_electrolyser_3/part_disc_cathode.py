import FreeCAD, Part, Mesh, math

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_disc_cathode"


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

cylinder_1 = Part.makeCylinder(34, 3)

cylinder_2 = Part.makeCylinder(4, 3)

cylinder_1 = cylinder_1.cut(cylinder_2)

# holes for fixing the disc cathode
degre = 120
for i in range(int(360/degre)):
    radius = 29.3
    alpha=(i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(2.5, 3)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

# cutting for passing the screw for fixing the disc anode
degres = [60, 180, 300]
for degre in degres:
    radius = 34
    alpha=(degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(9, 3)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

# holes for fixing the cathodes on the disc cathode
degre = 90
for i in range(int(360/degre)):
    radius = 10.5
    alpha=(i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(4, 3)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

degre = 30
for i in range(int(360/degre)):
    radius = 21
    alpha=(i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(4, 3)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)
    
depart = 30
for i in range(0, 6):
    degre = depart + i * 60
    radius = 31.5
    alpha=(degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(4, 3)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

# holes for emptying the disc cathode
degres = [105, 225, 345]
for degre in degres:
    radius = 29.3
    alpha=(degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(2.5, 3)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)
    
# holes for emptying the disc cathode
degres = [135, 255, 375]
for degre in degres:
    radius = 29.3
    alpha=(degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(2.5, 3)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)
    
# holes for emptying the disc cathode
degres = [45, 135, 225, 315]
for degre in degres:
    radius = 13
    alpha=(degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(2.5, 3)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_disc_cathode").getObject("Shape"))

stl_file = u"part_disc_cathode.stl"

Mesh.export(__objs__, stl_file)

setview()
        