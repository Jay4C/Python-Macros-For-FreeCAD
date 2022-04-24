import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_moteur_electrique"


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

# part_moteur_electrique
Mesh.insert(u"part_moteur_electrique.stl","assembly_moteur_electrique")
FreeCADGui.getDocument("assembly_moteur_electrique").getObject("part_moteur_electrique").ShapeColor = (0.10,0.10,0.10)
FreeCAD.getDocument("assembly_moteur_electrique").getObject("part_moteur_electrique").Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),0))

# part_poulie_moteur_electrique
Mesh.insert(u"part_poulie_moteur_electrique.stl","assembly_moteur_electrique")
FreeCADGui.getDocument("assembly_moteur_electrique").getObject("part_poulie_moteur_electrique").ShapeColor = (0.90,0.80,0.70)
FreeCAD.getDocument("assembly_moteur_electrique").getObject("part_poulie_moteur_electrique").Placement = App.Placement(App.Vector(-50,320/2,160),App.Rotation(App.Vector(0,1,0),90))

# part_moyeu_amovible_moteur_electrique
Mesh.insert(u"part_moyeu_amovible_moteur_electrique.stl","assembly_moteur_electrique")
FreeCADGui.getDocument("assembly_moteur_electrique").getObject("part_moyeu_amovible_moteur_electrique").ShapeColor = (0.10,0.20,0.30)
FreeCAD.getDocument("assembly_moteur_electrique").getObject("part_moyeu_amovible_moteur_electrique").Placement = App.Placement(App.Vector(-50,320/2,160),App.Rotation(App.Vector(0,1,0),90))

setview()

# Export assembly_moteur_electrique
__objs__=[]
__objs__.append(FreeCAD.getDocument("assembly_moteur_electrique").getObject("part_moteur_electrique"))
__objs__.append(FreeCAD.getDocument("assembly_moteur_electrique").getObject("part_poulie_moteur_electrique"))
__objs__.append(FreeCAD.getDocument("assembly_moteur_electrique").getObject("part_moyeu_amovible_moteur_electrique"))

Mesh.export(__objs__,u"assembly_moteur_electrique.stl")

del __objs__

# Generate PNG files
file = 'assembly_moteur_electrique_v2_'
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
