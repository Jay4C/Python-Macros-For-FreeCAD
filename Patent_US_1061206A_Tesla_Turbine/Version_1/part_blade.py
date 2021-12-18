import FreeCAD, Part, Drawing, math, Mesh, importDXF

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_blade"


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

diametre_maximal = 406.4 - 8*2 - 5*2

# part_blade
part_blade = Part.makeCylinder(diametre_maximal/2, 3)

# part_blade cut by cylinder_1
cylinder_1 = Part.makeCylinder(30/2, 3)
part_blade = part_blade.cut(cylinder_1)

# holes for evacuating the fluid from all the blades
degre = 45
for i in range(int(360/degre)):
    radius = 52/2 + 10
    alpha=(i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(10, 3)
    hole.translate(hole_vector)
    part_blade = part_blade.cut(hole)

Part.show(part_blade)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_blade").getObject("Shape"))

stl_file = u"part_blade.stl"

Mesh.export(__objs__, stl_file)

dxf_file = u"part_blade.dxf"

importDXF.export(__objs__, dxf_file)

setview()
    