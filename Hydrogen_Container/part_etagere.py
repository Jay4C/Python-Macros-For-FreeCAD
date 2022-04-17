import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_etagere"


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

# dimensions exterieures maximales
longueur_exterieure_maximale = 1000
largeur_exterieure_maximale = 300
hauteur_exterieure_maximale = 2000

etagere = Part.makeBox(longueur_exterieure_maximale, largeur_exterieure_maximale, hauteur_exterieure_maximale)

box_1 = Part.makeBox(longueur_exterieure_maximale - 2*20, largeur_exterieure_maximale, (hauteur_exterieure_maximale - 100 - 5*20)/4)

box_2 = Part.makeBox(longueur_exterieure_maximale, largeur_exterieure_maximale - 2*20, (hauteur_exterieure_maximale - 100 - 5*20)/4)

# etagere cut by box_1
box_1_vector = FreeCAD.Vector(20, 0, hauteur_exterieure_maximale)
box_1.translate(box_1_vector)
for i in range(0, 5):
    box_1_vector = FreeCAD.Vector(0, 0, - (hauteur_exterieure_maximale - 100 - 5*20)/4 - 20)
    box_1.translate(box_1_vector)
    etagere = etagere.cut(box_1)

# etagere cut by box_2
box_2_vector = FreeCAD.Vector(0, 20, hauteur_exterieure_maximale)
box_2.translate(box_2_vector)
for i in range(0, 5):
    box_2_vector = FreeCAD.Vector(0, 0, - (hauteur_exterieure_maximale - 100 - 5*20)/4 - 20)
    box_2.translate(box_2_vector)
    etagere = etagere.cut(box_2)

Part.show(etagere)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_etagere").getObject("Shape"))

stl_file = u"part_etagere.stl"

Mesh.export(__objs__, stl_file)

FreeCADGui.getDocument("part_etagere").getObject("Shape").ShapeColor = (1.00, 1.00, 0.00)

setview()

# Generate PNG files
file = 'part_etagere_'
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
        