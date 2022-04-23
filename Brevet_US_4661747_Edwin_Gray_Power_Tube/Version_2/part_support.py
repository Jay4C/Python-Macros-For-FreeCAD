import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_support"


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

cote_maximal = 2 + 8 + 8 + 8 + 86 + 8 + 8 + 8 + 2

hauteur_maximal = 1.5 + 1.5 + 6

# part_support
part_support = Part.makeCylinder(cote_maximal/2, hauteur_maximal)

# cylinder_1 for passing electrodes
cylinder_1 = Part.makeCylinder(4, hauteur_maximal)

# part_support cut by cylinder_1
part_support = part_support.cut(cylinder_1)

# cylinder_2 for fixing the tank
cylinder_2 = Part.makeCylinder(86/2, 1.5)

# part_support cut by cylinder_2
cylinder_2_vector = FreeCAD.Vector(0, 0, hauteur_maximal - 1.5)
cylinder_2.translate(cylinder_2_vector)
part_support = part_support.cut(cylinder_2)

# cylinder_3
cylinder_3 = Part.makeCylinder(cote_maximal/2 - 1, hauteur_maximal - 1.5 - 1.5)

# part_support cut by cylinder_3
part_support = part_support.cut(cylinder_3)

# holes for reducing the cost
degre = 15
for i in range(int(360/degre)):
    hole = Part.makeCylinder(4, hauteur_maximal)
    radius = 86/2 + 8 + 4
    alpha=(i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole.translate(hole_vector)
    part_support = part_support.cut(hole)

# Cut the holes for the screws fixing the assembly plant
degre = 15
for i in range(int(360/degre)):
    for j in range(0, 5):
        axe_y = FreeCAD.Vector(0, 1, 0)
        axe_z = FreeCAD.Vector(0, 0, 1)
        radius_screw = cote_maximal/2 - 5
        alpha = (i*degre*math.pi)/180
        vector = FreeCAD.Vector(radius_screw*math.cos(alpha), radius_screw*math.sin(alpha), j*0.75)        
        cylinder = Part.makeCylinder(3, 10, vector, axe_y)
        cylinder.rotate(vector, axe_z, alpha*(360/(2*math.pi)) - 90)
        part_support = part_support.cut(cylinder)

Part.show(part_support)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_support").getObject("Shape"))

stl_file = u"part_support.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_support_v2_'
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
