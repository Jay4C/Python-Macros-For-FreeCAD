import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_global"


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

# assembly_support_flywheel
Mesh.insert(u"assembly_support_flywheel.stl","assembly_global")
FreeCADGui.getDocument("assembly_global").getObject("assembly_support_flywheel").ShapeColor = (0.10,0.10,0.10)
FreeCAD.getDocument("assembly_global").getObject("assembly_support_flywheel").Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),0))

# assembly_support_alternateur
Mesh.insert(u"assembly_support_alternateur.stl","assembly_global")
FreeCADGui.getDocument("assembly_global").getObject("assembly_support_alternateur").ShapeColor = (0.10,0.20,0.30)
FreeCAD.getDocument("assembly_global").getObject("assembly_support_alternateur").Placement = App.Placement(App.Vector((1200 - 1000)/2 + 1000,1100,0),App.Rotation(App.Vector(0,0,1),90))

# assembly_support_moteur_electrique
Mesh.insert(u"assembly_support_moteur_electrique.stl","assembly_global")
FreeCADGui.getDocument("assembly_global").getObject("assembly_support_moteur_electrique").ShapeColor = (0.40,0.60,0.80)
FreeCAD.getDocument("assembly_global").getObject("assembly_support_moteur_electrique").Placement = App.Placement(App.Vector((1200 - 1000)/2,-150,0),App.Rotation(App.Vector(0,0,1),-90))

setview()

# Export assembly_global
__objs__ = []
__objs__.append(FreeCAD.getDocument("assembly_global").getObject("assembly_support_flywheel"))
__objs__.append(FreeCAD.getDocument("assembly_global").getObject("assembly_support_alternateur"))
__objs__.append(FreeCAD.getDocument("assembly_global").getObject("assembly_support_moteur_electrique"))

Mesh.export(__objs__,u"assembly_global.stl")

del __objs__

# Generate PNG files
file = 'assembly_global_v3_'
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
