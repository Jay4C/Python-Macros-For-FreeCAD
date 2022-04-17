import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_gas_entry"


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

diametre_maximal_of_nozzle_front = 85

# part_gas_entry
part_gas_entry = Part.makeCylinder(diametre_maximal_of_nozzle_front/2, 3)

# part_gas_entry cut by cylinder_1
cylinder_1 = Part.makeCylinder(11/2, 3)
part_gas_entry = part_gas_entry.cut(cylinder_1)

# holes for fixing the nozzle
degree = 60
for i in range(int(360/degree)):
    radius = diametre_maximal_of_nozzle_front/2 - 2.5 - 3.5
    alpha=(i*degree*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(2.5, 3)
    hole.translate(hole_vector)
    part_gas_entry = part_gas_entry.cut(hole)

Part.show(part_gas_entry)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_gas_entry").getObject("Shape"))

stl_file = u"part_gas_entry.stl"

Mesh.export(__objs__, stl_file)

setview()
