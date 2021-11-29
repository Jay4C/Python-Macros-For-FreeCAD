import time
import unittest
import os
import pywinauto.mouse
import pywinauto.keyboard


class brevet_us_4_124_463_water_electrolyser_2_for_industrial_plant(unittest.TestCase):
    # ok
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

cylinder_1 = Part.makeCylinder(4.5, 4)

cylinder_2 = Part.makeCylinder(2.5, 4)

cylinder_1 = cylinder_1.cut(cylinder_2)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_ecrou_5m").getObject("Shape"))

stl_file = u"part_ecrou_5m.stl"

Mesh.export(__objs__, stl_file)

setview()
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

cylinder_1 = Part.makeCylinder(7.5, 4)

cylinder_2 = Part.makeCylinder(5, 4)

cylinder_1 = cylinder_1.cut(cylinder_2)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_ecrou_10m").getObject("Shape"))

stl_file = u"part_ecrou_10m.stl"

Mesh.export(__objs__, stl_file)

setview()
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

__objs__.append(FreeCAD.getDocument("part_vis_metal_m5_20l").getObject("Shape"))

stl_file = u"part_vis_metal_m5_20l.stl"

Mesh.export(__objs__, stl_file)

setview()
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
    def test_part_vis_metal_m10_200l(self):
        print("test_part_vis_metal_m10_200l")

        if os.path.exists("part_vis_metal_m10_200l.py"):
            os.remove("part_vis_metal_m10_200l.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_vis_metal_m10_200l.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_vis_metal_m10_200l"


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

cylinder_1 = Part.makeCylinder(8.5, 202)

cylinder_2 = Part.makeCylinder(5, 200)

cylinder_3 = Part.makeCylinder(8.5, 200)

# cylinder_3 cut by cylinder_2
cylinder_3 = cylinder_3.cut(cylinder_2)

# cylinder_1 cut by cylinder_3
cylinder_3_vector = FreeCAD.Vector(0, 0, 2)
cylinder_3.translate(cylinder_3_vector)
cylinder_1 = cylinder_1.cut(cylinder_3)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_vis_metal_m10_200l").getObject("Shape"))

stl_file = u"part_vis_metal_m10_200l.stl"

Mesh.export(__objs__, stl_file)

setview()
        """)

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"part_vis_metal_m10_200l.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_part_rondelle_m5_12d(self):
        print("test_part_rondelle_m5_12d")

        if os.path.exists("part_rondelle_m5_12d.py"):
            os.remove("part_rondelle_m5_12d.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_rondelle_m5_12d.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_rondelle_m5_12d"


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

__objs__.append(FreeCAD.getDocument("part_rondelle_m5_12d").getObject("Shape"))

stl_file = u"part_rondelle_m5_12d.stl"

Mesh.export(__objs__, stl_file)

setview()
        """)

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"part_rondelle_m5_12d.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_part_rondelle_m10_17d(self):
        print("test_part_rondelle_m10_17d")

        if os.path.exists("part_rondelle_m10_17d.py"):
            os.remove("part_rondelle_m10_17d.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_rondelle_m10_17d.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_rondelle_m10_17d"


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

cylinder_1 = Part.makeCylinder(8.5, 1)

cylinder_2 = Part.makeCylinder(5, 1)

cylinder_1 = cylinder_1.cut(cylinder_2)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_rondelle_m10_17d").getObject("Shape"))

stl_file = u"part_rondelle_m10_17d.stl"

Mesh.export(__objs__, stl_file)

setview()
        """)

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"part_rondelle_m10_17d.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_part_tank_d25(self):
        print("test_part_tank_d25")

        if os.path.exists("part_tank_d25.py"):
            os.remove("part_tank_d25.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_tank_d25.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh, math

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_tank_d25"


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

# Diametre maximal du tank
diametre_maximal = 250

cylinder_1 = Part.makeCylinder(diametre_maximal/2, diametre_maximal)

cylinder_2 = Part.makeCylinder(diametre_maximal/2 - 3 - 5 - 3 - 2 - 3 - 2, diametre_maximal)

# cylinder_1 cut by cylinder_2
cylinder_1 = cylinder_1.cut(cylinder_2)

cylinder_3 = Part.makeCylinder(diametre_maximal/2, diametre_maximal - 3*2)

cylinder_4 = Part.makeCylinder(diametre_maximal/2 - 3 - 5 - 3, diametre_maximal - 3*2)

# cylinder_3 cut by cylinder_4
cylinder_3 = cylinder_3.cut(cylinder_4)

# cylinder_1 cut by cylinder_3
cylinder_3_vector = FreeCAD.Vector(0, 0, 3)
cylinder_3.translate(cylinder_3_vector)
cylinder_1 = cylinder_1.cut(cylinder_3)

# holes for fixing the bottom support and the top support
degre = 10
for i in range(int(360/degre)):
    radius = diametre_maximal/2 - 3 - 2.5
    alpha=(i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(2.5, diametre_maximal)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

cylinder_5 = Part.makeCylinder(diametre_maximal/2 - 3 - 5 - 3 - 2, 3)

cylinder_6 = Part.makeCylinder(diametre_maximal/2 - 3 - 5 - 3 - 2 - 3, 3)

# cylinder_5 cut by cylinder_6
cylinder_5 = cylinder_5.cut(cylinder_6)

# cylinder_1 cut by cylinder_5
cylinder_1 = cylinder_1.cut(cylinder_5)

cylinder_5_vector = FreeCAD.Vector(0, 0, diametre_maximal - 3)
cylinder_5.translate(cylinder_5_vector)
cylinder_1 = cylinder_1.cut(cylinder_5)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_tank_d25").getObject("Shape"))

stl_file = u"part_tank_d25.stl"

Mesh.export(__objs__, stl_file)

setview()
        """)

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"part_tank_d25.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_part_bottom_support_d25(self):
        print("test_part_bottom_support_d25")

        if os.path.exists("part_bottom_support_d25.py"):
            os.remove("part_bottom_support_d25.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_bottom_support_d25.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh, math

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_bottom_support_d25"


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

# Diametre maximal
diametre_maximal = 250

cylinder_1 = Part.makeCylinder(diametre_maximal/2, 6)

cylinder_2 = Part.makeCylinder(diametre_maximal/2 - 3 - 5 - 3 - 2 - 3, 3)

# cylinder_1 cut by cylinder_2
cylinder_2_vector = FreeCAD.Vector(0, 0, 3)
cylinder_2.translate(cylinder_2_vector)
cylinder_1 = cylinder_1.cut(cylinder_2)

cylinder_3 = Part.makeCylinder(diametre_maximal/2, 3)

cylinder_4 = Part.makeCylinder(diametre_maximal/2 - 3 - 5 - 3 - 2, 3)

# cylinder_3 cut by cylinder_4
cylinder_3 = cylinder_3.cut(cylinder_4)

# cylinder_1 cut by cylinder_3
cylinder_3_vector = FreeCAD.Vector(0, 0, 3)
cylinder_3.translate(cylinder_3_vector)
cylinder_1 = cylinder_1.cut(cylinder_3)

# holes for fixing the tank
degre = 10
for i in range(int(360/degre)):
    radius = diametre_maximal/2 - 3 - 2.5
    alpha=(i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(2.5, 3)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

# holes for fixing the anodes and the cathodes
degre = 60
for i in range(int(360/degre)):
    radius = diametre_maximal/2 - 3 - 5 - 3 - 2 - 3 - 2 - 2 - 4 - 5
    alpha=(i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(5, 3)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_bottom_support_d25").getObject("Shape"))

stl_file = u"part_bottom_support_d25.stl"

Mesh.export(__objs__, stl_file)

setview()
        """)

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"part_bottom_support_d25.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_part_top_support_d25(self):
        print("test_part_top_support_d25")

        if os.path.exists("part_top_support_d25.py"):
            os.remove("part_top_support_d25.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_top_support_d25.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh, math

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_top_support_d25"


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

# Diametre maximal
diametre_maximal = 250

cylinder_1 = Part.makeCylinder(diametre_maximal/2, 6)

cylinder_2 = Part.makeCylinder(diametre_maximal/2 - 3 - 5 - 3 - 2 - 3, 3)

# cylinder_1 cut by cylinder_2
cylinder_2_vector = FreeCAD.Vector(0, 0, 3)
cylinder_2.translate(cylinder_2_vector)
cylinder_1 = cylinder_1.cut(cylinder_2)

cylinder_3 = Part.makeCylinder(diametre_maximal/2, 3)

cylinder_4 = Part.makeCylinder(diametre_maximal/2 - 3 - 5 - 3 - 2, 3)

# cylinder_3 cut by cylinder_4
cylinder_3 = cylinder_3.cut(cylinder_4)

# cylinder_1 cut by cylinder_3
cylinder_3_vector = FreeCAD.Vector(0, 0, 3)
cylinder_3.translate(cylinder_3_vector)
cylinder_1 = cylinder_1.cut(cylinder_3)

# holes for fixing the tank
degre = 10
for i in range(int(360/degre)):
    radius = diametre_maximal/2 - 3 - 2.5
    alpha=(i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(2.5, 3)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

cylinder_5 = Part.makeCylinder(4, 3)

# cylinder_1 cut by cylinder_5 for fixing the volume sensor
cylinder_1 = cylinder_1.cut(cylinder_5)

# holes for the water input, the gas output, the pressure sensor
degre = 120
for i in range(int(360/degre)):
    radius = diametre_maximal/4
    alpha=(i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(8, 3)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_top_support_d25").getObject("Shape"))

stl_file = u"part_top_support_d25.stl"

Mesh.export(__objs__, stl_file)

setview()
        """)

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"part_top_support_d25.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_part_capacitor_plate(self):
        print("test_part_capacitor_plate")

        if os.path.exists("part_capacitor_plate.py"):
            os.remove("part_capacitor_plate.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_capacitor_plate.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh, math

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_capacitor_plate"


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

# Diametre maximal du tank
diametre_maximal_tank = 250

# Diametre maximal du capacitor plate
diametre_maximal_capacitor_plate = diametre_maximal_tank - 3*2 - 5*2 - 3*2 - 2*2 - 3*2 - 2*2 - 2*2

cylinder_1 = Part.makeCylinder(diametre_maximal_capacitor_plate/2, 1)

cylinder_2 = Part.makeCylinder(5, 1)

cylinder_1 = cylinder_1.cut(cylinder_2)

# holes for fixing the anodes
degre = 120
for i in range(int(360/degre)):
    radius = diametre_maximal_capacitor_plate/2 - 4 - 5
    alpha=(i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(5, 1)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

# holes for fixing the cathodes
degres = [60, 180, 300]
for degre in degres:
    radius = diametre_maximal_capacitor_plate/2
    alpha=(degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(15.5, 1)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

# holes for letting the gas mixture to go out
degre = 10
for i in range(int(360/degre)):
    radius = diametre_maximal_capacitor_plate/2 - 4 - 5
    alpha=(i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(2.5, 1)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

# holes for letting the gas mixture to go out
degre = 90
for i in range(int(360/degre)):
    radius = 20
    alpha=(i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(5, 1)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

# holes for letting the gas mixture to go out
degre = 30
for i in range(int(360/degre)):
    for i_1 in range(2, 5):
        radius = 20 * i_1
        alpha=(i*degre*math.pi)/180
        hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
        hole = Part.makeCylinder(5, 1)
        hole.translate(hole_vector)
        cylinder_1 = cylinder_1.cut(hole)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_capacitor_plate").getObject("Shape"))

stl_file = u"part_capacitor_plate.stl"

Mesh.export(__objs__, stl_file)

setview()
        """)

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"part_capacitor_plate.py"{)}.read{(}{)}{)}'
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
            file.write("""import FreeCAD, Part, Mesh, math

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

# Diametre maximal
diametre_maximal = 250

cylinder_1 = Part.makeCylinder(diametre_maximal/2, 6)

cylinder_2 = Part.makeCylinder(diametre_maximal/2 - 3 - 5 - 3 - 2 - 3, 3)

# cylinder_1 cut by cylinder_2
cylinder_2_vector = FreeCAD.Vector(0, 0, 3)
cylinder_2.translate(cylinder_2_vector)
cylinder_1 = cylinder_1.cut(cylinder_2)

cylinder_3 = Part.makeCylinder(diametre_maximal/2, 3)

cylinder_4 = Part.makeCylinder(diametre_maximal/2 - 3 - 5 - 3 - 2, 3)

# cylinder_3 cut by cylinder_4
cylinder_3 = cylinder_3.cut(cylinder_4)

# cylinder_1 cut by cylinder_3
cylinder_3_vector = FreeCAD.Vector(0, 0, 3)
cylinder_3.translate(cylinder_3_vector)
cylinder_1 = cylinder_1.cut(cylinder_3)

# holes for fixing the tank
degre = 10
for i in range(int(360/degre)):
    radius = diametre_maximal/2 - 3 - 2.5
    alpha=(i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(2.5, 3)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

# holes for fixing the anodes and the cathodes
degre = 60
for i in range(int(360/degre)):
    radius = diametre_maximal/2 - 3 - 5 - 3 - 2 - 3 - 2 - 2 - 4 - 5
    alpha=(i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(5, 3)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

Part.show(cylinder_1)

DOC.recompute()

# insertion part_rondelle_m10_17d - 0
degre = 60
radius = diametre_maximal/2 - 3 - 5 - 3 - 2 - 3 - 2 - 2 - 4 - 5
alpha=(degre*math.pi)/180
vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), -1)
Mesh.insert(u"part_rondelle_m10_17d.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_rondelle_m10_17d").Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly").getObject("part_rondelle_m10_17d").ShapeColor = (1.00,1.00,0.00)

# For placing the part_rondelle_m10_17d
i1 = 1
degres = [120, 180, 240, 300, 360]
for degre in degres:
    radius = diametre_maximal/2 - 3 - 5 - 3 - 2 - 3 - 2 - 2 - 4 - 5
    alpha=(degre*math.pi)/180
    vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), -1)
    Mesh.insert(u"part_rondelle_m10_17d.stl", "assembly")
    FreeCAD.getDocument("assembly").getObject("part_rondelle_m10_17d00" + str(i1)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
    FreeCADGui.getDocument("assembly").getObject("part_rondelle_m10_17d00" + str(i1)).ShapeColor = (1.00,1.00,0.00)
    i1 += 1

# For placing the part_rondelle_m10_17d
for i in range(7, 14):
    Mesh.insert(u"part_rondelle_m10_17d.stl", "assembly")

for i in range(7, 13):
    alpha=(i*60*math.pi)/180
    radius = diametre_maximal/2 - 3 - 5 - 3 - 2 - 3 - 2 - 2 - 4 - 5
    vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 3)
    
    if i < 10:
        FreeCAD.getDocument("assembly").getObject("part_rondelle_m10_17d00" + str(i)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
        FreeCADGui.getDocument("assembly").getObject("part_rondelle_m10_17d00" + str(i)).ShapeColor = (1.00,1.00,0.00)
    else:
        FreeCAD.getDocument("assembly").getObject("part_rondelle_m10_17d0" + str(i)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
        FreeCADGui.getDocument("assembly").getObject("part_rondelle_m10_17d0" + str(i)).ShapeColor = (1.00,1.00,0.00)

# insertion part_vis_metal_m10_200l - 0
degre = 60
radius = diametre_maximal/2 - 3 - 5 - 3 - 2 - 3 - 2 - 2 - 4 - 5
alpha=(degre*math.pi)/180
vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), -3)
Mesh.insert(u"part_vis_metal_m10_200l.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_vis_metal_m10_200l").Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly").getObject("part_vis_metal_m10_200l").ShapeColor = (0.00,1.00,1.00)

# For placing the part_vis_metal_m10_200l
i1 = 1
degres = [120, 180, 240, 300, 360]
for degre in degres:
    radius = diametre_maximal/2 - 3 - 5 - 3 - 2 - 3 - 2 - 2 - 4 - 5
    alpha=(degre*math.pi)/180
    vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), -3)
    Mesh.insert(u"part_vis_metal_m10_200l.stl", "assembly")
    FreeCAD.getDocument("assembly").getObject("part_vis_metal_m10_200l00" + str(i1)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
    FreeCADGui.getDocument("assembly").getObject("part_vis_metal_m10_200l00" + str(i1)).ShapeColor = (0.00,1.00,1.00)
    i1 += 1
    
# insertion part_ecrou_10m - 0
degre = 60
radius = diametre_maximal/2 - 3 - 5 - 3 - 2 - 3 - 2 - 2 - 4 - 5
alpha=(degre*math.pi)/180
vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 4)
Mesh.insert(u"part_ecrou_10m.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_ecrou_10m").Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly").getObject("part_ecrou_10m").ShapeColor = (0.00,0.00,1.00)

# For placing the part_ecrou_10m
i1 = 1
degres = [120, 180, 240, 300, 360]
for degre in degres:
    radius = diametre_maximal/2 - 3 - 5 - 3 - 2 - 3 - 2 - 2 - 4 - 5
    alpha=(degre*math.pi)/180
    vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 4)
    Mesh.insert(u"part_ecrou_10m.stl", "assembly")
    FreeCAD.getDocument("assembly").getObject("part_ecrou_10m00" + str(i1)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
    FreeCADGui.getDocument("assembly").getObject("part_ecrou_10m00" + str(i1)).ShapeColor = (0.00,0.00,1.00)
    i1 += 1

# For placing the part_rondelle_m10_17d
for i in range(15, 21):
    Mesh.insert(u"part_rondelle_m10_17d.stl", "assembly")

for i in range(13, 19):
    alpha=(i*60*math.pi)/180
    radius = diametre_maximal/2 - 3 - 5 - 3 - 2 - 3 - 2 - 2 - 4 - 5
    vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 8)
    FreeCAD.getDocument("assembly").getObject("part_rondelle_m10_17d0" + str(i)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
    FreeCADGui.getDocument("assembly").getObject("part_rondelle_m10_17d0" + str(i)).ShapeColor = (1.00,1.00,0.00)

# insertion part_capacitor_plate - 0
vector = App.Vector(0, 0, 9)
Mesh.insert(u"part_capacitor_plate.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_capacitor_plate").Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly").getObject("part_capacitor_plate").ShapeColor = (0.00,0.50,0.50)

# For placing the part_rondelle_m10_17d
for i in range(22, 28):
    Mesh.insert(u"part_rondelle_m10_17d.stl", "assembly")

for i in range(19, 25):
    alpha=(i*60*math.pi)/180
    radius = diametre_maximal/2 - 3 - 5 - 3 - 2 - 3 - 2 - 2 - 4 - 5
    vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 10)
    FreeCAD.getDocument("assembly").getObject("part_rondelle_m10_17d0" + str(i)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
    FreeCADGui.getDocument("assembly").getObject("part_rondelle_m10_17d0" + str(i)).ShapeColor = (1.00,1.00,0.00)

# insertion part_capacitor_plate - 1
vector = App.Vector(0, 0, 11)
Mesh.insert(u"part_capacitor_plate.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_capacitor_plate001").Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 60))
FreeCADGui.getDocument("assembly").getObject("part_capacitor_plate001").ShapeColor = (0.00,0.50,0.50)

# For placing all the part_capacitor_plate
for i in range(2, 10):
    if i % 2 == 0:
        vector = App.Vector(0, 0, i*2 + 9)
        Mesh.insert(u"part_capacitor_plate.stl", "assembly")
        FreeCAD.getDocument("assembly").getObject("part_capacitor_plate00" + str(i)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
        FreeCADGui.getDocument("assembly").getObject("part_capacitor_plate00" + str(i)).ShapeColor = (0.00,0.50,0.50)
    else:
        vector = App.Vector(0, 0, i*2 + 9)
        Mesh.insert(u"part_capacitor_plate.stl", "assembly")
        FreeCAD.getDocument("assembly").getObject("part_capacitor_plate00" + str(i)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 60))
        FreeCADGui.getDocument("assembly").getObject("part_capacitor_plate00" + str(i)).ShapeColor = (0.00,0.50,0.50)

# For placing all the part_capacitor_plate
for i in range(10, 90):
    if i % 2 == 0:
        vector = App.Vector(0, 0, i*2 + 9)
        Mesh.insert(u"part_capacitor_plate.stl", "assembly")
        FreeCAD.getDocument("assembly").getObject("part_capacitor_plate0" + str(i)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
        FreeCADGui.getDocument("assembly").getObject("part_capacitor_plate0" + str(i)).ShapeColor = (0.00,0.50,0.50)
    else:
        vector = App.Vector(0, 0, i*2 + 9)
        Mesh.insert(u"part_capacitor_plate.stl", "assembly")
        FreeCAD.getDocument("assembly").getObject("part_capacitor_plate0" + str(i)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 60))
        FreeCADGui.getDocument("assembly").getObject("part_capacitor_plate0" + str(i)).ShapeColor = (0.00,0.50,0.50)

setview()
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
