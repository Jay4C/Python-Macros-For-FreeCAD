import FreeCAD, Part, Drawing, math, Mesh, importDXF

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_stator"


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

# part_stator
part_stator = Part.makeCylinder(maximal_diameter/2, 1)

cylinder_1 = Part.makeCylinder(maximal_diameter/2 - 5 - 5 - 5, 1)

# part_stator cut by cylinder_1
part_stator = part_stator.cut(cylinder_1)

# holes for fixing the stator
degre = 180
for i in range(int(360/degre)):
    radius = maximal_diameter/2 - 5 - 2.5
    alpha=(i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(2.5, 1)
    hole.translate(hole_vector)
    part_stator = part_stator.cut(hole)

Part.show(part_stator)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_stator").getObject("Shape"))

stl_file = u"part_stator.stl"

Mesh.export(__objs__, stl_file)

dxf_file = u"part_stator.dxf"

importDXF.export(__objs__, dxf_file)

setview()
