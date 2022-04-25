import FreeCAD, Part, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_top_electrodes"


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

# top_electrodes
top_electrodes = Part.makeCylinder(radius_tank + 16, 6)

# cylinder_1
cylinder_1 = Part.makeCylinder(radius_tank + 2, 3)

# top_electrodes cut by cylinder_1
top_electrodes = top_electrodes.cut(cylinder_1)

# Cut the holes in top_electrodes for fixing screws on the tank
for i in range(12):
    radius_screw = radius_tank + 10.5
    cylinder = Part.makeCylinder(2.5, 10)
    alpha = (i*2*math.pi)/12
    cylinder_vector = FreeCAD.Vector(radius_screw*math.cos(alpha), radius_screw*math.sin(alpha), 0)
    cylinder.translate(cylinder_vector)
    top_electrodes = top_electrodes.cut(cylinder)
    
# cylinder_2
cylinder_2 = Part.makeCylinder(radius_tank + 16, 3)

# cylinder_3
cylinder_3 = Part.makeCylinder(radius_tank + 5, 3)

# cylinder_2 cut by cylinder_3
cylinder_2 = cylinder_2.cut(cylinder_3)

# top_electrodes cut by cylinder_2
top_electrodes = top_electrodes.cut(cylinder_2)

# cylinder_4
cylinder_4 = Part.makeCylinder(2.5, 10)

# top_electrodes cut by cylinder_4 for electric arc (plasmas)
top_electrodes = top_electrodes.cut(cylinder_4)

# top_electrodes cut by cylinder_4 for anode (electrolysis) 
cylinder_4_vector = FreeCAD.Vector(10, 0, 0)
cylinder_4.translate(cylinder_4_vector)
top_electrodes = top_electrodes.cut(cylinder_4)

# top_electrodes cut by cylinder_4 for cathode (electrolysis) 
cylinder_4_vector = FreeCAD.Vector(-20, 0, 0)
cylinder_4.translate(cylinder_4_vector)
top_electrodes = top_electrodes.cut(cylinder_4)

Part.show(top_electrodes)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_top_electrodes").getObject("Shape"))

stl_file = u"part_top_electrodes.stl"

Mesh.export(__objs__, stl_file)

setview()

del __objs__

# Generate PNG files
file = 'part_top_electrodes_'
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
