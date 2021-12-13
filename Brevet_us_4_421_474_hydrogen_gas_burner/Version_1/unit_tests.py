import time
import unittest
import os
import pywinauto.mouse
import pywinauto.keyboard


# https://patents.google.com/patent/US4421474A/en?oq=US4421474
class brevet_us_4_421_474_hydrogen_gas_burner_version_1(unittest.TestCase):
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
    # https://www.leroymerlin.fr/produits/chauffage-plomberie/circuit-alimentation-en-eau/tube-et-raccord-alimentation/raccord-alimentation/lot-de-2-manchons-a-visser-laiton-f-12-x-17-pour-tube-en-cuivre-65815253.html
    def test_part_element_64(self):
        print("test_part_element_64")

        if os.path.exists("part_element_64.py"):
            os.remove("part_element_64.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_element_64.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_element_64"


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

diametre_maximal = 22

cylinder_1 = Part.makeCylinder(diametre_maximal/2, 18)

cylinder_2 = Part.makeCylinder(16.4/2, 18)

cylinder_1 = cylinder_1.cut(cylinder_2)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_element_64").getObject("Shape"))

stl_file = u"part_element_64.stl"

Mesh.export(__objs__, stl_file)

setview()
    """)

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"part_element_64.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.leroymerlin.fr/produits/chauffage-plomberie/circuit-alimentation-en-eau/tube-et-raccord-alimentation/raccord-alimentation/lot-de-2-mamelons-a-visser-laiton-m-12-x-17-pour-tube-en-cuivre-65814231.html
    def test_part_element_32(self):
        print("test_part_element_32")

        if os.path.exists("part_element_32.py"):
            os.remove("part_element_32.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_element_32.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_element_32"


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

diametre_maximal = 19

cylinder_1 = Part.makeCylinder(diametre_maximal/2, 19)

cylinder_2 = Part.makeCylinder(11/2, 19)

cylinder_1 = cylinder_1.cut(cylinder_2)

cylinder_3 = Part.makeCylinder(diametre_maximal/2, 8)

cylinder_4 = Part.makeCylinder(16/2, 8)

cylinder_3 = cylinder_3.cut(cylinder_4)

cylinder_1 = cylinder_1.cut(cylinder_3)

cylinder_3_vector = FreeCAD.Vector(0, 0, 11)
cylinder_3.translate(cylinder_3_vector)
cylinder_1 = cylinder_1.cut(cylinder_3)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_element_32").getObject("Shape"))

stl_file = u"part_element_32.stl"

Mesh.export(__objs__, stl_file)

setview()
    """)

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"part_element_32.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_part_element_10(self):
        print("test_part_element_10")

        if os.path.exists("part_element_10.py"):
            os.remove("part_element_10.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_element_10.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh, math

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_element_10"


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

rayon_maximal = 11 + 5 + 1.5 + 2.5 + 3.5 + 5 + 3.5 + 2.5

cylinder_1 = Part.makeCylinder(rayon_maximal, 70)

cylinder_2 = Part.makeCylinder(11 + 5, 70)

cylinder_1 = cylinder_1.cut(cylinder_2)

cylinder_3 = Part.makeCylinder(rayon_maximal, 70)

cylinder_4 = Part.makeCylinder(11 + 5 + 1.5, 70)

cylinder_3 = cylinder_3.cut(cylinder_4)

cylinder_3_vector = FreeCAD.Vector(0, 0, 4)
cylinder_3.translate(cylinder_3_vector)
cylinder_1 = cylinder_1.cut(cylinder_3)

# holes for fixing the gas burner
degre = 60
for i in range(int(360/degre)):
    radius = 11 + 5 + 1.5 + 2.5 + 3.5 + 2.5
    alpha=(i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(2.5, 5)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

cylinder_5 = Part.makeCylinder(11 + 5 + 1.5 + 3.5, 2)

cylinder_6 = Part.makeCylinder(11 + 5 + 1.5 + 2, 2)

cylinder_5 = cylinder_5.cut(cylinder_6)

cylinder_1 = cylinder_1.cut(cylinder_5)

# Cut the holes for fixing the air
degre = 30
for i in range(int(360/degre)):
    axe_y = FreeCAD.Vector(0, 1, 0)
    axe_z = FreeCAD.Vector(0, 0, 1)
    radius_hole = 11 + 3.5
    alpha=(i*degre*math.pi)/180
    cylinder_vector = FreeCAD.Vector(radius_hole*math.cos(alpha), radius_hole*math.sin(alpha), 4 + 7.5)
    cylinder = Part.makeCylinder(2.5, 10, cylinder_vector, axe_y)
    cylinder.rotate(cylinder_vector, axe_z, alpha*(360/(2*math.pi)) - 90)
    cylinder_1 = cylinder_1.cut(cylinder)

# Cut the holes for fixing the air
degre = 30
for i in range(int(360/degre)):
    axe_y = FreeCAD.Vector(0, 1, 0)
    axe_z = FreeCAD.Vector(0, 0, 1)
    radius_hole = 11 + 3.5
    alpha=(i*degre*math.pi)/180
    cylinder_vector = FreeCAD.Vector(radius_hole*math.cos(alpha), radius_hole*math.sin(alpha), 70 - 7.5)
    cylinder = Part.makeCylinder(2.5, 10, cylinder_vector, axe_y)
    cylinder.rotate(cylinder_vector, axe_z, alpha*(360/(2*math.pi)) - 90)
    cylinder_1 = cylinder_1.cut(cylinder)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_element_10").getObject("Shape"))

stl_file = u"part_element_10.stl"

Mesh.export(__objs__, stl_file)

setview()
        """)

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"part_element_10.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_part_element_30(self):
        print("test_part_element_30")

        if os.path.exists("part_element_30.py"):
            os.remove("part_element_30.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_element_30.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh, math

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_element_30"


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

rayon_maximal = 11 + 5 + 1.5 + 2.5 + 3.5 + 5 + 3.5 + 2.5

cylinder_1 = Part.makeCylinder(rayon_maximal, 7)

cylinder_2 = Part.makeCylinder(16/2, 7)

cylinder_1 = cylinder_1.cut(cylinder_2)

cylinder_3 = Part.makeCylinder(11 + 5 + 1.5 + 2, 3)

cylinder_3_vector = FreeCAD.Vector(0, 0, 4)
cylinder_3.translate(cylinder_3_vector)
cylinder_1 = cylinder_1.cut(cylinder_3)

cylinder_4 = Part.makeCylinder(rayon_maximal, 3)

cylinder_5 = Part.makeCylinder(11 + 5 + 1.5 + 3.5, 3)

cylinder_4 = cylinder_4.cut(cylinder_5)

cylinder_4_vector = FreeCAD.Vector(0, 0, 4)
cylinder_4.translate(cylinder_4_vector)
cylinder_1 = cylinder_1.cut(cylinder_4)

# holes for fixing the gas burner
degre = 60
for i in range(int(360/degre)):
    radius = 11 + 5 + 1.5 + 2.5 + 3.5 + 2.5
    alpha=(i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(2.5, 5)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_element_30").getObject("Shape"))

stl_file = u"part_element_30.stl"

Mesh.export(__objs__, stl_file)

setview()
    """)

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"part_element_30.py"{)}.read{(}{)}{)}'
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
EPS_C = EPS * (-0.5)

# insertion part_element_30
Mesh.insert(u"part_element_30.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_element_30").Placement = App.Placement(App.Vector(0, 0, 0), App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly").getObject("part_element_30").ShapeColor = (1.00,1.00,0.00)

# insertion part_element_10
Mesh.insert(u"part_element_10.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_element_10").Placement = App.Placement(App.Vector(0, 0, 5), App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly").getObject("part_element_10").ShapeColor = (0.10,0.10,0.00)
FreeCADGui.getDocument("assembly").getObject("part_element_10").Transparency = 70

# insertion part_element_64
Mesh.insert(u"part_element_64.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_element_64").Placement = App.Placement(App.Vector(0, 0, 4), App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly").getObject("part_element_64").ShapeColor = (0.10,0.20,0.30)

# insertion part_element_32
Mesh.insert(u"part_element_32.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_element_32").Placement = App.Placement(App.Vector(0, 0, -11), App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly").getObject("part_element_32").ShapeColor = (0.20,0.40,0.60)

setview()

__objs__ = []
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_element_10"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_element_30"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_element_64"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_element_32"))

stl_file = u"assembly.stl"

Mesh.export(__objs__, stl_file)

del __objs__
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
