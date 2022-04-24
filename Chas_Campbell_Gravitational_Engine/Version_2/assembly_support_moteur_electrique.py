import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_support_moteur_electrique"


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

# assembly_moteur_electrique
Mesh.insert(u"assembly_moteur_electrique.stl","assembly_support_moteur_electrique")
FreeCADGui.getDocument("assembly_support_moteur_electrique").getObject("assembly_moteur_electrique").ShapeColor = (0.10,0.10,0.10)
FreeCAD.getDocument("assembly_support_moteur_electrique").getObject("assembly_moteur_electrique").Placement = App.Placement(App.Vector(-50,500 - 320/2,300),App.Rotation(App.Vector(0,0,1),0))

# part_palette - 1
Mesh.insert(u"part_palette.stl","assembly_support_moteur_electrique")
FreeCADGui.getDocument("assembly_support_moteur_electrique").getObject("part_palette").ShapeColor = (0.10,0.20,0.30)
FreeCAD.getDocument("assembly_support_moteur_electrique").getObject("part_palette").Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),0))

# part_palette - 2
Mesh.insert(u"part_palette.stl","assembly_support_moteur_electrique")
FreeCADGui.getDocument("assembly_support_moteur_electrique").getObject("part_palette001").ShapeColor = (0.10,0.20,0.30)
FreeCAD.getDocument("assembly_support_moteur_electrique").getObject("part_palette001").Placement = App.Placement(App.Vector(0,0,100),App.Rotation(App.Vector(0,0,1),0))

# part_palette - 3
Mesh.insert(u"part_palette.stl","assembly_support_moteur_electrique")
FreeCADGui.getDocument("assembly_support_moteur_electrique").getObject("part_palette002").ShapeColor = (0.10,0.20,0.30)
FreeCAD.getDocument("assembly_support_moteur_electrique").getObject("part_palette002").Placement = App.Placement(App.Vector(0,0,200),App.Rotation(App.Vector(0,0,1),0))

setview()

# Export assembly_support_moteur_electrique
__objs__ = []
__objs__.append(FreeCAD.getDocument("assembly_support_moteur_electrique").getObject("assembly_moteur_electrique"))
__objs__.append(FreeCAD.getDocument("assembly_support_moteur_electrique").getObject("part_palette"))
__objs__.append(FreeCAD.getDocument("assembly_support_moteur_electrique").getObject("part_palette001"))
__objs__.append(FreeCAD.getDocument("assembly_support_moteur_electrique").getObject("part_palette002"))

Mesh.export(__objs__,u"assembly_support_moteur_electrique.stl")

del __objs__

# Generate PNG files
file = 'assembly_support_moteur_electrique_v2_'
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
