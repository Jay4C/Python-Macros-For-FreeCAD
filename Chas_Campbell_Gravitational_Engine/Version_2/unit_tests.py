import os
import time
import unittest
import pywinauto.mouse
import pywinauto.keyboard


class UnitsChasCampbellGravitationalEngineVersion2Parts(unittest.TestCase):
    # ok
    # https://www.gensetcomponents.com/fr/Alternateur-Mecc-Alte-ECP34-1S/4-triphase-95-KVA-LTP-/-85-KVA-PRP-1500-rpm-50-Hz-avec-AVR
    def test_part_alternateur(self):
        print("test_part_alternateur")

        if os.path.exists("part_alternateur.py"):
            os.remove("part_alternateur.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_alternateur.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_alternateur"


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
x = 817.5
y = 470
z = 743
part_alternateur = Part.makeBox(x, y, z)

# arbre
D = 65
E = 99
arbre = Part.makeCylinder(D/2, E)

# rotation arbre moteur
axe_y = FreeCAD.Vector(0, 1, 0)
arbre_vector = FreeCAD.Vector(0, 0, 0)
arbre.rotate(arbre_vector, axe_y, -90)

# translation arbre moteur
arbre_vector = FreeCAD.Vector(0, 456/2, 250)
arbre.translate(arbre_vector)
part_alternateur = part_alternateur.fuse(arbre)

Part.show(part_alternateur)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_alternateur").getObject("Shape"))

stl_file = u"part_alternateur.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_alternateur_v2_'
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
            'exec{(}open{(}"'
            ''
            ''
            'part_alternateur.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.em-distribution.fr/moteur-%C3%A9lectrique-triphas%C3%A9-3000trmin/2873-moteur-electrique-triphase-cemer-b3-18-5-kw-3000-tr-min-400v-690v-ha-160-ie1-aluminium.html
    def test_part_moteur_electrique(self):
        print("test_part_moteur_electrique")

        if os.path.exists("part_moteur_electrique.py"):
            os.remove("part_moteur_electrique.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_moteur_electrique.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_moteur_electrique"


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
x = 740
y = 320
z = 420
part_moteur_electrique = Part.makeBox(x, y, z)

# arbre
D = 42
E = 110
arbre = Part.makeCylinder(D/2, E)

# rotation arbre moteur
axe_y = FreeCAD.Vector(0, 1, 0)
arbre_vector = FreeCAD.Vector(0, 0, 0)
arbre.rotate(arbre_vector, axe_y, -90)

# translation arbre moteur
H = 160
AA = 320
arbre_vector = FreeCAD.Vector(0, AA/2, H)
arbre.translate(arbre_vector)
part_moteur_electrique = part_moteur_electrique.fuse(arbre)

Part.show(part_moteur_electrique)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_moteur_electrique").getObject("Shape"))

stl_file = u"part_moteur_electrique.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_moteur_electrique_v2_'
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
            'exec{(}open{(}"'
            ''
            'part_moteur_electrique.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.123courroies.com/moyeu-amovible/71601-moyeu-amovible-ma1108-20-4014486251913.html
    def test_part_moyeu_amovible_volant_inertie(self):
        print("test_part_moyeu_amovible_volant_inertie")

        if os.path.exists("part_moyeu_amovible_volant_inertie.py"):
            os.remove("part_moyeu_amovible_volant_inertie.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_moyeu_amovible_volant_inertie.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_moyeu_amovible_volant_inertie"


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

# part_moyeu_amovible_volant_inertie
De = 38
L = 22.2
part_moyeu_amovible_volant_inertie = Part.makeCylinder(De/2, L)

cylinder_1 = Part.makeCylinder(20/2, L)

# Cut part_moyeu_amovible_volant_inertie by cylinder_1
part_moyeu_amovible_volant_inertie = part_moyeu_amovible_volant_inertie.cut(cylinder_1)

Part.show(part_moyeu_amovible_volant_inertie)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_moyeu_amovible_volant_inertie").getObject("Shape"))

stl_file = u"part_moyeu_amovible_volant_inertie.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_moyeu_amovible_volant_inertie_v2_'
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
            'exec{(}open{(}"'
            ''
            ''
            'part_moyeu_amovible_volant_inertie.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.123courroies.com/profil-z-10x6-spz-10x8/73958-poulie-trapezoidale-moyeu-amovible-spz63-1ma-4014486249743.html
    def test_part_poulie_volant_inertie(self):
        print("test_part_poulie_volant_inertie")

        if os.path.exists("part_poulie_volant_inertie.py"):
            os.remove("part_poulie_volant_inertie.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_poulie_volant_inertie.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_poulie_volant_inertie"


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

# part_poulie_volant_inertie
De = 67
L = 22.2
part_poulie_volant_inertie = Part.makeCylinder(De/2, L)

cylinder_1 = Part.makeCylinder(38/2, L)

# Cut part_poulie_volant_inertie by cylinder_1
part_poulie_volant_inertie = part_poulie_volant_inertie.cut(cylinder_1)

Part.show(part_poulie_volant_inertie)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_poulie_volant_inertie").getObject("Shape"))

stl_file = u"part_poulie_volant_inertie.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_poulie_volant_inertie_v2_'
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
            'exec{(}open{(}"'
            ''
            'part_poulie_volant_inertie.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.123courroies.com/moyeu-amovible/71717-moyeu-amovible-ma2517-65.html
    def test_part_moyeu_amovible_alternateur(self):
        print("test_part_moyeu_amovible_alternateur")

        if os.path.exists("part_moyeu_amovible_alternateur.py"):
            os.remove("part_moyeu_amovible_alternateur.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_moyeu_amovible_alternateur.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_moyeu_amovible_alternateur"


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

# part_moyeu_amovible_alternateur
De = 85.5
L = 44.45
part_moyeu_amovible_alternateur = Part.makeCylinder(De/2, L)

cylinder_1 = Part.makeCylinder(65/2, L)

# Cut part_moyeu_amovible_alternateur by cylinder_1
part_moyeu_amovible_alternateur = part_moyeu_amovible_alternateur.cut(cylinder_1)

Part.show(part_moyeu_amovible_alternateur)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_moyeu_amovible_alternateur").getObject("Shape"))

stl_file = u"part_moyeu_amovible_alternateur.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_moyeu_amovible_alternateur_v2_'
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
            'exec{(}open{(}"'
            ''
            ''
            'part_moyeu_amovible_alternateur.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.123courroies.com/profil-z-10x6-spz-10x8/74025-poulie-trapezoidale-moyeu-amovible-spz132-5ma-4014486250398.html
    def test_part_poulie_alternateur(self):
        print("test_part_poulie_alternateur")

        if os.path.exists("part_poulie_alternateur.py"):
            os.remove("part_poulie_alternateur.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_poulie_alternateur.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_poulie_alternateur"


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

# part_poulie_alternateur
De = 136
L = 44.45
part_poulie_alternateur = Part.makeCylinder(De/2, L)

cylinder_1 = Part.makeCylinder(85.5/2, L)

# Cut part_poulie_alternateur by cylinder_1
part_poulie_alternateur = part_poulie_alternateur.cut(cylinder_1)

Part.show(part_poulie_alternateur)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_poulie_alternateur").getObject("Shape"))

stl_file = u"part_poulie_alternateur.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_poulie_alternateur_v2_'
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
            'exec{(}open{(}"'
            ''
            'part_poulie_alternateur.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.123courroies.com/moyeu-amovible/71711-moyeu-amovible-ma2517-42-4014486252811.html
    def test_part_moyeu_amovible_moteur_electrique(self):
        print("test_part_moyeu_amovible_moteur_electrique")

        if os.path.exists("part_moyeu_amovible_moteur_electrique.py"):
            os.remove("part_moyeu_amovible_moteur_electrique.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_moyeu_amovible_moteur_electrique.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_moyeu_amovible_moteur_electrique"


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

# part_moyeu_amovible_moteur_electrique
De = 85.5
L = 44.45
part_moyeu_amovible_moteur_electrique = Part.makeCylinder(De/2, L)

cylinder_1 = Part.makeCylinder(42/2, L)

# Cut part_moyeu_amovible_moteur_electrique by cylinder_1
part_moyeu_amovible_moteur_electrique = part_moyeu_amovible_moteur_electrique.cut(cylinder_1)

Part.show(part_moyeu_amovible_moteur_electrique)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_moyeu_amovible_moteur_electrique").getObject("Shape"))

stl_file = u"part_moyeu_amovible_moteur_electrique.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_moyeu_amovible_moteur_electrique_v2_'
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
            'exec{(}open{(}"'
            ''
            ''
            'part_moyeu_amovible_moteur_electrique.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.france-poulies.com/paliers/5370-palier-alesage-o20-aplique-2-trous.html
    def test_part_palier(self):
        print("test_part_palier")

        if os.path.exists("part_palier.py"):
            os.remove("part_palier.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_palier.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_palier"


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

# part_palier
x = 127
y = 38
z = 65
part_palier = Part.makeBox(x, y, z)

trou_arbre = Part.makeCylinder(20/2, y)

# Cut part_palier by trou_arbre
# rotation trou_arbre
axe_x = FreeCAD.Vector(1, 0, 0)
trou_arbre_vector = FreeCAD.Vector(0, 0, 0)
trou_arbre.rotate(trou_arbre_vector, axe_x, 90)

# translation trou_arbre
trou_arbre_vector = FreeCAD.Vector(x/2, 38, 33.3)
trou_arbre.translate(trou_arbre_vector)

part_palier = part_palier.cut(trou_arbre)

# Cut part_palier by trou_vis
trou_vis = Part.makeCylinder(13/2, 65)

# translation trou_vis
trou_vis_vector = FreeCAD.Vector((127-95)/2, 38/2, 0)
trou_vis.translate(trou_vis_vector)

part_palier = part_palier.cut(trou_vis)

# translation trou_vis
trou_vis_vector = FreeCAD.Vector(95, 0, 0)
trou_vis.translate(trou_vis_vector)

part_palier = part_palier.cut(trou_vis)

Part.show(part_palier)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_palier").getObject("Shape"))

stl_file = u"part_palier.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_palier_v2_'
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
            'exec{(}open{(}"'
            ''
            'part_palier.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.123courroies.com/profil-z-10x6-spz-10x8/74127-poulie-trapezoidale-moyeu-amovible-spz630-3ma-4014486251418.html
    def test_part_poulie_moteur_electrique(self):
        print("test_part_poulie_moteur_electrique")

        if os.path.exists("part_poulie_moteur_electrique.py"):
            os.remove("part_poulie_moteur_electrique.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_poulie_moteur_electrique.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_poulie_moteur_electrique"


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

# part_poulie_moteur_electrique
De = 634
L = 44.45
part_poulie_moteur_electrique = Part.makeCylinder(De/2, L)

cylinder_1 = Part.makeCylinder(85.5/2, L)

# Cut part_poulie_moteur_electrique by cylinder_1
part_poulie_moteur_electrique = part_poulie_moteur_electrique.cut(cylinder_1)

Part.show(part_poulie_moteur_electrique)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_poulie_moteur_electrique").getObject("Shape"))

stl_file = u"part_poulie_moteur_electrique.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_poulie_moteur_electrique_v2_'
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
            'exec{(}open{(}"'
            ''
            'part_poulie_moteur_electrique.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.visseriefixations.fr/tiges-filetees/acier-classe-4-6/tige-filetee-acier-4-6-brut-din-975/tige-filetee-m20-acier-4-6-brut-din-975.html
    def test_part_tige_filetee_m20_1000l(self):
        print("test_part_tige_filetee_m20_1000l")

        if os.path.exists("part_tige_filetee_m20_1000l.py"):
            os.remove("part_tige_filetee_m20_1000l.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_tige_filetee_m20_1000l.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "tige_filetee_m20_1000l"


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

# tige_filetee_m20_1000l
tige_filetee_m20_1000l = Part.makeCylinder(20/2, 1000)

Part.show(tige_filetee_m20_1000l)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("tige_filetee_m20_1000l").getObject("Shape"))

stl_file = u"part_tige_filetee_m20_1000l.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'tige_filetee_m20_1000l_v2_'
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
            'exec{(}open{(}"'
            ''
            'part_tige_filetee_m20_1000l.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.visseriefixations.fr/ecrous/ecrous-autofreines/ecrou-hexagonal-autofreine-nylstop/ecrou-nylstop-acier-zingue-blanc-din-985/ecrou-nylstop-m20-z-blanc-din-985.html
    def test_part_ecrou_20m(self):
        print("test_part_ecrou_20m")

        if os.path.exists("part_ecrou_20m.py"):
            os.remove("part_ecrou_20m.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_ecrou_20m.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_ecrou_20m"


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

d1 = 20
e = 32.95
h = 20

cylinder_1 = Part.makeCylinder(e/2, h)

cylinder_2 = Part.makeCylinder(d1/2, h)

cylinder_1 = cylinder_1.cut(cylinder_2)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_ecrou_20m").getObject("Shape"))

stl_file = u"part_ecrou_20m.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_ecrou_20m_v2_'
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
            'exec{(}open{(}"'
            ''
            'part_ecrou_20m.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.visseriefixations.fr/rondelles-circlips/rondelles-plates/sans-chanfrein/serie-etroite-z/acier/rondelle-z-acier-zingue-blanc-nfe-25513/rondelle-z-0-20-z-blanc-nfe-25513.html
    def test_part_rondelle_20m(self):
        print("test_part_rondelle_20m")

        if os.path.exists("part_rondelle_20m.py"):
            os.remove("part_rondelle_20m.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_rondelle_20m.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_rondelle_20m"


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

d1 = 21
d2 = 36
s = 3

cylinder_1 = Part.makeCylinder(d2/2, s)

cylinder_2 = Part.makeCylinder(d1/2, s)

cylinder_1 = cylinder_1.cut(cylinder_2)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_rondelle_20m").getObject("Shape"))

stl_file = u"part_rondelle_20m.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_rondelle_20m_v2_'
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
            'exec{(}open{(}"'
            ''
            'part_rondelle_20m.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.mypalletsonline.com/fr/palette-occasion-1000x1200/197-palette-bois-1000-x-1200-recycle-demi-lourde-3s.html
    def test_part_support_masselotte(self):
        print("test_part_support_masselotte")

        if os.path.exists("part_support_masselotte.py"):
            os.remove("part_support_masselotte.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_support_masselotte.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_support_masselotte"


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

length = 1200
width = 70
thickness = 20

box_1 = Part.makeBox(length, width, thickness)

cylinder_1 = Part.makeCylinder(20/2, 20)

# box_1 cut by cylinder_1
cylinder_1_vector = FreeCAD.Vector(600, 35, 0)
cylinder_1.translate(cylinder_1_vector)
box_1 = box_1.cut(cylinder_1)

Part.show(box_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_support_masselotte").getObject("Shape"))

stl_file = u"part_support_masselotte.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_support_masselotte_v2_'
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
            'exec{(}open{(}"'
            ''
            'part_support_masselotte.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.mypalletsonline.com/fr/palette-occasion-1000x1200/197-palette-bois-1000-x-1200-recycle-demi-lourde-3s.html
    def test_part_masselotte(self):
        print("test_part_masselotte")

        if os.path.exists("part_masselotte.py"):
            os.remove("part_masselotte.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_masselotte.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_masselotte"


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

length = 200
width = 70
thickness = 20

box_1 = Part.makeBox(length, width, thickness)

Part.show(box_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_masselotte").getObject("Shape"))

stl_file = u"part_masselotte.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_masselotte_v2_'
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
            'exec{(}open{(}"'
            ''
            'part_masselotte.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.mypalletsonline.com/fr/palette-occasion-1000x1200/197-palette-bois-1000-x-1200-recycle-demi-lourde-3s.html
    def test_part_palette(self):
        print("test_part_palette")

        if os.path.exists("part_palette.py"):
            os.remove("part_palette.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_palette.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_palette"


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

length = 1200
width = 1000
thickness = 100

part_palette = Part.makeBox(length, width, thickness)

Part.show(part_palette)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_palette").getObject("Shape"))

stl_file = u"part_palette.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_palette_v2_'
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
            'exec{(}open{(}"'
            ''
            'part_palette.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')


class UnitsChasCampbellGravitationalEngineVersion2Assemblies(unittest.TestCase):
    # ok
    def test_assembly_slice_flywheel(self):
        print("test_assembly_slice_flywheel")

        if os.path.exists("assembly_slice_flywheel.py"):
            os.remove("assembly_slice_flywheel.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("assembly_slice_flywheel.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_slice_flywheel"


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

# part_support_masselotte
Mesh.insert(u"part_support_masselotte.stl","assembly_slice_flywheel")
FreeCADGui.getDocument("assembly_slice_flywheel").getObject("part_support_masselotte").ShapeColor = (0.10,0.10,0.10)
FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_support_masselotte").Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),0))

number_of_masselottes = 56
i1 = round((number_of_masselottes/4)*1)
i2 = round((number_of_masselottes/4)*2)
i3 = round((number_of_masselottes/4)*3)
i4 = round((number_of_masselottes/4)*4)

# part_masselotte
for i in range(0, i1):
    x = 1000
    y = -i * 20
    z = -25
    
    if i == 0:
        Mesh.insert(u"part_masselotte.stl","assembly_slice_flywheel")
        FreeCADGui.getDocument("assembly_slice_flywheel").getObject("part_masselotte").ShapeColor = (0.90,0.80,0.70)
        FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),90))
    elif i >= 1 and i < 10:
        Mesh.insert(u"part_masselotte.stl","assembly_slice_flywheel")
        FreeCADGui.getDocument("assembly_slice_flywheel").getObject("part_masselotte00" + str(i)).ShapeColor = (0.90,0.80,0.70)
        FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte00" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),90))
    elif i >= 10 and i < 100:
        Mesh.insert(u"part_masselotte.stl","assembly_slice_flywheel")
        FreeCADGui.getDocument("assembly_slice_flywheel").getObject("part_masselotte0" + str(i)).ShapeColor = (0.90,0.80,0.70)
        FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte0" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),90))
    elif i >= 100 and i < 1000:
        Mesh.insert(u"part_masselotte.stl","assembly_slice_flywheel")
        FreeCADGui.getDocument("assembly_slice_flywheel").getObject("part_masselotte" + str(i)).ShapeColor = (0.90,0.80,0.70)
        FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),90))
            
# part_masselotte
for i in range(i1, i2):
    x = 1000
    y = 90 + 20 * (i - i1)
    z = -25
    
    if i == 0:
        Mesh.insert(u"part_masselotte.stl","assembly_slice_flywheel")
        FreeCADGui.getDocument("assembly_slice_flywheel").getObject("part_masselotte").ShapeColor = (0.90,0.80,0.70)
        FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),90))
    elif i >= 1 and i < 10:
        Mesh.insert(u"part_masselotte.stl","assembly_slice_flywheel")
        FreeCADGui.getDocument("assembly_slice_flywheel").getObject("part_masselotte00" + str(i)).ShapeColor = (0.90,0.80,0.70)
        FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte00" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),90))
    elif i >= 10 and i < 100:
        Mesh.insert(u"part_masselotte.stl","assembly_slice_flywheel")
        FreeCADGui.getDocument("assembly_slice_flywheel").getObject("part_masselotte0" + str(i)).ShapeColor = (0.90,0.80,0.70)
        FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte0" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),90))
    elif i >= 100 and i < 1000:
        Mesh.insert(u"part_masselotte.stl","assembly_slice_flywheel")
        FreeCADGui.getDocument("assembly_slice_flywheel").getObject("part_masselotte" + str(i)).ShapeColor = (0.90,0.80,0.70)
        FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),90))

# part_masselotte
for i in range(i2, i3):
    x = 0
    y = -20 * (i - i2)
    z = -25
    
    if i == 0:
        Mesh.insert(u"part_masselotte.stl","assembly_slice_flywheel")
        FreeCADGui.getDocument("assembly_slice_flywheel").getObject("part_masselotte").ShapeColor = (0.90,0.80,0.70)
        FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),90))
    elif i >= 1 and i < 10:
        Mesh.insert(u"part_masselotte.stl","assembly_slice_flywheel")
        FreeCADGui.getDocument("assembly_slice_flywheel").getObject("part_masselotte00" + str(i)).ShapeColor = (0.90,0.80,0.70)
        FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte00" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),90))
    elif i >= 10 and i < 100:
        Mesh.insert(u"part_masselotte.stl","assembly_slice_flywheel")
        FreeCADGui.getDocument("assembly_slice_flywheel").getObject("part_masselotte0" + str(i)).ShapeColor = (0.90,0.80,0.70)
        FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte0" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),90))
    elif i >= 100 and i < 1000:
        Mesh.insert(u"part_masselotte.stl","assembly_slice_flywheel")
        FreeCADGui.getDocument("assembly_slice_flywheel").getObject("part_masselotte" + str(i)).ShapeColor = (0.90,0.80,0.70)
        FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),90))

# part_masselotte
for i in range(i3, i4):
    x = 0
    y = 90 + 20 * (i - i3)
    z = -25
    
    if i == 0:
        Mesh.insert(u"part_masselotte.stl","assembly_slice_flywheel")
        FreeCADGui.getDocument("assembly_slice_flywheel").getObject("part_masselotte").ShapeColor = (0.90,0.80,0.70)
        FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),90))
    elif i >= 1 and i < 10:
        Mesh.insert(u"part_masselotte.stl","assembly_slice_flywheel")
        FreeCADGui.getDocument("assembly_slice_flywheel").getObject("part_masselotte00" + str(i)).ShapeColor = (0.90,0.80,0.70)
        FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte00" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),90))
    elif i >= 10 and i < 100:
        Mesh.insert(u"part_masselotte.stl","assembly_slice_flywheel")
        FreeCADGui.getDocument("assembly_slice_flywheel").getObject("part_masselotte0" + str(i)).ShapeColor = (0.90,0.80,0.70)
        FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte0" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),90))
    elif i >= 100 and i < 1000:
        Mesh.insert(u"part_masselotte.stl","assembly_slice_flywheel")
        FreeCADGui.getDocument("assembly_slice_flywheel").getObject("part_masselotte" + str(i)).ShapeColor = (0.90,0.80,0.70)
        FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),90))

setview()

# Export assembly_slice_flywheel
__objs__=[]
__objs__.append(FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_support_masselotte"))

for i in range(0, i1):
    if i == 0:
        __objs__.append(FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte"))
    elif i >= 1 and i < 10:
        __objs__.append(FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte00" + str(i)))
    elif i >= 10 and i < 100:
        __objs__.append(FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte0" + str(i)))
    elif i >= 100 and i < 1000:
        __objs__.append(FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte" + str(i)))

for i in range(i1, i2):
    if i == 0:
        __objs__.append(FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte"))
    elif i >= 1 and i < 10:
        __objs__.append(FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte00" + str(i)))
    elif i >= 10 and i < 100:
        __objs__.append(FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte0" + str(i)))
    elif i >= 100 and i < 1000:
        __objs__.append(FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte" + str(i)))

for i in range(i2, i3):
    if i == 0:
        __objs__.append(FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte"))
    elif i >= 1 and i < 10:
        __objs__.append(FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte00" + str(i)))
    elif i >= 10 and i < 100:
        __objs__.append(FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte0" + str(i)))
    elif i >= 100 and i < 1000:
        __objs__.append(FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte" + str(i)))
    
for i in range(i3, i4):
    if i == 0:
        __objs__.append(FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte"))
    elif i >= 1 and i < 10:
        __objs__.append(FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte00" + str(i)))
    elif i >= 10 and i < 100:
        __objs__.append(FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte0" + str(i)))
    elif i >= 100 and i < 1000:
        __objs__.append(FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte" + str(i)))

Mesh.export(__objs__,u"assembly_slice_flywheel.stl")

del __objs__

# Generate PNG files
file = 'assembly_slice_flywheel_v2_'
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
            'exec{(}open{(}"'
            ''
            'assembly_slice_flywheel.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_assembly_flywheel(self):
        print("test_assembly_flywheel")

        if os.path.exists("assembly_flywheel.py"):
            os.remove("assembly_flywheel.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("assembly_flywheel.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_flywheel"


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

# part_tige_filetee_m20_1000l
Mesh.insert(u"part_tige_filetee_m20_1000l.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_tige_filetee_m20_1000l").ShapeColor = (0.40,0.20,0.10)
FreeCAD.getDocument("assembly_flywheel").getObject("part_tige_filetee_m20_1000l").Placement = App.Placement(App.Vector(600,35,-(1000-20)/2),App.Rotation(App.Vector(0,0,1),0))

# assembly_slice_flywheel - 0
Mesh.insert(u"assembly_slice_flywheel.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("assembly_slice_flywheel").ShapeColor = (0.10,0.20,0.40)
FreeCAD.getDocument("assembly_flywheel").getObject("assembly_slice_flywheel").Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),0))

# part_rondelle_20m for slice_flywheel
Mesh.insert(u"part_rondelle_20m.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_rondelle_20m").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m").Placement = App.Placement(App.Vector(600,35,20),App.Rotation(App.Vector(0,0,1),0))

# part_rondelle_20m for slice_flywheel
Mesh.insert(u"part_rondelle_20m.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_rondelle_20m001").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m001").Placement = App.Placement(App.Vector(600,35,-3),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_20m for slice_flywheel
Mesh.insert(u"part_ecrou_20m.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_ecrou_20m").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_flywheel").getObject("part_ecrou_20m").Placement = App.Placement(App.Vector(600,35,20 + 3),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_20m for slice_flywheel
Mesh.insert(u"part_ecrou_20m.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_ecrou_20m001").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_flywheel").getObject("part_ecrou_20m001").Placement = App.Placement(App.Vector(600,35,- 3 - 20),App.Rotation(App.Vector(0,0,1),0))

# For moteur electrique

# part_poulie_volant_inertie
Mesh.insert(u"part_poulie_volant_inertie.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_poulie_volant_inertie").ShapeColor = (0.20,0.40,0.60)
FreeCAD.getDocument("assembly_flywheel").getObject("part_poulie_volant_inertie").Placement = App.Placement(App.Vector(600,35,510 - 22.2 - 10 - 20 - 3),App.Rotation(App.Vector(0,0,1),0))

# part_moyeu_amovible_volant_inertie
Mesh.insert(u"part_moyeu_amovible_volant_inertie.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_moyeu_amovible_volant_inertie").ShapeColor = (0.50,0.50,0.50)
FreeCAD.getDocument("assembly_flywheel").getObject("part_moyeu_amovible_volant_inertie").Placement = App.Placement(App.Vector(600,35,510 - 22.2 - 10 - 20 - 3),App.Rotation(App.Vector(0,0,1),0))

# part_rondelle_20m
Mesh.insert(u"part_rondelle_20m.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_rondelle_20m002").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m002").Placement = App.Placement(App.Vector(600,35,510 - 3 - 10 - 20),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_20m
Mesh.insert(u"part_ecrou_20m.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_ecrou_20m002").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_flywheel").getObject("part_ecrou_20m002").Placement = App.Placement(App.Vector(600,35,510 - 20 - 10),App.Rotation(App.Vector(0,0,1),0))

# part_rondelle_20m
Mesh.insert(u"part_rondelle_20m.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_rondelle_20m003").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m003").Placement = App.Placement(App.Vector(600,35,510 - 3 - 10 - 20 - 22.2 - 3),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_20m
Mesh.insert(u"part_ecrou_20m.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_ecrou_20m003").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_flywheel").getObject("part_ecrou_20m003").Placement = App.Placement(App.Vector(600,35,510 - 20 - 10 - 20 - 3 - 22.2 - 3),App.Rotation(App.Vector(0,0,1),0))

# For alternateur

# part_poulie_volant_inertie
Mesh.insert(u"part_poulie_volant_inertie.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_poulie_volant_inertie001").ShapeColor = (0.20,0.40,0.60)
FreeCAD.getDocument("assembly_flywheel").getObject("part_poulie_volant_inertie001").Placement = App.Placement(App.Vector(600,35,-512.2 + 22.2 + 10 + 20 + 3),App.Rotation(App.Vector(0,0,1),0))

# part_moyeu_amovible_volant_inertie
Mesh.insert(u"part_moyeu_amovible_volant_inertie.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_moyeu_amovible_volant_inertie001").ShapeColor = (0.50,0.50,0.50)
FreeCAD.getDocument("assembly_flywheel").getObject("part_moyeu_amovible_volant_inertie001").Placement = App.Placement(App.Vector(600,35,-490 + 10 + 20 + 3),App.Rotation(App.Vector(0,0,1),0))

# part_rondelle_20m
Mesh.insert(u"part_rondelle_20m.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_rondelle_20m004").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m004").Placement = App.Placement(App.Vector(600,35,-490 + 10 + 20),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_20m
Mesh.insert(u"part_ecrou_20m.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_ecrou_20m004").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_flywheel").getObject("part_ecrou_20m004").Placement = App.Placement(App.Vector(600,35,-490 + 10),App.Rotation(App.Vector(0,0,1),0))

# part_rondelle_20m
Mesh.insert(u"part_rondelle_20m.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_rondelle_20m005").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m005").Placement = App.Placement(App.Vector(600,35,-490 + 10 + 20 + 3 + 22.2),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_20m
Mesh.insert(u"part_ecrou_20m.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_ecrou_20m005").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_flywheel").getObject("part_ecrou_20m005").Placement = App.Placement(App.Vector(600,35,-490 + 10 + 20 + 3 + 22.2 + 3),App.Rotation(App.Vector(0,0,1),0))

# For moteur electrique

# part_rondelle_20m
Mesh.insert(u"part_rondelle_20m.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_rondelle_20m006").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m006").Placement = App.Placement(App.Vector(600,35,510 - 3 - 10 - 20 - 22.2 - 3 - 20),App.Rotation(App.Vector(0,0,1),0))

# part_palier
Mesh.insert(u"part_palier.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_palier").ShapeColor = (0.30,0.30,0.30)
FreeCAD.getDocument("assembly_flywheel").getObject("part_palier").Placement = App.Placement(App.Vector(600 - 127/2,35 + 65/2,510 - 38 - 10 - 20 - 3 - 22.2 - 3 - 20),App.Rotation(App.Vector(1,0,0),90))

# part_rondelle_20m
Mesh.insert(u"part_rondelle_20m.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_rondelle_20m007").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m007").Placement = App.Placement(App.Vector(600,35,510 - 3 - 10 - 20 - 3 - 22.2 - 3 - 20 - 38),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_20m
Mesh.insert(u"part_ecrou_20m.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_ecrou_20m006").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_flywheel").getObject("part_ecrou_20m006").Placement = App.Placement(App.Vector(600,35,510 - 20 - 10 - 20 - 3 - 22.2 - 3 - 20 - 38 - 3),App.Rotation(App.Vector(0,0,1),0))

# For alternateur

# part_rondelle_20m
Mesh.insert(u"part_rondelle_20m.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_rondelle_20m008").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m008").Placement = App.Placement(App.Vector(600,35,-490 + 10 + 20 + 3 + 22.2 + 3 + 20),App.Rotation(App.Vector(0,0,1),0))

# part_palier
Mesh.insert(u"part_palier.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_palier001").ShapeColor = (0.30,0.30,0.30)
FreeCAD.getDocument("assembly_flywheel").getObject("part_palier001").Placement = App.Placement(App.Vector(600 - 127/2,35 + 65/2,-490 + 10 + 20 + 3 + 22.2 + 3 + 20 + 3),App.Rotation(App.Vector(1,0,0),90))

# part_rondelle_20m
Mesh.insert(u"part_rondelle_20m.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_rondelle_20m009").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m009").Placement = App.Placement(App.Vector(600,35,-(490 - 10 - 20 - 3 - 22.2 - 3 - 20 - 3 - 38)),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_20m
Mesh.insert(u"part_ecrou_20m.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_ecrou_20m007").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_flywheel").getObject("part_ecrou_20m007").Placement = App.Placement(App.Vector(600,35,-(490 - 10 - 20 - 3 - 22.2 - 3 - 20 -3 - 38 - 3)),App.Rotation(App.Vector(0,0,1),0))

# For assembly_slice_flywheel - 1
# part_rondelle_20m
Mesh.insert(u"part_rondelle_20m.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_rondelle_20m010").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m010").Placement = App.Placement(App.Vector(600,35,20 + 3 + 20),App.Rotation(App.Vector(0,0,1),0))

# assembly_slice_flywheel
Mesh.insert(u"assembly_slice_flywheel.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("assembly_slice_flywheel001").ShapeColor = (0.10,0.20,0.40)
FreeCAD.getDocument("assembly_flywheel").getObject("assembly_slice_flywheel001").Placement = App.Placement(App.Vector(600 + 35,-600 + 35,20 + 3 + 20 + 3),App.Rotation(App.Vector(0,0,1),90))

# part_rondelle_20m
Mesh.insert(u"part_rondelle_20m.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_rondelle_20m011").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m011").Placement = App.Placement(App.Vector(600,35,20 + 3 + 20 + 3 + 20),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_20m
Mesh.insert(u"part_ecrou_20m.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_ecrou_20m008").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_flywheel").getObject("part_ecrou_20m008").Placement = App.Placement(App.Vector(600,35,20 + 3 + 20 + 3 + 20 + 3),App.Rotation(App.Vector(0,0,1),0))

# For assembly_slice_flywheel - 2
# part_rondelle_20m
Mesh.insert(u"part_rondelle_20m.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_rondelle_20m012").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m012").Placement = App.Placement(App.Vector(600,35,-3 - 20),App.Rotation(App.Vector(0,0,1),0))

# assembly_slice_flywheel
Mesh.insert(u"assembly_slice_flywheel.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("assembly_slice_flywheel002").ShapeColor = (0.10,0.20,0.40)
FreeCAD.getDocument("assembly_flywheel").getObject("assembly_slice_flywheel002").Placement = App.Placement(App.Vector(600 + 35,-600 + 35,-20 - 3 - 20),App.Rotation(App.Vector(0,0,1),90))

# part_rondelle_20m
Mesh.insert(u"part_rondelle_20m.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_rondelle_20m013").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m013").Placement = App.Placement(App.Vector(600,35,-3 - 20 - 3 - 20),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_20m
Mesh.insert(u"part_ecrou_20m.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_ecrou_20m009").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_flywheel").getObject("part_ecrou_20m009").Placement = App.Placement(App.Vector(600,35,-20 - 3 - 20 - 3 - 20),App.Rotation(App.Vector(0,0,1),0))

setview()

# Export assembly_flywheel
__objs__ = []
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_tige_filetee_m20_1000l"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("assembly_slice_flywheel"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m001"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_ecrou_20m"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_ecrou_20m001"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_poulie_volant_inertie"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_moyeu_amovible_volant_inertie"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m002"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_ecrou_20m002"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m003"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_ecrou_20m003"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_poulie_volant_inertie001"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_moyeu_amovible_volant_inertie001"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m004"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_ecrou_20m004"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m005"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_ecrou_20m005"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m006"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_palier"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m007"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_ecrou_20m006"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m008"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_palier001"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m009"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_ecrou_20m007"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m010"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("assembly_slice_flywheel001"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m011"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_ecrou_20m008"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m012"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("assembly_slice_flywheel002"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m013"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_ecrou_20m009"))

Mesh.export(__objs__,u"assembly_flywheel.stl")

del __objs__

# Generate PNG files
file = 'assembly_flywheel_v2_'
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
            'exec{(}open{(}"'
            ''
            ''
            'assembly_flywheel.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_assembly_moteur_electrique(self):
        print("test_assembly_moteur_electrique")

        if os.path.exists("assembly_moteur_electrique.py"):
            os.remove("assembly_moteur_electrique.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("assembly_moteur_electrique.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

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
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"'
            ''
            'assembly_moteur_electrique.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_assembly_alternateur(self):
        print("test_assembly_alternateur")

        if os.path.exists("assembly_alternateur.py"):
            os.remove("assembly_alternateur.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("assembly_alternateur.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

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
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"'
            ''
            'assembly_alternateur.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_assembly_socle(self):
        print("test_assembly_socle")

        if os.path.exists("assembly_socle.py"):
            os.remove("assembly_socle.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("assembly_socle.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

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
total_number_of_masselottes = 56
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
    else:
        Mesh.insert(u"part_masselotte.stl","assembly_socle")
        FreeCADGui.getDocument("assembly_socle").getObject("part_masselotte0" + str(i)).ShapeColor = (0.90,0.80,0.70)
        FreeCAD.getDocument("assembly_socle").getObject("part_masselotte0" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))

# For palier - 2

i2 = i1 * 2

for i in range(i1 - 1, i2 - 2):
    x = (1200 - 200)/2
    y = 1000 - (70 + 10 + 20 + 3 + 22.2 + 3 + 20)
    z = 100 + (i - (i1 - 1)) * 20

    if i < 10:
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
    else:
        __objs__.append(FreeCAD.getDocument("assembly_socle").getObject("part_masselotte0" + str(i)))

# For palier - 2
for i in range(i1 - 1, i2 - 2):
    if i < 10:
        __objs__.append(FreeCAD.getDocument("assembly_socle").getObject("part_masselotte00" + str(i)))
    elif 10 <= i < 100:
        __objs__.append(FreeCAD.getDocument("assembly_socle").getObject("part_masselotte0" + str(i)))
    elif 100 <= i < 1000:
        __objs__.append(FreeCAD.getDocument("assembly_socle").getObject("part_masselotte" + str(i)))

Mesh.export(__objs__,u"assembly_socle.stl")

del __objs__

# Generate PNG files
file = 'assembly_socle_v2_'
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
            'exec{(}open{(}"'
            ''
            'assembly_socle.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_assembly_support_moteur_electrique(self):
        print("test_assembly_support_moteur_electrique")

        if os.path.exists("assembly_support_moteur_electrique.py"):
            os.remove("assembly_support_moteur_electrique.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("assembly_support_moteur_electrique.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

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
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"'
            ''
            ''
            'assembly_support_moteur_electrique.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_assembly_support_alternateur(self):
        print("test_assembly_support_alternateur")

        if os.path.exists("assembly_support_alternateur.py"):
            os.remove("assembly_support_alternateur.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("assembly_support_alternateur.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_support_alternateur"


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

# assembly_alternateur
Mesh.insert(u"assembly_alternateur.stl","assembly_support_alternateur")
FreeCADGui.getDocument("assembly_support_alternateur").getObject("assembly_alternateur").ShapeColor = (0.10,0.10,0.10)
FreeCAD.getDocument("assembly_support_alternateur").getObject("assembly_alternateur").Placement = App.Placement(App.Vector(0,500 - 470/2,100),App.Rotation(App.Vector(0,0,1),0))

# part_palette - 1
Mesh.insert(u"part_palette.stl","assembly_support_alternateur")
FreeCADGui.getDocument("assembly_support_alternateur").getObject("part_palette").ShapeColor = (0.10,0.20,0.30)
FreeCAD.getDocument("assembly_support_alternateur").getObject("part_palette").Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),0))

setview()

# Export assembly_support_moteur_electrique
__objs__ = []
__objs__.append(FreeCAD.getDocument("assembly_support_alternateur").getObject("assembly_alternateur"))
__objs__.append(FreeCAD.getDocument("assembly_support_alternateur").getObject("part_palette"))

Mesh.export(__objs__,u"assembly_support_alternateur.stl")

del __objs__

# Generate PNG files
file = 'assembly_support_alternateur_v2_'
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
            'exec{(}open{(}"'
            ''
            ''
            'assembly_support_alternateur.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_assembly_support_flywheel(self):
        print("test_assembly_support_flywheel")

        if os.path.exists("assembly_support_flywheel.py"):
            os.remove("assembly_support_flywheel.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("assembly_support_flywheel.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_support_flywheel"


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

# assembly_socle
Mesh.insert(u"assembly_socle.stl","assembly_support_flywheel")
FreeCADGui.getDocument("assembly_support_flywheel").getObject("assembly_socle").ShapeColor = (0.10,0.10,0.10)
FreeCAD.getDocument("assembly_support_flywheel").getObject("assembly_socle").Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),0))

height_alternateur = 200
total_number_of_masselottes = 56
number_of_masselottes_per_slice_flywheel_per_block = round(total_number_of_masselottes/4)
radius_flywheel = 500
maximal_radius_masselotte_compiled = round(math.sqrt(math.pow(radius_flywheel, 2) + math.pow(number_of_masselottes_per_slice_flywheel_per_block*20 + 35, 2)))
total_number_of_masselotte_compiled = round((maximal_radius_masselotte_compiled + height_alternateur)/20) - 1

# assembly_flywheel
Mesh.insert(u"assembly_flywheel.stl","assembly_support_flywheel")
FreeCADGui.getDocument("assembly_support_flywheel").getObject("assembly_flywheel").ShapeColor = (0.10,0.20,0.30)
FreeCAD.getDocument("assembly_support_flywheel").getObject("assembly_flywheel").Placement = App.Placement(App.Vector(0,490,70 + 100 + total_number_of_masselotte_compiled*20 - 2.5),App.Rotation(FreeCAD.Vector(1,0,0),-90))

setview()

# Export assembly_support_flywheel
__objs__ = []
__objs__.append(FreeCAD.getDocument("assembly_support_flywheel").getObject("assembly_socle"))
__objs__.append(FreeCAD.getDocument("assembly_support_flywheel").getObject("assembly_flywheel"))

Mesh.export(__objs__,u"assembly_support_flywheel.stl")

del __objs__

# Generate PNG files
file = 'assembly_support_flywheel_v2_'
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
            'exec{(}open{(}"'
            ''
            ''
            'assembly_support_flywheel.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_assembly_global(self):
        print("test_assembly_global")

        if os.path.exists("assembly_global.py"):
            os.remove("assembly_global.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("assembly_global.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

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
FreeCAD.getDocument("assembly_global").getObject("assembly_support_alternateur").Placement = App.Placement(App.Vector((1200 - 1000)/2 + 1000,1050,0),App.Rotation(App.Vector(0,0,1),90))

# assembly_support_moteur_electrique
Mesh.insert(u"assembly_support_moteur_electrique.stl","assembly_global")
FreeCADGui.getDocument("assembly_global").getObject("assembly_support_moteur_electrique").ShapeColor = (0.40,0.60,0.80)
FreeCAD.getDocument("assembly_global").getObject("assembly_support_moteur_electrique").Placement = App.Placement(App.Vector((1200 - 1000)/2,-100,0),App.Rotation(App.Vector(0,0,1),-90))

setview()

# Export assembly_global
__objs__ = []
__objs__.append(FreeCAD.getDocument("assembly_global").getObject("assembly_support_flywheel"))
__objs__.append(FreeCAD.getDocument("assembly_global").getObject("assembly_support_alternateur"))
__objs__.append(FreeCAD.getDocument("assembly_global").getObject("assembly_support_moteur_electrique"))

Mesh.export(__objs__,u"assembly_global.stl")

del __objs__

# Generate PNG files
file = 'assembly_global_v2_'
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
            'exec{(}open{(}"'
            ''
            'assembly_global.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')


class UnitsChasCampbellGravitationalEngineVersion1PartsSteelBoxTubeForFlywheel(unittest.TestCase):
    #
    # https://www.commentfer.fr/acier-sur-mesure/2212-8346-tube-carre-acier-sur-mesure.html#/47-epaisseur-3_mm/591-section-50_x_50_mm
    def test_part_steel_box_tube_for_the_rotor_flywheel(self):
        print("test_part_steel_box_tube_for_the_rotor_flywheel")

        if os.path.exists("part_steel_box_tube_for_the_rotor_flywheel.py"):
            os.remove("part_steel_box_tube_for_the_rotor_flywheel.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_steel_box_tube_for_the_rotor_flywheel.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_steel_box_tube_for_the_rotor_flywheel"


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

# part_steel_box_tube_for_the_rotor_flywheel
h = 50
l = 50
L = 1000
e = 3
part_steel_box_tube_for_the_rotor_flywheel = Part.makeBox(L, h, l)

# Cut part_steel_box_tube_for_the_rotor_flywheel by box_1
box_1 = Part.makeBox(L, h - e*2, l - e*2)
box_1_vector = FreeCAD.Vector(0, e, e)
box_1.translate(box_1_vector)
part_steel_box_tube_for_the_rotor_flywheel = part_steel_box_tube_for_the_rotor_flywheel.cut(box_1)

Part.show(part_steel_box_tube_for_the_rotor_flywheel)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_steel_box_tube_for_the_rotor_flywheel").getObject("Shape"))

stl_file = u"part_steel_box_tube_for_the_rotor_flywheel.stl"

Mesh.export(__objs__, stl_file)

setview()
        """)

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"'
            ''
            ''
            'part_steel_box_tube_for_the_rotor_flywheel.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    #
    # https://www.commentfer.fr/acier-sur-mesure/2212-8346-tube-carre-acier-sur-mesure.html#/47-epaisseur-3_mm/591-section-50_x_50_mm
    def test_part_steel_box_tube_for_support_ground_flywheel(self):
        print("test_part_steel_box_tube_for_support_ground_flywheel")

        if os.path.exists("part_steel_box_tube_for_support_ground_flywheel.py"):
            os.remove("part_steel_box_tube_for_support_ground_flywheel.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_steel_box_tube_for_support_ground_flywheel.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_steel_box_tube_for_support_ground_flywheel"


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

# part_steel_box_tube_for_support_ground_flywheel
h = 50
l = 50
L = 500
e = 3
part_steel_box_tube_for_support_ground_flywheel = Part.makeBox(L, h, l)

# Cut part_steel_box_tube_for_support_ground_flywheel by box_1
box_1 = Part.makeBox(L, h - e*2, l - e*2)
box_1_vector = FreeCAD.Vector(0, e, e)
box_1.translate(box_1_vector)
part_steel_box_tube_for_support_ground_flywheel = part_steel_box_tube_for_support_ground_flywheel.cut(box_1)

Part.show(part_steel_box_tube_for_support_ground_flywheel)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_steel_box_tube_for_support_ground_flywheel").getObject("Shape"))

stl_file = u"part_steel_box_tube_for_support_ground_flywheel.stl"

Mesh.export(__objs__, stl_file)

setview()
        """)

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"'
            ''
            ''
            'part_steel_box_tube_for_support_ground_flywheel.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    #
    # https://www.commentfer.fr/acier-sur-mesure/2212-8346-tube-carre-acier-sur-mesure.html#/47-epaisseur-3_mm/591-section-50_x_50_mm
    def test_part_steel_box_tube_for_support_palier_flywheel(self):
        print("test_part_steel_box_tube_for_support_palier_flywheel")

        if os.path.exists("part_steel_box_tube_for_support_palier_flywheel.py"):
            os.remove("part_steel_box_tube_for_support_palier_flywheel.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_steel_box_tube_for_support_palier_flywheel.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_steel_box_tube_for_support_palier_flywheel"


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

# part_steel_box_tube_for_support_palier_flywheel
h = 50
l = 50
L = 50*2 + 20*2 + 127
e = 3
part_steel_box_tube_for_support_palier_flywheel = Part.makeBox(L, h, l)

# Cut part_steel_box_tube_for_support_palier_flywheel by box_1
box_1 = Part.makeBox(L, h - e*2, l - e*2)
box_1_vector = FreeCAD.Vector(0, e, e)
box_1.translate(box_1_vector)
part_steel_box_tube_for_support_palier_flywheel = part_steel_box_tube_for_support_palier_flywheel.cut(box_1)

Part.show(part_steel_box_tube_for_support_palier_flywheel)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_steel_box_tube_for_support_palier_flywheel").getObject("Shape"))

stl_file = u"part_steel_box_tube_for_support_palier_flywheel.stl"

Mesh.export(__objs__, stl_file)

setview()
        """)

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"'
            ''
            ''
            'part_steel_box_tube_for_support_palier_flywheel.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    #
    # https://www.commentfer.fr/acier-sur-mesure/2212-8346-tube-carre-acier-sur-mesure.html#/47-epaisseur-3_mm/591-section-50_x_50_mm
    def test_part_steel_box_tube_for_support_elevator_flywheel(self):
        print("test_part_steel_box_tube_for_support_elevator_flywheel")

        if os.path.exists("part_steel_box_tube_for_support_elevator_flywheel.py"):
            os.remove("part_steel_box_tube_for_support_elevator_flywheel.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_steel_box_tube_for_support_elevator_flywheel.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_steel_box_tube_for_support_elevator_flywheel"


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

# part_steel_box_tube_for_support_elevator_flywheel
h = 50
l = 50
L = 500 + 50*3
e = 3
part_steel_box_tube_for_support_elevator_flywheel = Part.makeBox(L, h, l)

# Cut part_steel_box_tube_for_support_elevator_flywheel by box_1
box_1 = Part.makeBox(L, h - e*2, l - e*2)
box_1_vector = FreeCAD.Vector(0, e, e)
box_1.translate(box_1_vector)
part_steel_box_tube_for_support_elevator_flywheel = part_steel_box_tube_for_support_elevator_flywheel.cut(box_1)

Part.show(part_steel_box_tube_for_support_elevator_flywheel)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_steel_box_tube_for_support_elevator_flywheel").getObject("Shape"))

stl_file = u"part_steel_box_tube_for_support_elevator_flywheel.stl"

Mesh.export(__objs__, stl_file)

setview()
        """)

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"'
            ''
            ''
            'part_steel_box_tube_for_support_elevator_flywheel.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    #
    # https://www.commentfer.fr/acier-sur-mesure/2212-8346-tube-carre-acier-sur-mesure.html#/47-epaisseur-3_mm/591-section-50_x_50_mm
    def test_part_steel_box_tube_for_support_link_flywheel(self):
        print("test_part_steel_box_tube_for_support_link_flywheel")

        if os.path.exists("part_steel_box_tube_for_support_link_flywheel.py"):
            os.remove("part_steel_box_tube_for_support_link_flywheel.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_steel_box_tube_for_support_link_flywheel.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_steel_box_tube_for_support_link_flywheel"


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

# part_steel_box_tube_for_support_link_flywheel
h = 50
l = 50
L = 1000 - 10*2 - 20*2 - 3*2
e = 3
part_steel_box_tube_for_support_link_flywheel = Part.makeBox(L, h, l)

# Cut part_steel_box_tube_for_support_link_flywheel by box_1
box_1 = Part.makeBox(L, h - e*2, l - e*2)
box_1_vector = FreeCAD.Vector(0, e, e)
box_1.translate(box_1_vector)
part_steel_box_tube_for_support_link_flywheel = part_steel_box_tube_for_support_link_flywheel.cut(box_1)

Part.show(part_steel_box_tube_for_support_link_flywheel)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_steel_box_tube_for_support_link_flywheel").getObject("Shape"))

stl_file = u"part_steel_box_tube_for_support_link_flywheel.stl"

Mesh.export(__objs__, stl_file)

setview()
        """)

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"'
            ''
            ''
            'part_steel_box_tube_for_support_link_flywheel.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    #
    # https://www.commentfer.fr/acier-sur-mesure/2239-8441-fer-carre-acier-sur-mesure.html#/586-section-25_x_25_mm
    def test_part_steel_box_for_weight(self):
        print("test_part_steel_box_for_weight")

        if os.path.exists("part_steel_box_for_weight.py"):
            os.remove("part_steel_box_for_weight.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_steel_box_for_weight.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_steel_box_for_weight"


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

# part_steel_box_for_weight
h = 25
l = 25
L = 500
part_steel_box_for_weight = Part.makeBox(L, h, l)

Part.show(part_steel_box_for_weight)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_steel_box_for_weight").getObject("Shape"))

stl_file = u"part_steel_box_for_weight.stl"

Mesh.export(__objs__, stl_file)

setview()
        """)

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"'
            ''
            ''
            'part_steel_box_for_weight.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')


class UnitsChasCampbellGravitationalEngineVersion1PartsSteelBoxTubeForMotor(unittest.TestCase):
    #
    # https://www.commentfer.fr/acier-sur-mesure/2212-8346-tube-carre-acier-sur-mesure.html#/47-epaisseur-3_mm/591-section-50_x_50_mm
    def test_part_steel_box_tube_for_support_horizontal_motor(self):
        print("test_part_steel_box_tube_for_support_horizontal_motor")

        if os.path.exists("part_steel_box_tube_for_support_horizontal_motor.py"):
            os.remove("part_steel_box_tube_for_support_horizontal_motor.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_steel_box_tube_for_support_horizontal_motor.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_steel_box_tube_for_support_horizontal_motor"


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

# part_steel_box_tube_for_support_horizontal_motor
h = 50
l = 50
L = 740
e = 3
part_steel_box_tube_for_support_horizontal_motor = Part.makeBox(L, h, l)

# Cut part_steel_box_tube_for_support_horizontal_motor by box_1
box_1 = Part.makeBox(L, h - e*2, l - e*2)
box_1_vector = FreeCAD.Vector(0, e, e)
box_1.translate(box_1_vector)
part_steel_box_tube_for_support_horizontal_motor = part_steel_box_tube_for_support_horizontal_motor.cut(box_1)

Part.show(part_steel_box_tube_for_support_horizontal_motor)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_steel_box_tube_for_support_horizontal_motor").getObject("Shape"))

stl_file = u"part_steel_box_tube_for_support_horizontal_motor.stl"

Mesh.export(__objs__, stl_file)

setview()
        """)

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"'
            ''
            ''
            'part_steel_box_tube_for_support_horizontal_motor.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    #
    # https://www.commentfer.fr/acier-sur-mesure/2212-8346-tube-carre-acier-sur-mesure.html#/47-epaisseur-3_mm/591-section-50_x_50_mm
    def test_part_steel_box_tube_for_support_vertical_motor(self):
        print("test_part_steel_box_tube_for_support_vertical_motor")

        if os.path.exists("part_steel_box_tube_for_support_vertical_motor.py"):
            os.remove("part_steel_box_tube_for_support_vertical_motor.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_steel_box_tube_for_support_vertical_motor.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_steel_box_tube_for_support_vertical_motor"


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

# part_steel_box_tube_for_support_vertical_motor
h = 50
l = 50
L = 50*2 + 50*3
e = 3
part_steel_box_tube_for_support_vertical_motor = Part.makeBox(L, h, l)

# Cut part_steel_box_tube_for_support_vertical_motor by box_1
box_1 = Part.makeBox(L, h - e*2, l - e*2)
box_1_vector = FreeCAD.Vector(0, e, e)
box_1.translate(box_1_vector)
part_steel_box_tube_for_support_vertical_motor = part_steel_box_tube_for_support_vertical_motor.cut(box_1)

Part.show(part_steel_box_tube_for_support_vertical_motor)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_steel_box_tube_for_support_vertical_motor").getObject("Shape"))

stl_file = u"part_steel_box_tube_for_support_vertical_motor.stl"

Mesh.export(__objs__, stl_file)

setview()
        """)

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"'
            ''
            ''
            'part_steel_box_tube_for_support_vertical_motor.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    #
    # https://www.commentfer.fr/acier-sur-mesure/2212-8346-tube-carre-acier-sur-mesure.html#/47-epaisseur-3_mm/591-section-50_x_50_mm
    def test_part_steel_box_tube_for_support_link_motor(self):
        print("test_part_steel_box_tube_for_support_link_motor")

        if os.path.exists("part_steel_box_tube_for_support_link_motor.py"):
            os.remove("part_steel_box_tube_for_support_link_motor.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_steel_box_tube_for_support_link_motor.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_steel_box_tube_for_support_link_motor"


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

# part_steel_box_tube_for_support_link_motor
h = 50
l = 50
L = 320
e = 3
part_steel_box_tube_for_support_link_motor = Part.makeBox(L, h, l)

# Cut part_steel_box_tube_for_support_link_motor by box_1
box_1 = Part.makeBox(L, h - e*2, l - e*2)
box_1_vector = FreeCAD.Vector(0, e, e)
box_1.translate(box_1_vector)
part_steel_box_tube_for_support_link_motor = part_steel_box_tube_for_support_link_motor.cut(box_1)

Part.show(part_steel_box_tube_for_support_link_motor)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_steel_box_tube_for_support_link_motor").getObject("Shape"))

stl_file = u"part_steel_box_tube_for_support_link_motor.stl"

Mesh.export(__objs__, stl_file)

setview()
        """)

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"'
            ''
            ''
            'part_steel_box_tube_for_support_link_motor.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')


class UnitsChasCampbellGravitationalEngineVersion1PartsSteelBoxTubeForGenerator(unittest.TestCase):
    #
    # https://www.commentfer.fr/acier-sur-mesure/2212-8346-tube-carre-acier-sur-mesure.html#/47-epaisseur-3_mm/591-section-50_x_50_mm
    def test_part_steel_box_tube_for_support_horizontal_generator(self):
        print("test_part_steel_box_tube_for_support_horizontal_generator")

        if os.path.exists("part_steel_box_tube_for_support_horizontal_generator.py"):
            os.remove("part_steel_box_tube_for_support_horizontal_generator.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_steel_box_tube_for_support_horizontal_generator.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_steel_box_tube_for_support_horizontal_generator"


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

# part_steel_box_tube_for_support_horizontal_generator
h = 50
l = 50
L = 817.5
e = 3
part_steel_box_tube_for_support_horizontal_generator = Part.makeBox(L, h, l)

# Cut part_steel_box_tube_for_support_horizontal_generator by box_1
box_1 = Part.makeBox(L, h - e*2, l - e*2)
box_1_vector = FreeCAD.Vector(0, e, e)
box_1.translate(box_1_vector)
part_steel_box_tube_for_support_horizontal_generator = part_steel_box_tube_for_support_horizontal_generator.cut(box_1)

Part.show(part_steel_box_tube_for_support_horizontal_generator)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_steel_box_tube_for_support_horizontal_generator").getObject("Shape"))

stl_file = u"part_steel_box_tube_for_support_horizontal_generator.stl"

Mesh.export(__objs__, stl_file)

setview()
        """)

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"'
            ''
            ''
            'part_steel_box_tube_for_support_horizontal_generator.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    #
    # https://www.commentfer.fr/acier-sur-mesure/2212-8346-tube-carre-acier-sur-mesure.html#/47-epaisseur-3_mm/591-section-50_x_50_mm
    def test_part_steel_box_tube_for_support_vertical_generator(self):
        print("test_part_steel_box_tube_for_support_vertical_generator")

        if os.path.exists("part_steel_box_tube_for_support_vertical_generator.py"):
            os.remove("part_steel_box_tube_for_support_vertical_generator.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_steel_box_tube_for_support_vertical_generator.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_steel_box_tube_for_support_vertical_generator"


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

# part_steel_box_tube_for_support_vertical_generator
h = 50
l = 50
L = 50*2 + 50*3
e = 3
part_steel_box_tube_for_support_vertical_generator = Part.makeBox(L, h, l)

# Cut part_steel_box_tube_for_support_vertical_generator by box_1
box_1 = Part.makeBox(L, h - e*2, l - e*2)
box_1_vector = FreeCAD.Vector(0, e, e)
box_1.translate(box_1_vector)
part_steel_box_tube_for_support_vertical_generator = part_steel_box_tube_for_support_vertical_generator.cut(box_1)

Part.show(part_steel_box_tube_for_support_vertical_generator)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_steel_box_tube_for_support_vertical_generator").getObject("Shape"))

stl_file = u"part_steel_box_tube_for_support_vertical_generator.stl"

Mesh.export(__objs__, stl_file)

setview()
        """)

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"'
            ''
            ''
            'part_steel_box_tube_for_support_vertical_generator.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    #
    # https://www.commentfer.fr/acier-sur-mesure/2212-8346-tube-carre-acier-sur-mesure.html#/47-epaisseur-3_mm/591-section-50_x_50_mm
    def test_part_steel_box_tube_for_support_link_generator(self):
        print("test_part_steel_box_tube_for_support_link_generator")

        if os.path.exists("part_steel_box_tube_for_support_link_generator.py"):
            os.remove("part_steel_box_tube_for_support_link_generator.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_steel_box_tube_for_support_link_generator.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_steel_box_tube_for_support_link_generator"


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

# part_steel_box_tube_for_support_link_generator
h = 50
l = 50
L = 470
e = 3
part_steel_box_tube_for_support_link_generator = Part.makeBox(L, h, l)

# Cut part_steel_box_tube_for_support_link_generator by box_1
box_1 = Part.makeBox(L, h - e*2, l - e*2)
box_1_vector = FreeCAD.Vector(0, e, e)
box_1.translate(box_1_vector)
part_steel_box_tube_for_support_link_generator = part_steel_box_tube_for_support_link_generator.cut(box_1)

Part.show(part_steel_box_tube_for_support_link_generator)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_steel_box_tube_for_support_link_generator").getObject("Shape"))

stl_file = u"part_steel_box_tube_for_support_link_generator.stl"

Mesh.export(__objs__, stl_file)

setview()
        """)

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"'
            ''
            ''
            'part_steel_box_tube_for_support_link_generator.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')


if __name__ == '__main__':
    unittest.main()
