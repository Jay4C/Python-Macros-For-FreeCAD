import os
import time
import unittest
import pywinauto.mouse
import pywinauto.keyboard


# https://patents.google.com/patent/US4324640A/en?q=pyrolysis+reactor&country=US&before=priority:19900101&page=2
class UnitTestsPatentUS4324640APyrolysisProcess(unittest.TestCase):
    # ok
    def test_part_chamber(self):
        print("test_part_chamber")

        if os.path.exists("part_chamber.py"):
            os.remove("part_chamber.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_chamber.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_chamber"


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

diametre_maximal_of_the_chamber = 500

height_maximal_of_the_chamber = 1000

# part_chamber
part_chamber = Part.makeCylinder(diametre_maximal_of_the_chamber/2, height_maximal_of_the_chamber)

cylinder_1 = Part.makeCylinder(diametre_maximal_of_the_chamber/2 - 3, height_maximal_of_the_chamber)

# part_chamber cut by cylinder_1
part_chamber = part_chamber.cut(cylinder_1)

Part.show(part_chamber)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_chamber").getObject("Shape"))

stl_file = u"part_chamber.stl"

Mesh.export(__objs__, stl_file)

setview()
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"part_chamber.py"{)}.read{(}{)}{)}'
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
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

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

diametre_maximal_of_the_chamber = 500 

# part_bottom_support
part_bottom_support = Part.makeCylinder((diametre_maximal_of_the_chamber + 10*2 + 10*2 + 10*2)/2, 5)

# holes for fixing the bottom support
degree = 90
for i in range(int(360/degree)):
    radius = (diametre_maximal_of_the_chamber)/2 + 10 + 5
    alpha=(i*degree*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(5, 5)
    hole.translate(hole_vector)
    part_bottom_support = part_bottom_support.cut(hole)

Part.show(part_bottom_support)

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
            'exec{(}open{(}"part_bottom_support.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_part_top_support(self):
        print("test_part_top_support")

        if os.path.exists("part_top_support.py"):
            os.remove("part_top_support.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_top_support.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

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

diametre_maximal_of_the_chamber = 500 

# part_top_support
part_top_support = Part.makeCylinder((diametre_maximal_of_the_chamber + 10*2 + 10*2 + 10*2)/2, 5)

# holes for fixing the top support
degree = 90
for i in range(int(360/degree)):
    radius = (diametre_maximal_of_the_chamber)/2 + 10 + 5
    alpha=(i*degree*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(5, 5)
    hole.translate(hole_vector)
    part_top_support = part_top_support.cut(hole)
    
# holes for letting the gas to go out of the chamber and putting the waste to go into the chamber
degree = 180
for i in range(int(360/degree)):
    radius = (diametre_maximal_of_the_chamber)/4
    alpha=(i*degree*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(50, 5)
    hole.translate(hole_vector)
    part_top_support = part_top_support.cut(hole)

Part.show(part_top_support)

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
            'exec{(}open{(}"part_top_support.py"{)}.read{(}{)}{)}'
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

# insertion part_top_support
Mesh.insert(u"part_top_support.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_top_support").Placement = App.Placement(App.Vector(0, 0, 1000), App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly").getObject("part_top_support").ShapeColor = (0.10,0.10,0.10)

# insertion part_chamber
Mesh.insert(u"part_chamber.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_chamber").Placement = App.Placement(App.Vector(0, 0, 0), App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly").getObject("part_chamber").ShapeColor = (0.30,0.20,0.10)
FreeCADGui.getDocument("assembly").getObject("part_chamber").Transparency = 70

# insertion part_bottom_support
Mesh.insert(u"part_bottom_support.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_bottom_support").Placement = App.Placement(App.Vector(0, 0, -5), App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly").getObject("part_bottom_support").ShapeColor = (0.90,0.80,0.70)

setview()

__objs__ = []
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_chamber"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_bottom_support"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_top_support"))

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
