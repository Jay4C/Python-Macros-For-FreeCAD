import os
import time
import unittest
import pywinauto.mouse
import pywinauto.keyboard


class UnitTestsEdwinGrayPowerTubeVersion2(unittest.TestCase):
    # ok
    def test_part_tank(self):
        print("test_part_tank")

        if os.path.exists("part_tank.py"):
            os.remove("part_tank.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_tank.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_tank"


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

hauteur_maximal = 960

# tank
tank = Part.makeCylinder(84.5/2, hauteur_maximal)

# Cylinder_1
cylinder_1 = Part.makeCylinder(84.5/2 - 2, hauteur_maximal)

# Tank cut by cylinder_1
cylinder_1_vector = FreeCAD.Vector(0, 0, 0)
cylinder_1.translate(cylinder_1_vector)
tank = tank.cut(cylinder_1)

Part.show(tank)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_tank").getObject("Shape"))

stl_file = u"part_tank.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_tank_v3_'
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
            'exec{(}open{(}"part_tank.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.visseriefixations.fr/tiges-filetees/acier-classe-4-6/tige-filetee-acier-4-6-brut-din-975/tige-filetee-m8-acier-4-6-brut-din-975.html
    def test_part_tige_filetee_m8_1000l(self):
        print("test_part_tige_filetee_m8_1000l")

        if os.path.exists("part_tige_filetee_m8_1000l.py"):
            os.remove("part_tige_filetee_m8_1000l.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_tige_filetee_m8_1000l.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_tige_filetee_m8_1000l"


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

# tige_filetee_m8_l1000
tige_filetee_m8_l1000 = Part.makeCylinder(8/2, 1000)

Part.show(tige_filetee_m8_l1000)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_tige_filetee_m8_1000l").getObject("Shape"))

stl_file = u"part_tige_filetee_m8_1000l.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_tige_filetee_m8_1000l_v3_'
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
            'exec{(}open{(}"part_tige_filetee_m8_1000l.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.visseriefixations.fr/vis-a-tete-hexagonale/vis-a-tete-hexagonale-standard/acier-8-8-noir/th-acier-8-8-noir-filetage-total-din-933/th-m8x50-acier-8-8-noir-ef-din-933.html
    def test_part_vis_metal_m8_50l(self):
        print("test_part_vis_metal_m8_50l")

        if os.path.exists("part_vis_metal_m8_50l.py"):
            os.remove("part_vis_metal_m8_50l.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_vis_metal_m8_50l.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_vis_metal_m8_50l"


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

d1 = 8
L = 50
k = 5.30
e = 14.38

cylinder_1 = Part.makeCylinder(e/2, L + k)

cylinder_2 = Part.makeCylinder(d1/2, L)

cylinder_3 = Part.makeCylinder(e/2, L)

# cylinder_3 cut by cylinder_2
cylinder_3 = cylinder_3.cut(cylinder_2)

# cylinder_1 cut by cylinder_3
cylinder_3_vector = FreeCAD.Vector(0, 0, k)
cylinder_3.translate(cylinder_3_vector)
cylinder_1 = cylinder_1.cut(cylinder_3)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_vis_metal_m8_50l").getObject("Shape"))

stl_file = u"part_vis_metal_m8_50l.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_vis_metal_m8_50l_v3_'
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
            'exec{(}open{(}"part_vis_metal_m8_50l.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.visseriefixations.fr/ecrous/ecrous-autofreines/ecrou-hexagonal-autofreine-nylstop/ecrou-nylstop-acier-zingue-blanc-din-985/ecrou-nylstop-m8-z-blanc-din-985.html
    def test_part_ecrou_8m(self):
        print("test_part_ecrou_8m")

        if os.path.exists("part_ecrou_8m.py"):
            os.remove("part_ecrou_8m.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_ecrou_8m.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_ecrou_8m"


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

d1 = 8
e = 14.38
h = 8

cylinder_1 = Part.makeCylinder(e/2, h)

cylinder_2 = Part.makeCylinder(d1/2, h)

cylinder_1 = cylinder_1.cut(cylinder_2)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_ecrou_8m").getObject("Shape"))

stl_file = u"part_ecrou_8m.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_ecrou_8m_v3_'
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
            'exec{(}open{(}"part_ecrou_8m.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.visseriefixations.fr/rondelles-circlips/rondelles-plates/sans-chanfrein/serie-etroite-z/acier/rondelle-z-acier-zingue-blanc-nfe-25513/rondelle-z-0-8-z-blanc-nfe-25513.html
    def test_part_rondelle_8m(self):
        print("test_part_rondelle_8m")

        if os.path.exists("part_rondelle_8m.py"):
            os.remove("part_rondelle_8m.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_rondelle_8m.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_rondelle_8m"


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

d1 = 8.40
d2 = 16
s = 1.5

cylinder_1 = Part.makeCylinder(d2/2, s)

cylinder_2 = Part.makeCylinder(d1/2, s)

cylinder_1 = cylinder_1.cut(cylinder_2)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_rondelle_8m").getObject("Shape"))

stl_file = u"part_rondelle_8m.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_rondelle_8m_v3_'
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
            'exec{(}open{(}"part_rondelle_8m.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.visseriefixations.fr/vis-a-tete-hexagonale/vis-a-tete-hexagonale-standard/acier-8-8-noir/th-acier-8-8-noir-filetage-total-din-933/th-m5x20-acier-8-8-noir-ef-din-933.html
    def test_part_vis_metal_m5_20l(self):
        print("test_part_vis_metal_m5_20l")

        if os.path.exists("part_vis_metal_m5_20l.py"):
            os.remove("part_vis_metal_m5_20l.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_vis_metal_m5_20l.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_vis_metal_m5_20l"


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

d1 = 5
L = 20
k = 3.5
e = 8.79

cylinder_1 = Part.makeCylinder(e/2, L + k)

cylinder_2 = Part.makeCylinder(d1/2, L)

cylinder_3 = Part.makeCylinder(e/2, L)

# cylinder_3 cut by cylinder_2
cylinder_3 = cylinder_3.cut(cylinder_2)

# cylinder_1 cut by cylinder_3
cylinder_3_vector = FreeCAD.Vector(0, 0, k)
cylinder_3.translate(cylinder_3_vector)
cylinder_1 = cylinder_1.cut(cylinder_3)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_vis_metal_m5_20l").getObject("Shape"))

stl_file = u"part_vis_metal_m5_20l.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_vis_metal_m5_20l_v3_'
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
            'exec{(}open{(}"part_vis_metal_m5_20l.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.visseriefixations.fr/ecrous/ecrous-autofreines/ecrou-hexagonal-autofreine-nylstop/ecrou-nylstop-acier-zingue-blanc-din-985/ecrou-nylstop-m5-z-blanc-din-985.html
    def test_part_ecrou_5m(self):
        print("test_part_ecrou_5m")

        if os.path.exists("part_ecrou_5m.py"):
            os.remove("part_ecrou_5m.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_ecrou_5m.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_ecrou_5m"


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

d1 = 5
e = 8.79
h = 5

cylinder_1 = Part.makeCylinder(e/2, h)

cylinder_2 = Part.makeCylinder(d1/2, h)

cylinder_1 = cylinder_1.cut(cylinder_2)

Part.show(cylinder_1)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_ecrou_5m").getObject("Shape"))

stl_file = u"part_ecrou_5m.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_ecrou_5m_v3_'
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
            'exec{(}open{(}"part_ecrou_5m.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_part_equerre_assemblage_laser_cutting(self):
        print("test_part_equerre_assemblage_laser_cutting")

        if os.path.exists("part_equerre_assemblage_laser_cutting.py"):
            os.remove("part_equerre_assemblage_laser_cutting.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_equerre_assemblage_laser_cutting.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh, importDXF

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_equerre_assemblage_laser_cutting"


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

d1 = 8.40
d2 = 16
s = 1.5
space_between_electrodes_axes = (50/2 - 4 - 4)*2

cylinder_1 = Part.makeCylinder(d2/2, s)

cylinder_2 = Part.makeCylinder(d1/2, s)

cylinder_1 = cylinder_1.cut(cylinder_2)

box_1 = Part.makeBox(space_between_electrodes_axes - (d1/2)*2 - (d2/2-d1/2)*2 + 4, 3, s)
box_1_vector = FreeCAD.Vector(d2/2 - 2, -3/2, 0)
box_1.translate(box_1_vector)
box_1 = box_1.fuse(cylinder_1)

cylinder_3 = cylinder_1
cylinder_3_vector = FreeCAD.Vector(space_between_electrodes_axes, 0, 0)
cylinder_3.translate(cylinder_3_vector)
box_1 = box_1.fuse(cylinder_3)

Part.show(box_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_equerre_assemblage_laser_cutting").getObject("Shape"))

stl_file = u"part_equerre_assemblage_laser_cutting.stl"

Mesh.export(__objs__, stl_file)

dxf_file = u"part_equerre_assemblage_laser_cutting.dxf"

importDXF.export(__objs__, dxf_file)

setview()

# Generate PNG files
file = 'part_equerre_assemblage_laser_cutting_v3_'
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
            'exec{(}open{(}"part_equerre_assemblage_laser_cutting.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_part_equerre_assemblage_laser_cutting_v2(self):
        print("test_part_equerre_assemblage_laser_cutting_v2")

        if os.path.exists("part_equerre_assemblage_laser_cutting_v2.py"):
            os.remove("part_equerre_assemblage_laser_cutting_v2.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_equerre_assemblage_laser_cutting_v2.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh, importDXF

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_equerre_assemblage_laser_cutting_v2"


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

d1 = 8.40
d2 = 16
s = 1.5
space_between_electrodes_axes = (50/2 - 4 - 4)*2

box_1 = Part.makeBox(space_between_electrodes_axes + d2, d2, s)

cylinder_1 = Part.makeCylinder(d1/2, s)
cylinder_1_vector = FreeCAD.Vector(d2/2, d2/2, 0)
cylinder_1.translate(cylinder_1_vector)
box_1 = box_1.cut(cylinder_1)

cylinder_1_vector = FreeCAD.Vector(space_between_electrodes_axes, 0, 0)
cylinder_1.translate(cylinder_1_vector)
box_1 = box_1.cut(cylinder_1)

box_2 = Part.makeBox(space_between_electrodes_axes - d2, (d2-3)/2, s)
box_2_vector = FreeCAD.Vector(d2, 0, 0)
box_2.translate(box_2_vector)
box_1 = box_1.cut(box_2)

box_2_vector = FreeCAD.Vector(0, (d2-3)/2 + 3, 0)
box_2.translate(box_2_vector)
box_1 = box_1.cut(box_2)

cylinder_2 = Part.makeCylinder((d2+10)/2, s)
cylinder_3 = Part.makeCylinder(d2/2, s)
cylinder_2 = cylinder_2.cut(cylinder_3)
box_3 = Part.makeBox(d2+10, 3, s)
box_3_vector = FreeCAD.Vector(0, -1.5, 0)
box_3.translate(box_3_vector)
cylinder_2 = cylinder_2.cut(box_3)

cylinder_2_vector = FreeCAD.Vector(d2/2, d2/2, 0)
cylinder_2.translate(cylinder_2_vector)
box_1 = box_1.cut(cylinder_2)

cylinder_4 = Part.makeCylinder((d2+10)/2, s)
cylinder_4 = cylinder_4.cut(cylinder_3)
box_4 = Part.makeBox(d2+10, 3, s)
box_4_vector = FreeCAD.Vector(-d2 - 5, -1.5, 0)
box_4.translate(box_4_vector)
cylinder_4 = cylinder_4.cut(box_4)

cylinder_4_vector = FreeCAD.Vector(d2/2 + space_between_electrodes_axes, d2/2, 0)
cylinder_4.translate(cylinder_4_vector)
box_1 = box_1.cut(cylinder_4)

Part.show(box_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_equerre_assemblage_laser_cutting_v2").getObject("Shape"))

stl_file = u"part_equerre_assemblage_laser_cutting_v2.stl"

Mesh.export(__objs__, stl_file)

dxf_file = u"part_equerre_assemblage_laser_cutting_v2.dxf"

importDXF.export(__objs__, dxf_file)

setview()

# Generate PNG files
file = 'part_equerre_assemblage_laser_cutting_v2_v3_'
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
            'exec{(}open{(}"part_equerre_assemblage_laser_cutting_v2.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_part_electrode_laser_cutting(self):
        print("test_part_electrode_laser_cutting")

        if os.path.exists("part_electrode_laser_cutting.py"):
            os.remove("part_electrode_laser_cutting.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_electrode_laser_cutting.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh, importDXF

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_electrode_laser_cutting"


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
EPS_C = EPS * (-0.5)

cote_maximal = 50

hauteur_maximal = 1

# part_electrode_laser_cutting
part_electrode_laser_cutting = Part.makeCylinder(cote_maximal/2, hauteur_maximal)

# part_electrode_laser_cutting cut by cylinder_1
cylinder_1 = Part.makeCylinder(4, hauteur_maximal)
part_electrode_laser_cutting = part_electrode_laser_cutting.cut(cylinder_1)

# holes for fixing the cathode or the anode
degre = 180
for i in range(int(360/degre)):
    hole = Part.makeCylinder(4, hauteur_maximal)
    radius = cote_maximal/2 - 4 - 4
    alpha=(i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole.translate(hole_vector)
    part_electrode_laser_cutting = part_electrode_laser_cutting.cut(hole)

# holes for passing the cathode or the anode
degre = 360
for i in range(int(360/degre)):
    hole = Part.makeCylinder(14, hauteur_maximal)
    radius = cote_maximal/2
    alpha=(i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole.translate(hole_vector)
    part_electrode_laser_cutting = part_electrode_laser_cutting.cut(hole)

Part.show(part_electrode_laser_cutting)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_electrode_laser_cutting").getObject("Shape"))

stl_file = u"part_electrode_laser_cutting.stl"

Mesh.export(__objs__, stl_file)

dxf_file = u"part_electrode_laser_cutting.dxf"

importDXF.export(__objs__, dxf_file)

setview()

# Generate PNG files
file = 'part_electrode_laser_cutting_v3_'
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
            'exec{(}open{(}"part_electrode_laser_cutting.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_part_support_laser_cutting(self):
        print("test_part_support_laser_cutting")

        if os.path.exists("part_support_laser_cutting.py"):
            os.remove("part_support_laser_cutting.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_support_laser_cutting.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh, importDXF

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_support_laser_cutting"


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
EPS_C = EPS * (-0.5)

cote_maximal = 2 + 8 + 8 + 8 + 86 + 8 + 8 + 8 + 2

hauteur_maximal = 2

# part_support_laser_cutting
part_support_laser_cutting = Part.makeCylinder(cote_maximal/2, hauteur_maximal)

# holes for fixing the electrodes
degre = 180
for i in range(int(360/degre)):
    hole = Part.makeCylinder(4, hauteur_maximal)
    radius = 50/2 - 4 - 4
    alpha=(i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole.translate(hole_vector)
    part_support_laser_cutting = part_support_laser_cutting.cut(hole)

# holes for reducing the cost
degre = 15
for i in range(int(360/degre)):
    hole = Part.makeCylinder(4, hauteur_maximal)
    radius = 86/2 + 8 + 4
    alpha=(i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole.translate(hole_vector)
    part_support_laser_cutting = part_support_laser_cutting.cut(hole)

Part.show(part_support_laser_cutting)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_support_laser_cutting").getObject("Shape"))

stl_file = u"part_support_laser_cutting.stl"

Mesh.export(__objs__, stl_file)

dxf_file = u"part_support_laser_cutting.dxf"

importDXF.export(__objs__, dxf_file)

setview()

# Generate PNG files
file = 'part_support_laser_cutting_v3_'
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
            'exec{(}open{(}"part_support_laser_cutting.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_assembly(self):
        print("test_assembly")

        if os.path.exists("assembly.py"):
            os.remove("assembly.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("assembly.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly"


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

# part_tank
Mesh.insert(u"part_tank.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_tank").ShapeColor = (0.10,0.10,0.10)
FreeCAD.getDocument("assembly").getObject("part_tank").Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),0))
FreeCADGui.getDocument("assembly").getObject("part_tank").Transparency = 80

# part_support_laser_cutting _ 1
Mesh.insert(u"part_support_laser_cutting.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_support_laser_cutting").ShapeColor = (1.00,1.00,0.00)
FreeCAD.getDocument("assembly").getObject("part_support_laser_cutting").Placement = App.Placement(App.Vector(0,0,-2),App.Rotation(App.Vector(0,1,0),0))

# part_tige_filetee_m8_1000l for the cathode
Mesh.insert(u"part_tige_filetee_m8_1000l.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_tige_filetee_m8_1000l").ShapeColor = (0.50,0.50,0.50)
FreeCAD.getDocument("assembly").getObject("part_tige_filetee_m8_1000l").Placement = App.Placement(App.Vector(50/2 - 4 - 4, 0, -20),App.Rotation(App.Vector(0,0,1),0))

# part_tige_filetee_m8_1000l for the anode
Mesh.insert(u"part_tige_filetee_m8_1000l.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_tige_filetee_m8_1000l001").ShapeColor = (0.50,0.50,0.50)
FreeCAD.getDocument("assembly").getObject("part_tige_filetee_m8_1000l001").Placement = App.Placement(App.Vector(-50/2 + 4 + 4, 0, -20),App.Rotation(App.Vector(0,0,1),0))

# Rank 1
# part_rondelle_8m for part_tige_filetee_m8_1000l
Mesh.insert(u"part_rondelle_8m.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_rondelle_8m").ShapeColor = (0.30,0.20,0.20)
FreeCAD.getDocument("assembly").getObject("part_rondelle_8m").Placement = App.Placement(App.Vector(50/2 - 4 - 4, 0, -3.5),App.Rotation(App.Vector(0,0,1),0))

# part_rondelle_8m for part_tige_filetee_m8_1000l001
Mesh.insert(u"part_rondelle_8m.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_rondelle_8m001").ShapeColor = (0.30,0.20,0.20)
FreeCAD.getDocument("assembly").getObject("part_rondelle_8m001").Placement = App.Placement(App.Vector(-50/2 + 4 + 4, 0, -3.5),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_8m for part_tige_filetee_m8_1000l
Mesh.insert(u"part_ecrou_8m.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_ecrou_8m").ShapeColor = (0.25,0.25,0.20)
FreeCAD.getDocument("assembly").getObject("part_ecrou_8m").Placement = App.Placement(App.Vector(50/2 - 4 - 4, 0, -11.5),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_8m for part_tige_filetee_m8_1000l001
Mesh.insert(u"part_ecrou_8m.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_ecrou_8m001").ShapeColor = (0.25,0.25,0.20)
FreeCAD.getDocument("assembly").getObject("part_ecrou_8m001").Placement = App.Placement(App.Vector(-50/2 + 4 + 4, 0, -11.5),App.Rotation(App.Vector(0,0,1),0))

# Rank 2
# part_rondelle_8m for part_tige_filetee_m8_1000l
Mesh.insert(u"part_rondelle_8m.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_rondelle_8m002").ShapeColor = (0.30,0.20,0.20)
FreeCAD.getDocument("assembly").getObject("part_rondelle_8m002").Placement = App.Placement(App.Vector(50/2 - 4 - 4, 0, 0),App.Rotation(App.Vector(0,0,1),0))

# part_rondelle_8m for part_tige_filetee_m8_1000l001
Mesh.insert(u"part_rondelle_8m.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_rondelle_8m003").ShapeColor = (0.30,0.20,0.20)
FreeCAD.getDocument("assembly").getObject("part_rondelle_8m003").Placement = App.Placement(App.Vector(-50/2 + 4 + 4, 0, 0),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_8m for part_tige_filetee_m8_1000l
Mesh.insert(u"part_ecrou_8m.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_ecrou_8m002").ShapeColor = (0.25,0.25,0.20)
FreeCAD.getDocument("assembly").getObject("part_ecrou_8m002").Placement = App.Placement(App.Vector(50/2 - 4 - 4, 0, 1.5),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_8m for part_tige_filetee_m8_1000l001
Mesh.insert(u"part_ecrou_8m.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_ecrou_8m003").ShapeColor = (0.25,0.25,0.20)
FreeCAD.getDocument("assembly").getObject("part_ecrou_8m003").Placement = App.Placement(App.Vector(-50/2 + 4 + 4, 0, 1.5),App.Rotation(App.Vector(0,0,1),0))

number_of_steps_electrode = 180

number_of_steps = number_of_steps_electrode * 2 + 2

# insertion part_rondelle_8m for the cathode
for i in range(0, number_of_steps):
    location = (2.5*i + 9.5)
    
    if i < 6:
        Mesh.insert(u"part_rondelle_8m.stl", "assembly")
        FreeCAD.getDocument("assembly").getObject("part_rondelle_8m00" + str(i+4)).Placement = App.Placement(App.Vector(50/2 - 4 - 4, 0, location), App.Rotation(App.Vector(0,0,1), 0))
        FreeCADGui.getDocument("assembly").getObject("part_rondelle_8m00" + str(i+4)).ShapeColor = (0.30,0.20,0.20)
    elif i < 96:
        Mesh.insert(u"part_rondelle_8m.stl", "assembly")
        FreeCAD.getDocument("assembly").getObject("part_rondelle_8m0" + str(i+4)).Placement = App.Placement(App.Vector(50/2 - 4 - 4, 0, location), App.Rotation(App.Vector(0,0,1), 0))
        FreeCADGui.getDocument("assembly").getObject("part_rondelle_8m0" + str(i+4)).ShapeColor = (0.30,0.20,0.20)
    else:
        Mesh.insert(u"part_rondelle_8m.stl", "assembly")
        FreeCAD.getDocument("assembly").getObject("part_rondelle_8m" + str(i+4)).Placement = App.Placement(App.Vector(50/2 - 4 - 4, 0, location), App.Rotation(App.Vector(0,0,1), 0))
        FreeCADGui.getDocument("assembly").getObject("part_rondelle_8m" + str(i+4)).ShapeColor = (0.30,0.20,0.20)
        
# insertion part_rondelle_8m for the anode
for i in range(0, number_of_steps):
    location = (2.5*i + 9.5)
    
    Mesh.insert(u"part_rondelle_8m.stl", "assembly")
    FreeCAD.getDocument("assembly").getObject("part_rondelle_8m" + str(i + number_of_steps + 4)).Placement = App.Placement(App.Vector(-50/2 + 4 + 4, 0, location), App.Rotation(App.Vector(0,0,1), 0))
    FreeCADGui.getDocument("assembly").getObject("part_rondelle_8m" + str(i + number_of_steps +4)).ShapeColor = (0.30,0.20,0.20)

# insertion part_electrode_laser_cutting for the cathode
Mesh.insert(u"part_electrode_laser_cutting.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_electrode_laser_cutting").Placement = App.Placement(App.Vector(0, 0, 11), App.Rotation(App.Vector(0, 0, 1), 0))
FreeCADGui.getDocument("assembly").getObject("part_electrode_laser_cutting").ShapeColor = (0.60,0.40,0.20)

for i in range(0, number_of_steps_electrode):
    location = 5*i + 16
    
    if i < 9:
        Mesh.insert(u"part_electrode_laser_cutting.stl", "assembly")
        FreeCAD.getDocument("assembly").getObject("part_electrode_laser_cutting00" + str(i+1)).Placement = App.Placement(App.Vector(0, 0, location), App.Rotation(App.Vector(0, 0, 1), 0))
        FreeCADGui.getDocument("assembly").getObject("part_electrode_laser_cutting00" + str(i+1)).ShapeColor = (0.60,0.40,0.20)
    elif i < 99:
        Mesh.insert(u"part_electrode_laser_cutting.stl", "assembly")
        FreeCAD.getDocument("assembly").getObject("part_electrode_laser_cutting0" + str(i+1)).Placement = App.Placement(App.Vector(0, 0, location), App.Rotation(App.Vector(0, 0, 1), 0))
        FreeCADGui.getDocument("assembly").getObject("part_electrode_laser_cutting0" + str(i+1)).ShapeColor = (0.60,0.40,0.20)
    else:
        Mesh.insert(u"part_electrode_laser_cutting.stl", "assembly")
        FreeCAD.getDocument("assembly").getObject("part_electrode_laser_cutting" + str(i+1)).Placement = App.Placement(App.Vector(0, 0, location), App.Rotation(App.Vector(0, 0, 1), 0))
        FreeCADGui.getDocument("assembly").getObject("part_electrode_laser_cutting" + str(i+1)).ShapeColor = (0.60,0.40,0.20)

# insertion part_electrode_laser_cutting for the anode
for i in range(0, number_of_steps_electrode):
    location = 5*i + 13.5
    
    Mesh.insert(u"part_electrode_laser_cutting.stl", "assembly")
    FreeCAD.getDocument("assembly").getObject("part_electrode_laser_cutting" + str(i + number_of_steps_electrode + 1)).Placement = App.Placement(App.Vector(0, 0, location), App.Rotation(App.Vector(0, 0, 1), 180))
    FreeCADGui.getDocument("assembly").getObject("part_electrode_laser_cutting" + str(i + number_of_steps_electrode + 1)).ShapeColor = (0.20,0.40,0.60)

setview()

# Generate PNG files
file = 'assembly_v3_'
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
            'exec{(}open{(}"assembly.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_assembly_v1(self):
        print("test_assembly_v1")

        if os.path.exists("assembly_v1.py"):
            os.remove("assembly_v1.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("assembly_v1.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_v1"


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

# part_tank
Mesh.insert(u"part_tank.stl","assembly_v1")
FreeCADGui.getDocument("assembly_v1").getObject("part_tank").ShapeColor = (0.10,0.10,0.10)
FreeCAD.getDocument("assembly_v1").getObject("part_tank").Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),0))
FreeCADGui.getDocument("assembly_v1").getObject("part_tank").Transparency = 80

# part_support_laser_cutting _ 1
Mesh.insert(u"part_support_laser_cutting.stl","assembly_v1")
FreeCADGui.getDocument("assembly_v1").getObject("part_support_laser_cutting").ShapeColor = (1.00,1.00,0.00)
FreeCAD.getDocument("assembly_v1").getObject("part_support_laser_cutting").Placement = App.Placement(App.Vector(0,0,-2),App.Rotation(App.Vector(0,1,0),0))

# part_tige_filetee_m8_1000l for the cathode
Mesh.insert(u"part_tige_filetee_m8_1000l.stl","assembly_v1")
FreeCADGui.getDocument("assembly_v1").getObject("part_tige_filetee_m8_1000l").ShapeColor = (0.50,0.50,0.50)
FreeCAD.getDocument("assembly_v1").getObject("part_tige_filetee_m8_1000l").Placement = App.Placement(App.Vector(50/2 - 4 - 4, 0, -20),App.Rotation(App.Vector(0,0,1),0))

# part_tige_filetee_m8_1000l for the anode
Mesh.insert(u"part_tige_filetee_m8_1000l.stl","assembly_v1")
FreeCADGui.getDocument("assembly_v1").getObject("part_tige_filetee_m8_1000l001").ShapeColor = (0.50,0.50,0.50)
FreeCAD.getDocument("assembly_v1").getObject("part_tige_filetee_m8_1000l001").Placement = App.Placement(App.Vector(-50/2 + 4 + 4, 0, -20),App.Rotation(App.Vector(0,0,1),0))

# Rank 1
# part_rondelle_8m for part_tige_filetee_m8_1000l
Mesh.insert(u"part_rondelle_8m.stl","assembly_v1")
FreeCADGui.getDocument("assembly_v1").getObject("part_rondelle_8m").ShapeColor = (0.30,0.20,0.20)
FreeCAD.getDocument("assembly_v1").getObject("part_rondelle_8m").Placement = App.Placement(App.Vector(50/2 - 4 - 4, 0, -3.5),App.Rotation(App.Vector(0,0,1),0))

# part_rondelle_8m for part_tige_filetee_m8_1000l001
Mesh.insert(u"part_rondelle_8m.stl","assembly_v1")
FreeCADGui.getDocument("assembly_v1").getObject("part_rondelle_8m001").ShapeColor = (0.30,0.20,0.20)
FreeCAD.getDocument("assembly_v1").getObject("part_rondelle_8m001").Placement = App.Placement(App.Vector(-50/2 + 4 + 4, 0, -3.5),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_8m for part_tige_filetee_m8_1000l
Mesh.insert(u"part_ecrou_8m.stl","assembly_v1")
FreeCADGui.getDocument("assembly_v1").getObject("part_ecrou_8m").ShapeColor = (0.25,0.25,0.20)
FreeCAD.getDocument("assembly_v1").getObject("part_ecrou_8m").Placement = App.Placement(App.Vector(50/2 - 4 - 4, 0, -11.5),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_8m for part_tige_filetee_m8_1000l001
Mesh.insert(u"part_ecrou_8m.stl","assembly_v1")
FreeCADGui.getDocument("assembly_v1").getObject("part_ecrou_8m001").ShapeColor = (0.25,0.25,0.20)
FreeCAD.getDocument("assembly_v1").getObject("part_ecrou_8m001").Placement = App.Placement(App.Vector(-50/2 + 4 + 4, 0, -11.5),App.Rotation(App.Vector(0,0,1),0))

# Rank 2
# part_rondelle_8m for part_tige_filetee_m8_1000l
Mesh.insert(u"part_rondelle_8m.stl","assembly_v1")
FreeCADGui.getDocument("assembly_v1").getObject("part_rondelle_8m002").ShapeColor = (0.30,0.20,0.20)
FreeCAD.getDocument("assembly_v1").getObject("part_rondelle_8m002").Placement = App.Placement(App.Vector(50/2 - 4 - 4, 0, 0),App.Rotation(App.Vector(0,0,1),0))

# part_rondelle_8m for part_tige_filetee_m8_1000l001
Mesh.insert(u"part_rondelle_8m.stl","assembly_v1")
FreeCADGui.getDocument("assembly_v1").getObject("part_rondelle_8m003").ShapeColor = (0.30,0.20,0.20)
FreeCAD.getDocument("assembly_v1").getObject("part_rondelle_8m003").Placement = App.Placement(App.Vector(-50/2 + 4 + 4, 0, 0),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_8m for part_tige_filetee_m8_1000l
Mesh.insert(u"part_ecrou_8m.stl","assembly_v1")
FreeCADGui.getDocument("assembly_v1").getObject("part_ecrou_8m002").ShapeColor = (0.25,0.25,0.20)
FreeCAD.getDocument("assembly_v1").getObject("part_ecrou_8m002").Placement = App.Placement(App.Vector(50/2 - 4 - 4, 0, 1.5),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_8m for part_tige_filetee_m8_1000l001
Mesh.insert(u"part_ecrou_8m.stl","assembly_v1")
FreeCADGui.getDocument("assembly_v1").getObject("part_ecrou_8m003").ShapeColor = (0.25,0.25,0.20)
FreeCAD.getDocument("assembly_v1").getObject("part_ecrou_8m003").Placement = App.Placement(App.Vector(-50/2 + 4 + 4, 0, 1.5),App.Rotation(App.Vector(0,0,1),0))

number_of_steps_electrode = 180

number_of_steps = number_of_steps_electrode * 2 + 2

# insertion part_equerre_assemblage_laser_cutting for spacing the electrodes
for i in range(0, number_of_steps):
    location = (2.5*i + 9.5)

    if i < 1:
        Mesh.insert(u"part_equerre_assemblage_laser_cutting.stl","assembly_v1")
        FreeCAD.getDocument("assembly_v1").getObject("part_equerre_assemblage_laser_cutting").Placement = App.Placement(App.Vector(50/2 - 4 - 4, 0, location), App.Rotation(App.Vector(0,0,1), 180))
        FreeCADGui.getDocument("assembly_v1").getObject("part_equerre_assemblage_laser_cutting").ShapeColor = (0.30,0.20,0.20)
    elif 1 <= i < 10:
        Mesh.insert(u"part_equerre_assemblage_laser_cutting.stl","assembly_v1")
        FreeCAD.getDocument("assembly_v1").getObject("part_equerre_assemblage_laser_cutting00" + str(i)).Placement = App.Placement(App.Vector(50/2 - 4 - 4, 0, location), App.Rotation(App.Vector(0,0,1), 180))
        FreeCADGui.getDocument("assembly_v1").getObject("part_equerre_assemblage_laser_cutting00" + str(i)).ShapeColor = (0.30,0.20,0.20)
    elif i < 100:
        Mesh.insert(u"part_equerre_assemblage_laser_cutting.stl","assembly_v1")
        FreeCAD.getDocument("assembly_v1").getObject("part_equerre_assemblage_laser_cutting0" + str(i)).Placement = App.Placement(App.Vector(50/2 - 4 - 4, 0, location), App.Rotation(App.Vector(0,0,1), 180))
        FreeCADGui.getDocument("assembly_v1").getObject("part_equerre_assemblage_laser_cutting0" + str(i)).ShapeColor = (0.30,0.20,0.20)
    else:
        Mesh.insert(u"part_equerre_assemblage_laser_cutting.stl","assembly_v1")
        FreeCAD.getDocument("assembly_v1").getObject("part_equerre_assemblage_laser_cutting" + str(i)).Placement = App.Placement(App.Vector(50/2 - 4 - 4, 0, location), App.Rotation(App.Vector(0,0,1), 180))
        FreeCADGui.getDocument("assembly_v1").getObject("part_equerre_assemblage_laser_cutting" + str(i)).ShapeColor = (0.30,0.20,0.20)

# insertion part_electrode_laser_cutting for the cathode
Mesh.insert(u"part_electrode_laser_cutting.stl","assembly_v1")
FreeCAD.getDocument("assembly_v1").getObject("part_electrode_laser_cutting").Placement = App.Placement(App.Vector(0, 0, 11), App.Rotation(App.Vector(0, 0, 1), 0))
FreeCADGui.getDocument("assembly_v1").getObject("part_electrode_laser_cutting").ShapeColor = (0.60,0.40,0.20)

for i in range(0, number_of_steps_electrode):
    location = 5*i + 16

    if i < 9:
        Mesh.insert(u"part_electrode_laser_cutting.stl","assembly_v1")
        FreeCAD.getDocument("assembly_v1").getObject("part_electrode_laser_cutting00" + str(i+1)).Placement = App.Placement(App.Vector(0, 0, location), App.Rotation(App.Vector(0, 0, 1), 0))
        FreeCADGui.getDocument("assembly_v1").getObject("part_electrode_laser_cutting00" + str(i+1)).ShapeColor = (0.60,0.40,0.20)
    elif i < 99:
        Mesh.insert(u"part_electrode_laser_cutting.stl","assembly_v1")
        FreeCAD.getDocument("assembly_v1").getObject("part_electrode_laser_cutting0" + str(i+1)).Placement = App.Placement(App.Vector(0, 0, location), App.Rotation(App.Vector(0, 0, 1), 0))
        FreeCADGui.getDocument("assembly_v1").getObject("part_electrode_laser_cutting0" + str(i+1)).ShapeColor = (0.60,0.40,0.20)
    else:
        Mesh.insert(u"part_electrode_laser_cutting.stl","assembly_v1")
        FreeCAD.getDocument("assembly_v1").getObject("part_electrode_laser_cutting" + str(i+1)).Placement = App.Placement(App.Vector(0, 0, location), App.Rotation(App.Vector(0, 0, 1), 0))
        FreeCADGui.getDocument("assembly_v1").getObject("part_electrode_laser_cutting" + str(i+1)).ShapeColor = (0.60,0.40,0.20)

# insertion part_electrode_laser_cutting for the anode
for i in range(0, number_of_steps_electrode):
    location = 5*i + 13.5

    Mesh.insert(u"part_electrode_laser_cutting.stl","assembly_v1")
    FreeCAD.getDocument("assembly_v1").getObject("part_electrode_laser_cutting" + str(i + number_of_steps_electrode + 1)).Placement = App.Placement(App.Vector(0, 0, location), App.Rotation(App.Vector(0, 0, 1), 180))
    FreeCADGui.getDocument("assembly_v1").getObject("part_electrode_laser_cutting" + str(i + number_of_steps_electrode + 1)).ShapeColor = (0.20,0.40,0.60)

setview()

# Generate PNG files
file = 'assembly_v1_v3_'
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
            'exec{(}open{(}"assembly_v1.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_assembly_v2(self):
        print("test_assembly_v2")

        if os.path.exists("assembly_v2.py"):
            os.remove("assembly_v2.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("assembly_v2.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_v2"


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

# part_tank
Mesh.insert(u"part_tank.stl","assembly_v2")
FreeCADGui.getDocument("assembly_v2").getObject("part_tank").ShapeColor = (0.10,0.10,0.10)
FreeCAD.getDocument("assembly_v2").getObject("part_tank").Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),0))
FreeCADGui.getDocument("assembly_v2").getObject("part_tank").Transparency = 80

# part_support_laser_cutting _ 1
Mesh.insert(u"part_support_laser_cutting.stl","assembly_v2")
FreeCADGui.getDocument("assembly_v2").getObject("part_support_laser_cutting").ShapeColor = (1.00,1.00,0.00)
FreeCAD.getDocument("assembly_v2").getObject("part_support_laser_cutting").Placement = App.Placement(App.Vector(0,0,-2),App.Rotation(App.Vector(0,1,0),0))

# part_tige_filetee_m8_1000l for the cathode
Mesh.insert(u"part_tige_filetee_m8_1000l.stl","assembly_v2")
FreeCADGui.getDocument("assembly_v2").getObject("part_tige_filetee_m8_1000l").ShapeColor = (0.50,0.50,0.50)
FreeCAD.getDocument("assembly_v2").getObject("part_tige_filetee_m8_1000l").Placement = App.Placement(App.Vector(50/2 - 4 - 4, 0, -20),App.Rotation(App.Vector(0,0,1),0))

# part_tige_filetee_m8_1000l for the anode
Mesh.insert(u"part_tige_filetee_m8_1000l.stl","assembly_v2")
FreeCADGui.getDocument("assembly_v2").getObject("part_tige_filetee_m8_1000l001").ShapeColor = (0.50,0.50,0.50)
FreeCAD.getDocument("assembly_v2").getObject("part_tige_filetee_m8_1000l001").Placement = App.Placement(App.Vector(-50/2 + 4 + 4, 0, -20),App.Rotation(App.Vector(0,0,1),0))

# Rank 1
# part_rondelle_8m for part_tige_filetee_m8_1000l
Mesh.insert(u"part_rondelle_8m.stl","assembly_v2")
FreeCADGui.getDocument("assembly_v2").getObject("part_rondelle_8m").ShapeColor = (0.30,0.20,0.20)
FreeCAD.getDocument("assembly_v2").getObject("part_rondelle_8m").Placement = App.Placement(App.Vector(50/2 - 4 - 4, 0, -3.5),App.Rotation(App.Vector(0,0,1),0))

# part_rondelle_8m for part_tige_filetee_m8_1000l001
Mesh.insert(u"part_rondelle_8m.stl","assembly_v2")
FreeCADGui.getDocument("assembly_v2").getObject("part_rondelle_8m001").ShapeColor = (0.30,0.20,0.20)
FreeCAD.getDocument("assembly_v2").getObject("part_rondelle_8m001").Placement = App.Placement(App.Vector(-50/2 + 4 + 4, 0, -3.5),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_8m for part_tige_filetee_m8_1000l
Mesh.insert(u"part_ecrou_8m.stl","assembly_v2")
FreeCADGui.getDocument("assembly_v2").getObject("part_ecrou_8m").ShapeColor = (0.25,0.25,0.20)
FreeCAD.getDocument("assembly_v2").getObject("part_ecrou_8m").Placement = App.Placement(App.Vector(50/2 - 4 - 4, 0, -11.5),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_8m for part_tige_filetee_m8_1000l001
Mesh.insert(u"part_ecrou_8m.stl","assembly_v2")
FreeCADGui.getDocument("assembly_v2").getObject("part_ecrou_8m001").ShapeColor = (0.25,0.25,0.20)
FreeCAD.getDocument("assembly_v2").getObject("part_ecrou_8m001").Placement = App.Placement(App.Vector(-50/2 + 4 + 4, 0, -11.5),App.Rotation(App.Vector(0,0,1),0))

# Rank 2
# part_rondelle_8m for part_tige_filetee_m8_1000l
Mesh.insert(u"part_rondelle_8m.stl","assembly_v2")
FreeCADGui.getDocument("assembly_v2").getObject("part_rondelle_8m002").ShapeColor = (0.30,0.20,0.20)
FreeCAD.getDocument("assembly_v2").getObject("part_rondelle_8m002").Placement = App.Placement(App.Vector(50/2 - 4 - 4, 0, 0),App.Rotation(App.Vector(0,0,1),0))

# part_rondelle_8m for part_tige_filetee_m8_1000l001
Mesh.insert(u"part_rondelle_8m.stl","assembly_v2")
FreeCADGui.getDocument("assembly_v2").getObject("part_rondelle_8m003").ShapeColor = (0.30,0.20,0.20)
FreeCAD.getDocument("assembly_v2").getObject("part_rondelle_8m003").Placement = App.Placement(App.Vector(-50/2 + 4 + 4, 0, 0),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_8m for part_tige_filetee_m8_1000l
Mesh.insert(u"part_ecrou_8m.stl","assembly_v2")
FreeCADGui.getDocument("assembly_v2").getObject("part_ecrou_8m002").ShapeColor = (0.25,0.25,0.20)
FreeCAD.getDocument("assembly_v2").getObject("part_ecrou_8m002").Placement = App.Placement(App.Vector(50/2 - 4 - 4, 0, 1.5),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_8m for part_tige_filetee_m8_1000l001
Mesh.insert(u"part_ecrou_8m.stl","assembly_v2")
FreeCADGui.getDocument("assembly_v2").getObject("part_ecrou_8m003").ShapeColor = (0.25,0.25,0.20)
FreeCAD.getDocument("assembly_v2").getObject("part_ecrou_8m003").Placement = App.Placement(App.Vector(-50/2 + 4 + 4, 0, 1.5),App.Rotation(App.Vector(0,0,1),0))

number_of_steps_electrode = 180

number_of_steps = number_of_steps_electrode * 2 + 2

# insertion part_equerre_assemblage_laser_cutting_v2 for spacing the electrodes
for i in range(0, number_of_steps):
    location = (2.5*i + 9.5)

    if i < 1:
        Mesh.insert(u"part_equerre_assemblage_laser_cutting_v2.stl","assembly_v2")
        FreeCAD.getDocument("assembly_v2").getObject("part_equerre_assemblage_laser_cutting_v2").Placement = App.Placement(App.Vector(-50/2, -8, location), App.Rotation(App.Vector(0,0,1), 0))
        FreeCADGui.getDocument("assembly_v2").getObject("part_equerre_assemblage_laser_cutting_v2").ShapeColor = (0.30,0.20,0.20)
    elif 1 <= i < 10:
        Mesh.insert(u"part_equerre_assemblage_laser_cutting_v2.stl","assembly_v2")
        FreeCAD.getDocument("assembly_v2").getObject("part_equerre_assemblage_laser_cutting_v200" + str(i)).Placement = App.Placement(App.Vector(-50/2, -8, location), App.Rotation(App.Vector(0,0,1), 0))
        FreeCADGui.getDocument("assembly_v2").getObject("part_equerre_assemblage_laser_cutting_v200" + str(i)).ShapeColor = (0.30,0.20,0.20)
    elif i < 100:
        Mesh.insert(u"part_equerre_assemblage_laser_cutting_v2.stl","assembly_v2")
        FreeCAD.getDocument("assembly_v2").getObject("part_equerre_assemblage_laser_cutting_v20" + str(i)).Placement = App.Placement(App.Vector(-50/2, -8, location), App.Rotation(App.Vector(0,0,1), 0))
        FreeCADGui.getDocument("assembly_v2").getObject("part_equerre_assemblage_laser_cutting_v20" + str(i)).ShapeColor = (0.30,0.20,0.20)
    else:
        Mesh.insert(u"part_equerre_assemblage_laser_cutting_v2.stl","assembly_v2")
        FreeCAD.getDocument("assembly_v2").getObject("part_equerre_assemblage_laser_cutting_v2" + str(i)).Placement = App.Placement(App.Vector(-50/2, -8, location), App.Rotation(App.Vector(0,0,1), 0))
        FreeCADGui.getDocument("assembly_v2").getObject("part_equerre_assemblage_laser_cutting_v2" + str(i)).ShapeColor = (0.30,0.20,0.20)

# insertion part_electrode_laser_cutting for the cathode
Mesh.insert(u"part_electrode_laser_cutting.stl","assembly_v2")
FreeCAD.getDocument("assembly_v2").getObject("part_electrode_laser_cutting").Placement = App.Placement(App.Vector(0, 0, 11), App.Rotation(App.Vector(0, 0, 1), 0))
FreeCADGui.getDocument("assembly_v2").getObject("part_electrode_laser_cutting").ShapeColor = (0.60,0.40,0.20)

for i in range(0, number_of_steps_electrode):
    location = 5*i + 16

    if i < 9:
        Mesh.insert(u"part_electrode_laser_cutting.stl","assembly_v2")
        FreeCAD.getDocument("assembly_v2").getObject("part_electrode_laser_cutting00" + str(i+1)).Placement = App.Placement(App.Vector(0, 0, location), App.Rotation(App.Vector(0, 0, 1), 0))
        FreeCADGui.getDocument("assembly_v2").getObject("part_electrode_laser_cutting00" + str(i+1)).ShapeColor = (0.60,0.40,0.20)
    elif i < 99:
        Mesh.insert(u"part_electrode_laser_cutting.stl","assembly_v2")
        FreeCAD.getDocument("assembly_v2").getObject("part_electrode_laser_cutting0" + str(i+1)).Placement = App.Placement(App.Vector(0, 0, location), App.Rotation(App.Vector(0, 0, 1), 0))
        FreeCADGui.getDocument("assembly_v2").getObject("part_electrode_laser_cutting0" + str(i+1)).ShapeColor = (0.60,0.40,0.20)
    else:
        Mesh.insert(u"part_electrode_laser_cutting.stl","assembly_v2")
        FreeCAD.getDocument("assembly_v2").getObject("part_electrode_laser_cutting" + str(i+1)).Placement = App.Placement(App.Vector(0, 0, location), App.Rotation(App.Vector(0, 0, 1), 0))
        FreeCADGui.getDocument("assembly_v2").getObject("part_electrode_laser_cutting" + str(i+1)).ShapeColor = (0.60,0.40,0.20)

# insertion part_electrode_laser_cutting for the anode
for i in range(0, number_of_steps_electrode):
    location = 5*i + 13.5

    Mesh.insert(u"part_electrode_laser_cutting.stl","assembly_v2")
    FreeCAD.getDocument("assembly_v2").getObject("part_electrode_laser_cutting" + str(i + number_of_steps_electrode + 1)).Placement = App.Placement(App.Vector(0, 0, location), App.Rotation(App.Vector(0, 0, 1), 180))
    FreeCADGui.getDocument("assembly_v2").getObject("part_electrode_laser_cutting" + str(i + number_of_steps_electrode + 1)).ShapeColor = (0.20,0.40,0.60)

setview()

# Generate PNG files
file = 'assembly_v2_v3_'
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
            'exec{(}open{(}"assembly_v2.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')


if __name__ == '__main__':
    unittest.main()
