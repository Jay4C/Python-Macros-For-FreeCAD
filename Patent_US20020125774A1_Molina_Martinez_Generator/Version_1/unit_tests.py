import os
import time
import unittest
import pywinauto.mouse
import pywinauto.keyboard


# https://patents.google.com/patent/US20020125774A1/en?oq=US20020125774
class UnitTestsPatentUS20020125774A1MolinaMartinezGenerator(unittest.TestCase):
    # ok
    def test_part_stator(self):
        print("test_part_stator")

        if os.path.exists("part_stator.py"):
            os.remove("part_stator.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_stator.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh, importDXF

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_stator"


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

maximal_diameter = 100

# part_stator
part_stator = Part.makeCylinder(maximal_diameter/2, 1)

cylinder_1 = Part.makeCylinder(maximal_diameter/2 - 5 - 5 - 5, 1)

# part_stator cut by cylinder_1
part_stator = part_stator.cut(cylinder_1)

# holes for fixing the stator
degree = 180
for i in range(int(360/degree)):
    radius = maximal_diameter/2 - 5 - 2.5
    alpha=(i*degree*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(2.5, 1)
    hole.translate(hole_vector)
    part_stator = part_stator.cut(hole)

Part.show(part_stator)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_stator").getObject("Shape"))

stl_file = u"part_stator.stl"

Mesh.export(__objs__, stl_file)

dxf_file = u"part_stator.dxf"

importDXF.export(__objs__, dxf_file)

setview()
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"part_stator.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_part_rotor(self):
        print("test_part_rotor")

        if os.path.exists("part_rotor.py"):
            os.remove("part_rotor.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_rotor.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh, importDXF

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_rotor"


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

maximal_diameter = 100

# part_rotor
part_rotor = Part.makeCylinder(maximal_diameter/2 - 5 - 5 - 5, 1)

# part_rotor cut by cylinder_1
cylinder_1 = Part.makeCylinder(2.5, 1)
part_rotor = part_rotor.cut(cylinder_1)

# holes for fixing the rotors
degree = 180
for i in range(int(360/degree)):
    radius = 2.5 + 10 + 2.5
    alpha=(i*degree*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(2.5, 1)
    hole.translate(hole_vector)
    part_rotor = part_rotor.cut(hole)

# holes for fixing the wires
degree = 30
for i in range(int(360/degree)):
    radius = maximal_diameter/2 - 5 - 5 - 5
    alpha=(i*degree*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(6.5, 1)
    hole.translate(hole_vector)
    part_rotor = part_rotor.cut(hole)

Part.show(part_rotor)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_rotor").getObject("Shape"))

stl_file = u"part_rotor.stl"

Mesh.export(__objs__, stl_file)

dxf_file = u"part_rotor.dxf"

importDXF.export(__objs__, dxf_file)

setview()
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"part_rotor.py"{)}.read{(}{)}{)}'
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
            file.write("""import FreeCAD, Part, Drawing, math, Mesh, importDXF

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

maximal_diameter = 100

# part_support
part_support = Part.makeCylinder(maximal_diameter/2, 1)

# part_support cut by cylinder_1
cylinder_1 = Part.makeCylinder(2.5, 1)
part_support = part_support.cut(cylinder_1)

# holes for fixing the stator
degree = 180
for i in range(int(360/degree)):
    radius = maximal_diameter/2 - 5 - 2.5
    alpha=(i*degree*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(2.5, 1)
    hole.translate(hole_vector)
    part_support = part_support.cut(hole)

Part.show(part_support)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_support").getObject("Shape"))

stl_file = u"part_support.stl"

Mesh.export(__objs__, stl_file)

dxf_file = u"part_support.dxf"

importDXF.export(__objs__, dxf_file)

setview()
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

# insertion part_stator
Mesh.insert(u"part_stator.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_stator").Placement = App.Placement(App.Vector(0, 0, 0), App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly").getObject("part_stator").ShapeColor = (0.50,0.50,0.50)
FreeCADGui.getDocument("assembly").getObject("part_stator").Transparency = 70

# insertion part_rotor
Mesh.insert(u"part_rotor.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_rotor").Placement = App.Placement(App.Vector(0, 0, 0), App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly").getObject("part_rotor").ShapeColor = (0.10,0.20,0.30)

# insertion part_support
Mesh.insert(u"part_support.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_support").Placement = App.Placement(App.Vector(0, 0, -1), App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly").getObject("part_support").ShapeColor = (0.30,0.60,0.90)
FreeCADGui.getDocument("assembly").getObject("part_support").Transparency = 80

number_of_steps = 123

# insertion part_stator
for i in range(0, number_of_steps):
    location = (i+1)
    
    if i < 9:
        Mesh.insert(u"part_stator.stl", "assembly")
        FreeCAD.getDocument("assembly").getObject("part_stator00" + str(i+1)).Placement = App.Placement(App.Vector(0, 0, location), App.Rotation(App.Vector(0,0,1), 0))
        FreeCADGui.getDocument("assembly").getObject("part_stator00" + str(i+1)).ShapeColor = (0.50,0.50,0.50)
        FreeCADGui.getDocument("assembly").getObject("part_stator00" + str(i+1)).Transparency = 70
    elif i < 99:
        Mesh.insert(u"part_stator.stl", "assembly")
        FreeCAD.getDocument("assembly").getObject("part_stator0" + str(i+1)).Placement = App.Placement(App.Vector(0, 0, location), App.Rotation(App.Vector(0,0,1), 0))
        FreeCADGui.getDocument("assembly").getObject("part_stator0" + str(i+1)).ShapeColor = (0.50,0.50,0.50)
        FreeCADGui.getDocument("assembly").getObject("part_stator0" + str(i+1)).Transparency = 70
    else:
        Mesh.insert(u"part_stator.stl", "assembly")
        FreeCAD.getDocument("assembly").getObject("part_stator" + str(i+1)).Placement = App.Placement(App.Vector(0, 0, location), App.Rotation(App.Vector(0,0,1), 0))
        FreeCADGui.getDocument("assembly").getObject("part_stator" + str(i+1)).ShapeColor = (0.50,0.50,0.50)
        FreeCADGui.getDocument("assembly").getObject("part_stator" + str(i+1)).Transparency = 70
        
# insertion part_rotor
for i in range(0, number_of_steps):
    location = (i+1)
    
    if i < 9:
        Mesh.insert(u"part_rotor.stl", "assembly")
        FreeCAD.getDocument("assembly").getObject("part_rotor00" + str(i+1)).Placement = App.Placement(App.Vector(0, 0, location), App.Rotation(App.Vector(0,0,1), 0))
        FreeCADGui.getDocument("assembly").getObject("part_rotor00" + str(i+1)).ShapeColor = (0.10,0.20,0.30)
    elif i < 99:
        Mesh.insert(u"part_rotor.stl", "assembly")
        FreeCAD.getDocument("assembly").getObject("part_rotor0" + str(i+1)).Placement = App.Placement(App.Vector(0, 0, location), App.Rotation(App.Vector(0,0,1), 0))
        FreeCADGui.getDocument("assembly").getObject("part_rotor0" + str(i+1)).ShapeColor = (0.10,0.20,0.30)
    else:
        Mesh.insert(u"part_rotor.stl", "assembly")
        FreeCAD.getDocument("assembly").getObject("part_rotor" + str(i+1)).Placement = App.Placement(App.Vector(0, 0, location), App.Rotation(App.Vector(0,0,1), 0))
        FreeCADGui.getDocument("assembly").getObject("part_rotor" + str(i+1)).ShapeColor = (0.10,0.20,0.30)

# insertion part_support
Mesh.insert(u"part_support.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_support001").Placement = App.Placement(App.Vector(0, 0, number_of_steps+1), App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly").getObject("part_support001").ShapeColor = (0.30,0.60,0.90)
FreeCADGui.getDocument("assembly").getObject("part_support001").Transparency = 80

setview()

__objs__ = []
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_stator"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rotor"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_support"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_support001"))

# append part_stator
for i in range(0, number_of_steps):
    if i < 9:
        __objs__.append(FreeCAD.getDocument("assembly").getObject("part_stator00" + str(i+1)))
    elif i < 99:
        __objs__.append(FreeCAD.getDocument("assembly").getObject("part_stator0" + str(i+1)))
    else:
        __objs__.append(FreeCAD.getDocument("assembly").getObject("part_stator" + str(i+1)))

# append part_rotor
for i in range(0, number_of_steps):
    if i < 9:
        __objs__.append(FreeCAD.getDocument("assembly").getObject("part_rotor00" + str(i+1)))
    elif i < 99:
        __objs__.append(FreeCAD.getDocument("assembly").getObject("part_rotor0" + str(i+1)))
    else:
        __objs__.append(FreeCAD.getDocument("assembly").getObject("part_rotor" + str(i+1)))

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
