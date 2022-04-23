import os
import time
import unittest
import pywinauto.mouse
import pywinauto.keyboard


class UnitTestsEdwinGrayPowerTubeVersion1(unittest.TestCase):
    # ok
    def test_part_coil_transformer(self):
        print("test_part_coil_transformer")

        if os.path.exists("part_coil_transformer.py"):
            os.remove("part_coil_transformer.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_coil_transformer.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_coil_transformer"


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

# part_coil_transformer
part_coil_transformer = Part.makeCylinder(12, 50)

# cylinder_core_ferrite
cylinder_core_ferrite = Part.makeCylinder(5, 50)

# part_coil_transformer cut by cylinder_core_ferrite
part_coil_transformer = part_coil_transformer.cut(cylinder_core_ferrite)

# cylinder_1
cylinder_1 = Part.makeCylinder(12, 46)

# cylinder_2
cylinder_2 = Part.makeCylinder(7, 46)

# cylinder_1 cut by cylinder_2
cylinder_1 = cylinder_1.cut(cylinder_2)

# part_coil_transformer cut by cylinder_1
cylinder_1_vector = FreeCAD.Vector(0, 0, 2)
cylinder_1.translate(cylinder_1_vector)
part_coil_transformer = part_coil_transformer.cut(cylinder_1)

Part.show(part_coil_transformer)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_coil_transformer").getObject("Shape"))

stl_file = u"part_coil_transformer.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_coil_transformer_v1_'
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
            'exec{(}open{(}"part_coil_transformer.py"{)}.read{(}{)}{)}'
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

# part_support
part_support = Part.makeBox(53, 53, 5)

# cylinder
cylinder = Part.makeCylinder(2.5, 5)

# part_support cut by cylinder for hole 1
cylinder_vector = FreeCAD.Vector(5.5, 5.5, 0)
cylinder.translate(cylinder_vector)
part_support = part_support.cut(cylinder)

# part_support cut by cylinder for hole 2
cylinder_vector = FreeCAD.Vector(42, 0, 0)
cylinder.translate(cylinder_vector)
part_support = part_support.cut(cylinder)

# part_support cut by cylinder for hole 3
cylinder_vector = FreeCAD.Vector(0, 42, 0)
cylinder.translate(cylinder_vector)
part_support = part_support.cut(cylinder)

# part_support cut by cylinder for hole 4
cylinder_vector = FreeCAD.Vector(-42, 0, 0)
cylinder.translate(cylinder_vector)
part_support = part_support.cut(cylinder)

# part_support cut by cylinder for hole 5 for supporting the electrode
cylinder_vector = FreeCAD.Vector(21, -21, 0)
cylinder.translate(cylinder_vector)
part_support = part_support.cut(cylinder)

# box_1
box_1 = Part.makeBox(27, 27, 2)
box_1_vector = FreeCAD.Vector(13, 13, 0)
box_1.translate(box_1_vector)

# part_support cut by box_1
part_support = part_support.cut(box_1)

# box_2
box_2 = Part.makeBox(53, 53, 2)

# box_3
box_3 = Part.makeBox(29, 29, 2)
box_3_vector = FreeCAD.Vector(12, 12, 0)
box_3.translate(box_3_vector)

# box_2 cut by box_3
box_2 = box_2.cut(box_3)

# part_support cut by box_2
part_support = part_support.cut(box_2)

Part.show(part_support)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_support").getObject("Shape"))

stl_file = u"part_support.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_support_v1_'
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
    def test_part_support_v1(self):
        print("test_part_support_v1")

        if os.path.exists("part_support_v1.py"):
            os.remove("part_support_v1.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_support_v1.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_support_v1"


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

# part_support
part_support_v1 = Part.makeBox(53, 53, 8)

# cylinder
cylinder = Part.makeCylinder(2.5, 10)

# part_support_v1 cut by cylinder for hole 1
cylinder_vector = FreeCAD.Vector(5.5, 5.5, 0)
cylinder.translate(cylinder_vector)
part_support_v1 = part_support_v1.cut(cylinder)

# part_support_v1 cut by cylinder for hole 2
cylinder_vector = FreeCAD.Vector(42, 0, 0)
cylinder.translate(cylinder_vector)
part_support_v1 = part_support_v1.cut(cylinder)

# part_support_v1 cut by cylinder for hole 3
cylinder_vector = FreeCAD.Vector(0, 42, 0)
cylinder.translate(cylinder_vector)
part_support_v1 = part_support_v1.cut(cylinder)

# part_support_v1 cut by cylinder for hole 4
cylinder_vector = FreeCAD.Vector(-42, 0, 0)
cylinder.translate(cylinder_vector)
part_support_v1 = part_support_v1.cut(cylinder)

# part_support_v1 cut by cylinder for hole 5 for supporting the electrode
cylinder_vector = FreeCAD.Vector(21, -21, 0)
cylinder.translate(cylinder_vector)
part_support_v1 = part_support_v1.cut(cylinder)

# box_1
box_1 = Part.makeBox(27, 27, 5)
box_1_vector = FreeCAD.Vector(13, 13, 0)
box_1.translate(box_1_vector)

# part_support_v1 cut by box_1
part_support_v1 = part_support_v1.cut(box_1)

# box_2
box_2 = Part.makeBox(53, 53, 5)

# box_3
box_3 = Part.makeBox(29, 29, 5)
box_3_vector = FreeCAD.Vector(12, 12, 0)
box_3.translate(box_3_vector)

# box_2 cut by box_3
box_2 = box_2.cut(box_3)

# part_support_v1 cut by box_2
part_support_v1 = part_support_v1.cut(box_2)

Part.show(part_support_v1)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_support_v1").getObject("Shape"))

stl_file = u"part_support_v1.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_support_v1_v1_'
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
            'exec{(}open{(}"part_support_v1.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

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

height = 53

# tank
tank = Part.makeBox(53, 53, height)

# box_1 for chamber
box_1 = Part.makeBox(25, 25, height)
box_1_vector = FreeCAD.Vector(14, 14, 0)
box_1.translate(box_1_vector)

# cut tank by box_1
tank = tank.cut(box_1)

# box_2
box_2 = Part.makeBox(53, 53, height - 6)

# box_3
box_3 = Part.makeBox(31, 31, height - 6)
box_3_vector = FreeCAD.Vector(11, 11, 0)
box_3.translate(box_3_vector)

# cut box_2 by box_3
box_2 = box_2.cut(box_3)

# tank cut by box_2
box_2_vector = FreeCAD.Vector(0, 0, 3)
box_2.translate(box_2_vector)
tank = tank.cut(box_2)

# cylinder
cylinder = Part.makeCylinder(2.5, height)

# tank cut by cylinder for hole 1
cylinder_vector = FreeCAD.Vector(5.5, 5.5, 0)
cylinder.translate(cylinder_vector)
tank = tank.cut(cylinder)

# tank cut by cylinder for hole 2
cylinder_vector = FreeCAD.Vector(42, 0, 0)
cylinder.translate(cylinder_vector)
tank = tank.cut(cylinder)

# tank cut by cylinder for hole 3
cylinder_vector = FreeCAD.Vector(0, 42, 0)
cylinder.translate(cylinder_vector)
tank = tank.cut(cylinder)

# tank cut by cylinder for hole 4
cylinder_vector = FreeCAD.Vector(-42, 0, 0)
cylinder.translate(cylinder_vector)
tank = tank.cut(cylinder)

# tank cut by cylinder for hole 5
cylinder_output = Part.makeCylinder(2.5, 40)
cylinder_output_vector = FreeCAD.Vector(26.5, 26.5, 8.5)
cylinder_output.translate(cylinder_output_vector)
cylinder_output.rotate(FreeCAD.Vector(26.5, 26.5, 8.5),FreeCAD.Vector(0, 1, 0), 90)
tank = tank.cut(cylinder_output)

# box_4
box_4 = Part.makeBox(29, 29, 2)

# box_5
box_5 = Part.makeBox(27, 27, 2)
box_5_vector = FreeCAD.Vector(1, 1, 0)
box_5.translate(box_5_vector)

# box_4 cut by box_5
box_4 = box_4.cut(box_5)

# tank cut by box_4 for top support
box_4_vector = FreeCAD.Vector(12, 12, 0)
box_4.translate(box_4_vector)
tank = tank.cut(box_4)

# tank cut by box_4 for bottom support
box_4_vector = FreeCAD.Vector(0, 0, height - 2)
box_4.translate(box_4_vector)
tank = tank.cut(box_4)

Part.show(tank)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_tank").getObject("Shape"))

stl_file = u"part_tank.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_tank_v1_'
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
            'exec{(}open{(}"part_tank.py"{)}.read{(}{)}{)}')

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

height = 53

# tank
tank = Part.makeBox(53, 53, height)

# box_1 for chamber
box_1 = Part.makeBox(25, 25, height)
box_1_vector = FreeCAD.Vector(14, 14, 0)
box_1.translate(box_1_vector)

# cut tank by box_1
tank = tank.cut(box_1)

# box_2
box_2 = Part.makeBox(53, 53, height - 6)

# box_3
box_3 = Part.makeBox(31, 31, height - 6)
box_3_vector = FreeCAD.Vector(11, 11, 0)
box_3.translate(box_3_vector)

# cut box_2 by box_3
box_2 = box_2.cut(box_3)

# tank cut by box_2
box_2_vector = FreeCAD.Vector(0, 0, 3)
box_2.translate(box_2_vector)
tank = tank.cut(box_2)

# cylinder
cylinder = Part.makeCylinder(2.5, height)

# tank cut by cylinder for hole 1
cylinder_vector = FreeCAD.Vector(5.5, 5.5, 0)
cylinder.translate(cylinder_vector)
tank = tank.cut(cylinder)

# tank cut by cylinder for hole 2
cylinder_vector = FreeCAD.Vector(42, 0, 0)
cylinder.translate(cylinder_vector)
tank = tank.cut(cylinder)

# tank cut by cylinder for hole 3
cylinder_vector = FreeCAD.Vector(0, 42, 0)
cylinder.translate(cylinder_vector)
tank = tank.cut(cylinder)

# tank cut by cylinder for hole 4
cylinder_vector = FreeCAD.Vector(-42, 0, 0)
cylinder.translate(cylinder_vector)
tank = tank.cut(cylinder)

# tank cut by cylinder for hole 5
cylinder_output = Part.makeCylinder(2.5, 40)
cylinder_output_vector = FreeCAD.Vector(26.5, 26.5, 8.5)
cylinder_output.translate(cylinder_output_vector)
cylinder_output.rotate(FreeCAD.Vector(26.5, 26.5, 8.5),FreeCAD.Vector(0, 1, 0), 90)
tank = tank.cut(cylinder_output)

# box_4
box_4 = Part.makeBox(29, 29, 2)

# box_5
box_5 = Part.makeBox(27, 27, 2)
box_5_vector = FreeCAD.Vector(1, 1, 0)
box_5.translate(box_5_vector)

# box_4 cut by box_5
box_4 = box_4.cut(box_5)

# tank cut by box_4 for top support
box_4_vector = FreeCAD.Vector(12, 12, 0)
box_4.translate(box_4_vector)
tank = tank.cut(box_4)

# tank cut by box_4 for bottom support
box_4_vector = FreeCAD.Vector(0, 0, height - 2)
box_4.translate(box_4_vector)
tank = tank.cut(box_4)

Part.show(tank)

DOC.recompute()

Mesh.insert(u"part_support.stl","assembly")

FreeCAD.getDocument("assembly").getObject("part_support").Placement = App.Placement(App.Vector(0,0,52),App.Rotation(App.Vector(0,0,1),0))

Mesh.insert(u"part_support.stl","assembly")

FreeCAD.getDocument("assembly").getObject("part_support001").Placement = App.Placement(App.Vector(0,53,1),App.Rotation(App.Vector(1,0,0),180))

setview()

# Generate PNG files
file = 'assembly_v1_'
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


if __name__ == '__main__':
    unittest.main()
