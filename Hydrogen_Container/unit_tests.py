import time
import unittest
import os
import pywinauto.mouse
import pywinauto.keyboard


class unit_tests_hydrogen_container(unittest.TestCase):
    # ok
    # https://info-container.fr/dimensions-des-containers-maritimes/#:~:text=Dimensions%20des%20containers%20ext%C3%A9rieures%20maximales%20%20%20,591%20standard%20%2F%202%20896%20high%20cube%20
    def test_part_container_20pieds(self):
        print("test_part_container_20pieds")

        if os.path.exists("part_container_20pieds.py"):
            os.remove("part_container_20pieds.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_container_20pieds.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

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
        """)

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"part_container_20pieds.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.leroymerlin.fr/produits/quincaillerie/rangement-utilitaire/etagere-utilitaire/etagere-metallique-utilitaire/etagere-acier-orange-bleu-epoxy-simonrack-5-tablettes-l-100-x-h-200-x-p-30-cm-82130991.html
    def test_part_etagere(self):
        print("test_part_etagere")

        if os.path.exists("part_etagere.py"):
            os.remove("part_etagere.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_etagere.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

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
        """)

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"part_etagere.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_part_plancher(self):
        print("test_part_plancher")

        if os.path.exists("part_plancher.py"):
            os.remove("part_plancher.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_plancher.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_plancher"


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

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_plancher").getObject("Shape"))

stl_file = u"part_plancher.stl"

Mesh.export(__objs__, stl_file)

FreeCADGui.getDocument("part_plancher").getObject("Shape").ShapeColor = (1.00, 0.00, 0.00)

setview()

# Generate PNG files
file = 'part_plancher_'
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
        """)

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"part_plancher.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_assembly_we_and_etagere(self):
        print("test_assembly_we_and_etagere")

        if os.path.exists("assembly_we_and_etagere.py"):
            os.remove("assembly_we_and_etagere.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("assembly_we_and_etagere.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

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
        """)

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"assembly_we_and_etagere.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_assembly_wee_and_plancher(self):
        print("test_assembly_wee_and_plancher")

        if os.path.exists("assembly_wee_and_plancher.py"):
            os.remove("assembly_wee_and_plancher.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("assembly_wee_and_plancher.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

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
        """)

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"assembly_wee_and_plancher.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')


if __name__ == '__main__':
    unittest.main()
