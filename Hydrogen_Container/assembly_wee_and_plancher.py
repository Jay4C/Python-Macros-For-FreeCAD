import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_wee_and_plancher"


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
hauteur_exterieure_maximale = 2591

# dimensions interieures maximales
longueur_interieure_maximale = 5867
largeur_interieure_maximale = 2330
hauteur_interieure_maximale = 2350

plancher = Part.makeBox(longueur_interieure_maximale, largeur_interieure_maximale, (hauteur_exterieure_maximale - hauteur_interieure_maximale)/2)

Part.show(plancher)

DOC.recompute()

FreeCADGui.getDocument("assembly_wee_and_plancher").getObject("Shape").ShapeColor = (1.00, 0.00, 0.00)

# rang 1 / insertion assembly_we_and_etagere
vector = App.Vector(0, 0, (hauteur_exterieure_maximale - hauteur_interieure_maximale)/2)
Mesh.insert(u"assembly_we_and_etagere.stl", "assembly_wee_and_plancher")
FreeCAD.getDocument("assembly_wee_and_plancher").getObject("assembly_we_and_etagere").Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))

# rang 1 / insertion assembly_we_and_etagere
for i in range(1, 5):
    vector = App.Vector((1000 + 200)*i, (300 + 1100)*0, (hauteur_exterieure_maximale - hauteur_interieure_maximale)/2)
    Mesh.insert(u"assembly_we_and_etagere.stl", "assembly_wee_and_plancher")
    FreeCAD.getDocument("assembly_wee_and_plancher").getObject("assembly_we_and_etagere00" + str(i)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))

# rang 2 / insertion assembly_we_and_etagere
for i in range(5, 10):
    vector = App.Vector((1000 + 200)*(i-5), (300 + 1100)*1, (hauteur_exterieure_maximale - hauteur_interieure_maximale)/2)
    Mesh.insert(u"assembly_we_and_etagere.stl", "assembly_wee_and_plancher")
    FreeCAD.getDocument("assembly_wee_and_plancher").getObject("assembly_we_and_etagere00" + str(i)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
        
setview()

__objs__=[]
__objs__.append(FreeCAD.getDocument("assembly_wee_and_plancher").getObject("Shape"))
__objs__.append(FreeCAD.getDocument("assembly_wee_and_plancher").getObject("assembly_we_and_etagere"))
__objs__.append(FreeCAD.getDocument("assembly_wee_and_plancher").getObject("assembly_we_and_etagere001"))
__objs__.append(FreeCAD.getDocument("assembly_wee_and_plancher").getObject("assembly_we_and_etagere002"))
__objs__.append(FreeCAD.getDocument("assembly_wee_and_plancher").getObject("assembly_we_and_etagere003"))
__objs__.append(FreeCAD.getDocument("assembly_wee_and_plancher").getObject("assembly_we_and_etagere004"))
__objs__.append(FreeCAD.getDocument("assembly_wee_and_plancher").getObject("assembly_we_and_etagere005"))
__objs__.append(FreeCAD.getDocument("assembly_wee_and_plancher").getObject("assembly_we_and_etagere006"))
__objs__.append(FreeCAD.getDocument("assembly_wee_and_plancher").getObject("assembly_we_and_etagere007"))
__objs__.append(FreeCAD.getDocument("assembly_wee_and_plancher").getObject("assembly_we_and_etagere008"))
__objs__.append(FreeCAD.getDocument("assembly_wee_and_plancher").getObject("assembly_we_and_etagere009"))

stl_file = u"assembly_wee_and_plancher.stl"

Mesh.export(__objs__, stl_file)

del __objs__

# Generate PNG files
file = 'assembly_wee_and_plancher_'
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
        