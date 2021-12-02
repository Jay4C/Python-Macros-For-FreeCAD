import time
import unittest
import os
import pywinauto.mouse
import pywinauto.keyboard


class brevet_us_4_936_961_water_electrolyser_3(unittest.TestCase):
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
    def test_rondelle_m5_d12(self):
        print("test_rondelle_m5_d12")

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

cylinder_1 = Part.makeCylinder(2, 100)

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

cylinder_1 = Part.makeCylinder(4, 100)

cylinder_2 = Part.makeCylinder(3, 100)

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
degre = 10
for i in range(int(360/degre)):
    radius = 2
    alpha=(i*degre*math.pi)/180
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
    def test_part_bottom_support(self):
        print("test_part_bottom_support")

        if os.path.exists("part_bottom_support.py"):
            os.remove("part_bottom_support.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_bottom_support.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh, math

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
EPS_C = EPS * -0.5

cylinder_1 = Part.makeCylinder(34, 2)

cylinder_2 = Part.makeCylinder(2.5, 2)

cylinder_1 = cylinder_1.cut(cylinder_2)

# holes for fixing the disc anode and the disc cathode
degre = 60
for i in range(int(360/degre)):
    radius = 29.3
    alpha=(i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(2.5, 2)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

# holes for letting the gas miwture to go out
for i in range(int(360/degre)):
    radius = 14.25
    alpha=(i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(5, 2)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

degres = [30, 90, 150, -30, -90, -150]

for degre in degres:
    radius = 24
    alpha=(int(degre)*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(5, 2)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

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
            'exec{(}open{(}"part_bottom_support.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_part_disc_anode(self):
        print("test_part_disc_anode")

        if os.path.exists("part_disc_anode.py"):
            os.remove("part_disc_anode.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_disc_anode.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh, math

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

# EPS= tolerance to use to cut the parts
EPS = 0.10
EPS_C = EPS * -0.5

cylinder_1 = Part.makeCylinder(34, 3)

cylinder_2 = Part.makeCylinder(2, 3)

cylinder_1 = cylinder_1.cut(cylinder_2)

# holes for fixing the disc anode
degre = 120
for i in range(int(360/degre)):
    radius = 29.3
    alpha=(i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(2.5, 3)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

# cutting for passing the screw for fixing the disc cathode
degres = [60, 180, 300]
for degre in degres:
    radius = 34
    alpha=(degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(9, 3)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

# holes for fixing the anodes on the disc anode
degre = 90
for i in range(int(360/degre)):
    radius = 10.5
    alpha=(i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(2, 3)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

degre = 30
for i in range(int(360/degre)):
    radius = 21
    alpha=(i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(2, 3)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

depart = 30
for i in range(0, 6):
    degre = depart + i * 60
    radius = 31.5
    alpha=(degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(2, 3)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

# holes for emptying the disc anode
degres = [105, 225, 345]
for degre in degres:
    radius = 29.3
    alpha=(degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(2.5, 3)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)
    
# holes for emptying the disc anode
degres = [135, 255, 375]
for degre in degres:
    radius = 29.3
    alpha=(degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(2.5, 3)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)
    
# holes for emptying the disc anode
degres = [45, 135, 225, 315]
for degre in degres:
    radius = 13
    alpha=(degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(2.5, 3)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

# holes for emptying the disc anode
degres = [75, 195, 315]
for degre in degres:
    radius = 29.3
    alpha=(degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(2.5, 3)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)
    
# holes for emptying the disc anode
degres = [45, 165, 285]
for degre in degres:
    radius = 29.3
    alpha=(degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(2.5, 3)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

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
            'exec{(}open{(}"part_disc_anode.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_part_disc_cathode(self):
        print("test_part_disc_cathode")

        if os.path.exists("part_disc_cathode.py"):
            os.remove("part_disc_cathode.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_disc_cathode.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh, math

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

cylinder_1 = Part.makeCylinder(34, 3)

cylinder_2 = Part.makeCylinder(4, 3)

cylinder_1 = cylinder_1.cut(cylinder_2)

# holes for fixing the disc cathode
degre = 120
for i in range(int(360/degre)):
    radius = 29.3
    alpha=(i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(2.5, 3)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

# cutting for passing the screw for fixing the disc anode
degres = [60, 180, 300]
for degre in degres:
    radius = 34
    alpha=(degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(9, 3)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

# holes for fixing the cathodes on the disc cathode
degre = 90
for i in range(int(360/degre)):
    radius = 10.5
    alpha=(i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(4, 3)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

degre = 30
for i in range(int(360/degre)):
    radius = 21
    alpha=(i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(4, 3)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)
    
depart = 30
for i in range(0, 6):
    degre = depart + i * 60
    radius = 31.5
    alpha=(degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(4, 3)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

# holes for emptying the disc cathode
degres = [105, 225, 345]
for degre in degres:
    radius = 29.3
    alpha=(degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(2.5, 3)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)
    
# holes for emptying the disc cathode
degres = [135, 255, 375]
for degre in degres:
    radius = 29.3
    alpha=(degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(2.5, 3)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)
    
# holes for emptying the disc cathode
degres = [45, 135, 225, 315]
for degre in degres:
    radius = 13
    alpha=(degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(2.5, 3)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

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
            'exec{(}open{(}"part_disc_cathode.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    #
    def test_assembly_complete_electrolyser(self):
        print("test_assembly_complete_electrolyser")

        if os.path.exists("assembly_complete_electrolyser.py"):
            os.remove("assembly_complete_electrolyser.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("assembly_complete_electrolyser.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_complete_electrolyser"


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

# part_bottom_support
cylinder_1 = Part.makeCylinder(34, 2)

cylinder_2 = Part.makeCylinder(2.5, 2)

cylinder_1 = cylinder_1.cut(cylinder_2)

# holes for fixing the disc anode and the disc cathode
degre = 60
for i in range(int(360/degre)):
    radius = 28.5
    alpha=(i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(2.5, 2)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

# holes for letting the gas miwture to go out
for i in range(int(360/degre)):
    radius = 14.25
    alpha=(i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(5, 2)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

degres = [30, 90, 150, -30, -90, -150]

for degre in degres:
    radius = 24
    alpha=(int(degre)*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(5, 2)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

Part.show(cylinder_1)

DOC.recompute()

# change color of assembly_complete_electrolyser
FreeCADGui.getDocument("assembly_complete_electrolyser").getObject("Shape").ShapeColor = (0.67,0.00,0.00)

# insertion part_vis_metal_m5_l20 - 1
Mesh.insert(u"part_vis_metal_m5_l20.stl", "assembly_complete_electrolyser")
FreeCAD.getDocument("assembly_complete_electrolyser").getObject("part_vis_metal_m5_l20").Placement = App.Placement(App.Vector(84, 0, 0), App.Rotation(App.Vector(1,0,0), 0))
FreeCADGui.getDocument("assembly_complete_electrolyser").getObject("part_vis_metal_m5_l20").ShapeColor = (0.33,1.00,1.00)

DOC.recompute()

__objs__=[]
__objs__.append(FreeCAD.getDocument("assembly_complete_electrolyser").getObject("Shape"))

Mesh.export(__objs__,u"assembly_complete_electrolyser.stl")

del __objs__

setview()
         """)

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"assembly_complete_electrolyser.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')


if __name__ == '__main__':
    unittest.main()
