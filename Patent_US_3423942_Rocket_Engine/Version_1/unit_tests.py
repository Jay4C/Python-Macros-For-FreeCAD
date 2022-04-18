import os
import time
import unittest
import pywinauto.mouse
import pywinauto.keyboard


# https://patents.google.com/patent/US3423942A/en?q=rocket+engine&before=priority:19900101
class UnitTestsPatentUS3423942RocketEngineVersion(unittest.TestCase):
    # ok
    def test_part_nozzle(self):
        print("test_part_nozzle")

        if os.path.exists("part_nozzle.py"):
            os.remove("part_nozzle.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_nozzle.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_nozzle"


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

diametre_maximal_of_nozzle_front = 85

# part_nozzle
part_nozzle = Part.makeCylinder(diametre_maximal_of_nozzle_front/2, 3)

# part_nozzle cut by cylinder_1
cylinder_1 = Part.makeCylinder(diametre_maximal_of_nozzle_front/2 - 3.5 - 5 - 4.5 - 2, 3)
part_nozzle = part_nozzle.cut(cylinder_1)

# holes for fixing the nozzle
degree = 60
for i in range(int(360/degree)):
    radius = diametre_maximal_of_nozzle_front/2 - 2.5 - 3.5
    alpha=(i*degree*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(2.5, 3)
    hole.translate(hole_vector)
    part_nozzle = part_nozzle.cut(hole)

# cone_1
cone_1_radius_1 = diametre_maximal_of_nozzle_front/2 - 3.5 - 5 - 4.5
cone_1_radius_2 = 20/2
cone_1_height = 50
cone_1 = Part.makeCone(cone_1_radius_1, cone_1_radius_2, cone_1_height)    

# cone_2
cone_2_radius_1 = cone_1_radius_1 - 2
cone_2_radius_2 = cone_1_radius_2 - 2
cone_2_height = 50
cone_2 = Part.makeCone(cone_2_radius_1, cone_2_radius_2, cone_2_height)    

# cone_1 cut by cone_2
cone_1 = cone_1.cut(cone_2)

# part_nozzle fused with cone_1
cone_1_vector = FreeCAD.Vector(0, 0, 3)
cone_1.translate(cone_1_vector)
part_nozzle = part_nozzle.fuse(cone_1)

# cone_3
cone_3_radius_1 = 20/2
cone_3_radius_2 = diametre_maximal_of_nozzle_front/2
cone_3_height = 100
cone_3 = Part.makeCone(cone_3_radius_1, cone_3_radius_2, cone_3_height)    

# cone_4
cone_4_radius_1 = cone_3_radius_1 - 2
cone_4_radius_2 = cone_3_radius_2 - 2
cone_4_height = 100
cone_4 = Part.makeCone(cone_4_radius_1, cone_4_radius_2, cone_4_height)    

# cone_3 cut by cone_4
cone_3 = cone_3.cut(cone_4)

# part_nozzle fused with cone_3
cone_3_vector = FreeCAD.Vector(0, 0, 3 + cone_1_height)
cone_3.translate(cone_3_vector)
part_nozzle = part_nozzle.fuse(cone_3)

Part.show(part_nozzle)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_nozzle").getObject("Shape"))

stl_file = u"part_nozzle.stl"

Mesh.export(__objs__, stl_file)

setview()
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"part_nozzle.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_part_gas_entry(self):
        print("test_part_gas_entry")

        if os.path.exists("part_gas_entry.py"):
            os.remove("part_gas_entry.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_gas_entry.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_gas_entry"


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

diametre_maximal_of_nozzle_front = 85

# part_gas_entry
part_gas_entry = Part.makeCylinder(diametre_maximal_of_nozzle_front/2, 3)

# part_gas_entry cut by cylinder_1
cylinder_1 = Part.makeCylinder(11/2, 3)
part_gas_entry = part_gas_entry.cut(cylinder_1)

# holes for fixing the nozzle
degree = 60
for i in range(int(360/degree)):
    radius = diametre_maximal_of_nozzle_front/2 - 2.5 - 3.5
    alpha=(i*degree*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(2.5, 3)
    hole.translate(hole_vector)
    part_gas_entry = part_gas_entry.cut(hole)

Part.show(part_gas_entry)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_gas_entry").getObject("Shape"))

stl_file = u"part_gas_entry.stl"

Mesh.export(__objs__, stl_file)

setview()
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"part_gas_entry.py"{)}.read{(}{)}{)}'
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

# insertion part_gas_entry
Mesh.insert(u"part_gas_entry.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_gas_entry").Placement = App.Placement(App.Vector(0, 0, 0), App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly").getObject("part_gas_entry").ShapeColor = (0.50,0.40,0.30)

# insertion part_nozzle
Mesh.insert(u"part_nozzle.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_nozzle").Placement = App.Placement(App.Vector(0, 0, 3), App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly").getObject("part_nozzle").ShapeColor = (0.10,0.20,0.30)
FreeCADGui.getDocument("assembly").getObject("part_nozzle").Transparency = 70

# insertion part_element_64
Mesh.insert(u"part_element_64.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_element_64").Placement = App.Placement(App.Vector(0, 0, 3), App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly").getObject("part_element_64").ShapeColor = (0.90,0.80,0.70)

# insertion part_element_32
Mesh.insert(u"part_element_32.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_element_32").Placement = App.Placement(App.Vector(0, 0, -11), App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly").getObject("part_element_32").ShapeColor = (0.70,0.80,0.90)

setview()

__objs__ = []
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_gas_entry"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_nozzle"))
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
