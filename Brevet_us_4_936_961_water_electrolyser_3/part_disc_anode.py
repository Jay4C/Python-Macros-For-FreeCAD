import FreeCAD, Part, Mesh, math

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_disc_anode"


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

cylinder_2 = Part.makeCylinder(2, 3)

cylinder_1 = cylinder_1.cut(cylinder_2)

# holes for fixing the disc anode
degree = 120
for i in range(int(360/degree)):
    radius = 29.3
    alpha=(i*degree*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(2.5, 3)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

# cutting for passing the screw for fixing the disc cathode
degrees = [60, 180, 300]
for degree in degrees:
    radius = 34
    alpha=(degree*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(9, 3)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

# holes for fixing the anodes on the disc anode
degree = 90
for i in range(int(360/degree)):
    radius = 10.5
    alpha=(i*degree*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(2, 3)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

degree = 30
for i in range(int(360/degree)):
    radius = 21
    alpha=(i*degree*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(2, 3)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

depart = 30
for i in range(0, 6):
    degree = depart + i * 60
    radius = 31.5
    alpha=(degree*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(2, 3)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

# holes for emptying the disc anode
degrees = [105, 225, 345]
for degree in degrees:
    radius = 29.3
    alpha=(degree*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(2.5, 3)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)
    
# holes for emptying the disc anode
degrees = [135, 255, 375]
for degree in degrees:
    radius = 29.3
    alpha=(degree*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(2.5, 3)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)
    
# holes for emptying the disc anode
degrees = [45, 135, 225, 315]
for degree in degrees:
    radius = 13
    alpha=(degree*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(2.5, 3)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

# holes for emptying the disc anode
degrees = [75, 195, 315]
for degree in degrees:
    radius = 29.3
    alpha=(degree*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(2.5, 3)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)
    
# holes for emptying the disc anode
degrees = [45, 165, 285]
for degree in degrees:
    radius = 29.3
    alpha=(degree*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(2.5, 3)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_disc_anode").getObject("Shape"))

stl_file = u"part_disc_anode.stl"

Mesh.export(__objs__, stl_file)

setview()
        