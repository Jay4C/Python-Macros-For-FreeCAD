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

radius_tank = 20

maximal_height = 40 - radius_tank

radius_inner_tank = radius_tank - 3

# tank
tank = Part.makeSphere(radius_tank)

# sphere_1
sphere_1 = Part.makeSphere(radius_inner_tank)

# tank cut by sphere_1
tank = tank.cut(sphere_1)

# cylinder_1
cylinder_1 = Part.makeCylinder(radius_tank, radius_tank)

# tank cut by cylinder_1
tank = tank.cut(cylinder_1)

# cylinder_2
cylinder_2 = Part.makeCylinder(radius_tank, maximal_height)

# cylinder_3
cylinder_3 = Part.makeCylinder(radius_tank - 3, maximal_height)

# cylinder_2 cut by cylinder_3
cylinder_2 = cylinder_2.cut(cylinder_3)

# tank fuse with cylinder_2
tank = tank.fuse(cylinder_2)

# cylinder_4 for fixing the screw in the bottom of the tank
cylinder_4 = Part.makeCylinder(2.5, 15)
cylinder_4_vector = FreeCAD.Vector(0, 0, -radius_tank)
cylinder_4.translate(cylinder_4_vector)

# tank cut by cylinder_4
tank = tank.cut(cylinder_4)

# cylinder_5
cylinder_5 = Part.makeCylinder(radius_tank + 16, 5)

# cylinder_6
cylinder_6 = Part.makeCylinder(radius_tank - 3, 5)

# cylinder_5 cut by cylinder_6
cylinder_5 = cylinder_5.cut(cylinder_6)

# Cut the holes in cylinder_5 for fixing screws in the top of tank
for i in range(12):
    radius_screw = radius_tank + 10.5
    cylinder = Part.makeCylinder(2.5, 10)
    alpha = (i*2*math.pi)/12
    cylinder_vector = FreeCAD.Vector(radius_screw*math.cos(alpha), radius_screw*math.sin(alpha), 0)
    cylinder.translate(cylinder_vector)
    cylinder_5 = cylinder_5.cut(cylinder)

cylinder_5_vector = FreeCAD.Vector(0, 0, maximal_height)
cylinder_5.translate(cylinder_5_vector)

# tank fuse by cylinder_5
tank = tank.fuse(cylinder_5)

# cylinder_7
cylinder_7 = Part.makeCylinder(radius_tank + 5, 2.5)

# cylinder_8
cylinder_8 = Part.makeCylinder(radius_tank + 2, 2.5)

# cylinder_7 cut by cylinder_8
cylinder_7 = cylinder_7.cut(cylinder_8)

# tank cut by cylinder_7
cylinder_7_vector = FreeCAD.Vector(0, 0, maximal_height + 2.5)
cylinder_7.translate(cylinder_7_vector)
tank = tank.cut(cylinder_7)

Part.show(tank)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_tank").getObject("Shape"))

stl_file = u"part_tank.stl"

Mesh.export(__objs__, stl_file)

setview()

del __objs__

# Generate PNG files
file = 'part_tank_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')
