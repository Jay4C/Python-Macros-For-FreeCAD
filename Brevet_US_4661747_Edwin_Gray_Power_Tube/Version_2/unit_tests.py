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
file = 'part_tank_v2_'
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
file = 'part_tige_filetee_m8_1000l_v2_'
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
file = 'part_vis_metal_m8_50l_v2_'
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
file = 'part_ecrou_8m_v2_'
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
file = 'part_rondelle_8m_v2_'
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
file = 'part_vis_metal_m5_20l_v2_'
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
file = 'part_ecrou_5m_v2_'
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
    # https://www.visseriefixations.fr/rondelles-circlips/rondelles-plates/sans-chanfrein/serie-etroite-z/acier/rondelle-z-acier-zingue-blanc-nfe-25513/rondelle-z-0-5-z-blanc-nfe-25513.html
    def test_part_rondelle_5m(self):
        print("test_part_rondelle_5m")

        if os.path.exists("part_rondelle_5m.py"):
            os.remove("part_rondelle_5m.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_rondelle_5m.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_rondelle_5m"


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

d1 = 5.30
d2 = 10
s = 1

cylinder_1 = Part.makeCylinder(d2/2, s)

cylinder_2 = Part.makeCylinder(d1/2, s)

cylinder_1 = cylinder_1.cut(cylinder_2)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_rondelle_5m").getObject("Shape"))

stl_file = u"part_rondelle_5m.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_rondelle_5m_v2_'
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
            'exec{(}open{(}"part_rondelle_5m.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_part_support(self):
        print("test_part_support")

        if os.path.exists("part_support.py"):
            os.remove("part_support.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_support.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_support"


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

hauteur_maximal = 1.5 + 1.5 + 6

# part_support
part_support = Part.makeCylinder(cote_maximal/2, hauteur_maximal)

# cylinder_1 for passing electrodes
cylinder_1 = Part.makeCylinder(4, hauteur_maximal)

# part_support cut by cylinder_1
part_support = part_support.cut(cylinder_1)

# cylinder_2 for fixing the tank
cylinder_2 = Part.makeCylinder(86/2, 1.5)

# part_support cut by cylinder_2
cylinder_2_vector = FreeCAD.Vector(0, 0, hauteur_maximal - 1.5)
cylinder_2.translate(cylinder_2_vector)
part_support = part_support.cut(cylinder_2)

# cylinder_3
cylinder_3 = Part.makeCylinder(cote_maximal/2 - 1, hauteur_maximal - 1.5 - 1.5)

# part_support cut by cylinder_3
part_support = part_support.cut(cylinder_3)

# holes for reducing the cost
degre = 15
for i in range(int(360/degre)):
    hole = Part.makeCylinder(4, hauteur_maximal)
    radius = 86/2 + 8 + 4
    alpha=(i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole.translate(hole_vector)
    part_support = part_support.cut(hole)

# Cut the holes for the screws fixing the assembly plant
degre = 15
for i in range(int(360/degre)):
    for j in range(0, 5):
        axe_y = FreeCAD.Vector(0, 1, 0)
        axe_z = FreeCAD.Vector(0, 0, 1)
        radius_screw = cote_maximal/2 - 5
        alpha = (i*degre*math.pi)/180
        vector = FreeCAD.Vector(radius_screw*math.cos(alpha), radius_screw*math.sin(alpha), j*0.75)        
        cylinder = Part.makeCylinder(3, 10, vector, axe_y)
        cylinder.rotate(vector, axe_z, alpha*(360/(2*math.pi)) - 90)
        part_support = part_support.cut(cylinder)

Part.show(part_support)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_support").getObject("Shape"))

stl_file = u"part_support.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_support_v2_'
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
            'exec{(}open{(}"part_support.py"{)}.read{(}{)}{)}'
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

# cylinder_1 for passing electrodes
cylinder_1 = Part.makeCylinder(4, hauteur_maximal)

# part_support_laser_cutting cut by cylinder_1
part_support_laser_cutting = part_support_laser_cutting.cut(cylinder_1)

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
file = 'part_support_laser_cutting_v2_'
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
FreeCAD.getDocument("assembly").getObject("part_tank").Placement = App.Placement(App.Vector(0,0,20),App.Rotation(App.Vector(0,0,1),0))
FreeCADGui.getDocument("assembly").getObject("part_tank").Transparency = 80

# part_support_laser_cutting _ 1
Mesh.insert(u"part_support_laser_cutting.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_support_laser_cutting").ShapeColor = (1.00,1.00,0.00)
FreeCAD.getDocument("assembly").getObject("part_support_laser_cutting").Placement = App.Placement(App.Vector(0,0,18),App.Rotation(App.Vector(0,1,0),0))

# part_support_laser_cutting _ 2
Mesh.insert(u"part_support_laser_cutting.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_support_laser_cutting001").ShapeColor = (1.00,1.00,0.00)
FreeCAD.getDocument("assembly").getObject("part_support_laser_cutting001").Placement = App.Placement(App.Vector(0,0,1000 - 20),App.Rotation(App.Vector(0,1,0),0))

# part_vis_metal_m8_50l
Mesh.insert(u"part_vis_metal_m8_50l.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_vis_metal_m8_50l").ShapeColor = (0.60,0.60,0.10)
FreeCAD.getDocument("assembly").getObject("part_vis_metal_m8_50l").Placement = App.Placement(App.Vector(0,0,1000 - 21 - 29 - 5.3),App.Rotation(App.Vector(0,1,0),0))

# part_tige_filetee_m8_1000l for electrode
Mesh.insert(u"part_tige_filetee_m8_1000l.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_tige_filetee_m8_1000l").ShapeColor = (0.50,0.50,0.50)
FreeCAD.getDocument("assembly").getObject("part_tige_filetee_m8_1000l").Placement = App.Placement(App.Vector(0,0,- 21 - 29 - 5.3 - 3),App.Rotation(App.Vector(0,0,1),0))

# part_tige_filetee_m8_1000l for fixing the assembly _ 1
Mesh.insert(u"part_tige_filetee_m8_1000l.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_tige_filetee_m8_1000l001").ShapeColor = (0.50,0.50,0.50)
FreeCAD.getDocument("assembly").getObject("part_tige_filetee_m8_1000l001").Placement = App.Placement(App.Vector(86/2 + 8 + 4,0,0),App.Rotation(App.Vector(0,0,1),0))

# part_tige_filetee_m8_1000l for fixing the assembly _ 2
Mesh.insert(u"part_tige_filetee_m8_1000l.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_tige_filetee_m8_1000l002").ShapeColor = (0.50,0.50,0.50)
FreeCAD.getDocument("assembly").getObject("part_tige_filetee_m8_1000l002").Placement = App.Placement(App.Vector(-86/2 - 8 - 4,0,0),App.Rotation(App.Vector(0,0,1),0))

# Rank 1
# part_rondelle_8m for part_tige_filetee_m8_1000l
Mesh.insert(u"part_rondelle_8m.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_rondelle_8m").ShapeColor = (0.30,0.20,0.20)
FreeCAD.getDocument("assembly").getObject("part_rondelle_8m").Placement = App.Placement(App.Vector(0,0,16.5),App.Rotation(App.Vector(0,0,1),0))

# part_rondelle_8m for part_tige_filetee_m8_1000l001
Mesh.insert(u"part_rondelle_8m.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_rondelle_8m001").ShapeColor = (0.30,0.20,0.20)
FreeCAD.getDocument("assembly").getObject("part_rondelle_8m001").Placement = App.Placement(App.Vector(86/2 + 8 + 4,0,16.5),App.Rotation(App.Vector(0,0,1),0))

# part_rondelle_8m for part_tige_filetee_m8_1000l002
Mesh.insert(u"part_rondelle_8m.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_rondelle_8m002").ShapeColor = (0.30,0.20,0.20)
FreeCAD.getDocument("assembly").getObject("part_rondelle_8m002").Placement = App.Placement(App.Vector(-86/2 - 8 - 4,0,16.5),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_8m for part_tige_filetee_m8_1000l
Mesh.insert(u"part_ecrou_8m.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_ecrou_8m").ShapeColor = (0.25,0.25,0.20)
FreeCAD.getDocument("assembly").getObject("part_ecrou_8m").Placement = App.Placement(App.Vector(0,0,8.5),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_8m for part_tige_filetee_m8_1000l001
Mesh.insert(u"part_ecrou_8m.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_ecrou_8m001").ShapeColor = (0.25,0.25,0.20)
FreeCAD.getDocument("assembly").getObject("part_ecrou_8m001").Placement = App.Placement(App.Vector(86/2 + 8 + 4,0,8.5),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_8m for part_tige_filetee_m8_1000l002
Mesh.insert(u"part_ecrou_8m.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_ecrou_8m002").ShapeColor = (0.25,0.25,0.20)
FreeCAD.getDocument("assembly").getObject("part_ecrou_8m002").Placement = App.Placement(App.Vector(-86/2 - 8 - 4,0,8.5),App.Rotation(App.Vector(0,0,1),0))

# Rank 2
# part_rondelle_8m for part_tige_filetee_m8_1000l
Mesh.insert(u"part_rondelle_8m.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_rondelle_8m003").ShapeColor = (0.30,0.20,0.20)
FreeCAD.getDocument("assembly").getObject("part_rondelle_8m003").Placement = App.Placement(App.Vector(0,0,20),App.Rotation(App.Vector(0,0,1),0))

# part_rondelle_8m for part_tige_filetee_m8_1000l001
Mesh.insert(u"part_rondelle_8m.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_rondelle_8m004").ShapeColor = (0.30,0.20,0.20)
FreeCAD.getDocument("assembly").getObject("part_rondelle_8m004").Placement = App.Placement(App.Vector(86/2 + 8 + 4,0,20),App.Rotation(App.Vector(0,0,1),0))

# part_rondelle_8m for part_tige_filetee_m8_1000l002
Mesh.insert(u"part_rondelle_8m.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_rondelle_8m005").ShapeColor = (0.30,0.20,0.20)
FreeCAD.getDocument("assembly").getObject("part_rondelle_8m005").Placement = App.Placement(App.Vector(-86/2 - 8 - 4,0,20),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_8m for part_tige_filetee_m8_1000l
Mesh.insert(u"part_ecrou_8m.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_ecrou_8m003").ShapeColor = (0.25,0.25,0.20)
FreeCAD.getDocument("assembly").getObject("part_ecrou_8m003").Placement = App.Placement(App.Vector(0,0,21.5),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_8m for part_tige_filetee_m8_1000l001
Mesh.insert(u"part_ecrou_8m.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_ecrou_8m004").ShapeColor = (0.25,0.25,0.20)
FreeCAD.getDocument("assembly").getObject("part_ecrou_8m004").Placement = App.Placement(App.Vector(86/2 + 8 + 4,0,21.5),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_8m for part_tige_filetee_m8_1000l002
Mesh.insert(u"part_ecrou_8m.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_ecrou_8m005").ShapeColor = (0.25,0.25,0.20)
FreeCAD.getDocument("assembly").getObject("part_ecrou_8m005").Placement = App.Placement(App.Vector(-86/2 - 8 - 4,0,21.5),App.Rotation(App.Vector(0,0,1),0))

# Rank 3
# part_rondelle_8m for part_tige_filetee_m8_1000l
Mesh.insert(u"part_rondelle_8m.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_rondelle_8m006").ShapeColor = (0.30,0.20,0.20)
FreeCAD.getDocument("assembly").getObject("part_rondelle_8m006").Placement = App.Placement(App.Vector(0,0,1000 - 21.5),App.Rotation(App.Vector(0,0,1),0))

# part_rondelle_8m for part_tige_filetee_m8_1000l001
Mesh.insert(u"part_rondelle_8m.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_rondelle_8m007").ShapeColor = (0.30,0.20,0.20)
FreeCAD.getDocument("assembly").getObject("part_rondelle_8m007").Placement = App.Placement(App.Vector(86/2 + 8 + 4,0,1000 - 21.5),App.Rotation(App.Vector(0,0,1),0))

# part_rondelle_8m for part_tige_filetee_m8_1000l002
Mesh.insert(u"part_rondelle_8m.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_rondelle_8m008").ShapeColor = (0.30,0.20,0.20)
FreeCAD.getDocument("assembly").getObject("part_rondelle_8m008").Placement = App.Placement(App.Vector(-86/2 - 8 - 4,0,1000 - 21.5),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_8m for part_tige_filetee_m8_1000l
Mesh.insert(u"part_ecrou_8m.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_ecrou_8m006").ShapeColor = (0.25,0.25,0.20)
FreeCAD.getDocument("assembly").getObject("part_ecrou_8m006").Placement = App.Placement(App.Vector(0,0,1000 - 21.5 - 8),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_8m for part_tige_filetee_m8_1000l001
Mesh.insert(u"part_ecrou_8m.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_ecrou_8m007").ShapeColor = (0.25,0.25,0.20)
FreeCAD.getDocument("assembly").getObject("part_ecrou_8m007").Placement = App.Placement(App.Vector(86/2 + 8 + 4,0,1000 - 21.5 - 8),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_8m for part_tige_filetee_m8_1000l002
Mesh.insert(u"part_ecrou_8m.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_ecrou_8m008").ShapeColor = (0.25,0.25,0.20)
FreeCAD.getDocument("assembly").getObject("part_ecrou_8m008").Placement = App.Placement(App.Vector(-86/2 - 8 - 4,0,1000 - 21.5 - 8),App.Rotation(App.Vector(0,0,1),0))

# Rank 4
# part_rondelle_8m for part_tige_filetee_m8_1000l
Mesh.insert(u"part_rondelle_8m.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_rondelle_8m009").ShapeColor = (0.30,0.20,0.20)
FreeCAD.getDocument("assembly").getObject("part_rondelle_8m009").Placement = App.Placement(App.Vector(0,0,1000 - 21 + 3),App.Rotation(App.Vector(0,0,1),0))

# part_rondelle_8m for part_tige_filetee_m8_1000l001
Mesh.insert(u"part_rondelle_8m.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_rondelle_8m010").ShapeColor = (0.30,0.20,0.20)
FreeCAD.getDocument("assembly").getObject("part_rondelle_8m010").Placement = App.Placement(App.Vector(86/2 + 8 + 4,0,1000 - 21 + 3),App.Rotation(App.Vector(0,0,1),0))

# part_rondelle_8m for part_tige_filetee_m8_1000l002
Mesh.insert(u"part_rondelle_8m.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_rondelle_8m011").ShapeColor = (0.30,0.20,0.20)
FreeCAD.getDocument("assembly").getObject("part_rondelle_8m011").Placement = App.Placement(App.Vector(-86/2 - 8 - 4,0,1000 - 21 + 3),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_8m for part_tige_filetee_m8_1000l
Mesh.insert(u"part_ecrou_8m.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_ecrou_8m009").ShapeColor = (0.25,0.25,0.20)
FreeCAD.getDocument("assembly").getObject("part_ecrou_8m009").Placement = App.Placement(App.Vector(0,0,1000 - 21 + 3 + 1.5),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_8m for part_tige_filetee_m8_1000l001
Mesh.insert(u"part_ecrou_8m.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_ecrou_8m010").ShapeColor = (0.25,0.25,0.20)
FreeCAD.getDocument("assembly").getObject("part_ecrou_8m010").Placement = App.Placement(App.Vector(86/2 + 8 + 4,0,1000 - 21 + 3 + 1.5),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_8m for part_tige_filetee_m8_1000l002
Mesh.insert(u"part_ecrou_8m.stl","assembly")
FreeCADGui.getDocument("assembly").getObject("part_ecrou_8m011").ShapeColor = (0.25,0.25,0.20)
FreeCAD.getDocument("assembly").getObject("part_ecrou_8m011").Placement = App.Placement(App.Vector(-86/2 - 8 - 4,0,1000 - 21 + 3 + 1.5),App.Rotation(App.Vector(0,0,1),0))

setview()

# Export assembly
__objs__=[]
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_8m008"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_tank"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_8m011"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_8m"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_tige_filetee_m8_1000l002"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_ecrou_8m005"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_ecrou_8m007"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_8m010"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_ecrou_8m003"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_ecrou_8m006"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_8m005"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_8m004"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_vis_metal_m8_50l"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_ecrou_8m004"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_8m009"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_ecrou_8m010"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_ecrou_8m009"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_support_laser_cutting001"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_8m007"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_8m003"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_ecrou_8m008"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_tige_filetee_m8_1000l"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_ecrou_8m001"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_8m006"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_tige_filetee_m8_1000l001"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_ecrou_8m002"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_8m002"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_support_laser_cutting"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rondelle_8m001"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_ecrou_8m"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_ecrou_8m011"))

Mesh.export(__objs__,u"assembly.stl")

del __objs__

# Generate PNG files
file = 'assembly_v2_'
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
    def test_assembly_plant(self):
        print("test_assembly_plant")

        if os.path.exists("assembly_plant.py"):
            os.remove("assembly_plant.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("assembly_plant.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_plant"


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

cote_maximal = 2 + 8 + 8 + 8 + 86 + 8 + 8 + 8 + 2

# assembly
Mesh.insert(u"assembly.stl","assembly_plant")
FreeCADGui.getDocument("assembly_plant").getObject("assembly").ShapeColor = (0.10,0.10,0.10)
FreeCAD.getDocument("assembly_plant").getObject("assembly").Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),90))

Mesh.insert(u"assembly.stl","assembly_plant")
FreeCADGui.getDocument("assembly_plant").getObject("assembly001").ShapeColor = (0.0,0.10,0.10)
FreeCAD.getDocument("assembly_plant").getObject("assembly001").Placement = App.Placement(App.Vector(cote_maximal + 1 + 5 + 1,0,0),App.Rotation(App.Vector(0,0,1),90))

setview()

# Generate PNG files
file = 'assembly_plant_v2_'
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
            'exec{(}open{(}"assembly_plant.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')


if __name__ == '__main__':
    unittest.main()
