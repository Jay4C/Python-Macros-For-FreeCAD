import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_socle"


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

# part_palette
Mesh.insert(u"part_palette.stl","assembly_socle")
FreeCADGui.getDocument("assembly_socle").getObject("part_palette").ShapeColor = (0.10,0.10,0.10)
FreeCAD.getDocument("assembly_socle").getObject("part_palette").Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),0))

height_alternateur = 200
total_number_of_masselottes = 840
number_of_masselottes_per_slice_flywheel_per_block = round(total_number_of_masselottes/4)
radius_flywheel = 500
maximal_radius_masselotte_compiled = round(math.sqrt(math.pow(radius_flywheel, 2) + math.pow(number_of_masselottes_per_slice_flywheel_per_block*20 + 35, 2)))
number_of_masselottes_for_moteur_electrique = 8

# For palier - 1
i1 = round((maximal_radius_masselotte_compiled + height_alternateur)/20)

# part_masselotte
for i in range(0, i1 - 1):
    x = (1200 - 200)/2
    y = 10 + 20 + 3 + 22.2 + 3 + 20 + 3
    z = 100 + i * 20

    if i == 0:
        Mesh.insert(u"part_masselotte.stl","assembly_socle")
        FreeCADGui.getDocument("assembly_socle").getObject("part_masselotte").ShapeColor = (0.90,0.80,0.70)
        FreeCAD.getDocument("assembly_socle").getObject("part_masselotte").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
    elif 1 <= i < 10:
        Mesh.insert(u"part_masselotte.stl","assembly_socle")
        FreeCADGui.getDocument("assembly_socle").getObject("part_masselotte00" + str(i)).ShapeColor = (0.90,0.80,0.70)
        FreeCAD.getDocument("assembly_socle").getObject("part_masselotte00" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
    elif 10 <= i < 100:
        Mesh.insert(u"part_masselotte.stl","assembly_socle")
        FreeCADGui.getDocument("assembly_socle").getObject("part_masselotte0" + str(i)).ShapeColor = (0.90,0.80,0.70)
        FreeCAD.getDocument("assembly_socle").getObject("part_masselotte0" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
    elif 100 <= i < 1000:
        Mesh.insert(u"part_masselotte.stl","assembly_socle")
        FreeCADGui.getDocument("assembly_socle").getObject("part_masselotte" + str(i)).ShapeColor = (0.90,0.80,0.70)
        FreeCAD.getDocument("assembly_socle").getObject("part_masselotte" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
    
# For palier - 2

i2 = i1 * 2

for i in range(i1 - 1, i2 - 2):
    x = (1200 - 200)/2
    y = 1000 - (70 + 10 + 20 + 3 + 22.2 + 3 + 20)
    z = 100 + (i - (i1 - 1)) * 20

    if i == 0:
        Mesh.insert(u"part_masselotte.stl","assembly_socle")
        FreeCADGui.getDocument("assembly_socle").getObject("part_masselotte").ShapeColor = (0.90,0.80,0.70)
        FreeCAD.getDocument("assembly_socle").getObject("part_masselotte").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
    elif 1 <= i < 10:
        Mesh.insert(u"part_masselotte.stl","assembly_socle")
        FreeCADGui.getDocument("assembly_socle").getObject("part_masselotte00" + str(i)).ShapeColor = (0.90,0.80,0.70)
        FreeCAD.getDocument("assembly_socle").getObject("part_masselotte00" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
    elif 10 <= i < 100:
        Mesh.insert(u"part_masselotte.stl","assembly_socle")
        FreeCADGui.getDocument("assembly_socle").getObject("part_masselotte0" + str(i)).ShapeColor = (0.90,0.80,0.70)
        FreeCAD.getDocument("assembly_socle").getObject("part_masselotte0" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
    elif 100 <= i < 1000:
        Mesh.insert(u"part_masselotte.stl","assembly_socle")
        FreeCADGui.getDocument("assembly_socle").getObject("part_masselotte" + str(i)).ShapeColor = (0.90,0.80,0.70)
        FreeCAD.getDocument("assembly_socle").getObject("part_masselotte" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))

setview()

# Export assembly_socle
__objs__=[]
__objs__.append(FreeCAD.getDocument("assembly_socle").getObject("part_palette"))

# For palier - 1
for i in range(0, i1 - 1):
    if i == 0:
        __objs__.append(FreeCAD.getDocument("assembly_socle").getObject("part_masselotte"))
    elif 1 <= i < 10:
        __objs__.append(FreeCAD.getDocument("assembly_socle").getObject("part_masselotte00" + str(i)))
    elif 10 <= i < 100:
        __objs__.append(FreeCAD.getDocument("assembly_socle").getObject("part_masselotte0" + str(i)))
    elif 100 <= i < 1000:
        __objs__.append(FreeCAD.getDocument("assembly_socle").getObject("part_masselotte" + str(i)))
    
# For palier - 2
for i in range(i1 - 1, i2 - 2):
    if i == 0:
        __objs__.append(FreeCAD.getDocument("assembly_socle").getObject("part_masselotte"))
    elif 1 <= i < 10:
        __objs__.append(FreeCAD.getDocument("assembly_socle").getObject("part_masselotte00" + str(i)))
    elif 10 <= i < 100:
        __objs__.append(FreeCAD.getDocument("assembly_socle").getObject("part_masselotte0" + str(i)))
    elif 100 <= i < 1000:
        __objs__.append(FreeCAD.getDocument("assembly_socle").getObject("part_masselotte" + str(i)))

Mesh.export(__objs__,u"assembly_socle.stl")

del __objs__

# Generate PNG files
file = 'assembly_socle_v3_'
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
