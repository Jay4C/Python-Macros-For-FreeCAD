import FreeCAD, Part, Drawing, math, Mesh, importDXF

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_rotor"


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

maximal_diameter = 100

maximal_heigth = 15

# part_rotor
part_rotor = Part.makeCylinder(maximal_diameter/2, maximal_heigth)

# part_rotor cut by cylinder_1
cylinder_1 = Part.makeCylinder(5, maximal_heigth)
part_rotor = part_rotor.cut(cylinder_1)

# holes for fixing the magnets
degre = 30
for i in range(int(360/degre)):
    radius = maximal_diameter/2 - 12.5
    alpha=(i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(7.5, maximal_heigth)
    hole.translate(hole_vector)
    part_rotor = part_rotor.cut(hole)

# holes for the cooling
degre = 90
for i in range(int(360/degre)):
    radius = 5 + 12.5
    alpha=(i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(7.5, maximal_heigth)
    hole.translate(hole_vector)
    part_rotor = part_rotor.cut(hole)

# holes for the cooling
degres = [1*45, 3*45, 5*45, 7*45]
for degre in degres:
    radius = math.sqrt(2*math.pow(16.25,2))
    alpha=(degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(7.5, maximal_heigth)
    hole.translate(hole_vector)
    part_rotor = part_rotor.cut(hole)

# Cut the holes for the screws fixing the magnets
for i in range(12):
    axe_y = FreeCAD.Vector(0, 1, 0)
    axe_z = FreeCAD.Vector(0, 0, 1)
    radius_screw = maximal_diameter/2 - 10
    alpha = (i*2*math.pi)/12
    hole_vector = FreeCAD.Vector(radius_screw*math.cos(alpha), radius_screw*math.sin(alpha), 7.5)
    hole = Part.makeCylinder(2.5, maximal_diameter/2 - 10, hole_vector, axe_y)
    hole.rotate(hole_vector, axe_z, alpha*(360/(2*math.pi)) - 90)
    part_rotor = part_rotor.cut(hole)

Part.show(part_rotor)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_rotor").getObject("Shape"))

stl_file = u"part_rotor.stl"

Mesh.export(__objs__, stl_file)

dxf_file = u"part_rotor.dxf"

importDXF.export(__objs__, dxf_file)

setview()
