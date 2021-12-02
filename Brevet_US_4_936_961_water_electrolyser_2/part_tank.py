import FreeCAD, Part, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_tank"


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

# tank
tank = Part.makeBox(200, 200, 250)

# box_1 for chamber
box_1 = Part.makeBox(162, 162, 250)
box_1_vector = FreeCAD.Vector(19, 19, 0)
box_1.translate(box_1_vector)

# cut tank by box_1
tank = tank.cut(box_1)

# box_2
box_2 = Part.makeBox(200, 200, 244)

# box_3
box_3 = Part.makeBox(178, 178, 244)
box_3_vector = FreeCAD.Vector(11, 11, 0)
box_3.translate(box_3_vector)

# cut box_2 by box_3
box_2 = box_2.cut(box_3)

# tank cut by box_2
box_2_vector = FreeCAD.Vector(0, 0, 3)
box_2.translate(box_2_vector)
tank = tank.cut(box_2)

# cylinder
cylinder = Part.makeCylinder(2.5, 250)

# tank cut by cylinder for hole 1
cylinder_vector = FreeCAD.Vector(5.5, 5.5, 0)
cylinder.translate(cylinder_vector)
tank = tank.cut(cylinder)

# tank cut by cylinder for intermediate holes
for i in range(19):
    cylinder_vector = FreeCAD.Vector(9.45, 0, 0)
    cylinder.translate(cylinder_vector)
    tank = tank.cut(cylinder)

# tank cut by cylinder for hole 2
cylinder_vector = FreeCAD.Vector(9.45, 0, 0)
cylinder.translate(cylinder_vector)
tank = tank.cut(cylinder)

# tank cut by cylinder for intermediate holes
for i in range(19):
    cylinder_vector = FreeCAD.Vector(0, 9.45, 0)
    cylinder.translate(cylinder_vector)
    tank = tank.cut(cylinder)

# tank cut by cylinder for hole 3
cylinder_vector = FreeCAD.Vector(0, 9.45, 0)
cylinder.translate(cylinder_vector)
tank = tank.cut(cylinder)

# tank cut by cylinder for intermediate holes
for i in range(19):
    cylinder_vector = FreeCAD.Vector(-9.45, 0, 0)
    cylinder.translate(cylinder_vector)
    tank = tank.cut(cylinder)

# tank cut by cylinder for hole 4
cylinder_vector = FreeCAD.Vector(-9.45, 0, 0)
cylinder.translate(cylinder_vector)
tank = tank.cut(cylinder)

# tank cut by cylinder for intermediate holes
for i in range(19):
    cylinder_vector = FreeCAD.Vector(0, -9.45, 0)
    cylinder.translate(cylinder_vector)
    tank = tank.cut(cylinder)

# box_4
box_4 = Part.makeBox(172, 172, 2)

# box_5
box_5 = Part.makeBox(168, 168, 2)
box_5_vector = FreeCAD.Vector(2, 2, 0)
box_5.translate(box_5_vector)

# box_4 cut by box_5
box_4 = box_4.cut(box_5)

# tank cut by box_4 for top support
box_4_vector = FreeCAD.Vector(14, 14, 0)
box_4.translate(box_4_vector)
tank = tank.cut(box_4)

# tank cut by box_4 for bottom support
box_4_vector = FreeCAD.Vector(0, 0, 248)
box_4.translate(box_4_vector)
tank = tank.cut(box_4)

Part.show(tank)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_tank").getObject("Shape"))

stl_file = u"part_tank.stl"

Mesh.export(__objs__, stl_file)

setview()
