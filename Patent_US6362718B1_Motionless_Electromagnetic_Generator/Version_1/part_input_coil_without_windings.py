import FreeCAD, Part, Mesh, math

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_input_coil_without_windings"


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

L_vis_10m = 100
h_tube = 25
h_ecrou_10m = 10
s_rondelle_10m = 2
D = 60

h_coil = (L_vis_10m - h_tube*2 - s_rondelle_10m*2 - h_ecrou_10m - 5)/2

cylinder_1 = Part.makeCylinder(D/2, h_coil)

cylinder_3 = Part.makeCylinder(D/2, h_coil - 2*3)

radius_box = math.sqrt(math.pow(h_tube/2,2) + math.pow(h_tube/2,2)) + 1
cylinder_4 = Part.makeCylinder(radius_box, h_coil - 2*3)

# cylinder_3 cut by cylinder_4
cylinder_3 = cylinder_3.cut(cylinder_4)

# cylinder_1 cut by cylinder_3
cylinder_3_vector = FreeCAD.Vector(0, 0, 3)
cylinder_3.translate(cylinder_3_vector)
cylinder_1 = cylinder_1.cut(cylinder_3)

# cylinder_1 cut by box_1
box_1 = Part.makeBox(h_tube, h_tube, h_coil)
box_1_vector = FreeCAD.Vector(-h_tube/2, -h_tube/2, 0)
box_1.translate(box_1_vector)
cylinder_1 = cylinder_1.cut(box_1)

# cylinder_1 cut by cylinder_5 in several times
degre = 30
for i in range(int(360/degre)):
    radius = h_tube/2 + h_tube/7
    alpha=(i*degre*math.pi)/180
    cylinder_5_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    cylinder_5 = Part.makeCylinder(5/2, h_coil)
    cylinder_5.translate(cylinder_5_vector)
    cylinder_1 = cylinder_1.cut(cylinder_5)

# cylinder_1 cut by cylinder_5 in several times
degre = 30
for i in range(int(360/degre)):
    radius = h_tube/2 + h_tube/7 + h_tube/3
    alpha=(i*degre*math.pi)/180
    cylinder_5_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    cylinder_5 = Part.makeCylinder(5/2, h_coil)
    cylinder_5.translate(cylinder_5_vector)
    cylinder_1 = cylinder_1.cut(cylinder_5)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_input_coil_without_windings").getObject("Shape"))

stl_file = u"part_input_coil_without_windings.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_input_coil_without_windings_'
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
