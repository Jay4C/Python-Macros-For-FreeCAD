import FreeCAD, Part, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_bottom_support"


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

# bottom_support
bottom_support = Part.makeBox(200, 200, 6)

# cylinder
cylinder = Part.makeCylinder(2.5, 6)

# bottom_support cut by cylinder for hole 1
cylinder_vector = FreeCAD.Vector(5.5, 5.5, 0)
cylinder.translate(cylinder_vector)
bottom_support = bottom_support.cut(cylinder)

# bottom_support cut by cylinder for intermediate holes
for i in range(19):
    cylinder_vector = FreeCAD.Vector(9.45, 0, 0)
    cylinder.translate(cylinder_vector)
    bottom_support = bottom_support.cut(cylinder)

# bottom_support cut by cylinder for hole 2
cylinder_vector = FreeCAD.Vector(9.45, 0, 0)
cylinder.translate(cylinder_vector)
bottom_support = bottom_support.cut(cylinder)

# bottom_support cut by cylinder for intermediate holes
for i in range(19):
    cylinder_vector = FreeCAD.Vector(0, 9.45, 0)
    cylinder.translate(cylinder_vector)
    bottom_support = bottom_support.cut(cylinder)

# bottom_support cut by cylinder for hole 3
cylinder_vector = FreeCAD.Vector(0, 9.45, 0)
cylinder.translate(cylinder_vector)
bottom_support = bottom_support.cut(cylinder)

# bottom_support cut by cylinder for intermediate holes
for i in range(19):
    cylinder_vector = FreeCAD.Vector(-9.45, 0, 0)
    cylinder.translate(cylinder_vector)
    bottom_support = bottom_support.cut(cylinder)

# bottom_support cut by cylinder for hole 4
cylinder_vector = FreeCAD.Vector(-9.45, 0, 0)
cylinder.translate(cylinder_vector)
bottom_support = bottom_support.cut(cylinder)

# bottom_support cut by cylinder for intermediate holes
for i in range(19):
    cylinder_vector = FreeCAD.Vector(0, -9.45, 0)
    cylinder.translate(cylinder_vector)
    bottom_support = bottom_support.cut(cylinder)

# box_1
box_1 = Part.makeBox(168, 168, 3)
box_1_vector = FreeCAD.Vector(16, 16, 0)
box_1.translate(box_1_vector)

# bottom_support cut by box_1
bottom_support = bottom_support.cut(box_1)

# box_2
box_2 = Part.makeBox(200, 200, 3)

# box_3
box_3 = Part.makeBox(172, 172, 3)
box_3_vector = FreeCAD.Vector(14, 14, 0)
box_3.translate(box_3_vector)

# box_2 cut by box_3
box_2 = box_2.cut(box_3)

# bottom_support cut by box_2
bottom_support = bottom_support.cut(box_2)

# cylinder_1 for screw 5mm of diametre
cylinder_1 = Part.makeCylinder(2.5, 6)

# bottom_support cut by cylinder_1 for hole 1 for supporting disk cathode
cylinder_1_vector = FreeCAD.Vector(24.5, 24.5, 0)
cylinder_1.translate(cylinder_1_vector)
bottom_support = bottom_support.cut(cylinder_1)

# bottom_support cut by cylinder_1 for hole 2 for supporting disk cathode
cylinder_1_vector = FreeCAD.Vector(151, 0, 0)
cylinder_1.translate(cylinder_1_vector)
bottom_support = bottom_support.cut(cylinder_1)

# bottom_support cut by cylinder_1 for hole 3 for supporting disk cathode
cylinder_1_vector = FreeCAD.Vector(0, 151, 0)
cylinder_1.translate(cylinder_1_vector)
bottom_support = bottom_support.cut(cylinder_1)

# bottom_support cut by cylinder_1 for hole 4 for supporting disk cathode
cylinder_1_vector = FreeCAD.Vector(-151, 0, 0)
cylinder_1.translate(cylinder_1_vector)
bottom_support = bottom_support.cut(cylinder_1)

# bottom_support cut by cylinder_1 for hole 1 for supporting disk anode
cylinder_1_vector = FreeCAD.Vector(11, 0, 0)
cylinder_1.translate(cylinder_1_vector)
bottom_support = bottom_support.cut(cylinder_1)

# bottom_support cut by cylinder_1 for hole 2 for supporting disk anode
cylinder_1_vector = FreeCAD.Vector(129, 0, 0)
cylinder_1.translate(cylinder_1_vector)
bottom_support = bottom_support.cut(cylinder_1)

# bottom_support cut by cylinder_1 for hole 3 for supporting disk anode
cylinder_1_vector = FreeCAD.Vector(0, -151, 0)
cylinder_1.translate(cylinder_1_vector)
bottom_support = bottom_support.cut(cylinder_1)

# bottom_support cut by cylinder_1 for hole 4 for supporting disk anode
cylinder_1_vector = FreeCAD.Vector(-129, 0, 0)
cylinder_1.translate(cylinder_1_vector)
bottom_support = bottom_support.cut(cylinder_1)

Part.show(bottom_support)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_bottom_support").getObject("Shape"))

stl_file = u"part_bottom_support.stl"

Mesh.export(__objs__, stl_file)

setview()
