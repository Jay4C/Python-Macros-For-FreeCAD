import FreeCAD, Part, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_top_support_gas"


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

# top_support_gas
top_support_gas = Part.makeCylinder(radius_tank + 16, 6)

# cylinder_1
cylinder_1 = Part.makeCylinder(radius_tank + 2, 3)

# top_support_gas cut by cylinder_1
top_support_gas = top_support_gas.cut(cylinder_1)

# Cut the holes in top_support_gas for fixing screws on the tank
for i in range(12):
    radius_screw = radius_tank + 10.5
    cylinder = Part.makeCylinder(2.5, 10)
    alpha = (i*2*math.pi)/12
    cylinder_vector = FreeCAD.Vector(radius_screw*math.cos(alpha), radius_screw*math.sin(alpha), 0)
    cylinder.translate(cylinder_vector)
    top_support_gas = top_support_gas.cut(cylinder)

# cylinder_2
cylinder_2 = Part.makeCylinder(radius_tank + 16, 3)

# cylinder_3
cylinder_3 = Part.makeCylinder(radius_tank + 5, 3)

# cylinder_2 cut by cylinder_3
cylinder_2 = cylinder_2.cut(cylinder_3)

# top_support_gas cut by cylinder_2
top_support_gas = top_support_gas.cut(cylinder_2)

# cylinder_4
cylinder_4 = Part.makeCylinder(8, 10)

# top_support_gas cut by cylinder_4 for the out of the gas
top_support_gas = top_support_gas.cut(cylinder_4)

Part.show(top_support_gas)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_top_support_gas").getObject("Shape"))

stl_file = u"part_top_support_gas.stl"

Mesh.export(__objs__, stl_file)

setview()

del __objs__

# Generate PNG files
file = 'part_top_support_gas_'
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
