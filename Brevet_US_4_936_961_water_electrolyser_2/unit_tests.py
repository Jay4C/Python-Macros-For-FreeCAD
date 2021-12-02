import time
import unittest
import os
import pywinauto.mouse
import pywinauto.keyboard


class brevet_us_4_936_961_water_electrolyser_2(unittest.TestCase):
    # ok
    def test_assembly_of_the_voltage_intensifier_circuit_in_stl_format(self):
        print("test_assembly_of_the_voltage_intensifier_circuit_in_stl_format")

        if os.path.exists("assembly_of_the_voltage_intensifier_circuit.py"):
            os.remove("assembly_of_the_voltage_intensifier_circuit.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("assembly_of_the_voltage_intensifier_circuit.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_of_the_voltage_intensifier_circuit"


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

# part_squelette_primaire_d80_l80
cylinder_1 = Part.makeCylinder(40, 80)

cylinder_2 = Part.makeCylinder(6, 80)

# cylinder_1 cut by cylinder_2
cylinder_1 = cylinder_1.cut(cylinder_2)

cylinder_3 = Part.makeCylinder(40, 33.5)

cylinder_4 = Part.makeCylinder(8, 33.5)

# cylinder_3 cut by cylinder_4
cylinder_3 = cylinder_3.cut(cylinder_4)

# cylinder_1 cut by cylinder_3 in 2 times
cylinder_3_vector = FreeCAD.Vector(0, 0, 2)
cylinder_3.translate(cylinder_3_vector)
cylinder_1 = cylinder_1.cut(cylinder_3)
cylinder_3_vector = FreeCAD.Vector(0, 0, 42.5)
cylinder_3.translate(cylinder_3_vector)
cylinder_1 = cylinder_1.cut(cylinder_3)

cylinder_5 = Part.makeCylinder(40, 5)

cylinder_6 = Part.makeCylinder(8, 5)

# cylinder_5 cut by cylinder_6
cylinder_5 = cylinder_5.cut(cylinder_6)

# cylinder_1 cut by cylinder_5
cylinder_5_vector = FreeCAD.Vector(0, 0, 37.5)
cylinder_5.translate(cylinder_5_vector)
cylinder_1 = cylinder_1.cut(cylinder_5)

Part.show(cylinder_1)

DOC.recompute()

# change color of assembly_of_the_voltage_intensifier_circuit
FreeCADGui.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("Shape").ShapeColor = (0.67,0.00,0.00)

# insertion part_squelette_secondaire_d80_l80
Mesh.insert(u"part_squelette_secondaire_d80_l80.stl", "assembly_of_the_voltage_intensifier_circuit")
FreeCAD.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("part_squelette_secondaire_d80_l80").Placement = App.Placement(App.Vector(84, 0, 0), App.Rotation(App.Vector(1,0,0), 0))
FreeCADGui.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("part_squelette_secondaire_d80_l80").ShapeColor = (0.33,1.00,1.00)

# insertion equerre_assemblage_plat_l100 - 1
Mesh.insert(u"equerre_assemblage_plat_l100.stl", "assembly_of_the_voltage_intensifier_circuit")
FreeCAD.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("equerre_assemblage_plat_l100").Placement = App.Placement(App.Vector(-8, -8, -2), App.Rotation(App.Vector(1,0,0), 0))
FreeCADGui.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("equerre_assemblage_plat_l100").ShapeColor = (1.00,1.00,0.50)

# insertion equerre_assemblage_plat_l100 - 2
Mesh.insert(u"equerre_assemblage_plat_l100.stl", "assembly_of_the_voltage_intensifier_circuit")
FreeCAD.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("equerre_assemblage_plat_l100001").Placement = App.Placement(App.Vector(-8, -8, -4), App.Rotation(App.Vector(1,0,0), 0))
FreeCADGui.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("equerre_assemblage_plat_l100001").ShapeColor = (1.00,0.33,1.00)

# insertion equerre_assemblage_plat_l100 - 3
Mesh.insert(u"equerre_assemblage_plat_l100.stl", "assembly_of_the_voltage_intensifier_circuit")
FreeCAD.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("equerre_assemblage_plat_l100002").Placement = App.Placement(App.Vector(-8, -8, 80), App.Rotation(App.Vector(1,0,0), 0))
FreeCADGui.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("equerre_assemblage_plat_l100002").ShapeColor = (1.00,1.00,0.50)

# insertion equerre_assemblage_plat_l100 - 4
Mesh.insert(u"equerre_assemblage_plat_l100.stl", "assembly_of_the_voltage_intensifier_circuit")
FreeCAD.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("equerre_assemblage_plat_l100003").Placement = App.Placement(App.Vector(-8, -8, 82), App.Rotation(App.Vector(1,0,0), 0))
FreeCADGui.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("equerre_assemblage_plat_l100003").ShapeColor = (1.00,0.33,1.00)

# insertion part_equerre_assemblage_angle_droit_l42 - 1
Mesh.insert(u"part_equerre_assemblage_angle_droit_l42.stl", "assembly_of_the_voltage_intensifier_circuit")
FreeCAD.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("part_equerre_assemblage_angle_droit_l42").Placement = App.Placement(App.Vector(-8, -32.5, -4), App.Rotation(App.Vector(0,1,0), 90))
FreeCADGui.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("part_equerre_assemblage_angle_droit_l42").ShapeColor = (1.00,0.33,0.00)

# insertion part_equerre_assemblage_angle_droit_l42 - 2
Mesh.insert(u"part_equerre_assemblage_angle_droit_l42.stl", "assembly_of_the_voltage_intensifier_circuit")
FreeCAD.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("part_equerre_assemblage_angle_droit_l42001").Placement = App.Placement(App.Vector(78, -32.5, -4), App.Rotation(App.Vector(0,1,0), 90))
FreeCADGui.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("part_equerre_assemblage_angle_droit_l42001").ShapeColor = (1.00,0.33,0.00)

# insertion part_equerre_assemblage_angle_droit_l42 - 3
Mesh.insert(u"part_equerre_assemblage_angle_droit_l42.stl", "assembly_of_the_voltage_intensifier_circuit")
FreeCAD.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("part_equerre_assemblage_angle_droit_l42002").Placement = App.Placement(App.Vector(8, -32.5, 84), App.Rotation(App.Vector(0,1,0), -90))
FreeCADGui.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("part_equerre_assemblage_angle_droit_l42002").ShapeColor = (1.00,0.33,0.00)

# insertion part_equerre_assemblage_angle_droit_l42 - 4
Mesh.insert(u"part_equerre_assemblage_angle_droit_l42.stl", "assembly_of_the_voltage_intensifier_circuit")
FreeCAD.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("part_equerre_assemblage_angle_droit_l42003").Placement = App.Placement(App.Vector(90, -32.5, 84), App.Rotation(App.Vector(0,1,0), -90))
FreeCADGui.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("part_equerre_assemblage_angle_droit_l42003").ShapeColor = (1.00,0.33,0.00)

# insertion part_vis_metal_m12_l100 - 1
Mesh.insert(u"part_vis_metal_m12_l100.stl", "assembly_of_the_voltage_intensifier_circuit")
FreeCAD.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("part_vis_metal_m12_l100").Placement = App.Placement(App.Vector(0, 0, -14), App.Rotation(App.Vector(0,1,0), 0))
FreeCADGui.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("part_vis_metal_m12_l100").ShapeColor = (0.67,0.67,0.00)

# insertion part_vis_metal_m12_l100 - 2
Mesh.insert(u"part_vis_metal_m12_l100.stl", "assembly_of_the_voltage_intensifier_circuit")
FreeCAD.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("part_vis_metal_m12_l100001").Placement = App.Placement(App.Vector(84, 0, -14), App.Rotation(App.Vector(0,1,0), 0))
FreeCADGui.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("part_vis_metal_m12_l100001").ShapeColor = (0.67,0.67,0.00)

# insertion part_ecrou_m12 - 1
Mesh.insert(u"part_ecrou_m12.stl", "assembly_of_the_voltage_intensifier_circuit")
FreeCAD.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("part_ecrou_m12").Placement = App.Placement(App.Vector(0, 0, 86), App.Rotation(App.Vector(0,1,0), 0))
FreeCADGui.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("part_ecrou_m12").ShapeColor = (0.67,0.33,0.50)

# insertion part_ecrou_m12 - 2
Mesh.insert(u"part_ecrou_m12.stl", "assembly_of_the_voltage_intensifier_circuit")
FreeCAD.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("part_ecrou_m12001").Placement = App.Placement(App.Vector(84, 0, 86), App.Rotation(App.Vector(0,1,0), 0))
FreeCADGui.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("part_ecrou_m12001").ShapeColor = (0.67,0.33,0.50)

__objs__=[]
__objs__.append(FreeCAD.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("Shape"))
__objs__.append(FreeCAD.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("part_squelette_secondaire_d80_l80"))
__objs__.append(FreeCAD.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("equerre_assemblage_plat_l100"))
__objs__.append(FreeCAD.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("equerre_assemblage_plat_l100001"))
__objs__.append(FreeCAD.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("equerre_assemblage_plat_l100002"))
__objs__.append(FreeCAD.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("equerre_assemblage_plat_l100003"))
__objs__.append(FreeCAD.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("part_equerre_assemblage_angle_droit_l42"))
__objs__.append(FreeCAD.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("part_equerre_assemblage_angle_droit_l42001"))
__objs__.append(FreeCAD.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("part_equerre_assemblage_angle_droit_l42002"))
__objs__.append(FreeCAD.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("part_equerre_assemblage_angle_droit_l42003"))
__objs__.append(FreeCAD.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("part_vis_metal_m12_l100"))
__objs__.append(FreeCAD.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("part_vis_metal_m12_l100001"))
__objs__.append(FreeCAD.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("part_ecrou_m12"))
__objs__.append(FreeCAD.getDocument("assembly_of_the_voltage_intensifier_circuit").getObject("part_ecrou_m12001"))

Mesh.export(__objs__,u"assembly_of_the_voltage_intensifier_circuit.stl")
 
del __objs__

setview()
         """)

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"assembly_of_the_voltage_intensifier_circuit.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_part_for_the_squelette_primaire_d80_l80_in_stl_format(self):
        print('test_part_for_the_squelette_primaire_d80_l80_in_stl_format')

        if os.path.exists("part_squelette_primaire_d80_l80.py"):
            os.remove("part_squelette_primaire_d80_l80.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_squelette_primaire_d80_l80.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_squelette_primaire_d80_l80"


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

cylinder_1 = Part.makeCylinder(40, 80)

cylinder_2 = Part.makeCylinder(5, 80)

# cylinder_1 cut by cylinder_2
cylinder_1 = cylinder_1.cut(cylinder_2)

cylinder_3 = Part.makeCylinder(40, 33.5)

cylinder_4 = Part.makeCylinder(26/2, 33.5)

# cylinder_3 cut by cylinder_4
cylinder_3 = cylinder_3.cut(cylinder_4)

# cylinder_1 cut by cylinder_3 in 2 times
cylinder_3_vector = FreeCAD.Vector(0, 0, 2)
cylinder_3.translate(cylinder_3_vector)
cylinder_1 = cylinder_1.cut(cylinder_3)
cylinder_3_vector = FreeCAD.Vector(0, 0, 42.5)
cylinder_3.translate(cylinder_3_vector)
cylinder_1 = cylinder_1.cut(cylinder_3)

cylinder_5 = Part.makeCylinder(40, 5)

cylinder_6 = Part.makeCylinder(26/2, 5)

# cylinder_5 cut by cylinder_6
cylinder_5 = cylinder_5.cut(cylinder_6)

# cylinder_1 cut by cylinder_5
cylinder_5_vector = FreeCAD.Vector(0, 0, 37.5)
cylinder_5.translate(cylinder_5_vector)
cylinder_1 = cylinder_1.cut(cylinder_5)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_squelette_primaire_d80_l80").getObject("Shape"))

stl_file = u"part_squelette_primaire_d80_l80.stl"

Mesh.export(__objs__, stl_file)

setview()
        """)

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"part_squelette_primaire_d80_l80.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_part_for_the_squelette_secondaire_d80_l80_in_stl_format(self):
        print('test_part_for_the_squelette_secondaire_d80_l80_in_stl_format')

        if os.path.exists("part_squelette_secondaire_d80_l80.py"):
            os.remove("part_squelette_secondaire_d80_l80.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_squelette_secondaire_d80_l80.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_squelette_secondaire_d80_l80"


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

cylinder_1 = Part.makeCylinder(40, 80)

cylinder_2 = Part.makeCylinder(5, 80)

cylinder_3 = Part.makeCylinder(40, 37)

cylinder_4 = Part.makeCylinder(26/2, 37)

# cylinder_1 cut by cylinder_2
cylinder_1 = cylinder_1.cut(cylinder_2)

# cylinder_3 cut by cylinder_4
cylinder_3 = cylinder_3.cut(cylinder_4)

# cylinder_1 cut by cylinder_3 in 2 times
cylinder_3_vector = FreeCAD.Vector(0, 0, 2)
cylinder_3.translate(cylinder_3_vector)
cylinder_1 = cylinder_1.cut(cylinder_3)
cylinder_3_vector = FreeCAD.Vector(0, 0, 39)
cylinder_3.translate(cylinder_3_vector)
cylinder_1 = cylinder_1.cut(cylinder_3)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_squelette_secondaire_d80_l80").getObject("Shape"))

stl_file = u"part_squelette_secondaire_d80_l80.stl"

Mesh.export(__objs__, stl_file)

setview()
        """)

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"part_squelette_secondaire_d80_l80.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_part_for_the_squelette_d35_l80_in_stl_format(self):
        print('test_part_for_the_squelette_d35_l80_in_stl_format')

        if os.path.exists("part_squelette_d35_l80.py"):
            os.remove("part_squelette_d35_l80.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_squelette_d35_l80.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh, math, ImportGui

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_squelette_d35_l80"


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

cylinder_1 = Part.makeCylinder(35/2, 80)

cylinder_2 = Part.makeCylinder(5, 80)

cylinder_3 = Part.makeCylinder(35/2, 37)

cylinder_4 = Part.makeCylinder(26/2, 37)

# cylinder_1 cut by cylinder_2
cylinder_1 = cylinder_1.cut(cylinder_2)

# cylinder_3 cut by cylinder_4
cylinder_3 = cylinder_3.cut(cylinder_4)

# cylinder_1 cut by cylinder_3 in 2 times
cylinder_3_vector = FreeCAD.Vector(0, 0, 2)
cylinder_3.translate(cylinder_3_vector)
cylinder_1 = cylinder_1.cut(cylinder_3)
cylinder_3_vector = FreeCAD.Vector(0, 0, 39)
cylinder_3.translate(cylinder_3_vector)
cylinder_1 = cylinder_1.cut(cylinder_3)

# cylinder_1 cut by cylinder_5 in several times
degre = 40
for i in range(int(360/degre)):
    radius = 5 + 1.5 + 2.5
    alpha=(i*degre*math.pi)/180
    cylinder_5_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    cylinder_5 = Part.makeCylinder(2.5, 80)
    cylinder_5.translate(cylinder_5_vector)
    cylinder_1 = cylinder_1.cut(cylinder_5)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_squelette_d35_l80").getObject("Shape"))

stl_file = u"part_squelette_d35_l80.stl"

Mesh.export(__objs__, stl_file)

step_file = u"part_squelette_d35_l80.step"

ImportGui.export(__objs__, step_file)

setview()
        """)

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"part_squelette_d35_l80.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_part_for_the_equerre_assemblage_angle_droit_l42_in_stl_format(self):
        print("test_part_for_the_equerre_assemblage_angle_droit_l42_in_stl_format")

        if os.path.exists("part_equerre_assemblage_angle_droit_l42.py"):
            os.remove("part_equerre_assemblage_angle_droit_l42.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_equerre_assemblage_angle_droit_l42.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_equerre_assemblage_angle_droit_l42"


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

box_1 = Part.makeBox(42, 42, 15)

box_2 = Part.makeBox(40, 40, 15)

# box_1 cut by box_2
box_2_vector = FreeCAD.Vector(2, 2, 0)
box_2.translate(box_2_vector)
box_1 = box_1.cut(box_2)

cylinder_1 = Part.makeCylinder(6, 3)

# box_1 cut by cylinder_1
cylinder_1_vector = FreeCAD.Vector(0, 32.5, 7.5)
cylinder_1.translate(cylinder_1_vector)
axe_y  = FreeCAD.Vector(0, 1, 0)
cylinder_1.rotate(cylinder_1_vector, axe_y, 90)
box_1 = box_1.cut(cylinder_1)

cylinder_2 = Part.makeCylinder(2.5, 3)

# box_1 cut by cylinder_2
cylinder_2_vector = FreeCAD.Vector(35, 0, 7.5)
cylinder_2.translate(cylinder_2_vector)
axe_x = FreeCAD.Vector(1, 0, 0)
cylinder_2.rotate(cylinder_2_vector, axe_x, -90)
box_1 = box_1.cut(cylinder_2)

Part.show(box_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_equerre_assemblage_angle_droit_l42").getObject("Shape"))

stl_file = u"part_equerre_assemblage_angle_droit_l42.stl"

Mesh.export(__objs__, stl_file)

setview()
        """)

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"part_equerre_assemblage_angle_droit_l42.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_part_for_the_equerre_assemblage_plat_l100_in_stl_format(self):
        print("test_part_for_the_equerre_assemblage_plat_l100_in_stl_format")

        if os.path.exists("equerre_assemblage_plat_l100.py"):
            os.remove("equerre_assemblage_plat_l100.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("equerre_assemblage_plat_l100.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "equerre_assemblage_plat_l100"


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

box_1 = Part.makeBox(100, 15, 2)

cylinder_1 = Part.makeCylinder(6, 3)

# box_1 cut by cilnder_1 in 2 times
cylinder_1_vector = FreeCAD.Vector(8, 7.5, 0)
cylinder_1.translate(cylinder_1_vector)
box_1 = box_1.cut(cylinder_1)

cylinder_1_vector = FreeCAD.Vector(84, 0, 0)
cylinder_1.translate(cylinder_1_vector)
box_1 = box_1.cut(cylinder_1)

Part.show(box_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("equerre_assemblage_plat_l100").getObject("Shape"))

stl_file = u"equerre_assemblage_plat_l100.stl"

Mesh.export(__objs__, stl_file)

setview()
        """)

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"equerre_assemblage_plat_l100.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_part_for_the_vis_metal_m12_l100_in_stl_format(self):
        print('test_part_for_the_vis_metal_m12_l100_in_stl_format')

        if os.path.exists("part_vis_metal_m12_l100.py"):
            os.remove("part_vis_metal_m12_l100.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_vis_metal_m12_l100.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_vis_metal_m12_l100"


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

cylinder_1 = Part.makeCylinder(11, 108)

cylinder_2 = Part.makeCylinder(6, 100)
 
cylinder_3 = Part.makeCylinder(11, 100)

# cylinder_3 cut by cylinder_2
cylinder_3 = cylinder_3.cut(cylinder_2)

# cylinder_1 cut by cylinder_3
cylinder_3_vector = FreeCAD.Vector(0, 0, 8)
cylinder_3.translate(cylinder_3_vector)
cylinder_1 = cylinder_1.cut(cylinder_3)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_vis_metal_m12_l100").getObject("Shape"))

stl_file = u"part_vis_metal_m12_l100.stl"

Mesh.export(__objs__, stl_file)

setview()
            """)

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"part_vis_metal_m12_l100.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_part_for_the_ecrou_m12_in_stl_format(self):
        print('test_part_for_the_ecrou_m12_in_stl_format')

        if os.path.exists("part_ecrou_m12.py"):
            os.remove("part_ecrou_m12.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_ecrou_m12.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_ecrou_m12"


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

cylinder_1 = Part.makeCylinder(11, 10)

cylinder_2 = Part.makeCylinder(6, 10)

cylinder_1 = cylinder_1.cut(cylinder_2)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_ecrou_m12").getObject("Shape"))

stl_file = u"part_ecrou_m12.stl"

Mesh.export(__objs__, stl_file)

setview()
    """)

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"part_ecrou_m12.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_part_for_the_cathode_of_the_electrolyser_in_step_format(self):
        print("test_part_for_the_cathode_of_the_electrolyser_in_step_format")

        # Dimensions : radius = 4 mm and height = 300 mm

        if os.path.exists("part_cathode.py"):
            os.remove("part_cathode.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_cathode.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_cathode"


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

cylinder_1 = Part.makeCylinder(4, 180)

cylinder_2 = Part.makeCylinder(3, 180)

cut_1 = cylinder_1.cut(cylinder_2)

Part.show(cut_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_cathode").getObject("Shape"))

stl_file = u"part_cathode.stl"

Mesh.export(__objs__, stl_file)

setview()
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"part_cathode.py"{)}.read{(}{)}{)}')

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_part_for_the_anode_of_the_electrolyser_in_step_format(self):
        print("test_part_for_the_anode_of_the_electrolyser_in_step_format")

        # Dimensions : radius = 2 mm and height = 300 mm

        if os.path.exists("part_anode.py"):
            os.remove("part_anode.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_anode.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_anode"


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

cylinder_1 = Part.makeCylinder(2, 200)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_anode").getObject("Shape"))

stl_file = u"part_anode.stl"

Mesh.export(__objs__, stl_file)

setview()
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"part_anode.py"{)}.read{(}{)}{)}')

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.youtube.com/watch?v=5pctHhgaJVw
    def test_part_for_the_transformer_in_step_format(self):
        print("test_part_for_the_block_of_coil_of_the_transformer_in_step_format")

        if os.path.exists("part_transformer.py"):
            os.remove("part_transformer.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_transformer.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_transformer"

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

# transformer
transformer = Part.makeBox(65.4, 50.8, 87.4776)

# ferroxcube_1
ferroxcube_1 = Part.makeBox(28, 16, 87.4776)
ferroxcube_1_vector = FreeCAD.Vector(18.7, 17.4, 0)
ferroxcube_1.translate(ferroxcube_1_vector)

# cut transformer with ferroxcube_1
transformer = transformer.cut(ferroxcube_1)

# coil
coil = Part.makeBox(65.4, 50.8, 33.3248)

# ferroxcube_2
ferroxcube_2 = Part.makeBox(32, 20, 33.3248)
ferroxcube_2_vector = FreeCAD.Vector(16.7, 15.4, 0)
ferroxcube_2.translate(ferroxcube_2_vector)

# cut coil with ferroxcube_2
coil = coil.cut(ferroxcube_2)

# first cut for transformer with coil
coil_vector = FreeCAD.Vector(0, 0, 2.794)
coil.translate(coil_vector)
transformer = transformer.cut(coil)

# second cut for transformer with coil
coil_vector = FreeCAD.Vector(0, 0, 48.5648)
coil.translate(coil_vector)
transformer = transformer.cut(coil)

# pick_up_coil
pick_up_coil = Part.makeBox(65.4, 50.8, 9.652)

# cut pick_up_coil with ferroxcube_2
pick_up_coil = pick_up_coil.cut(ferroxcube_2)

# cut for transformer with pick_up_coil
pick_up_coil_vector = FreeCAD.Vector(0, 0, 38.9128)
pick_up_coil.translate(pick_up_coil_vector)
transformer = transformer.cut(pick_up_coil)

Part.show(transformer)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_transformer").getObject("Shape"))

stl_file = u"part_transformer.stl"

Mesh.export(__objs__, stl_file)

setview()
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"part_transformer.py"{)}.read{(}{)}{)}')

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_part_for_the_spacer_between_the_anode_and_the_cathode_in_step_format(self):
        print("test_part_for_the_spacer_between_the_anode_and_the_cathode_in_step_format")

        if os.path.exists("part_spacer.py"):
            os.remove("part_spacer.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_spacer.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_spacer"


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

# spacer
spacer = Part.makeCylinder(4.5, 15)

# anode
anode = Part.makeCylinder(2, 15)

# cut spacer by anode
spacer = spacer.cut(anode)

# space_anode_cathode
space_anode_cathode = Part.makeCylinder(4.5, 13)

# space_plus_anode
space_plus_anode = Part.makeCylinder(3, 13)

# space_anode_cathode cut by space_plus_anode
space_anode_cathode = space_anode_cathode.cut(space_plus_anode)

# spacer cut by space_anode_cathode
space_anode_cathode_vector = FreeCAD.Vector(0, 0, 2)
space_anode_cathode.translate(space_anode_cathode_vector)
spacer = spacer.cut(space_anode_cathode)

# space_bubble
degre = 10
for i in range(int(360/degre)):
    radius = 2
    alpha=(i*degre*math.pi)/180
    space_bubble_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    space_bubble = Part.makeCylinder(0.3, 15)
    space_bubble.translate(space_bubble_vector)
    spacer = spacer.cut(space_bubble)

Part.show(spacer)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_spacer").getObject("Shape"))

stl_file = u"part_spacer.stl"

Mesh.export(__objs__, stl_file)

setview()
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"part_spacer.py"{)}.read{(}{)}{)}')

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_part_for_the_tank_of_the_electrolyzer_in_step_format(self):
        print("test_part_for_the_tank_of_the_electrolyzer_in_step_format")

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

# tank
tank = Part.makeBox(200, 200, 250)

# box_1 for chamber
box_1 = Part.makeBox(162, 162, 250)
box_1_vector = FreeCAD.Vector(19, 19, 0)
box_1.translate(box_1_vector)

# cut tank by box_1
tank = tank.cut(box_1)

# box_2
box_2 = Part.makeBox(200, 200, 244)

# box_3
box_3 = Part.makeBox(178, 178, 244)
box_3_vector = FreeCAD.Vector(11, 11, 0)
box_3.translate(box_3_vector)

# cut box_2 by box_3
box_2 = box_2.cut(box_3)

# tank cut by box_2
box_2_vector = FreeCAD.Vector(0, 0, 3)
box_2.translate(box_2_vector)
tank = tank.cut(box_2)

# cylinder
cylinder = Part.makeCylinder(2.5, 250)

# tank cut by cylinder for hole 1
cylinder_vector = FreeCAD.Vector(5.5, 5.5, 0)
cylinder.translate(cylinder_vector)
tank = tank.cut(cylinder)

# tank cut by cylinder for intermediate holes
for i in range(19):
    cylinder_vector = FreeCAD.Vector(9.45, 0, 0)
    cylinder.translate(cylinder_vector)
    tank = tank.cut(cylinder)

# tank cut by cylinder for hole 2
cylinder_vector = FreeCAD.Vector(9.45, 0, 0)
cylinder.translate(cylinder_vector)
tank = tank.cut(cylinder)

# tank cut by cylinder for intermediate holes
for i in range(19):
    cylinder_vector = FreeCAD.Vector(0, 9.45, 0)
    cylinder.translate(cylinder_vector)
    tank = tank.cut(cylinder)

# tank cut by cylinder for hole 3
cylinder_vector = FreeCAD.Vector(0, 9.45, 0)
cylinder.translate(cylinder_vector)
tank = tank.cut(cylinder)

# tank cut by cylinder for intermediate holes
for i in range(19):
    cylinder_vector = FreeCAD.Vector(-9.45, 0, 0)
    cylinder.translate(cylinder_vector)
    tank = tank.cut(cylinder)

# tank cut by cylinder for hole 4
cylinder_vector = FreeCAD.Vector(-9.45, 0, 0)
cylinder.translate(cylinder_vector)
tank = tank.cut(cylinder)

# tank cut by cylinder for intermediate holes
for i in range(19):
    cylinder_vector = FreeCAD.Vector(0, -9.45, 0)
    cylinder.translate(cylinder_vector)
    tank = tank.cut(cylinder)

# box_4
box_4 = Part.makeBox(172, 172, 2)

# box_5
box_5 = Part.makeBox(168, 168, 2)
box_5_vector = FreeCAD.Vector(2, 2, 0)
box_5.translate(box_5_vector)

# box_4 cut by box_5
box_4 = box_4.cut(box_5)

# tank cut by box_4 for top support
box_4_vector = FreeCAD.Vector(14, 14, 0)
box_4.translate(box_4_vector)
tank = tank.cut(box_4)

# tank cut by box_4 for bottom support
box_4_vector = FreeCAD.Vector(0, 0, 248)
box_4.translate(box_4_vector)
tank = tank.cut(box_4)

Part.show(tank)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_tank").getObject("Shape"))

stl_file = u"part_tank.stl"

Mesh.export(__objs__, stl_file)

setview()
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
    def test_part_for_the_top_support_of_the_electrolyzer_in_step_format(self):
        print("test_part_for_the_top_support_of_the_electrolyzer_in_step_format")

        if os.path.exists("part_top_support.py"):
            os.remove("part_top_support.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_top_support.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_top_support"


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

# top_support
top_support = Part.makeBox(200, 200, 6)

# cylinder
cylinder = Part.makeCylinder(2.5, 6)

# top_support cut by cylinder for hole 1
cylinder_vector = FreeCAD.Vector(5.5, 5.5, 0)
cylinder.translate(cylinder_vector)
top_support = top_support.cut(cylinder)

# top_support cut by cylinder for intermediate holes
for i in range(19):
    cylinder_vector = FreeCAD.Vector(9.45, 0, 0)
    cylinder.translate(cylinder_vector)
    top_support = top_support.cut(cylinder)

# top_support cut by cylinder for hole 2
cylinder_vector = FreeCAD.Vector(9.45, 0, 0)
cylinder.translate(cylinder_vector)
top_support = top_support.cut(cylinder)

# top_support cut by cylinder for intermediate holes
for i in range(19):
    cylinder_vector = FreeCAD.Vector(0, 9.45, 0)
    cylinder.translate(cylinder_vector)
    top_support = top_support.cut(cylinder)

# top_support cut by cylinder for hole 3
cylinder_vector = FreeCAD.Vector(0, 9.45, 0)
cylinder.translate(cylinder_vector)
top_support = top_support.cut(cylinder)

# top_support cut by cylinder for intermediate holes
for i in range(19):
    cylinder_vector = FreeCAD.Vector(-9.45, 0, 0)
    cylinder.translate(cylinder_vector)
    top_support = top_support.cut(cylinder)

# top_support cut by cylinder for hole 4
cylinder_vector = FreeCAD.Vector(-9.45, 0, 0)
cylinder.translate(cylinder_vector)
top_support = top_support.cut(cylinder)

# top_support cut by cylinder for intermediate holes
for i in range(19):
    cylinder_vector = FreeCAD.Vector(0, -9.45, 0)
    cylinder.translate(cylinder_vector)
    top_support = top_support.cut(cylinder)

# box_1
box_1 = Part.makeBox(168, 168, 3)
box_1_vector = FreeCAD.Vector(16, 16, 0)
box_1.translate(box_1_vector)

# top_support cut by box_1
top_support = top_support.cut(box_1)

# box_2
box_2 = Part.makeBox(200, 200, 3)

# box_3
box_3 = Part.makeBox(172, 172, 3)
box_3_vector = FreeCAD.Vector(14, 14, 0)
box_3.translate(box_3_vector)

# box_2 cut by box_3
box_2 = box_2.cut(box_3)

# top_support cut by box_2
top_support = top_support.cut(box_2)

# cylinder_1 for volume sensor
cylinder_1 = Part.makeCylinder(4, 6)
cylinder_1_vector = FreeCAD.Vector(100, 100, 0)
cylinder_1.translate(cylinder_1_vector)

# top_support cut by cylinder_1
top_support = top_support.cut(cylinder_1)

# cylinder_2 for gas sensor to computer
cylinder_2 = Part.makeCylinder(8.5, 6)
cylinder_2_vector = FreeCAD.Vector(47.5, 47.5, 0)
cylinder_2.translate(cylinder_2_vector)

# top_support cut by cylinder_2
top_support = top_support.cut(cylinder_2)

# cylinder_3 for gas sensor to human eye
cylinder_3 = Part.makeCylinder(8.5, 6)
cylinder_3_vector = FreeCAD.Vector(47.5, 152.5, 0)
cylinder_3.translate(cylinder_3_vector)

# top_support cut by cylinder_3
top_support = top_support.cut(cylinder_3)

# cylinder_4 for water input
cylinder_4 = Part.makeCylinder(8.5, 6)
cylinder_4_vector = FreeCAD.Vector(152.5, 47.5, 0)
cylinder_4.translate(cylinder_4_vector)

# top_support cut by cylinder_4
top_support = top_support.cut(cylinder_4)

# cylinder_5 for gas output
cylinder_5 = Part.makeCylinder(8.5, 6)
cylinder_5_vector = FreeCAD.Vector(152.5, 152.5, 0)
cylinder_5.translate(cylinder_5_vector)

# top_support cut by cylinder_5
top_support = top_support.cut(cylinder_5)

Part.show(top_support)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_top_support").getObject("Shape"))

stl_file = u"part_top_support.stl"

Mesh.export(__objs__, stl_file)

setview()
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"part_top_support.py"{)}.read{(}{)}{)}')

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_part_for_the_bottom_support_of_the_electrolyzer_in_step_format(self):
        print("test_part_for_the_bottom_support_of_the_electrolyzer_in_step_format")

        if os.path.exists("part_bottom_support.py"):
            os.remove("part_bottom_support.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_bottom_support.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_bottom_support"


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

# bottom_support
bottom_support = Part.makeBox(200, 200, 6)

# cylinder
cylinder = Part.makeCylinder(2.5, 6)

# bottom_support cut by cylinder for hole 1
cylinder_vector = FreeCAD.Vector(5.5, 5.5, 0)
cylinder.translate(cylinder_vector)
bottom_support = bottom_support.cut(cylinder)

# bottom_support cut by cylinder for intermediate holes
for i in range(19):
    cylinder_vector = FreeCAD.Vector(9.45, 0, 0)
    cylinder.translate(cylinder_vector)
    bottom_support = bottom_support.cut(cylinder)

# bottom_support cut by cylinder for hole 2
cylinder_vector = FreeCAD.Vector(9.45, 0, 0)
cylinder.translate(cylinder_vector)
bottom_support = bottom_support.cut(cylinder)

# bottom_support cut by cylinder for intermediate holes
for i in range(19):
    cylinder_vector = FreeCAD.Vector(0, 9.45, 0)
    cylinder.translate(cylinder_vector)
    bottom_support = bottom_support.cut(cylinder)

# bottom_support cut by cylinder for hole 3
cylinder_vector = FreeCAD.Vector(0, 9.45, 0)
cylinder.translate(cylinder_vector)
bottom_support = bottom_support.cut(cylinder)

# bottom_support cut by cylinder for intermediate holes
for i in range(19):
    cylinder_vector = FreeCAD.Vector(-9.45, 0, 0)
    cylinder.translate(cylinder_vector)
    bottom_support = bottom_support.cut(cylinder)

# bottom_support cut by cylinder for hole 4
cylinder_vector = FreeCAD.Vector(-9.45, 0, 0)
cylinder.translate(cylinder_vector)
bottom_support = bottom_support.cut(cylinder)

# bottom_support cut by cylinder for intermediate holes
for i in range(19):
    cylinder_vector = FreeCAD.Vector(0, -9.45, 0)
    cylinder.translate(cylinder_vector)
    bottom_support = bottom_support.cut(cylinder)

# box_1
box_1 = Part.makeBox(168, 168, 3)
box_1_vector = FreeCAD.Vector(16, 16, 0)
box_1.translate(box_1_vector)

# bottom_support cut by box_1
bottom_support = bottom_support.cut(box_1)

# box_2
box_2 = Part.makeBox(200, 200, 3)

# box_3
box_3 = Part.makeBox(172, 172, 3)
box_3_vector = FreeCAD.Vector(14, 14, 0)
box_3.translate(box_3_vector)

# box_2 cut by box_3
box_2 = box_2.cut(box_3)

# bottom_support cut by box_2
bottom_support = bottom_support.cut(box_2)

# cylinder_1 for screw 5mm of diametre
cylinder_1 = Part.makeCylinder(2.5, 6)

# bottom_support cut by cylinder_1 for hole 1 for supporting disk cathode
cylinder_1_vector = FreeCAD.Vector(24.5, 24.5, 0)
cylinder_1.translate(cylinder_1_vector)
bottom_support = bottom_support.cut(cylinder_1)

# bottom_support cut by cylinder_1 for hole 2 for supporting disk cathode
cylinder_1_vector = FreeCAD.Vector(151, 0, 0)
cylinder_1.translate(cylinder_1_vector)
bottom_support = bottom_support.cut(cylinder_1)

# bottom_support cut by cylinder_1 for hole 3 for supporting disk cathode
cylinder_1_vector = FreeCAD.Vector(0, 151, 0)
cylinder_1.translate(cylinder_1_vector)
bottom_support = bottom_support.cut(cylinder_1)

# bottom_support cut by cylinder_1 for hole 4 for supporting disk cathode
cylinder_1_vector = FreeCAD.Vector(-151, 0, 0)
cylinder_1.translate(cylinder_1_vector)
bottom_support = bottom_support.cut(cylinder_1)

# bottom_support cut by cylinder_1 for hole 1 for supporting disk anode
cylinder_1_vector = FreeCAD.Vector(11, 0, 0)
cylinder_1.translate(cylinder_1_vector)
bottom_support = bottom_support.cut(cylinder_1)

# bottom_support cut by cylinder_1 for hole 2 for supporting disk anode
cylinder_1_vector = FreeCAD.Vector(129, 0, 0)
cylinder_1.translate(cylinder_1_vector)
bottom_support = bottom_support.cut(cylinder_1)

# bottom_support cut by cylinder_1 for hole 3 for supporting disk anode
cylinder_1_vector = FreeCAD.Vector(0, -151, 0)
cylinder_1.translate(cylinder_1_vector)
bottom_support = bottom_support.cut(cylinder_1)

# bottom_support cut by cylinder_1 for hole 4 for supporting disk anode
cylinder_1_vector = FreeCAD.Vector(-129, 0, 0)
cylinder_1.translate(cylinder_1_vector)
bottom_support = bottom_support.cut(cylinder_1)

Part.show(bottom_support)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_bottom_support").getObject("Shape"))

stl_file = u"part_bottom_support.stl"

Mesh.export(__objs__, stl_file)

setview()
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"part_bottom_support.py"{)}.read{(}{)}{)}')

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_part_for_the_disc_of_the_cathode_of_the_electrolyzer_in_step_format(self):
        print("test_part_for_the_disc_of_the_cathode_of_the_electrolyzer_in_step_format")

        if os.path.exists("part_disc_cathode.py"):
            os.remove("part_disc_cathode.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_disc_cathode.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_disc_cathode"

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

disc_cathode = Part.makeBox(162, 162, 5)

# cylinder_screw
cylinder_screw = Part.makeCylinder(2.5, 5)

# Cut the holes for fixing the disc on the bottom support
# hole n°1
cylinder_screw_vector = FreeCAD.Vector(5.5, 5.5, 0)
cylinder_screw.translate(cylinder_screw_vector)
disc_cathode = disc_cathode.cut(cylinder_screw)

# hole n°2
cylinder_screw_vector = FreeCAD.Vector(151, 0, 0)
cylinder_screw.translate(cylinder_screw_vector)
disc_cathode = disc_cathode.cut(cylinder_screw)

# hole n°3
cylinder_screw_vector = FreeCAD.Vector(0, 151, 0)
cylinder_screw.translate(cylinder_screw_vector)
disc_cathode = disc_cathode.cut(cylinder_screw)

# hole n°4
cylinder_screw_vector = FreeCAD.Vector(-151, 0, 0)
cylinder_screw.translate(cylinder_screw_vector)
disc_cathode = disc_cathode.cut(cylinder_screw)

# Cut the holes for fixing the cathodes
cylinder_cathode = Part.makeCylinder(4, 3)

cylinder_cathode_vector = FreeCAD.Vector(13.5, 22, 0)
cylinder_cathode.translate(cylinder_cathode_vector)
disc_cathode = disc_cathode.cut(cylinder_cathode)

for w in range(11):
    for l in range(11):
        cylinder_cathode_vector = FreeCAD.Vector(math.pow(-1, w)*12, 0, 0)
        cylinder_cathode.translate(cylinder_cathode_vector)
        disc_cathode = disc_cathode.cut(cylinder_cathode)

    if w < 10:
        cylinder_cathode_vector = FreeCAD.Vector(0, 12, 0)
        cylinder_cathode.translate(cylinder_cathode_vector)
        disc_cathode = disc_cathode.cut(cylinder_cathode)

# Cut the holes for passing the anodes and the spacers
cylinder_anode = Part.makeCylinder(3, 5)

cylinder_anode_vector = FreeCAD.Vector(13.5, 22, 0)
cylinder_anode.translate(cylinder_anode_vector)
disc_cathode = disc_cathode.cut(cylinder_anode)

for w in range(11):
    for l in range(11):
        cylinder_anode_vector = FreeCAD.Vector(math.pow(-1, w)*12, 0, 0)
        cylinder_anode.translate(cylinder_anode_vector)
        disc_cathode = disc_cathode.cut(cylinder_anode)

    if w < 10:
        cylinder_anode_vector = FreeCAD.Vector(0, 12, 0)
        cylinder_anode.translate(cylinder_anode_vector)
        disc_cathode = disc_cathode.cut(cylinder_anode)

# box_evidemment_1
box_evidemment_1 = Part.makeBox(140, 15, 5)

box_evidemment_1_vector = FreeCAD.Vector(11, 0, 0)
box_evidemment_1.translate(box_evidemment_1_vector)
disc_cathode = disc_cathode.cut(box_evidemment_1)

box_evidemment_1_vector = FreeCAD.Vector(0, 152, 0)
box_evidemment_1.translate(box_evidemment_1_vector)
disc_cathode = disc_cathode.cut(box_evidemment_1)

# box_evidemment_2
box_evidemment_2 = Part.makeBox(5, 120, 5)

box_evidemment_2_vector = FreeCAD.Vector(0, 21, 0)
box_evidemment_2.translate(box_evidemment_2_vector)
disc_cathode = disc_cathode.cut(box_evidemment_2)

box_evidemment_2_vector = FreeCAD.Vector(157, 0, 0)
box_evidemment_2.translate(box_evidemment_2_vector)
disc_cathode = disc_cathode.cut(box_evidemment_2)

Part.show(disc_cathode)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_disc_cathode").getObject("Shape"))

stl_file = u"part_disc_cathode.stl"

Mesh.export(__objs__, stl_file)

setview()
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"part_disc_cathode.py"{)}.read{(}{)}{)}')

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_part_for_the_disc_of_the_anode_of_the_electrolyzer_in_step_format(self):
        print("test_part_for_the_disc_of_the_anode_of_the_electrolyzer_in_step_format")

        if os.path.exists("part_disc_anode.py"):
            os.remove("part_disc_anode.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_disc_anode.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_disc_anode"

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
EPS = 0.10
EPS_C = EPS * -0.5

# disc_anode
disc_anode = Part.makeBox(162, 140, 5)

# cylinder_screw
cylinder_screw = Part.makeCylinder(2.5, 5)

# Cut the holes for fixing the disc on the bottom support
# hole n°1
cylinder_screw_vector = FreeCAD.Vector(5.5, 5.5, 0)
cylinder_screw.translate(cylinder_screw_vector)
disc_anode = disc_anode.cut(cylinder_screw)

# hole n°2
cylinder_screw_vector = FreeCAD.Vector(151, 0, 0)
cylinder_screw.translate(cylinder_screw_vector)
disc_anode = disc_anode.cut(cylinder_screw)

# hole n°3
cylinder_screw_vector = FreeCAD.Vector(0, 129, 0)
cylinder_screw.translate(cylinder_screw_vector)
disc_anode = disc_anode.cut(cylinder_screw)

# hole n°4
cylinder_screw_vector = FreeCAD.Vector(-151, 0, 0)
cylinder_screw.translate(cylinder_screw_vector)
disc_anode = disc_anode.cut(cylinder_screw)

# Cut the holes for fixing the anodes
cylinder_anode = Part.makeCylinder(2, 5)

cylinder_anode_vector = FreeCAD.Vector(13.5, 11, 0)
cylinder_anode.translate(cylinder_anode_vector)
disc_anode = disc_anode.cut(cylinder_anode)

for w in range(11):
    for l in range(11):
        cylinder_anode_vector = FreeCAD.Vector(math.pow(-1, w)*12, 0, 0)
        cylinder_anode.translate(cylinder_anode_vector)
        disc_anode = disc_anode.cut(cylinder_anode)

    if w < 10:
        cylinder_anode_vector = FreeCAD.Vector(0, 12, 0)
        cylinder_anode.translate(cylinder_anode_vector)
        disc_anode = disc_anode.cut(cylinder_anode)

# box_evidemment_1
box_evidemment_1 = Part.makeBox(140, 3, 5)

box_evidemment_1_vector = FreeCAD.Vector(11, 0, 0)
box_evidemment_1.translate(box_evidemment_1_vector)
disc_anode = disc_anode.cut(box_evidemment_1)

box_evidemment_1_vector = FreeCAD.Vector(0, 137, 0)
box_evidemment_1.translate(box_evidemment_1_vector)
disc_anode = disc_anode.cut(box_evidemment_1)

# box_evidemment_2
box_evidemment_2 = Part.makeBox(3, 110, 5)

box_evidemment_2_vector = FreeCAD.Vector(0, 15, 0)
box_evidemment_2.translate(box_evidemment_2_vector)
disc_anode = disc_anode.cut(box_evidemment_2)

box_evidemment_2_vector = FreeCAD.Vector(159, 0, 0)
box_evidemment_2.translate(box_evidemment_2_vector)
disc_anode = disc_anode.cut(box_evidemment_2)

Part.show(disc_anode)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_disc_anode").getObject("Shape"))

stl_file = u"part_disc_anode.stl"

Mesh.export(__objs__, stl_file)

setview()
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"part_disc_anode.py"{)}.read{(}{)}{)}')

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_part_core_ferrite_electrolyser_in_step_format(self):
        print("test_part_core_ferrite_electrolyser_in_step_format")

        if os.path.exists("part_core_ferrite.py"):
            os.remove("part_core_ferrite.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_core_ferrite.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_core_ferrite"

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
EPS = 0.10
EPS_C = EPS * -0.5

# part_core_ferrite
part_core_ferrite = Part.makeBox(93, 76, 16)

# box_1
box_1 = Part.makeBox(37, 48, 16)
box_1_vector = FreeCAD.Vector(28, 0, 0)
box_1.translate(box_1_vector)

# part_core_ferrite cut by box_1
part_core_ferrite = part_core_ferrite.cut(box_1)

Part.show(part_core_ferrite)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_core_ferrite").getObject("Shape"))

stl_file = u"part_core_ferrite.stl"

Mesh.export(__objs__, stl_file)

setview()
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"part_core_ferrite.py"{)}.read{(}{)}{)}')

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_assembly_for_the_complete_transformer_in_step_format(self):
        print("test_assembly_for_the_complete_transformer_in_step_format")

        if os.path.exists("assembly_complete_transformer.py"):
            os.remove("assembly_complete_transformer.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("assembly_complete_transformer.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_complete_transformer"

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
EPS = 0.10
EPS_C = EPS * -0.5

# part_core_ferrite
part_core_ferrite = Part.makeBox(93, 76, 16)

# box_1
box_1 = Part.makeBox(37, 48, 16)
box_1_vector = FreeCAD.Vector(28, 0, 0)
box_1.translate(box_1_vector)

# part_core_ferrite cut by box_1
part_core_ferrite = part_core_ferrite.cut(box_1)

Part.show(part_core_ferrite)

DOC.recompute()

# insert transformer
Mesh.insert(u"part_transformer.stl", "assembly_complete_transformer")

FreeCAD.getDocument("assembly_complete_transformer").getObject("part_transformer").Placement = App.Placement(App.Vector(-18.7, 48, -17.4), App.Rotation(App.Vector(1,0,0), 90))

# insert transformer
Mesh.insert(u"part_transformer.stl", "assembly_complete_transformer")

FreeCAD.getDocument("assembly_complete_transformer").getObject("part_transformer001").Placement = App.Placement(App.Vector(18.7 + 28, 48, -17.4), App.Rotation(App.Vector(1,0,0), 90))

# insert part_core_ferrite
Mesh.insert(u"part_core_ferrite.stl", "assembly_complete_transformer")

FreeCAD.getDocument("assembly_complete_transformer").getObject("part_core_ferrite").Placement = App.Placement(App.Vector(0, 0, 17.3), App.Rotation(App.Vector(1,0,0), 180))

setview()
        """)

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"assembly_complete_transformer.py"{)}.read{(}{)}{)}')

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')


if __name__ == '__main__':
    unittest.main()
