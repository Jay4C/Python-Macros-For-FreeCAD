import unittest
import os
import pywinauto.mouse
import pywinauto.keyboard
import time


# Transmute mercury into gold
# https://patents.google.com/patent/FR599762A/en?oq=FR_599762_A
class UnitsTransmutator(unittest.TestCase):
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
            file.write("""import FreeCAD, Part, math, Mesh

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

radius_tank = 20

maximal_height = 40 - radius_tank

radius_inner_tank = radius_tank - 3

# tank
tank = Part.makeSphere(radius_tank)

# sphere_1
sphere_1 = Part.makeSphere(radius_inner_tank)

# tank cut by sphere_1
tank = tank.cut(sphere_1)

# cylinder_1
cylinder_1 = Part.makeCylinder(radius_tank, radius_tank)

# tank cut by cylinder_1
tank = tank.cut(cylinder_1)

# cylinder_2
cylinder_2 = Part.makeCylinder(radius_tank, maximal_height)

# cylinder_3
cylinder_3 = Part.makeCylinder(radius_tank - 3, maximal_height)

# cylinder_2 cut by cylinder_3
cylinder_2 = cylinder_2.cut(cylinder_3)

# tank fuse with cylinder_2
tank = tank.fuse(cylinder_2)

# cylinder_4 for fixing the screw in the bottom of the tank
cylinder_4 = Part.makeCylinder(2.5, 15)
cylinder_4_vector = FreeCAD.Vector(0, 0, -radius_tank)
cylinder_4.translate(cylinder_4_vector)

# tank cut by cylinder_4
tank = tank.cut(cylinder_4)

# cylinder_5
cylinder_5 = Part.makeCylinder(radius_tank + 16, 5)

# cylinder_6
cylinder_6 = Part.makeCylinder(radius_tank - 3, 5)

# cylinder_5 cut by cylinder_6
cylinder_5 = cylinder_5.cut(cylinder_6)

# Cut the holes in cylinder_5 for fixing screws in the top of tank
for i in range(12):
    radius_screw = radius_tank + 10.5
    cylinder = Part.makeCylinder(2.5, 10)
    alpha = (i*2*math.pi)/12
    cylinder_vector = FreeCAD.Vector(radius_screw*math.cos(alpha), radius_screw*math.sin(alpha), 0)
    cylinder.translate(cylinder_vector)
    cylinder_5 = cylinder_5.cut(cylinder)

cylinder_5_vector = FreeCAD.Vector(0, 0, maximal_height)
cylinder_5.translate(cylinder_5_vector)

# tank fuse by cylinder_5
tank = tank.fuse(cylinder_5)

# cylinder_7
cylinder_7 = Part.makeCylinder(radius_tank + 5, 2.5)

# cylinder_8
cylinder_8 = Part.makeCylinder(radius_tank + 2, 2.5)

# cylinder_7 cut by cylinder_8
cylinder_7 = cylinder_7.cut(cylinder_8)

# tank cut by cylinder_7
cylinder_7_vector = FreeCAD.Vector(0, 0, maximal_height + 2.5)
cylinder_7.translate(cylinder_7_vector)
tank = tank.cut(cylinder_7)

Part.show(tank)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_tank").getObject("Shape"))

stl_file = u"/part_tank.stl"

Mesh.export(__objs__, stl_file)

setview()

del __objs__

# Generate PNG files
file = 'part_tank_'
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
    def test_part_top_support_electrodes(self):
        print("test_part_top_support_electrodes")

        if os.path.exists("part_top_electrodes.py"):
            os.remove("part_top_electrodes.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_top_electrodes.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_top_electrodes"


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

radius_tank = 20

# top_electrodes
top_electrodes = Part.makeCylinder(radius_tank + 16, 6)

# cylinder_1
cylinder_1 = Part.makeCylinder(radius_tank + 2, 3)

# top_electrodes cut by cylinder_1
top_electrodes = top_electrodes.cut(cylinder_1)

# Cut the holes in top_electrodes for fixing screws on the tank
for i in range(12):
    radius_screw = radius_tank + 10.5
    cylinder = Part.makeCylinder(2.5, 10)
    alpha = (i*2*math.pi)/12
    cylinder_vector = FreeCAD.Vector(radius_screw*math.cos(alpha), radius_screw*math.sin(alpha), 0)
    cylinder.translate(cylinder_vector)
    top_electrodes = top_electrodes.cut(cylinder)
    
# cylinder_2
cylinder_2 = Part.makeCylinder(radius_tank + 16, 3)

# cylinder_3
cylinder_3 = Part.makeCylinder(radius_tank + 5, 3)

# cylinder_2 cut by cylinder_3
cylinder_2 = cylinder_2.cut(cylinder_3)

# top_electrodes cut by cylinder_2
top_electrodes = top_electrodes.cut(cylinder_2)

# cylinder_4
cylinder_4 = Part.makeCylinder(2.5, 10)

# top_electrodes cut by cylinder_4 for electric arc (plasmas)
top_electrodes = top_electrodes.cut(cylinder_4)

# top_electrodes cut by cylinder_4 for anode (electrolysis) 
cylinder_4_vector = FreeCAD.Vector(10, 0, 0)
cylinder_4.translate(cylinder_4_vector)
top_electrodes = top_electrodes.cut(cylinder_4)

# top_electrodes cut by cylinder_4 for cathode (electrolysis) 
cylinder_4_vector = FreeCAD.Vector(-20, 0, 0)
cylinder_4.translate(cylinder_4_vector)
top_electrodes = top_electrodes.cut(cylinder_4)

Part.show(top_electrodes)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_top_electrodes").getObject("Shape"))

stl_file = u"/part_top_electrodes.stl"

Mesh.export(__objs__, stl_file)

setview()

del __objs__

# Generate PNG files
file = 'part_top_electrodes_'
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
            'exec{(}open{(}"part_top_electrodes.py"{)}.read{(}{)}{)}')

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_part_top_support_gas(self):
        print("test_part_top_support_gas")

        if os.path.exists("part_top_support_gas.py"):
            os.remove("part_top_support_gas.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_top_support_gas.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_top_support_gas"


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

radius_tank = 20

# top_support_gas
top_support_gas = Part.makeCylinder(radius_tank + 16, 6)

# cylinder_1
cylinder_1 = Part.makeCylinder(radius_tank + 2, 3)

# top_support_gas cut by cylinder_1
top_support_gas = top_support_gas.cut(cylinder_1)

# Cut the holes in top_support_gas for fixing screws on the tank
for i in range(12):
    radius_screw = radius_tank + 10.5
    cylinder = Part.makeCylinder(2.5, 10)
    alpha = (i*2*math.pi)/12
    cylinder_vector = FreeCAD.Vector(radius_screw*math.cos(alpha), radius_screw*math.sin(alpha), 0)
    cylinder.translate(cylinder_vector)
    top_support_gas = top_support_gas.cut(cylinder)

# cylinder_2
cylinder_2 = Part.makeCylinder(radius_tank + 16, 3)

# cylinder_3
cylinder_3 = Part.makeCylinder(radius_tank + 5, 3)

# cylinder_2 cut by cylinder_3
cylinder_2 = cylinder_2.cut(cylinder_3)

# top_support_gas cut by cylinder_2
top_support_gas = top_support_gas.cut(cylinder_2)

# cylinder_4
cylinder_4 = Part.makeCylinder(8, 10)

# top_support_gas cut by cylinder_4 for the out of the gas
top_support_gas = top_support_gas.cut(cylinder_4)

Part.show(top_support_gas)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_top_support_gas").getObject("Shape"))

stl_file = u"/part_top_support_gas.stl"

Mesh.export(__objs__, stl_file)

setview()

del __objs__

# Generate PNG files
file = 'part_top_support_gas_'
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
            'exec{(}open{(}"part_top_support_gas.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_part_electrode(self):
        print("test_part_electrode")

        if os.path.exists("part_electrode.py"):
            os.remove("part_electrode.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_electrode.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_electrode"


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

# electrode
electrode = Part.makeCylinder(2.5, 80)

Part.show(electrode)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_electrode").getObject("Shape"))

stl_file = u"/part_electrode.stl"

Mesh.export(__objs__, stl_file)

setview()

del __objs__

# Generate PNG files
file = 'part_electrode_'
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
            'exec{(}open{(}"part_electrode.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_part_ecrou(self):
        print("test_part_ecrou")

        if os.path.exists("part_ecrou.py"):
            os.remove("part_ecrou.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_ecrou.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_ecrou"


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

# ecrou
ecrou = Part.makeCylinder(4.5, 4)

# cylinder_1
cylinder_1 = Part.makeCylinder(2.5, 5)

# ecrou cut by cylinder_1
ecrou = ecrou.cut(cylinder_1)

Part.show(ecrou)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_ecrou").getObject("Shape"))

stl_file = u"/part_ecrou.stl"

Mesh.export(__objs__, stl_file)

setview()

del __objs__

# Generate PNG files
file = 'part_ecrou_'
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
            'exec{(}open{(}"part_ecrou.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_assembly_with_electrodes(self):
        print("test_assembly_with_electrodes")

        if os.path.exists("assembly_with_electrodes.py"):
            os.remove("assembly_with_electrodes.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("assembly_with_electrodes.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_with_electrodes"


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

radius_tank = 20

maximal_height = 40 - radius_tank

radius_inner_tank = radius_tank - 3

# tank
tank = Part.makeSphere(radius_tank)

# sphere_1
sphere_1 = Part.makeSphere(radius_inner_tank)

# tank cut by sphere_1
tank = tank.cut(sphere_1)

# cylinder_1
cylinder_1 = Part.makeCylinder(radius_tank, radius_tank)

# tank cut by cylinder_1
tank = tank.cut(cylinder_1)

# cylinder_2
cylinder_2 = Part.makeCylinder(radius_tank, maximal_height)

# cylinder_3
cylinder_3 = Part.makeCylinder(radius_tank - 3, maximal_height)

# cylinder_2 cut by cylinder_3
cylinder_2 = cylinder_2.cut(cylinder_3)

# tank fuse with cylinder_2
tank = tank.fuse(cylinder_2)

# cylinder_4 for fixing the screw in the bottom of the tank
cylinder_4 = Part.makeCylinder(2.5, 15)
cylinder_4_vector = FreeCAD.Vector(0, 0, -radius_tank)
cylinder_4.translate(cylinder_4_vector)

# tank cut by cylinder_4
tank = tank.cut(cylinder_4)

# cylinder_5
cylinder_5 = Part.makeCylinder(radius_tank + 16, 5)

# cylinder_6
cylinder_6 = Part.makeCylinder(radius_tank - 3, 5)

# cylinder_5 cut by cylinder_6
cylinder_5 = cylinder_5.cut(cylinder_6)

# Cut the holes in cylinder_5 for fixing screws in the top of tank
for i in range(12):
    radius_screw = radius_tank + 10.5
    cylinder = Part.makeCylinder(2.5, 10)
    alpha = (i*2*math.pi)/12
    cylinder_vector = FreeCAD.Vector(radius_screw*math.cos(alpha), radius_screw*math.sin(alpha), 0)
    cylinder.translate(cylinder_vector)
    cylinder_5 = cylinder_5.cut(cylinder)

cylinder_5_vector = FreeCAD.Vector(0, 0, maximal_height)
cylinder_5.translate(cylinder_5_vector)

# tank fuse by cylinder_5
tank = tank.fuse(cylinder_5)

# cylinder_7
cylinder_7 = Part.makeCylinder(radius_tank + 5, 2.5)

# cylinder_8
cylinder_8 = Part.makeCylinder(radius_tank + 2, 2.5)

# cylinder_7 cut by cylinder_8
cylinder_7 = cylinder_7.cut(cylinder_8)

# tank cut by cylinder_7
cylinder_7_vector = FreeCAD.Vector(0, 0, maximal_height + 2.5)
cylinder_7.translate(cylinder_7_vector)
tank = tank.cut(cylinder_7)

Part.show(tank)

DOC.recompute()

# Insert part_top_electrodes
Mesh.insert(u"part_top_electrodes.stl","assembly_with_electrodes")
FreeCAD.getDocument("assembly_with_electrodes").getObject("part_top_electrodes").Placement = App.Placement(App.Vector(0, 0, maximal_height + 2.5),App.Rotation(App.Vector(0,0,0),0))

# Insert part_electrode
Mesh.insert(u"part_electrode.stl","assembly_with_electrodes")
FreeCAD.getDocument("assembly_with_electrodes").getObject("part_electrode").Placement = App.Placement(App.Vector(0, 0, -radius_tank/3),App.Rotation(App.Vector(0,0,0),0))

# Insert part_electrode
Mesh.insert(u"part_electrode.stl","assembly_with_electrodes")
FreeCAD.getDocument("assembly_with_electrodes").getObject("part_electrode001").Placement = App.Placement(App.Vector(10, 0, -radius_tank/3),App.Rotation(App.Vector(0,0,0),0))

# Insert part_electrode
Mesh.insert(u"part_electrode.stl","assembly_with_electrodes")
FreeCAD.getDocument("assembly_with_electrodes").getObject("part_electrode002").Placement = App.Placement(App.Vector(-10, 0, -radius_tank/3),App.Rotation(App.Vector(0,0,0),0))

# Insert part_ecrou
Mesh.insert(u"part_ecrou.stl","assembly_with_electrodes")
FreeCAD.getDocument("assembly_with_electrodes").getObject("part_ecrou").Placement = App.Placement(App.Vector(0, 0, radius_tank/3),App.Rotation(App.Vector(0,0,0),0))

# Insert part_ecrou
Mesh.insert(u"part_ecrou.stl","assembly_with_electrodes")
FreeCAD.getDocument("assembly_with_electrodes").getObject("part_ecrou001").Placement = App.Placement(App.Vector(10, 0, radius_tank/3),App.Rotation(App.Vector(0,0,0),0))

# Insert part_ecrou
Mesh.insert(u"part_ecrou.stl","assembly_with_electrodes")
FreeCAD.getDocument("assembly_with_electrodes").getObject("part_ecrou002").Placement = App.Placement(App.Vector(-10, 0, radius_tank/3),App.Rotation(App.Vector(0,0,0),0))

setview()

# Generate PNG files
file = 'assembly_with_electrodes_'
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
            'exec{(}open{(}"assembly_with_electrodes.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_assembly_with_gas(self):
        print("test_assembly_with_gas")

        if os.path.exists("assembly_with_gas.py"):
            os.remove("assembly_with_gas.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("assembly_with_gas.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_with_gas"


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

radius_tank = 20

maximal_height = 40 - radius_tank

radius_inner_tank = radius_tank - 3

# tank
tank = Part.makeSphere(radius_tank)

# sphere_1
sphere_1 = Part.makeSphere(radius_inner_tank)

# tank cut by sphere_1
tank = tank.cut(sphere_1)

# cylinder_1
cylinder_1 = Part.makeCylinder(radius_tank, radius_tank)

# tank cut by cylinder_1
tank = tank.cut(cylinder_1)

# cylinder_2
cylinder_2 = Part.makeCylinder(radius_tank, maximal_height)

# cylinder_3
cylinder_3 = Part.makeCylinder(radius_tank - 3, maximal_height)

# cylinder_2 cut by cylinder_3
cylinder_2 = cylinder_2.cut(cylinder_3)

# tank fuse with cylinder_2
tank = tank.fuse(cylinder_2)

# cylinder_4 for fixing the screw in the bottom of the tank
cylinder_4 = Part.makeCylinder(2.5, 15)
cylinder_4_vector = FreeCAD.Vector(0, 0, -radius_tank)
cylinder_4.translate(cylinder_4_vector)

# tank cut by cylinder_4
tank = tank.cut(cylinder_4)

# cylinder_5
cylinder_5 = Part.makeCylinder(radius_tank + 16, 5)

# cylinder_6
cylinder_6 = Part.makeCylinder(radius_tank - 3, 5)

# cylinder_5 cut by cylinder_6
cylinder_5 = cylinder_5.cut(cylinder_6)

# Cut the holes in cylinder_5 for fixing screws in the top of tank
for i in range(12):
    radius_screw = radius_tank + 10.5
    cylinder = Part.makeCylinder(2.5, 10)
    alpha = (i*2*math.pi)/12
    cylinder_vector = FreeCAD.Vector(radius_screw*math.cos(alpha), radius_screw*math.sin(alpha), 0)
    cylinder.translate(cylinder_vector)
    cylinder_5 = cylinder_5.cut(cylinder)

cylinder_5_vector = FreeCAD.Vector(0, 0, maximal_height)
cylinder_5.translate(cylinder_5_vector)

# tank fuse by cylinder_5
tank = tank.fuse(cylinder_5)

# cylinder_7
cylinder_7 = Part.makeCylinder(radius_tank + 5, 2.5)

# cylinder_8
cylinder_8 = Part.makeCylinder(radius_tank + 2, 2.5)

# cylinder_7 cut by cylinder_8
cylinder_7 = cylinder_7.cut(cylinder_8)

# tank cut by cylinder_7
cylinder_7_vector = FreeCAD.Vector(0, 0, maximal_height + 2.5)
cylinder_7.translate(cylinder_7_vector)
tank = tank.cut(cylinder_7)

Part.show(tank)

DOC.recompute()

Mesh.insert(u"part_top_support_gas.stl", "assembly_with_gas")

FreeCAD.getDocument("assembly_with_gas").getObject("part_top_support_gas").Placement = App.Placement(App.Vector(0, 0, maximal_height + 2.5), App.Rotation(App.Vector(0,0,0), 0))

setview()

# Generate PNG files
file = 'assembly_with_gas_'
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
            'exec{(}open{(}"assembly_with_gas.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')


if __name__ == '__main__':
    unittest.main()
