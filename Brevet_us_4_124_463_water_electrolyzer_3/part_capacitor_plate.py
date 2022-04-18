import FreeCAD, Part, math, Mesh, ImportGui, importDXF

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_capacitor_plate"


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

epaisseur = 1

# Diametre maximal du tank
diametre_maximal_tank = 200

# Diametre maximal du capacitor plate
diametre_maximal_capacitor_plate = diametre_maximal_tank - 3*2 - 5*2

cylinder_1 = Part.makeCylinder(diametre_maximal_capacitor_plate/2, epaisseur)

cylinder_2 = Part.makeCylinder(25, epaisseur)

cylinder_1 = cylinder_1.cut(cylinder_2)

# holes for fixing the anodes and the cathodes
degree = 90
radius = diametre_maximal_capacitor_plate/2 - 5 - 5
alpha=(degree*math.pi)/180
hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
hole = Part.makeCylinder(5, epaisseur)
hole.translate(hole_vector)
cylinder_1 = cylinder_1.cut(hole)

# holes for fixing the cathodes
degree = 270
radius = diametre_maximal_capacitor_plate/2
alpha=(degree*math.pi)/180
hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
hole = Part.makeCylinder(16.50, epaisseur)
hole.translate(hole_vector)
cylinder_1 = cylinder_1.cut(hole)

# holes for letting the gas mixture to go out
degree = 30
for i in range(int(360/degree)):
    radius = diametre_maximal_capacitor_plate/2 - 5 - 5
    alpha=(i*degree*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(5, epaisseur)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

# holes for letting the gas mixture to go out
degree = 90
for i in range(int(360/degree)):
    radius = 20
    alpha=(i*degree*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(5, epaisseur)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

# holes for letting the gas mixture to go out
degree = 30
for i in range(int(360/degree)):
    for i_1 in range(2, 4):
        radius = 20 * i_1
        alpha=(i*degree*math.pi)/180
        hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
        hole = Part.makeCylinder(5, epaisseur)
        hole.translate(hole_vector)
        cylinder_1 = cylinder_1.cut(hole)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_capacitor_plate").getObject("Shape"))

step_file = u"part_capacitor_plate.step"

ImportGui.export(__objs__, step_file)

stl_file = u"part_capacitor_plate.stl"

Mesh.export(__objs__, stl_file)

dxf_file = u"part_capacitor_plate.dxf"

importDXF.export(__objs__, dxf_file)

del __objs__

setview()

# Generate PNG files
file = 'part_capacitor_plate_'
# Ombr�
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
        