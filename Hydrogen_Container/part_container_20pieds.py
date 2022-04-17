import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_container_20pieds"


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
longueur_exterieure_maximale = 6058 
largeur_exterieure_maximale = 2438
hauteur_exterieure_maximale = 2591

container = Part.makeBox(longueur_exterieure_maximale, largeur_exterieure_maximale, hauteur_exterieure_maximale)

# dimensions interieures maximales
longueur_interieure_maximale = 5867
largeur_interieure_maximale = 2330
Hauteur_interieure_maximale = 2350

box_1 = Part.makeBox(longueur_interieure_maximale, largeur_interieure_maximale, Hauteur_interieure_maximale)

# container cut by box_1
x = (longueur_exterieure_maximale - longueur_interieure_maximale)/2
y = (largeur_exterieure_maximale - largeur_interieure_maximale)/2
z = (hauteur_exterieure_maximale - Hauteur_interieure_maximale)/2

box_1_vector = FreeCAD.Vector(x, y, z)
box_1.translate(box_1_vector)
container = container.cut(box_1)

Part.show(container)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_container_20pieds").getObject("Shape"))

stl_file = u"part_container_20pieds.stl"

Mesh.export(__objs__, stl_file)

setview()

FreeCADGui.getDocument("part_container_20pieds").getObject("Shape").Transparency = 80

# Generate PNG files
file = 'part_container_20pieds_'
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
        