import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_we_and_etagere"


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

FreeCADGui.getDocument("assembly_we_and_etagere").getObject("Shape").ShapeColor = (1.00, 1.00, 0.00)

# etage 1 / insertion assembly_water_electrolyzer
vector = App.Vector(250/2 + 50, 250/2 + 25, 100 + 40 + (450 + 20)*0)
Mesh.insert(u"assembly_water_electrolyzer.stl", "assembly_we_and_etagere")
FreeCAD.getDocument("assembly_we_and_etagere").getObject("assembly_water_electrolyzer").Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))

# insertion assembly_water_electrolyzer
for i in range(1, 3):
    vector = App.Vector((250/2 + 62.5) + (250 + 62.5)*i, 250/2 + 25, 100 + 40 + (450 + 20)*0)
    Mesh.insert(u"assembly_water_electrolyzer.stl", "assembly_we_and_etagere")
    FreeCAD.getDocument("assembly_we_and_etagere").getObject("assembly_water_electrolyzer00" + str(i)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))

# etage 2 / insertion assembly_water_electrolyzer
for i in range(3, 6):
    vector = App.Vector((250/2 + 62.5) + (250 + 62.5)*(i-3), 250/2 + 25, 100 + 40 + (450 + 20)*1)
    Mesh.insert(u"assembly_water_electrolyzer.stl", "assembly_we_and_etagere")
    FreeCAD.getDocument("assembly_we_and_etagere").getObject("assembly_water_electrolyzer00" + str(i)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))

# etage 3 / insertion assembly_water_electrolyzer
for i in range(6, 9):
    vector = App.Vector((250/2 + 62.5) + (250 + 62.5)*(i-6), 250/2 + 25, 100 + 40 + (450 + 20)*2)
    Mesh.insert(u"assembly_water_electrolyzer.stl", "assembly_we_and_etagere")
    FreeCAD.getDocument("assembly_we_and_etagere").getObject("assembly_water_electrolyzer00" + str(i)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
    
# etage 4 / insertion assembly_water_electrolyzer
for i in range(9, 12):
    if i < 10:
        vector = App.Vector((250/2 + 62.5) + (250 + 62.5)*(i-9), 250/2 + 25, 100 + 40 + (450 + 20)*3)
        Mesh.insert(u"assembly_water_electrolyzer.stl", "assembly_we_and_etagere")
        FreeCAD.getDocument("assembly_we_and_etagere").getObject("assembly_water_electrolyzer00" + str(i)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
    else:
        vector = App.Vector((250/2 + 62.5) + (250 + 62.5)*(i-9), 250/2 + 25, 100 + 40 + (450 + 20)*3)
        Mesh.insert(u"assembly_water_electrolyzer.stl", "assembly_we_and_etagere")
        FreeCAD.getDocument("assembly_we_and_etagere").getObject("assembly_water_electrolyzer0" + str(i)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
    
# etage 5 / insertion assembly_water_electrolyzer
for i in range(12, 15):
    vector = App.Vector((250/2 + 62.5) + (250 + 62.5)*(i-12), 250/2 + 25, 100 + 40 + (450 + 20)*4)
    Mesh.insert(u"assembly_water_electrolyzer.stl", "assembly_we_and_etagere")
    FreeCAD.getDocument("assembly_we_and_etagere").getObject("assembly_water_electrolyzer0" + str(i)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
    
setview()

__objs__=[]
__objs__.append(FreeCAD.getDocument("assembly_we_and_etagere").getObject("Shape"))
__objs__.append(FreeCAD.getDocument("assembly_we_and_etagere").getObject("assembly_water_electrolyzer003"))
__objs__.append(FreeCAD.getDocument("assembly_we_and_etagere").getObject("assembly_water_electrolyzer007"))
__objs__.append(FreeCAD.getDocument("assembly_we_and_etagere").getObject("assembly_water_electrolyzer008"))
__objs__.append(FreeCAD.getDocument("assembly_we_and_etagere").getObject("assembly_water_electrolyzer009"))
__objs__.append(FreeCAD.getDocument("assembly_we_and_etagere").getObject("assembly_water_electrolyzer006"))
__objs__.append(FreeCAD.getDocument("assembly_we_and_etagere").getObject("assembly_water_electrolyzer004"))
__objs__.append(FreeCAD.getDocument("assembly_we_and_etagere").getObject("assembly_water_electrolyzer010"))
__objs__.append(FreeCAD.getDocument("assembly_we_and_etagere").getObject("assembly_water_electrolyzer"))
__objs__.append(FreeCAD.getDocument("assembly_we_and_etagere").getObject("assembly_water_electrolyzer011"))
__objs__.append(FreeCAD.getDocument("assembly_we_and_etagere").getObject("assembly_water_electrolyzer012"))
__objs__.append(FreeCAD.getDocument("assembly_we_and_etagere").getObject("assembly_water_electrolyzer001"))
__objs__.append(FreeCAD.getDocument("assembly_we_and_etagere").getObject("assembly_water_electrolyzer013"))
__objs__.append(FreeCAD.getDocument("assembly_we_and_etagere").getObject("assembly_water_electrolyzer005"))
__objs__.append(FreeCAD.getDocument("assembly_we_and_etagere").getObject("assembly_water_electrolyzer014"))
__objs__.append(FreeCAD.getDocument("assembly_we_and_etagere").getObject("assembly_water_electrolyzer002"))

stl_file = u"assembly_we_and_etagere.stl"

Mesh.export(__objs__, stl_file)

del __objs__

# Generate PNG files
file = 'assembly_we_and_etagere_'
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
        