import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_alternateur"


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

# part_alternateur
Mesh.insert(u"part_alternateur.stl","assembly_alternateur")
FreeCADGui.getDocument("assembly_alternateur").getObject("part_alternateur").ShapeColor = (0.10,0.10,0.10)
FreeCAD.getDocument("assembly_alternateur").getObject("part_alternateur").Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),0))

# part_poulie_alternateur
Mesh.insert(u"part_poulie_alternateur.stl","assembly_alternateur")
FreeCADGui.getDocument("assembly_alternateur").getObject("part_poulie_alternateur").ShapeColor = (0.90,0.80,0.70)
FreeCAD.getDocument("assembly_alternateur").getObject("part_poulie_alternateur").Placement = App.Placement(App.Vector(-50,456/2,250),App.Rotation(App.Vector(0,1,0),90))

# part_moyeu_amovible_alternateur
Mesh.insert(u"part_moyeu_amovible_alternateur.stl","assembly_alternateur")
FreeCADGui.getDocument("assembly_alternateur").getObject("part_moyeu_amovible_alternateur").ShapeColor = (0.10,0.20,0.30)
FreeCAD.getDocument("assembly_alternateur").getObject("part_moyeu_amovible_alternateur").Placement = App.Placement(App.Vector(-50,456/2,250),App.Rotation(App.Vector(0,1,0),90))

setview()

# Export assembly_alternateur
__objs__=[]
__objs__.append(FreeCAD.getDocument("assembly_alternateur").getObject("part_alternateur"))
__objs__.append(FreeCAD.getDocument("assembly_alternateur").getObject("part_poulie_alternateur"))
__objs__.append(FreeCAD.getDocument("assembly_alternateur").getObject("part_moyeu_amovible_alternateur"))

Mesh.export(__objs__,u"assembly_alternateur.stl")

del __objs__

# Generate PNG files
file = 'assembly_alternateur_v2_'
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
