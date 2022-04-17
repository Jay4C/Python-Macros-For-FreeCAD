import time
import unittest
import os
import pywinauto.mouse
import pywinauto.keyboard


class brevet_us_4_936_961_water_electrolyser_4(unittest.TestCase):
    # ok
    def test_part_anode(self):
        print("test_part_anode")

        # Dimensions : radius = 2 mm and height = 100 mm

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

cylinder_1 = Part.makeCylinder(2, 150)

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
            'exec{(}open{(}"part_anode.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_part_cathode(self):
        print("test_part_cathode")

        # Dimensions : radius = 4 mm and height = 100 mm
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

cylinder_1 = Part.makeCylinder(4, 150)

cylinder_2 = Part.makeCylinder(3, 150)

cylinder_1 = cylinder_1.cut(cylinder_2)

Part.show(cylinder_1)

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
            'exec{(}open{(}"part_cathode.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_part_spacer(self):
        print("test_part_spacer")

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
spacer = Part.makeCylinder(4.5, 13)

# anode
anode = Part.makeCylinder(2, 13)

# cut spacer by anode
spacer = spacer.cut(anode)

# space_anode_cathode
space_anode_cathode = Part.makeCylinder(4.5, 12)

# space_plus_anode
space_plus_anode = Part.makeCylinder(3, 12)

# space_anode_cathode cut by space_plus_anode
space_anode_cathode = space_anode_cathode.cut(space_plus_anode)

# spacer cut by space_anode_cathode
space_anode_cathode_vector = FreeCAD.Vector(0, 0, 2)
space_anode_cathode.translate(space_anode_cathode_vector)
spacer = spacer.cut(space_anode_cathode)

# space_bubble
degree = 10
for i in range(int(360/degree)):
    radius = 2
    alpha=(i*degree*math.pi)/180
    space_bubble_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    space_bubble = Part.makeCylinder(0.3, 13)
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
            'exec{(}open{(}"part_spacer.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_part_ecrou_m5(self):
        print("test_part_ecrou_m5")

        if os.path.exists("part_ecrou_m5.py"):
            os.remove("part_ecrou_m5.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_ecrou_m5.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_ecrou_m5"


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

cylinder_1 = Part.makeCylinder(4.5, 4)

cylinder_2 = Part.makeCylinder(2.5, 4)

cylinder_1 = cylinder_1.cut(cylinder_2)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_ecrou_m5").getObject("Shape"))

stl_file = u"part_ecrou_m5.stl"

Mesh.export(__objs__, stl_file)

setview()
        """)

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"part_ecrou_m5.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_part_vis_metal_m5_l20(self):
        print("test_part_vis_metal_m5_l20")

        if os.path.exists("part_vis_metal_m5_l20.py"):
            os.remove("part_vis_metal_m5_l20.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_vis_metal_m5_l20.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_vis_metal_m5_l20"


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

cylinder_1 = Part.makeCylinder(6, 22)

cylinder_2 = Part.makeCylinder(2.5, 20)

cylinder_3 = Part.makeCylinder(6, 20)

# cylinder_3 cut by cylinder_2
cylinder_3 = cylinder_3.cut(cylinder_2)

# cylinder_1 cut by cylinder_3
cylinder_3_vector = FreeCAD.Vector(0, 0, 2)
cylinder_3.translate(cylinder_3_vector)
cylinder_1 = cylinder_1.cut(cylinder_3)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_vis_metal_m5_l20").getObject("Shape"))

stl_file = u"part_vis_metal_m5_l20.stl"

Mesh.export(__objs__, stl_file)

setview()
        """)

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"part_vis_metal_m5_l20.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_part_vis_metal_m5_l60(self):
        print("test_part_vis_metal_m5_l60")

        if os.path.exists("part_vis_metal_m5_l60.py"):
            os.remove("part_vis_metal_m5_l60.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_vis_metal_m5_l60.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_vis_metal_m5_l60"


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

cylinder_1 = Part.makeCylinder(6, 62)

cylinder_2 = Part.makeCylinder(2.5, 60)

cylinder_3 = Part.makeCylinder(6, 60)

# cylinder_3 cut by cylinder_2
cylinder_3 = cylinder_3.cut(cylinder_2)

# cylinder_1 cut by cylinder_3
cylinder_3_vector = FreeCAD.Vector(0, 0, 2)
cylinder_3.translate(cylinder_3_vector)
cylinder_1 = cylinder_1.cut(cylinder_3)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_vis_metal_m5_l60").getObject("Shape"))

stl_file = u"part_vis_metal_m5_l60.stl"

Mesh.export(__objs__, stl_file)

setview()
        """)

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"part_vis_metal_m5_l60.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_part_rondelle_m5_d12(self):
        print("test_part_rondelle_m5_d12")

        if os.path.exists("part_rondelle_m5_d12.py"):
            os.remove("part_rondelle_m5_d12.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_rondelle_m5_d12.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_rondelle_m5_d12"


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

cylinder_1 = Part.makeCylinder(6, 1)

cylinder_2 = Part.makeCylinder(2.5, 1)

cylinder_1 = cylinder_1.cut(cylinder_2)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_rondelle_m5_d12").getObject("Shape"))

stl_file = u"part_rondelle_m5_d12.stl"

Mesh.export(__objs__, stl_file)

setview()
        """)

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"part_rondelle_m5_d12.py"{)}.read{(}{)}{)}'
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
            file.write("""import FreeCAD, Part, Mesh, math

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

cylinder_1 = Part.makeCylinder(150, 200)

cylinder_2 = Part.makeCylinder(132, 200)

# cylinder_1 cut by cylinder_2
cylinder_1 = cylinder_1.cut(cylinder_2)

cylinder_3 = Part.makeCylinder(150, 194)

cylinder_4 = Part.makeCylinder(139, 194)

# cylinder_3 cut by cylinder_4
cylinder_3 = cylinder_3.cut(cylinder_4)

# cylinder_1 cut by cylinder_3
cylinder_3_vector = FreeCAD.Vector(0, 0, 3)
cylinder_3.translate(cylinder_3_vector)
cylinder_1 = cylinder_1.cut(cylinder_3)

# holes for fixing the bottom support and the top support
degree = 10
for i in range(int(360/degree)):
    radius = 144.5
    alpha=(i*degree*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(2.5, 200)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

cylinder_5 = Part.makeCylinder(137, 2)

cylinder_6 = Part.makeCylinder(135, 2)

# cylinder_5 cut by cylinder_6
cylinder_5 = cylinder_5.cut(cylinder_6)

# cylinder_1 cut by cylinder_5
cylinder_1 = cylinder_1.cut(cylinder_5)

cylinder_5_vector = FreeCAD.Vector(0, 0, 198)
cylinder_5.translate(cylinder_5_vector)
cylinder_1 = cylinder_1.cut(cylinder_5)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

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
            'exec{(}open{(}"part_tank.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_part_bottom_support_d30(self):
        print("test_part_bottom_support_d30")

        if os.path.exists("part_bottom_support_d30.py"):
            os.remove("part_bottom_support_d30.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_bottom_support_d30.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh, math

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_bottom_support_d30"


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

cylinder_1 = Part.makeCylinder(150, 6)

cylinder_2 = Part.makeCylinder(135, 3)

# cylinder_1 cut by cylinder_2
cylinder_2_vector = FreeCAD.Vector(0, 0, 3)
cylinder_2.translate(cylinder_2_vector)
cylinder_1 = cylinder_1.cut(cylinder_2)

cylinder_3 = Part.makeCylinder(150, 3)

cylinder_4 = Part.makeCylinder(137, 3)

# cylinder_3 cut by cylinder_4
cylinder_3 = cylinder_3.cut(cylinder_4)

# cylinder_1 cut by cylinder_3
cylinder_3_vector = FreeCAD.Vector(0, 0, 3)
cylinder_3.translate(cylinder_3_vector)
cylinder_1 = cylinder_1.cut(cylinder_3)

# holes for fixing the tank
degree = 10
for i in range(int(360/degree)):
    radius = 144.5
    alpha=(i*degree*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(2.5, 3)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

# holes for fixing the disc anode and the disc cathode
degree = 60
for i in range(int(360/degree)):
    radius = 125
    alpha=(i*degree*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(2.5, 3)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_bottom_support_d30").getObject("Shape"))

stl_file = u"part_bottom_support_d30.stl"

Mesh.export(__objs__, stl_file)

setview()
        """)

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"part_bottom_support_d30.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_part_top_support_d30(self):
        print("test_part_top_support_d30")

        if os.path.exists("part_top_support_d30.py"):
            os.remove("part_top_support_d30.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_top_support_d30.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh, math

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_top_support_d30"


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

cylinder_1 = Part.makeCylinder(150, 6)

cylinder_2 = Part.makeCylinder(135, 3)

# cylinder_1 cut by cylinder_2
cylinder_2_vector = FreeCAD.Vector(0, 0, 3)
cylinder_2.translate(cylinder_2_vector)
cylinder_1 = cylinder_1.cut(cylinder_2)

cylinder_3 = Part.makeCylinder(150, 3)

cylinder_4 = Part.makeCylinder(137, 3)

# cylinder_3 cut by cylinder_4
cylinder_3 = cylinder_3.cut(cylinder_4)

# cylinder_1 cut by cylinder_3
cylinder_3_vector = FreeCAD.Vector(0, 0, 3)
cylinder_3.translate(cylinder_3_vector)
cylinder_1 = cylinder_1.cut(cylinder_3)

# holes for fixing the tank
degree = 10
for i in range(int(360/degree)):
    radius = 144.5
    alpha=(i*degree*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(2.5, 3)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

cylinder_5 = Part.makeCylinder(4, 3)

# cylinder_1 cut by cylinder_5 for fixing the volume sensor
cylinder_1 = cylinder_1.cut(cylinder_5)

# holes for the water input, the gas output, the pressure sensor
degree = 120
for i in range(int(360/degree)):
    radius = 80
    alpha=(i*degree*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(8, 3)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_top_support_d30").getObject("Shape"))

stl_file = u"part_top_support_d30.stl"

Mesh.export(__objs__, stl_file)

setview()
        """)

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"part_top_support_d30.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_part_disc_cathode_d30(self):
        print("test_part_disc_cathode_d30")

        if os.path.exists("part_disc_cathode_d30.py"):
            os.remove("part_disc_cathode_d30.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_disc_cathode_d30.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh, math

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_disc_cathode_d30"


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

cylinder_1 = Part.makeCylinder(130, 3)

cylinder_2 = Part.makeCylinder(4, 3)

cylinder_1 = cylinder_1.cut(cylinder_2)

# holes for fixing the disc cathode on the bottom support
degree = 7.5
for i in range(int(360/degree)):
    radius = 125
    alpha=(i*degree*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(2.5, 3)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

# cutting for passing the screw for fixing the disc anode
degrees = [60, 180, 300]
for degree in degrees:
    radius = 130
    alpha=(degree*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(9, 3)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

# holes for fixing the cathodes on the disc cathode
degree = 90
for i in range(int(360/degree)):
    radius = 10.5
    alpha=(i*degree*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(4, 3)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

degree = 30
for i in range(int(360/degree)):
    for n in range(2, 12):
        radius = 10.5 * n
        alpha=(i*degree*math.pi)/180
        hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
        hole = Part.makeCylinder(4, 3)
        hole.translate(hole_vector)
        cylinder_1 = cylinder_1.cut(hole)

depart = 15
for i in range(0, 12):
    for n in range(4, 12):
        radius = 10.5 * n
        degree = depart + 30 * i
        alpha=(degree*math.pi)/180
        hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
        hole = Part.makeCylinder(4, 3)
        hole.translate(hole_vector)
        cylinder_1 = cylinder_1.cut(hole)

depart = 7.5
for i in range(0, 24):
    for n in range(8, 12):
        radius = 10.5 * n
        degree = depart + 15 * i
        alpha=(degree*math.pi)/180
        hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
        hole = Part.makeCylinder(4, 3)
        hole.translate(hole_vector)
        cylinder_1 = cylinder_1.cut(hole)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_disc_cathode_d30").getObject("Shape"))

stl_file = u"part_disc_cathode_d30.stl"

Mesh.export(__objs__, stl_file)

setview()
        """)

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"part_disc_cathode_d30.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_part_disc_anode_d30(self):
        print("test_part_disc_anode_d30")

        if os.path.exists("part_disc_anode_d30.py"):
            os.remove("part_disc_anode_d30.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_disc_anode_d30.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh, math

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_disc_anode_d30"


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

cylinder_1 = Part.makeCylinder(130, 3)

cylinder_2 = Part.makeCylinder(2, 3)

cylinder_1 = cylinder_1.cut(cylinder_2)

# holes for fixing the disc anode on the bottom support
degree = 7.5
for i in range(int(360/degree)):
    radius = 125
    alpha=(i*degree*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(2.5, 3)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

# cutting for passing the screw for fixing the disc cathode
degrees = [60, 180, 300]
for degree in degrees:
    radius = 130
    alpha=(degree*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(9, 3)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

# holes for fixing the anodes on the disc anode
degree = 45
for i in range(int(360/degree)):
    radius = 10.5
    alpha=(i*degree*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(2, 3)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

degree = 30
for i in range(int(360/degree)):
    for n in range(2, 12):
        radius = 10.5 * n
        alpha=(i*degree*math.pi)/180
        hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
        hole = Part.makeCylinder(2, 3)
        hole.translate(hole_vector)
        cylinder_1 = cylinder_1.cut(hole)

depart = 15
for i in range(0, 12):
    for n in range(3, 12):
        radius = 10.5 * n
        degree = depart + 30 * i
        alpha=(degree*math.pi)/180
        hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
        hole = Part.makeCylinder(2, 3)
        hole.translate(hole_vector)
        cylinder_1 = cylinder_1.cut(hole)

depart = 7.5
for i in range(0, 24):
    for n in range(5, 12):
        radius = 10.5 * n
        degree = depart + 15 * i
        alpha=(degree*math.pi)/180
        hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
        hole = Part.makeCylinder(2, 3)
        hole.translate(hole_vector)
        cylinder_1 = cylinder_1.cut(hole)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_disc_anode_d30").getObject("Shape"))

stl_file = u"part_disc_anode_d30.stl"

Mesh.export(__objs__, stl_file)

setview()
        """)

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"part_disc_anode_d30.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')


if __name__ == '__main__':
    unittest.main()
