import os
import time
import unittest
import pywinauto.mouse
import pywinauto.keyboard

# https://patents.google.com/patent/US6362718B1/en?oq=US6362718


class UnitTestsPatentUS6362718B1MotionlessElectromagneticGeneratorForPartsForPermanentMagnets(unittest.TestCase):
    # ok
    # https://www.magnosphere.fr/ferrite/anneaux-aimantes/anneau-40-0-x-20-0-x-10-0-mm-y30-ferrite-adherence-2-kg/a-1151
    def test_part_permanent_magnet_40mm_20mm_10mm_y30(self):
        print("test_part_permanent_magnet_40mm_20mm_10mm_y30")

        if os.path.exists("part_permanent_magnet_40mm_20mm_10mm_y30.py"):
            os.remove("part_permanent_magnet_40mm_20mm_10mm_y30.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_permanent_magnet_40mm_20mm_10mm_y30.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_permanent_magnet_40mm_20mm_10mm_y30"


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

De = 40
Di = 20
h = 10

cylinder_1 = Part.makeCylinder(De/2, h)

# Cut cylinder_1 by cylinder_2
cylinder_2 = Part.makeCylinder(Di/2, h)
cylinder_1 = cylinder_1.cut(cylinder_2)

Part.show(cylinder_1)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_permanent_magnet_40mm_20mm_10mm_y30").getObject("Shape"))

stl_file = u"part_permanent_magnet_40mm_20mm_10mm_y30.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_permanent_magnet_40_20_10_y30_'
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
            'exec{(}open{(}"part_permanent_magnet_40mm_20mm_10mm_y30.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.magnosphere.fr/aimants-neodyme-puissants/aimants-anneaux-neodyme-anneau-magnetique/anneau-magnetique-20-10-x-6-mm-neodyme-n44-niquel-force-7-kg/a-1887
    def test_part_permanent_magnet_20mm_10mm_6mm(self):
        print("test_part_permanent_magnet_20mm_10mm_6mm")

        if os.path.exists("part_permanent_magnet_20mm_10mm_6mm.py"):
            os.remove("part_permanent_magnet_20mm_10mm_6mm.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_permanent_magnet_20mm_10mm_6mm.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_permanent_magnet_20mm_10mm_6mm"


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

De = 20
Di = 10
h = 6

cylinder_1 = Part.makeCylinder(De/2, h)

# Cut cylinder_1 by cylinder_2
cylinder_2 = Part.makeCylinder(Di/2, h)
cylinder_1 = cylinder_1.cut(cylinder_2)

Part.show(cylinder_1)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_permanent_magnet_20mm_10mm_6mm").getObject("Shape"))

stl_file = u"part_permanent_magnet_20mm_10mm_6mm.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_permanent_magnet_20_10_6_'
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
            'exec{(}open{(}"part_permanent_magnet_20mm_10mm_6mm.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.magnosphere.fr/aimants-neodyme-puissants/aimants-anneaux-neodyme-anneau-magnetique/anneau-magnetique-15-10-x-2-mm-neodyme-n40-niquel-force-800g/a-1883
    def test_part_permanent_magnet_15mm_10mm_2mm(self):
        print("test_part_permanent_magnet_15mm_10mm_2mm")

        if os.path.exists("part_permanent_magnet_15mm_10mm_2mm.py"):
            os.remove("part_permanent_magnet_15mm_10mm_2mm.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_permanent_magnet_15mm_10mm_2mm.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_permanent_magnet_15mm_10mm_2mm"


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

De = 15
Di = 10
h = 2

cylinder_1 = Part.makeCylinder(De/2, h)

# Cut cylinder_1 by cylinder_2
cylinder_2 = Part.makeCylinder(Di/2, h)
cylinder_1 = cylinder_1.cut(cylinder_2)

Part.show(cylinder_1)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_permanent_magnet_15mm_10mm_2mm").getObject("Shape"))

stl_file = u"part_permanent_magnet_15mm_10mm_2mm.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_permanent_magnet_15_10_2_'
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
            'exec{(}open{(}"part_permanent_magnet_15mm_10mm_2mm.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.magnosphere.fr/aimants-en-ferrite/aimants-disques-ferrite/disque-magnetique-8-x-2mm-ferrite-y30-sans-plaquage-force-150g/a-1869
    def test_part_permanent_magnet_ferrite_y30_8mm_2mm(self):
        print("test_part_permanent_magnet_ferrite_y30_8mm_2mm")

        if os.path.exists("part_permanent_magnet_ferrite_y30_8mm_2mm.py"):
            os.remove("part_permanent_magnet_ferrite_y30_8mm_2mm.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_permanent_magnet_ferrite_y30_8mm_2mm.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_permanent_magnet_ferrite_y30_8mm_2mm"


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

De = 8
h = 2

cylinder_1 = Part.makeCylinder(De/2, h)

Part.show(cylinder_1)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_permanent_magnet_ferrite_y30_8mm_2mm").getObject("Shape"))

stl_file = u"part_permanent_magnet_ferrite_y30_8mm_2mm.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_permanent_magnet_ferrite_y30_8_2_'
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
            'exec{(}open{(}"part_permanent_magnet_ferrite_y30_8mm_2mm.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.magnosphere.fr/aimants-neodyme-puissants/disques-magnetiques-neodyme/disques-magnetiques-neodyme-1mm-10mm/aimant-disque-8-x-3mm-neodyme-n40-nickele-force-1-5-kg/a-1769
    def test_part_permanent_magnet_neodyme_n40_8mm_3mm(self):
        print("test_part_permanent_magnet_neodyme_n40_8mm_3mm")

        if os.path.exists("part_permanent_magnet_neodyme_n40_8mm_3mm.py"):
            os.remove("part_permanent_magnet_neodyme_n40_8mm_3mm.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_permanent_magnet_neodyme_n40_8mm_3mm.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_permanent_magnet_neodyme_n40_8mm_3mm"


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

De = 8
h = 3

cylinder_1 = Part.makeCylinder(De/2, h)

Part.show(cylinder_1)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_permanent_magnet_neodyme_n40_8mm_3mm").getObject("Shape"))

stl_file = u"part_permanent_magnet_neodyme_n40_8mm_3mm.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_permanent_magnet_neodyme_n40_8_3_'
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
            'exec{(}open{(}"part_permanent_magnet_neodyme_n40_8mm_3mm.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.magnosphere.fr/aimants-en-neodyme/cylindres-magnetiques-neodyme-cylindre-magnetique/cylindre-magnetique-10-x-40-mm-neodyme-n40-nickele-force-4-5-kg/a-2119
    def test_part_permanent_magnet_neodyme_n40_10mm_40mm(self):
        print("test_part_permanent_magnet_neodyme_n40_10mm_40mm")

        if os.path.exists("part_permanent_magnet_neodyme_n40_10mm_40mm.py"):
            os.remove("part_permanent_magnet_neodyme_n40_10mm_40mm.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_permanent_magnet_neodyme_n40_10mm_40mm.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_permanent_magnet_neodyme_n40_10mm_40mm"


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

# EPS = tolerance to use to cut the parts
EPS = 0.30
EPS_C = EPS * (-0.5)

De = 10
h = 40

cylinder_1 = Part.makeCylinder(De/2, h)

Part.show(cylinder_1)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_permanent_magnet_neodyme_n40_10mm_40mm").getObject("Shape"))

stl_file = u"part_permanent_magnet_neodyme_n40_10mm_40mm.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_permanent_magnet_neodyme_n40_10_40_'
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
            'exec{(}open{(}"part_permanent_magnet_neodyme_n40_10mm_40mm.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')


class UnitTestsPatentUS6362718B1MotionlessElectromagneticGeneratorForPartsForFixations(unittest.TestCase):
    # ok
    # https://www.visseriefixations.fr/ecrous/ecrous-hexagonaux/ecrou-hexagonal-hu/ecrou-hu-acier-brut-din-934/ecrou-hu-acier-brut-classe-8-din-934/ecrou-hu-m10-brut-din-934.html
    def test_part_ecrou_10m(self):
        print("test_part_ecrou_10m")

        if os.path.exists("part_ecrou_10m.py"):
            os.remove("part_ecrou_10m.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_ecrou_10m.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_ecrou_10m"


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

d1 = 10
e = 18.9
h = 8

cylinder_1 = Part.makeCylinder(e/2, h)

cylinder_2 = Part.makeCylinder(d1/2, h)

cylinder_1 = cylinder_1.cut(cylinder_2)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_ecrou_10m").getObject("Shape"))

stl_file = u"part_ecrou_10m.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_ecrou_10m_'
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
            'exec{(}open{(}"part_ecrou_10m.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.visseriefixations.fr/rondelles-circlips/rondelles-plates/sans-chanfrein/serie-etroite-z/acier/rondelle-z-acier-zingue-blanc-nfe-25513/rondelle-z-0-10-z-blanc-nfe-25513.html
    def test_part_rondelle_10m(self):
        print("test_part_rondelle_10m")

        if os.path.exists("part_rondelle_10m.py"):
            os.remove("part_rondelle_10m.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_rondelle_10m.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_rondelle_10m"


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

d1 = 10.5
d2 = 20
s = 2

cylinder_1 = Part.makeCylinder(d2/2, s)

cylinder_2 = Part.makeCylinder(d1/2, s)

cylinder_1 = cylinder_1.cut(cylinder_2)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_rondelle_10m").getObject("Shape"))

stl_file = u"part_rondelle_10m.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_rondelle_10m_'
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
            'exec{(}open{(}"part_rondelle_10m.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.visseriefixations.fr/vis-a-tete-hexagonale/vis-a-tete-hexagonale-standard/acier-8-8-noir/th-acier-8-8-noir-filetage-total-din-933/th-m10x100-acier-8-8-noir-ef-din-933.html
    def test_part_vis_metal_m10_100l(self):
        print("test_part_vis_metal_m10_100l")

        if os.path.exists("part_vis_metal_m10_100l.py"):
            os.remove("part_vis_metal_m10_100l.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_vis_metal_m10_100l.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_vis_metal_m10_100l"


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

d1 = 10
L = 100
k = 6.4
e = 18.9

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

__objs__.append(FreeCAD.getDocument("part_vis_metal_m10_100l").getObject("Shape"))

stl_file = u"part_vis_metal_m10_100l.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_vis_metal_m10_100l_'
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
            'exec{(}open{(}"part_vis_metal_m10_100l.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.commentfer.fr/acier-sur-mesure/2239-8441-fer-carre-acier-sur-mesure.html#/586-section-25_x_25_mm
    def test_part_steel_box_for_core(self):
        print("test_part_steel_box_for_core")

        if os.path.exists("part_steel_box_for_core.py"):
            os.remove("part_steel_box_for_core.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_steel_box_for_core.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_steel_box_for_core"


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

# part_steel_box_for_core
h = 25
l = 25
L = 200
part_steel_box_for_core = Part.makeBox(L, h, l)

# Cut part_steel_box_for_core by cylinder_1
cylinder_1 = Part.makeCylinder(10/2, h)
# translation cylinder_1 for the first hole
cylinder_1_vector = FreeCAD.Vector(h, h/2, 0)
cylinder_1.translate(cylinder_1_vector)
part_steel_box_for_core = part_steel_box_for_core.cut(cylinder_1)
# translation cylinder_1 for the second hole
cylinder_1_vector = FreeCAD.Vector((L - 2*h)/2, 0, 0)
cylinder_1.translate(cylinder_1_vector)
part_steel_box_for_core = part_steel_box_for_core.cut(cylinder_1)
# translation cylinder_1 for the third hole
cylinder_1_vector = FreeCAD.Vector((L - 2*h)/2, 0, 0)
cylinder_1.translate(cylinder_1_vector)
part_steel_box_for_core = part_steel_box_for_core.cut(cylinder_1)

Part.show(part_steel_box_for_core)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_steel_box_for_core").getObject("Shape"))

stl_file = u"part_steel_box_for_core.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_steel_box_for_core_'
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
            'exec{(}open{(}"part_steel_box_for_core.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.commentfer.fr/acier-sur-mesure/2239-8436-fer-carre-acier-sur-mesure.html#/578-section-10_x_10_mm
    def test_part_steel_box_for_core_10mm_10mm_200mm(self):
        print("test_part_steel_box_for_core_10mm_10mm_200mm")

        if os.path.exists("part_steel_box_for_core_10mm_10mm_200mm.py"):
            os.remove("part_steel_box_for_core_10mm_10mm_200mm.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_steel_box_for_core_10mm_10mm_200mm.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_steel_box_for_core_10mm_10mm_200mm"


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

# part_steel_box_for_core_10mm_10mm_200mm
h = 10
l = 10
L = 200
part_steel_box_for_core_10mm_10mm_200mm = Part.makeBox(L, h, l)

Part.show(part_steel_box_for_core_10mm_10mm_200mm)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_steel_box_for_core_10mm_10mm_200mm").getObject("Shape"))

stl_file = u"part_steel_box_for_core_10mm_10mm_200mm.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_steel_box_for_core_'
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
            'exec{(}open{(}"part_steel_box_for_core_10mm_10mm_200mm.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.commentfer.fr/acier-sur-mesure/2239-8435-fer-carre-acier-sur-mesure.html#/577-section-8_x_8_mm
    def test_part_steel_box_for_core_8mm_8mm_200mm(self):
        print("test_part_steel_box_for_core_8mm_8mm_200mm")

        if os.path.exists("part_steel_box_for_core_8mm_8mm_200mm.py"):
            os.remove("part_steel_box_for_core_8mm_8mm_200mm.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_steel_box_for_core_8mm_8mm_200mm.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_steel_box_for_core_8mm_8mm_200mm"


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

# part_steel_box_for_core_8mm_8mm_200mm
h = 8
l = 8
L = 200
part_steel_box_for_core_8mm_8mm_200mm = Part.makeBox(L, h, l)

Part.show(part_steel_box_for_core_8mm_8mm_200mm)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_steel_box_for_core_8mm_8mm_200mm").getObject("Shape"))

stl_file = u"part_steel_box_for_core_8mm_8mm_200mm.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_steel_box_for_core_8_8_200_'
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
            'exec{(}open{(}"part_steel_box_for_core_8mm_8mm_200mm.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # 3D printing
    def test_part_steel_box_for_core_v2(self):
        print("test_part_steel_box_for_core_v2")

        if os.path.exists("part_steel_box_for_core_v2.py"):
            os.remove("part_steel_box_for_core_v2.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_steel_box_for_core_v2.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_steel_box_for_core_v2"


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

# part_steel_box_for_core_v2
l = 2.2
L = 100
D_percage = 11
h = D_percage + 2*2
e_percage = 2.2
part_steel_box_for_core_v2 = Part.makeBox(L, h, l)

# Cut part_steel_box_for_core_v2 by cylinder_1
nombre_percage = round(L/(D_percage + e_percage))
for i in range(0, nombre_percage + 1):
    cylinder_1 = Part.makeCylinder(D_percage/2, l)
    cylinder_1_vector = FreeCAD.Vector((D_percage + e_percage)*i, h/2, 0)
    cylinder_1.translate(cylinder_1_vector)
    part_steel_box_for_core_v2 = part_steel_box_for_core_v2.cut(cylinder_1)

Part.show(part_steel_box_for_core_v2)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_steel_box_for_core_v2").getObject("Shape"))

stl_file = u"part_steel_box_for_core_v2.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_steel_box_for_core_v2_'
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
            'exec{(}open{(}"part_steel_box_for_core_v2.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')


class UnitTestsPatentUS6362718B1MotionlessElectromagneticGeneratorForPartsForInputCoils(unittest.TestCase):
    # ok
    # 3D printing
    def test_part_input_coil_without_windings(self):
        print('test_part_input_coil_without_windings')

        if os.path.exists("part_input_coil_without_windings.py"):
            os.remove("part_input_coil_without_windings.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_input_coil_without_windings.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh, math

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_input_coil_without_windings"


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

L_vis_10m = 100
h_tube = 25
h_ecrou_10m = 10
s_rondelle_10m = 2
D = 60

h_coil = (L_vis_10m - h_tube*2 - s_rondelle_10m*2 - h_ecrou_10m - 5)/2

cylinder_1 = Part.makeCylinder(D/2, h_coil)

cylinder_3 = Part.makeCylinder(D/2, h_coil - 2*3)

radius_box = math.sqrt(math.pow(h_tube/2,2) + math.pow(h_tube/2,2)) + 1
cylinder_4 = Part.makeCylinder(radius_box, h_coil - 2*3)

# cylinder_3 cut by cylinder_4
cylinder_3 = cylinder_3.cut(cylinder_4)

# cylinder_1 cut by cylinder_3
cylinder_3_vector = FreeCAD.Vector(0, 0, 3)
cylinder_3.translate(cylinder_3_vector)
cylinder_1 = cylinder_1.cut(cylinder_3)

# cylinder_1 cut by box_1
box_1 = Part.makeBox(h_tube, h_tube, h_coil)
box_1_vector = FreeCAD.Vector(-h_tube/2, -h_tube/2, 0)
box_1.translate(box_1_vector)
cylinder_1 = cylinder_1.cut(box_1)

# cylinder_1 cut by cylinder_5 in several times
degre = 30
for i in range(int(360/degre)):
    radius = h_tube/2 + h_tube/7
    alpha=(i*degre*math.pi)/180
    cylinder_5_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    cylinder_5 = Part.makeCylinder(5/2, h_coil)
    cylinder_5.translate(cylinder_5_vector)
    cylinder_1 = cylinder_1.cut(cylinder_5)

# cylinder_1 cut by cylinder_5 in several times
degre = 30
for i in range(int(360/degre)):
    radius = h_tube/2 + h_tube/7 + h_tube/3
    alpha=(i*degre*math.pi)/180
    cylinder_5_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    cylinder_5 = Part.makeCylinder(5/2, h_coil)
    cylinder_5.translate(cylinder_5_vector)
    cylinder_1 = cylinder_1.cut(cylinder_5)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_input_coil_without_windings").getObject("Shape"))

stl_file = u"part_input_coil_without_windings.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_input_coil_without_windings_'
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
            'exec{(}open{(}"part_input_coil_without_windings.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # 3D printing
    def test_part_input_coil_without_windings_v2(self):
        print('test_part_input_coil_without_windings_v2')

        if os.path.exists("part_input_coil_without_windings_v2.py"):
            os.remove("part_input_coil_without_windings_v2.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_input_coil_without_windings_v2.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh, math

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_input_coil_without_windings_v2"


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

L_vis_10m = 100
h = 25
l = 2.2
h_ecrou_10m = 10
s_rondelle_10m = 2
D = 60

h_coil = (L_vis_10m - h*2 - s_rondelle_10m*2 - h_ecrou_10m - 5)/2

cylinder_1 = Part.makeCylinder(D/2, h_coil)

cylinder_3 = Part.makeCylinder(D/2, h_coil - 2*3)

radius_box = math.sqrt(math.pow(h/2,2) + math.pow(h/2,2)) + 1
cylinder_4 = Part.makeCylinder(radius_box, h_coil - 2*3)

# cylinder_3 cut by cylinder_4
cylinder_3 = cylinder_3.cut(cylinder_4)

# cylinder_1 cut by cylinder_3
cylinder_3_vector = FreeCAD.Vector(0, 0, 3)
cylinder_3.translate(cylinder_3_vector)
cylinder_1 = cylinder_1.cut(cylinder_3)

# cylinder_1 cut by box_1
box_1 = Part.makeBox(h, l, h_coil)
box_1_vector = FreeCAD.Vector(-h/2, -l/2, 0)
box_1.translate(box_1_vector)
cylinder_1 = cylinder_1.cut(box_1)

# cylinder_1 cut by cylinder_5 in several times
degre = 45
for i in range(int(360/degre)):
    radius = h/2 - h/7
    alpha=(i*degre*math.pi)/180
    cylinder_5_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    cylinder_5 = Part.makeCylinder(5/2, h_coil)
    cylinder_5.translate(cylinder_5_vector)
    cylinder_1 = cylinder_1.cut(cylinder_5)

# cylinder_1 cut by cylinder_5 in several times
degre = 30
for i in range(int(360/degre)):
    radius = h/2 + h/7
    alpha=(i*degre*math.pi)/180
    cylinder_5_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    cylinder_5 = Part.makeCylinder(5/2, h_coil)
    cylinder_5.translate(cylinder_5_vector)
    cylinder_1 = cylinder_1.cut(cylinder_5)

# cylinder_1 cut by cylinder_5 in several times
degre = 15
for i in range(int(360/degre)):
    radius = h/2 + h/7 + h/3
    alpha=(i*degre*math.pi)/180
    cylinder_5_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    cylinder_5 = Part.makeCylinder(5/2, h_coil)
    cylinder_5.translate(cylinder_5_vector)
    cylinder_1 = cylinder_1.cut(cylinder_5)

# cylinder_1 cut by cylinder_5
cylinder_5_vector = FreeCAD.Vector(0, 0, 0)
cylinder_5 = Part.makeCylinder(5/2, h_coil)
cylinder_5.translate(cylinder_5_vector)
cylinder_1 = cylinder_1.cut(cylinder_5)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_input_coil_without_windings_v2").getObject("Shape"))

stl_file = u"part_input_coil_without_windings_v2.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_input_coil_without_windings_v2_'
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
            'exec{(}open{(}"part_input_coil_without_windings_v2.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # 3D printing
    def test_part_input_coil_without_windings_htube8mm_de40mm(self):
        print('test_part_input_coil_without_windings_htube8mm_de40mm')

        if os.path.exists("part_input_coil_without_windings_htube8mm_de40mm.py"):
            os.remove("part_input_coil_without_windings_htube8mm_de40mm.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_input_coil_without_windings_htube8mm_de40mm.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh, math

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_input_coil_without_windings_htube8mm_de40mm"


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

h_tube = 8.1
De = 40
h_coil = 20
D_percage_10 = 10
a = 2

cylinder_1 = Part.makeCylinder(De/2, h_coil)

cylinder_3 = Part.makeCylinder(De/2, h_coil - 2*a)

radius_box = math.sqrt(math.pow(h_tube/2,2) + math.pow(h_tube/2,2)) + 1
cylinder_4 = Part.makeCylinder(radius_box, h_coil - 2*a)

# cylinder_3 cut by cylinder_4
cylinder_3 = cylinder_3.cut(cylinder_4)

# cylinder_1 cut by cylinder_3
cylinder_3_vector = FreeCAD.Vector(0, 0, a)
cylinder_3.translate(cylinder_3_vector)
cylinder_1 = cylinder_1.cut(cylinder_3)

# cylinder_1 cut by box_1
box_1 = Part.makeBox(h_tube, h_tube, h_coil)
box_1_vector = FreeCAD.Vector(-h_tube/2, -h_tube/2, 0)
box_1.translate(box_1_vector)
cylinder_1 = cylinder_1.cut(box_1)

# cylinder_1 cut by cylinder_5 in several times
degre = 60
for i in range(int(360/degre)):
    radius = De/2 - D_percage_10/2 - 1.5
    alpha=(i*degre*math.pi)/180
    cylinder_5_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    cylinder_5 = Part.makeCylinder(D_percage_10/2, h_coil)
    cylinder_5.translate(cylinder_5_vector)
    cylinder_1 = cylinder_1.cut(cylinder_5)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_input_coil_without_windings_htube8mm_de40mm").getObject("Shape"))

stl_file = u"part_input_coil_without_windings_htube8mm_de40mm.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_input_coil_without_windings_htube8mm_de40_'
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
            'exec{(}open{(}"part_input_coil_without_windings_htube8mm_de40mm.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # 3D printing
    def test_part_input_coil_without_windings_di10mm_dw14mm_de40mm_hc18mm(self):
        print('test_part_input_coil_without_windings_di10mm_dw14mm_de40mm_hc18mm')

        if os.path.exists("part_input_coil_without_windings_di10mm_dw14mm_de40mm_hc18mm.py"):
            os.remove("part_input_coil_without_windings_di10mm_dw14mm_de40mm_hc18mm.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_input_coil_without_windings_di10mm_dw14mm_de40mm_hc18mm.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh, math

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_input_coil_without_windings_di10mm_dw14mm_de40mm_hc18mm"


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
EPS = 0.30
EPS_C = EPS * -0.5

Di = 10 + EPS
Dw = Di + 4
hc = 18 + EPS
De = 40 + EPS
a = 2

cylinder_1 = Part.makeCylinder(De/2, hc)

cylinder_2 = Part.makeCylinder(Di/2, hc)

# cylinder_1 cut by cylinder_2
cylinder_1 = cylinder_1.cut(cylinder_2)

cylinder_3 = Part.makeCylinder(De/2, hc - 2*a)

cylinder_4 = Part.makeCylinder(Dw/2, hc - 2*a)

# cylinder_3 cut by cylinder_4
cylinder_3 = cylinder_3.cut(cylinder_4)

# cylinder_1 cut by cylinder_3
cylinder_3_vector = FreeCAD.Vector(0, 0, a)
cylinder_3.translate(cylinder_3_vector)
cylinder_1 = cylinder_1.cut(cylinder_3)

# cylinder_1 cut by cylinder_5 in several times
degre = 60
for i in range(int(360/degre)):
    radius = De/2 - Di/2 - 1.5
    alpha=(i*degre*math.pi)/180
    cylinder_5_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    cylinder_5 = Part.makeCylinder(Di/2, hc)
    cylinder_5.translate(cylinder_5_vector)
    cylinder_1 = cylinder_1.cut(cylinder_5)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_input_coil_without_windings_di10mm_dw14mm_de40mm_hc18mm").getObject("Shape"))

stl_file = u"part_input_coil_without_windings_di10mm_dw14mm_de40mm_hc18mm.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_input_coil_without_windings_di10_dw14_de40_hc18_'
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
            'exec{(}open{(}"part_input_coil_without_windings_di10mm_dw14mm_de40mm_hc18mm.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')


class UnitTestsPatentUS6362718B1MotionlessElectromagneticGeneratorForPartsForOutputCoils(unittest.TestCase):
    # ok
    # 3D printing
    def test_part_output_coil_without_windings(self):
        print('test_part_output_coil_without_windings')

        if os.path.exists("part_output_coil_without_windings.py"):
            os.remove("part_output_coil_without_windings.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_output_coil_without_windings.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_output_coil_without_windings"


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

L_vis_10m = 100
h_equerre = 2.2
h_ecrou_10m = 10
s_rondelle_10m = 2
D = 60
D_aimant = 16
D_winding = 26
D_percage_2_5 = 2.5
D_percage_5 = 5

h_coil = L_vis_10m - h_equerre*2 - s_rondelle_10m*2 - h_ecrou_10m - 5

cylinder_1 = Part.makeCylinder(D/2, h_coil)

cylinder_2 = Part.makeCylinder(D_aimant/2, h_coil)

cylinder_3 = Part.makeCylinder(D/2, h_coil - 2*3)

cylinder_4 = Part.makeCylinder(D_winding/2, h_coil - 2*3)

# cylinder_1 cut by cylinder_2
cylinder_1 = cylinder_1.cut(cylinder_2)

# cylinder_3 cut by cylinder_4
cylinder_3 = cylinder_3.cut(cylinder_4)

# cylinder_1 cut by cylinder_3
cylinder_3_vector = FreeCAD.Vector(0, 0, 3)
cylinder_3.translate(cylinder_3_vector)
cylinder_1 = cylinder_1.cut(cylinder_3)

# cylinder_1 cut by cylinder_5 in several times
degre = 20
for i in range(int(360/degre)):
    radius = D_winding/2 - D_percage_2_5
    alpha=(i*degre*math.pi)/180
    cylinder_5_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    cylinder_5 = Part.makeCylinder(D_percage_2_5/2, h_coil)
    cylinder_5.translate(cylinder_5_vector)
    cylinder_1 = cylinder_1.cut(cylinder_5)

# cylinder_1 cut by cylinder_5 in several times
degre = 20
for i in range(int(360/degre)):
    radius = D_winding/2 + D_percage_5
    alpha=(i*degre*math.pi)/180
    cylinder_5_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    cylinder_5 = Part.makeCylinder(D_percage_5/2, h_coil)
    cylinder_5.translate(cylinder_5_vector)
    cylinder_1 = cylinder_1.cut(cylinder_5)

# cylinder_1 cut by cylinder_5 in several times
degre = 20
for i in range(int(360/degre)):
    radius = D_winding/2 + D_percage_5*2 + 2
    alpha=(i*degre*math.pi)/180
    cylinder_5_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    cylinder_5 = Part.makeCylinder(D_percage_5/2, h_coil)
    cylinder_5.translate(cylinder_5_vector)
    cylinder_1 = cylinder_1.cut(cylinder_5)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_output_coil_without_windings").getObject("Shape"))

stl_file = u"part_output_coil_without_windings.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_output_coil_without_windings_'
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
            'exec{(}open{(}"part_output_coil_without_windings.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # 3D printing
    def test_part_output_coil_without_windings_di8mm_dc26mm_de40mm_hc50mm(self):
        print('test_part_output_coil_without_windings_di8mm_dc26mm_de40mm_hc50mm')

        if os.path.exists("part_output_coil_without_windings_di8mm_dc26mm_de40mm_hc50mm.py"):
            os.remove("part_output_coil_without_windings_di8mm_dc26mm_de40mm_hc50mm.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_output_coil_without_windings_di8mm_dc26mm_de40mm_hc50mm.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_output_coil_without_windings_di8mm_dc26mm_de40mm_hc50mm"


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

De = 40
D_aimant = 8.1
D_winding = 26
D_percage_2_5 = 2.5
D_percage_5 = 5
h_coil = 50
e = 2

cylinder_1 = Part.makeCylinder(De/2, h_coil)

cylinder_2 = Part.makeCylinder(D_aimant/2, h_coil)

cylinder_3 = Part.makeCylinder(De/2, h_coil - 2*e)

cylinder_4 = Part.makeCylinder(D_winding/2, h_coil - 2*e)

# cylinder_1 cut by cylinder_2
cylinder_1 = cylinder_1.cut(cylinder_2)

# cylinder_3 cut by cylinder_4
cylinder_3 = cylinder_3.cut(cylinder_4)

# cylinder_1 cut by cylinder_3
cylinder_3_vector = FreeCAD.Vector(0, 0, e)
cylinder_3.translate(cylinder_3_vector)
cylinder_1 = cylinder_1.cut(cylinder_3)

# cylinder_1 cut by cylinder_5 in several times
degre = 45
for i in range(int(360/degre)):
    radius = D_winding/2 - D_percage_5/2 - 1.3
    alpha=(i*degre*math.pi)/180
    cylinder_5_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    cylinder_5 = Part.makeCylinder(D_percage_5/2, h_coil)
    cylinder_5.translate(cylinder_5_vector)
    cylinder_1 = cylinder_1.cut(cylinder_5)

# cylinder_1 cut by cylinder_5 in several times
degre = 30
for i in range(int(360/degre)):
    radius = De/2 - D_percage_5/2 - 1.3
    alpha=(i*degre*math.pi)/180
    cylinder_5_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    cylinder_5 = Part.makeCylinder(D_percage_5/2, h_coil)
    cylinder_5.translate(cylinder_5_vector)
    cylinder_1 = cylinder_1.cut(cylinder_5)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_output_coil_without_windings_di8mm_dc26mm_de40mm_hc50mm").getObject("Shape"))

stl_file = u"part_output_coil_without_windings_di8mm_dc26mm_de40mm_hc50mm.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_output_coil_without_windings_di8_dc26_de40_hc50_'
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
            'exec{(}open{(}"part_output_coil_without_windings_di8mm_dc26mm_de40mm_hc50mm.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # 3D printing
    def test_part_output_coil_without_windings_di10mm_dw14mm_de40mm_hc36mm(self):
        print('test_part_output_coil_without_windings_di10mm_dw14mm_de40mm_hc36mm')

        if os.path.exists("part_output_coil_without_windings_di10mm_dw14mm_de40mm_hc36mm.py"):
            os.remove("part_output_coil_without_windings_di10mm_dw14mm_de40mm_hc36mm.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_output_coil_without_windings_di10mm_dw14mm_de40mm_hc36mm.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh, math

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_output_coil_without_windings_di10mm_dw14mm_de40mm_hc36mm"


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
EPS = 0.30
EPS_C = EPS * -0.5

Di = 10 + EPS
Dw = Di + 4
hc = 36 + EPS
De = 40 + EPS
a = 2

cylinder_1 = Part.makeCylinder(De/2, hc)

cylinder_2 = Part.makeCylinder(Di/2, hc)

# cylinder_1 cut by cylinder_2
cylinder_1 = cylinder_1.cut(cylinder_2)

cylinder_3 = Part.makeCylinder(De/2, hc - 2*a)

cylinder_4 = Part.makeCylinder(Dw/2, hc - 2*a)

# cylinder_3 cut by cylinder_4
cylinder_3 = cylinder_3.cut(cylinder_4)

# cylinder_1 cut by cylinder_3
cylinder_3_vector = FreeCAD.Vector(0, 0, a)
cylinder_3.translate(cylinder_3_vector)
cylinder_1 = cylinder_1.cut(cylinder_3)

# cylinder_1 cut by cylinder_5 in several times
degre = 60
for i in range(int(360/degre)):
    radius = De/2 - Di/2 - 1.5
    alpha=(i*degre*math.pi)/180
    cylinder_5_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    cylinder_5 = Part.makeCylinder(Di/2, hc)
    cylinder_5.translate(cylinder_5_vector)
    cylinder_1 = cylinder_1.cut(cylinder_5)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_output_coil_without_windings_di10mm_dw14mm_de40mm_hc36mm").getObject("Shape"))

stl_file = u"part_output_coil_without_windings_di10mm_dw14mm_de40mm_hc36mm.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_output_coil_without_windings_di10_dw14_de40_hc36_'
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
            'exec{(}open{(}"part_output_coil_without_windings_di10mm_dw14mm_de40mm_hc36mm.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')


class UnitTestsPatentUS6362718B1MotionlessElectromagneticGeneratorForAssemblies(unittest.TestCase):
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

L_part_steel_box_for_core_8mm_8mm_200mm = 200

# Export assembly_global
__objs__ = []

# part_steel_box_for_core_8mm_8mm_200mm - 1
Mesh.insert(u"part_steel_box_for_core_8mm_8mm_200mm.stl","assembly_global")
FreeCADGui.getDocument("assembly_global").getObject("part_steel_box_for_core_8mm_8mm_200mm").ShapeColor = (0.10,0.20,0.30)
FreeCAD.getDocument("assembly_global").getObject("part_steel_box_for_core_8mm_8mm_200mm").Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_global").getObject("part_steel_box_for_core_8mm_8mm_200mm"))

number_of_permanent_magnet_neodyme_n40_8mm_3mm_per_output_coil = round(50/3)

# part_permanent_magnet_neodyme_n40_8mm_3mm
for i in range(0, number_of_permanent_magnet_neodyme_n40_8mm_3mm_per_output_coil):
    if i == 0:
        Mesh.insert(u"part_permanent_magnet_neodyme_n40_8mm_3mm.stl","assembly_global")
        FreeCADGui.getDocument("assembly_global").getObject("part_permanent_magnet_neodyme_n40_8mm_3mm").ShapeColor = (0.30,0.30,0.30)
        FreeCAD.getDocument("assembly_global").getObject("part_permanent_magnet_neodyme_n40_8mm_3mm").Placement = App.Placement(App.Vector(4,4,8 + 3*i),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument("assembly_global").getObject("part_permanent_magnet_neodyme_n40_8mm_3mm"))
    elif i >= 1 and i < 10:
        Mesh.insert(u"part_permanent_magnet_neodyme_n40_8mm_3mm.stl","assembly_global")
        FreeCADGui.getDocument("assembly_global").getObject("part_permanent_magnet_neodyme_n40_8mm_3mm00" + str(i)).ShapeColor = (0.30,0.30,0.30)
        FreeCAD.getDocument("assembly_global").getObject("part_permanent_magnet_neodyme_n40_8mm_3mm00" + str(i)).Placement = App.Placement(App.Vector(4,4,8 + 3*i),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument("assembly_global").getObject("part_permanent_magnet_neodyme_n40_8mm_3mm00" + str(i)))
    elif i >= 10 and i < 100:
        Mesh.insert(u"part_permanent_magnet_neodyme_n40_8mm_3mm.stl","assembly_global")
        FreeCADGui.getDocument("assembly_global").getObject("part_permanent_magnet_neodyme_n40_8mm_3mm0" + str(i)).ShapeColor = (0.30,0.30,0.30)
        FreeCAD.getDocument("assembly_global").getObject("part_permanent_magnet_neodyme_n40_8mm_3mm0" + str(i)).Placement = App.Placement(App.Vector(4,4,8 + 3*i),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument("assembly_global").getObject("part_permanent_magnet_neodyme_n40_8mm_3mm0" + str(i)))
    elif i >= 100 and i < 1000:
        Mesh.insert(u"part_permanent_magnet_neodyme_n40_8mm_3mm.stl","assembly_global")
        FreeCADGui.getDocument("assembly_global").getObject("part_permanent_magnet_neodyme_n40_8mm_3mm" + str(i)).ShapeColor = (0.30,0.30,0.30)
        FreeCAD.getDocument("assembly_global").getObject("part_permanent_magnet_neodyme_n40_8mm_3mm" + str(i)).Placement = App.Placement(App.Vector(4,4,8 + 3*i),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument("assembly_global").getObject("part_permanent_magnet_neodyme_n40_8mm_3mm" + str(i)))

for i in range(number_of_permanent_magnet_neodyme_n40_8mm_3mm_per_output_coil, number_of_permanent_magnet_neodyme_n40_8mm_3mm_per_output_coil*2):
    if i == 0:
        Mesh.insert(u"part_permanent_magnet_neodyme_n40_8mm_3mm.stl","assembly_global")
        FreeCADGui.getDocument("assembly_global").getObject("part_permanent_magnet_neodyme_n40_8mm_3mm").ShapeColor = (0.30,0.30,0.30)
        FreeCAD.getDocument("assembly_global").getObject("part_permanent_magnet_neodyme_n40_8mm_3mm").Placement = App.Placement(App.Vector(L_part_steel_box_for_core_8mm_8mm_200mm/2,4,8 + 3*(i-number_of_permanent_magnet_neodyme_n40_8mm_3mm_per_output_coil)),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument("assembly_global").getObject("part_permanent_magnet_neodyme_n40_8mm_3mm"))
    elif i >= 1 and i < 10:
        Mesh.insert(u"part_permanent_magnet_neodyme_n40_8mm_3mm.stl","assembly_global")
        FreeCADGui.getDocument("assembly_global").getObject("part_permanent_magnet_neodyme_n40_8mm_3mm00" + str(i)).ShapeColor = (0.30,0.30,0.30)
        FreeCAD.getDocument("assembly_global").getObject("part_permanent_magnet_neodyme_n40_8mm_3mm00" + str(i)).Placement = App.Placement(App.Vector(L_part_steel_box_for_core_8mm_8mm_200mm/2,4,8 + 3*(i-number_of_permanent_magnet_neodyme_n40_8mm_3mm_per_output_coil)),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument("assembly_global").getObject("part_permanent_magnet_neodyme_n40_8mm_3mm00" + str(i)))
    elif i >= 10 and i < 100:
        Mesh.insert(u"part_permanent_magnet_neodyme_n40_8mm_3mm.stl","assembly_global")
        FreeCADGui.getDocument("assembly_global").getObject("part_permanent_magnet_neodyme_n40_8mm_3mm0" + str(i)).ShapeColor = (0.30,0.30,0.30)
        FreeCAD.getDocument("assembly_global").getObject("part_permanent_magnet_neodyme_n40_8mm_3mm0" + str(i)).Placement = App.Placement(App.Vector(L_part_steel_box_for_core_8mm_8mm_200mm/2,4,8 + 3*(i-number_of_permanent_magnet_neodyme_n40_8mm_3mm_per_output_coil)),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument("assembly_global").getObject("part_permanent_magnet_neodyme_n40_8mm_3mm0" + str(i)))
    elif i >= 100 and i < 1000:
        Mesh.insert(u"part_permanent_magnet_neodyme_n40_8mm_3mm.stl","assembly_global")
        FreeCADGui.getDocument("assembly_global").getObject("part_permanent_magnet_neodyme_n40_8mm_3mm" + str(i)).ShapeColor = (0.30,0.30,0.30)
        FreeCAD.getDocument("assembly_global").getObject("part_permanent_magnet_neodyme_n40_8mm_3mm" + str(i)).Placement = App.Placement(App.Vector(L_part_steel_box_for_core_8mm_8mm_200mm/2,4,8 + 3*(i-number_of_permanent_magnet_neodyme_n40_8mm_3mm_per_output_coil)),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument("assembly_global").getObject("part_permanent_magnet_neodyme_n40_8mm_3mm" + str(i)))
        
for i in range(number_of_permanent_magnet_neodyme_n40_8mm_3mm_per_output_coil*2, number_of_permanent_magnet_neodyme_n40_8mm_3mm_per_output_coil*3):
    if i == 0:
        Mesh.insert(u"part_permanent_magnet_neodyme_n40_8mm_3mm.stl","assembly_global")
        FreeCADGui.getDocument("assembly_global").getObject("part_permanent_magnet_neodyme_n40_8mm_3mm").ShapeColor = (0.30,0.30,0.30)
        FreeCAD.getDocument("assembly_global").getObject("part_permanent_magnet_neodyme_n40_8mm_3mm").Placement = App.Placement(App.Vector(L_part_steel_box_for_core_8mm_8mm_200mm - 4,4,8 + 3*(i-number_of_permanent_magnet_neodyme_n40_8mm_3mm_per_output_coil*2)),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument("assembly_global").getObject("part_permanent_magnet_neodyme_n40_8mm_3mm"))
    elif i >= 1 and i < 10:
        Mesh.insert(u"part_permanent_magnet_neodyme_n40_8mm_3mm.stl","assembly_global")
        FreeCADGui.getDocument("assembly_global").getObject("part_permanent_magnet_neodyme_n40_8mm_3mm00" + str(i)).ShapeColor = (0.30,0.30,0.30)
        FreeCAD.getDocument("assembly_global").getObject("part_permanent_magnet_neodyme_n40_8mm_3mm00" + str(i)).Placement = App.Placement(App.Vector(L_part_steel_box_for_core_8mm_8mm_200mm - 4,4,8 + 3*(i-number_of_permanent_magnet_neodyme_n40_8mm_3mm_per_output_coil*2)),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument("assembly_global").getObject("part_permanent_magnet_neodyme_n40_8mm_3mm00" + str(i)))
    elif i >= 10 and i < 100:
        Mesh.insert(u"part_permanent_magnet_neodyme_n40_8mm_3mm.stl","assembly_global")
        FreeCADGui.getDocument("assembly_global").getObject("part_permanent_magnet_neodyme_n40_8mm_3mm0" + str(i)).ShapeColor = (0.30,0.30,0.30)
        FreeCAD.getDocument("assembly_global").getObject("part_permanent_magnet_neodyme_n40_8mm_3mm0" + str(i)).Placement = App.Placement(App.Vector(L_part_steel_box_for_core_8mm_8mm_200mm - 4,4,8 + 3*(i-number_of_permanent_magnet_neodyme_n40_8mm_3mm_per_output_coil*2)),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument("assembly_global").getObject("part_permanent_magnet_neodyme_n40_8mm_3mm0" + str(i)))
    elif i >= 100 and i < 1000:
        Mesh.insert(u"part_permanent_magnet_neodyme_n40_8mm_3mm.stl","assembly_global")
        FreeCADGui.getDocument("assembly_global").getObject("part_permanent_magnet_neodyme_n40_8mm_3mm" + str(i)).ShapeColor = (0.30,0.30,0.30)
        FreeCAD.getDocument("assembly_global").getObject("part_permanent_magnet_neodyme_n40_8mm_3mm" + str(i)).Placement = App.Placement(App.Vector(L_part_steel_box_for_core_8mm_8mm_200mm - 4,4,8 + 3*(i-number_of_permanent_magnet_neodyme_n40_8mm_3mm_per_output_coil*2)),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument("assembly_global").getObject("part_permanent_magnet_neodyme_n40_8mm_3mm" + str(i)))

# part_steel_box_for_core_8mm_8mm_200mm - 2
Mesh.insert(u"part_steel_box_for_core_8mm_8mm_200mm.stl","assembly_global")
FreeCADGui.getDocument("assembly_global").getObject("part_steel_box_for_core_8mm_8mm_200mm001").ShapeColor = (0.10,0.20,0.30)
FreeCAD.getDocument("assembly_global").getObject("part_steel_box_for_core_8mm_8mm_200mm001").Placement = App.Placement(App.Vector(0,0,8 + 3*number_of_permanent_magnet_neodyme_n40_8mm_3mm_per_output_coil),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_global").getObject("part_steel_box_for_core_8mm_8mm_200mm001"))

# part_output_coil_without_windings_di8mm_dc26mm_de40mm_hc50mm - 1
Mesh.insert(u"part_output_coil_without_windings_di8mm_dc26mm_de40mm_hc50mm.stl","assembly_global")
FreeCADGui.getDocument("assembly_global").getObject("part_output_coil_without_windings_di8mm_dc26mm_de40mm_hc50mm").ShapeColor = (0.90,0.60,0.30)
FreeCAD.getDocument("assembly_global").getObject("part_output_coil_without_windings_di8mm_dc26mm_de40mm_hc50mm").Placement = App.Placement(App.Vector(4,4,8),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_global").getObject("part_output_coil_without_windings_di8mm_dc26mm_de40mm_hc50mm"))

# part_output_coil_without_windings_di8mm_dc26mm_de40mm_hc50mm - 2
Mesh.insert(u"part_output_coil_without_windings_di8mm_dc26mm_de40mm_hc50mm.stl","assembly_global")
FreeCADGui.getDocument("assembly_global").getObject("part_output_coil_without_windings_di8mm_dc26mm_de40mm_hc50mm001").ShapeColor = (0.90,0.60,0.30)
FreeCAD.getDocument("assembly_global").getObject("part_output_coil_without_windings_di8mm_dc26mm_de40mm_hc50mm001").Placement = App.Placement(App.Vector(L_part_steel_box_for_core_8mm_8mm_200mm/2,4,8),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_global").getObject("part_output_coil_without_windings_di8mm_dc26mm_de40mm_hc50mm001"))

# part_output_coil_without_windings_di8mm_dc26mm_de40mm_hc50mm - 3
Mesh.insert(u"part_output_coil_without_windings_di8mm_dc26mm_de40mm_hc50mm.stl","assembly_global")
FreeCADGui.getDocument("assembly_global").getObject("part_output_coil_without_windings_di8mm_dc26mm_de40mm_hc50mm002").ShapeColor = (0.90,0.60,0.30)
FreeCAD.getDocument("assembly_global").getObject("part_output_coil_without_windings_di8mm_dc26mm_de40mm_hc50mm002").Placement = App.Placement(App.Vector(L_part_steel_box_for_core_8mm_8mm_200mm - 4,4,8),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_global").getObject("part_output_coil_without_windings_di8mm_dc26mm_de40mm_hc50mm002"))

# part_input_coil_without_windings_htube8mm_de40mm - 1
Mesh.insert(u"part_input_coil_without_windings_htube8mm_de40mm.stl","assembly_global")
FreeCADGui.getDocument("assembly_global").getObject("part_input_coil_without_windings_htube8mm_de40mm").ShapeColor = (0.30,0.60,0.60)
FreeCAD.getDocument("assembly_global").getObject("part_input_coil_without_windings_htube8mm_de40mm").Placement = App.Placement(App.Vector(L_part_steel_box_for_core_8mm_8mm_200mm/4,4,4),App.Rotation(App.Vector(0,1,0),90))
__objs__.append(FreeCAD.getDocument("assembly_global").getObject("part_input_coil_without_windings_htube8mm_de40mm"))

# part_input_coil_without_windings_htube8mm_de40mm - 2
Mesh.insert(u"part_input_coil_without_windings_htube8mm_de40mm.stl","assembly_global")
FreeCADGui.getDocument("assembly_global").getObject("part_input_coil_without_windings_htube8mm_de40mm001").ShapeColor = (0.30,0.60,0.60)
FreeCAD.getDocument("assembly_global").getObject("part_input_coil_without_windings_htube8mm_de40mm001").Placement = App.Placement(App.Vector(3*(L_part_steel_box_for_core_8mm_8mm_200mm/4),4,4),App.Rotation(App.Vector(0,1,0),90))
__objs__.append(FreeCAD.getDocument("assembly_global").getObject("part_input_coil_without_windings_htube8mm_de40mm001"))

# part_input_coil_without_windings_htube8mm_de40mm - 3
Mesh.insert(u"part_input_coil_without_windings_htube8mm_de40mm.stl","assembly_global")
FreeCADGui.getDocument("assembly_global").getObject("part_input_coil_without_windings_htube8mm_de40mm002").ShapeColor = (0.30,0.60,0.60)
FreeCAD.getDocument("assembly_global").getObject("part_input_coil_without_windings_htube8mm_de40mm002").Placement = App.Placement(App.Vector(L_part_steel_box_for_core_8mm_8mm_200mm/4,4,4 + 8 + 3*number_of_permanent_magnet_neodyme_n40_8mm_3mm_per_output_coil),App.Rotation(App.Vector(0,1,0),90))
__objs__.append(FreeCAD.getDocument("assembly_global").getObject("part_input_coil_without_windings_htube8mm_de40mm002"))

# part_input_coil_without_windings_htube8mm_de40mm - 4
Mesh.insert(u"part_input_coil_without_windings_htube8mm_de40mm.stl","assembly_global")
FreeCADGui.getDocument("assembly_global").getObject("part_input_coil_without_windings_htube8mm_de40mm003").ShapeColor = (0.30,0.60,0.60)
FreeCAD.getDocument("assembly_global").getObject("part_input_coil_without_windings_htube8mm_de40mm003").Placement = App.Placement(App.Vector(3*(L_part_steel_box_for_core_8mm_8mm_200mm/4),4,4 + 8 + 3*number_of_permanent_magnet_neodyme_n40_8mm_3mm_per_output_coil),App.Rotation(App.Vector(0,1,0),90))
__objs__.append(FreeCAD.getDocument("assembly_global").getObject("part_input_coil_without_windings_htube8mm_de40mm003"))

setview()

Mesh.export(__objs__,u"assembly_global.stl")

del __objs__

# Generate PNG files
file = 'assembly_global_'
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
            'exec{(}open{(}"assembly_global.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_assembly_global_v2(self):
        print("test_assembly_global_v2")

        if os.path.exists("assembly_global_v2.py"):
            os.remove("assembly_global_v2.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("assembly_global_v2.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_global_v2"


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

# Export assembly_global_v2
__objs__ = []

# part_permanent_magnet_neodyme_n40_10mm_40mm - 1
Mesh.insert(u"part_permanent_magnet_neodyme_n40_10mm_40mm.stl","assembly_global_v2")
FreeCADGui.getDocument("assembly_global_v2").getObject("part_permanent_magnet_neodyme_n40_10mm_40mm").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_global_v2").getObject("part_permanent_magnet_neodyme_n40_10mm_40mm").Placement = App.Placement(App.Vector(40*0,0,0),App.Rotation(App.Vector(0,1,0),90))
__objs__.append(FreeCAD.getDocument("assembly_global_v2").getObject("part_permanent_magnet_neodyme_n40_10mm_40mm"))

# part_permanent_magnet_neodyme_n40_10mm_40mm - 2
Mesh.insert(u"part_permanent_magnet_neodyme_n40_10mm_40mm.stl","assembly_global_v2")
FreeCADGui.getDocument("assembly_global_v2").getObject("part_permanent_magnet_neodyme_n40_10mm_40mm001").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_global_v2").getObject("part_permanent_magnet_neodyme_n40_10mm_40mm001").Placement = App.Placement(App.Vector(40*1,0,0),App.Rotation(App.Vector(0,1,0),90))
__objs__.append(FreeCAD.getDocument("assembly_global_v2").getObject("part_permanent_magnet_neodyme_n40_10mm_40mm001"))

# part_permanent_magnet_neodyme_n40_10mm_40mm - 3
Mesh.insert(u"part_permanent_magnet_neodyme_n40_10mm_40mm.stl","assembly_global_v2")
FreeCADGui.getDocument("assembly_global_v2").getObject("part_permanent_magnet_neodyme_n40_10mm_40mm002").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_global_v2").getObject("part_permanent_magnet_neodyme_n40_10mm_40mm002").Placement = App.Placement(App.Vector(40*0,0,40 + 10),App.Rotation(App.Vector(0,1,0),90))
__objs__.append(FreeCAD.getDocument("assembly_global_v2").getObject("part_permanent_magnet_neodyme_n40_10mm_40mm002"))

# part_permanent_magnet_neodyme_n40_10mm_40mm - 4
Mesh.insert(u"part_permanent_magnet_neodyme_n40_10mm_40mm.stl","assembly_global_v2")
FreeCADGui.getDocument("assembly_global_v2").getObject("part_permanent_magnet_neodyme_n40_10mm_40mm003").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_global_v2").getObject("part_permanent_magnet_neodyme_n40_10mm_40mm003").Placement = App.Placement(App.Vector(5,0,5),App.Rotation(App.Vector(0,1,0),0))
__objs__.append(FreeCAD.getDocument("assembly_global_v2").getObject("part_permanent_magnet_neodyme_n40_10mm_40mm003"))

# part_permanent_magnet_neodyme_n40_10mm_40mm - 5
Mesh.insert(u"part_permanent_magnet_neodyme_n40_10mm_40mm.stl","assembly_global_v2")
FreeCADGui.getDocument("assembly_global_v2").getObject("part_permanent_magnet_neodyme_n40_10mm_40mm004").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_global_v2").getObject("part_permanent_magnet_neodyme_n40_10mm_40mm004").Placement = App.Placement(App.Vector(40*2 - 5,0,5),App.Rotation(App.Vector(0,1,0),0))
__objs__.append(FreeCAD.getDocument("assembly_global_v2").getObject("part_permanent_magnet_neodyme_n40_10mm_40mm004"))

# part_permanent_magnet_neodyme_n40_10mm_40mm - 6
Mesh.insert(u"part_permanent_magnet_neodyme_n40_10mm_40mm.stl","assembly_global_v2")
FreeCADGui.getDocument("assembly_global_v2").getObject("part_permanent_magnet_neodyme_n40_10mm_40mm005").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_global_v2").getObject("part_permanent_magnet_neodyme_n40_10mm_40mm005").Placement = App.Placement(App.Vector(40*1,0,40 + 10),App.Rotation(App.Vector(0,1,0),90))
__objs__.append(FreeCAD.getDocument("assembly_global_v2").getObject("part_permanent_magnet_neodyme_n40_10mm_40mm005"))

# part_output_coil_without_windings_di10mm_dw14mm_de40mm_hc36mm - 1
Mesh.insert(u"part_output_coil_without_windings_di10mm_dw14mm_de40mm_hc36mm.stl","assembly_global_v2")
FreeCADGui.getDocument("assembly_global_v2").getObject("part_output_coil_without_windings_di10mm_dw14mm_de40mm_hc36mm").ShapeColor = (0.60,0.60,0.60)
FreeCAD.getDocument("assembly_global_v2").getObject("part_output_coil_without_windings_di10mm_dw14mm_de40mm_hc36mm").Placement = App.Placement(App.Vector(5,0,7),App.Rotation(App.Vector(0,1,0),0))
__objs__.append(FreeCAD.getDocument("assembly_global_v2").getObject("part_output_coil_without_windings_di10mm_dw14mm_de40mm_hc36mm"))

# part_output_coil_without_windings_di10mm_dw14mm_de40mm_hc36mm - 2
Mesh.insert(u"part_output_coil_without_windings_di10mm_dw14mm_de40mm_hc36mm.stl","assembly_global_v2")
FreeCADGui.getDocument("assembly_global_v2").getObject("part_output_coil_without_windings_di10mm_dw14mm_de40mm_hc36mm001").ShapeColor = (0.60,0.60,0.60)
FreeCAD.getDocument("assembly_global_v2").getObject("part_output_coil_without_windings_di10mm_dw14mm_de40mm_hc36mm001").Placement = App.Placement(App.Vector(40*2 - 5,0,7),App.Rotation(App.Vector(0,1,0),0))
__objs__.append(FreeCAD.getDocument("assembly_global_v2").getObject("part_output_coil_without_windings_di10mm_dw14mm_de40mm_hc36mm001"))

# part_input_coil_without_windings_di10mm_dw14mm_de40mm_hc18mm - 1
Mesh.insert(u"part_input_coil_without_windings_di10mm_dw14mm_de40mm_hc18mm.stl","assembly_global_v2")
FreeCADGui.getDocument("assembly_global_v2").getObject("part_input_coil_without_windings_di10mm_dw14mm_de40mm_hc18mm").ShapeColor = (0.60,0.90,0.60)
FreeCAD.getDocument("assembly_global_v2").getObject("part_input_coil_without_windings_di10mm_dw14mm_de40mm_hc18mm").Placement = App.Placement(App.Vector((40*2 - 18)/2,0,0),App.Rotation(App.Vector(0,1,0),90))
__objs__.append(FreeCAD.getDocument("assembly_global_v2").getObject("part_input_coil_without_windings_di10mm_dw14mm_de40mm_hc18mm"))

# part_input_coil_without_windings_di10mm_dw14mm_de40mm_hc18mm - 2
Mesh.insert(u"part_input_coil_without_windings_di10mm_dw14mm_de40mm_hc18mm.stl","assembly_global_v2")
FreeCADGui.getDocument("assembly_global_v2").getObject("part_input_coil_without_windings_di10mm_dw14mm_de40mm_hc18mm001").ShapeColor = (0.60,0.90,0.60)
FreeCAD.getDocument("assembly_global_v2").getObject("part_input_coil_without_windings_di10mm_dw14mm_de40mm_hc18mm001").Placement = App.Placement(App.Vector((40*2 - 18)/2,0,40 + 10),App.Rotation(App.Vector(0,1,0),90))
__objs__.append(FreeCAD.getDocument("assembly_global_v2").getObject("part_input_coil_without_windings_di10mm_dw14mm_de40mm_hc18mm001"))

setview()

Mesh.export(__objs__,u"assembly_global_v2.stl")

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
            'exec{(}open{(}"assembly_global_v2.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_assembly_global_v3(self):
        print("test_assembly_global_v3")

        if os.path.exists("assembly_global_v3.py"):
            os.remove("assembly_global_v3.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("assembly_global_v3.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_global_v3"


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

# Export assembly_global_v2
__objs__ = []

# part_permanent_magnet_neodyme_n40_10mm_40mm - 1
Mesh.insert(u"part_permanent_magnet_neodyme_n40_10mm_40mm.stl","assembly_global_v3")
FreeCADGui.getDocument("assembly_global_v3").getObject("part_permanent_magnet_neodyme_n40_10mm_40mm").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_global_v3").getObject("part_permanent_magnet_neodyme_n40_10mm_40mm").Placement = App.Placement(App.Vector(40*0,0,0),App.Rotation(App.Vector(0,1,0),90))
__objs__.append(FreeCAD.getDocument("assembly_global_v3").getObject("part_permanent_magnet_neodyme_n40_10mm_40mm"))

# part_permanent_magnet_neodyme_n40_10mm_40mm - 2
Mesh.insert(u"part_permanent_magnet_neodyme_n40_10mm_40mm.stl","assembly_global_v3")
FreeCADGui.getDocument("assembly_global_v3").getObject("part_permanent_magnet_neodyme_n40_10mm_40mm001").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_global_v3").getObject("part_permanent_magnet_neodyme_n40_10mm_40mm001").Placement = App.Placement(App.Vector(40*1,0,0),App.Rotation(App.Vector(0,1,0),90))
__objs__.append(FreeCAD.getDocument("assembly_global_v3").getObject("part_permanent_magnet_neodyme_n40_10mm_40mm001"))

# part_permanent_magnet_neodyme_n40_10mm_40mm - 3
Mesh.insert(u"part_permanent_magnet_neodyme_n40_10mm_40mm.stl","assembly_global_v3")
FreeCADGui.getDocument("assembly_global_v3").getObject("part_permanent_magnet_neodyme_n40_10mm_40mm002").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_global_v3").getObject("part_permanent_magnet_neodyme_n40_10mm_40mm002").Placement = App.Placement(App.Vector(40*0,0,40 + 10),App.Rotation(App.Vector(0,1,0),90))
__objs__.append(FreeCAD.getDocument("assembly_global_v3").getObject("part_permanent_magnet_neodyme_n40_10mm_40mm002"))

# part_permanent_magnet_neodyme_n40_10mm_40mm - 4
Mesh.insert(u"part_permanent_magnet_neodyme_n40_10mm_40mm.stl","assembly_global_v3")
FreeCADGui.getDocument("assembly_global_v3").getObject("part_permanent_magnet_neodyme_n40_10mm_40mm003").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_global_v3").getObject("part_permanent_magnet_neodyme_n40_10mm_40mm003").Placement = App.Placement(App.Vector(5,0,5),App.Rotation(App.Vector(0,1,0),0))
__objs__.append(FreeCAD.getDocument("assembly_global_v3").getObject("part_permanent_magnet_neodyme_n40_10mm_40mm003"))

# part_permanent_magnet_neodyme_n40_10mm_40mm - 5
Mesh.insert(u"part_permanent_magnet_neodyme_n40_10mm_40mm.stl","assembly_global_v3")
FreeCADGui.getDocument("assembly_global_v3").getObject("part_permanent_magnet_neodyme_n40_10mm_40mm004").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_global_v3").getObject("part_permanent_magnet_neodyme_n40_10mm_40mm004").Placement = App.Placement(App.Vector(40*3 - 5,0,5),App.Rotation(App.Vector(0,1,0),0))
__objs__.append(FreeCAD.getDocument("assembly_global_v3").getObject("part_permanent_magnet_neodyme_n40_10mm_40mm004"))

# part_permanent_magnet_neodyme_n40_10mm_40mm - 6
Mesh.insert(u"part_permanent_magnet_neodyme_n40_10mm_40mm.stl","assembly_global_v3")
FreeCADGui.getDocument("assembly_global_v3").getObject("part_permanent_magnet_neodyme_n40_10mm_40mm005").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_global_v3").getObject("part_permanent_magnet_neodyme_n40_10mm_40mm005").Placement = App.Placement(App.Vector(40*1,0,40 + 10),App.Rotation(App.Vector(0,1,0),90))
__objs__.append(FreeCAD.getDocument("assembly_global_v3").getObject("part_permanent_magnet_neodyme_n40_10mm_40mm005"))

# part_permanent_magnet_neodyme_n40_10mm_40mm - 7
Mesh.insert(u"part_permanent_magnet_neodyme_n40_10mm_40mm.stl","assembly_global_v3")
FreeCADGui.getDocument("assembly_global_v3").getObject("part_permanent_magnet_neodyme_n40_10mm_40mm006").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_global_v3").getObject("part_permanent_magnet_neodyme_n40_10mm_40mm006").Placement = App.Placement(App.Vector(40*2,0,0),App.Rotation(App.Vector(0,1,0),90))
__objs__.append(FreeCAD.getDocument("assembly_global_v3").getObject("part_permanent_magnet_neodyme_n40_10mm_40mm006"))

# part_permanent_magnet_neodyme_n40_10mm_40mm - 8
Mesh.insert(u"part_permanent_magnet_neodyme_n40_10mm_40mm.stl","assembly_global_v3")
FreeCADGui.getDocument("assembly_global_v3").getObject("part_permanent_magnet_neodyme_n40_10mm_40mm007").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_global_v3").getObject("part_permanent_magnet_neodyme_n40_10mm_40mm007").Placement = App.Placement(App.Vector(40*2,0,40 + 10),App.Rotation(App.Vector(0,1,0),90))
__objs__.append(FreeCAD.getDocument("assembly_global_v3").getObject("part_permanent_magnet_neodyme_n40_10mm_40mm007"))

# part_permanent_magnet_neodyme_n40_10mm_40mm - 9
Mesh.insert(u"part_permanent_magnet_neodyme_n40_10mm_40mm.stl","assembly_global_v3")
FreeCADGui.getDocument("assembly_global_v3").getObject("part_permanent_magnet_neodyme_n40_10mm_40mm008").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_global_v3").getObject("part_permanent_magnet_neodyme_n40_10mm_40mm008").Placement = App.Placement(App.Vector(60,0,5),App.Rotation(App.Vector(0,1,0),0))
__objs__.append(FreeCAD.getDocument("assembly_global_v3").getObject("part_permanent_magnet_neodyme_n40_10mm_40mm008"))

# part_output_coil_without_windings_di10mm_dw14mm_de40mm_hc36mm - 1
Mesh.insert(u"part_output_coil_without_windings_di10mm_dw14mm_de40mm_hc36mm.stl","assembly_global_v3")
FreeCADGui.getDocument("assembly_global_v3").getObject("part_output_coil_without_windings_di10mm_dw14mm_de40mm_hc36mm").ShapeColor = (0.60,0.60,0.60)
FreeCAD.getDocument("assembly_global_v3").getObject("part_output_coil_without_windings_di10mm_dw14mm_de40mm_hc36mm").Placement = App.Placement(App.Vector(5,0,7),App.Rotation(App.Vector(0,1,0),0))
__objs__.append(FreeCAD.getDocument("assembly_global_v3").getObject("part_output_coil_without_windings_di10mm_dw14mm_de40mm_hc36mm"))

# part_output_coil_without_windings_di10mm_dw14mm_de40mm_hc36mm - 2
Mesh.insert(u"part_output_coil_without_windings_di10mm_dw14mm_de40mm_hc36mm.stl","assembly_global_v3")
FreeCADGui.getDocument("assembly_global_v3").getObject("part_output_coil_without_windings_di10mm_dw14mm_de40mm_hc36mm001").ShapeColor = (0.60,0.60,0.60)
FreeCAD.getDocument("assembly_global_v3").getObject("part_output_coil_without_windings_di10mm_dw14mm_de40mm_hc36mm001").Placement = App.Placement(App.Vector(40*3 - 5,0,7),App.Rotation(App.Vector(0,1,0),0))
__objs__.append(FreeCAD.getDocument("assembly_global_v3").getObject("part_output_coil_without_windings_di10mm_dw14mm_de40mm_hc36mm001"))

# part_input_coil_without_windings_di10mm_dw14mm_de40mm_hc18mm - 1
Mesh.insert(u"part_input_coil_without_windings_di10mm_dw14mm_de40mm_hc18mm.stl","assembly_global_v3")
FreeCADGui.getDocument("assembly_global_v3").getObject("part_input_coil_without_windings_di10mm_dw14mm_de40mm_hc18mm").ShapeColor = (0.60,0.90,0.60)
FreeCAD.getDocument("assembly_global_v3").getObject("part_input_coil_without_windings_di10mm_dw14mm_de40mm_hc18mm").Placement = App.Placement(App.Vector((40*2 - 18)/2,0,0),App.Rotation(App.Vector(0,1,0),90))
__objs__.append(FreeCAD.getDocument("assembly_global_v3").getObject("part_input_coil_without_windings_di10mm_dw14mm_de40mm_hc18mm"))

# part_input_coil_without_windings_di10mm_dw14mm_de40mm_hc18mm - 2
Mesh.insert(u"part_input_coil_without_windings_di10mm_dw14mm_de40mm_hc18mm.stl","assembly_global_v3")
FreeCADGui.getDocument("assembly_global_v3").getObject("part_input_coil_without_windings_di10mm_dw14mm_de40mm_hc18mm001").ShapeColor = (0.60,0.90,0.60)
FreeCAD.getDocument("assembly_global_v3").getObject("part_input_coil_without_windings_di10mm_dw14mm_de40mm_hc18mm001").Placement = App.Placement(App.Vector((40*2 - 18)/2 + 40,0,40 + 10),App.Rotation(App.Vector(0,1,0),90))
__objs__.append(FreeCAD.getDocument("assembly_global_v3").getObject("part_input_coil_without_windings_di10mm_dw14mm_de40mm_hc18mm001"))

setview()

Mesh.export(__objs__,u"assembly_global_v3.stl")

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
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"assembly_global_v3.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')


if __name__ == '__main__':
    unittest.main()
