import os
import time
import unittest
import pywinauto.mouse
import pywinauto.keyboard


# https://patents.google.com/patent/US20150188400A1/en?q=H02K53%2f00
class UnitTestsPatentUS20150188400A1MagneticFlywheelInductionEMGakaHatemMotor(unittest.TestCase):
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

maximal_heigth = 15

# part_rotor
part_rotor = Part.makeCylinder(maximal_diameter/2, maximal_heigth)

# part_rotor cut by cylinder_1
cylinder_1 = Part.makeCylinder(5, maximal_heigth)
part_rotor = part_rotor.cut(cylinder_1)

# holes for fixing the magnets
degre = 30
for i in range(int(360/degre)):
    radius = maximal_diameter/2 - 12.5
    alpha=(i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(7.5, maximal_heigth)
    hole.translate(hole_vector)
    part_rotor = part_rotor.cut(hole)

# holes for the cooling
degre = 90
for i in range(int(360/degre)):
    radius = 5 + 12.5
    alpha=(i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(7.5, maximal_heigth)
    hole.translate(hole_vector)
    part_rotor = part_rotor.cut(hole)

# holes for the cooling
degres = [1*45, 3*45, 5*45, 7*45]
for degre in degres:
    radius = math.sqrt(2*math.pow(16.25,2))
    alpha=(degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(7.5, maximal_heigth)
    hole.translate(hole_vector)
    part_rotor = part_rotor.cut(hole)

# Cut the holes for the screws fixing the magnets
for i in range(12):
    axe_y = FreeCAD.Vector(0, 1, 0)
    axe_z = FreeCAD.Vector(0, 0, 1)
    radius_screw = maximal_diameter/2 - 10
    alpha = (i*2*math.pi)/12
    hole_vector = FreeCAD.Vector(radius_screw*math.cos(alpha), radius_screw*math.sin(alpha), 7.5)
    hole = Part.makeCylinder(2.5, maximal_diameter/2 - 10, hole_vector, axe_y)
    hole.rotate(hole_vector, axe_z, alpha*(360/(2*math.pi)) - 90)
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
    def test_part_magnet(self):
        print("test_part_magnet")

        if os.path.exists("part_magnet.py"):
            os.remove("part_magnet.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_magnet.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_magnet"


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

maximal_diameter = 15

maximal_heigth = 3

# part_magnet
part_magnet = Part.makeCylinder(maximal_diameter/2, maximal_heigth)

# part_magnet cut by cylinder_1
cylinder_1 = Part.makeCylinder(2.5, maximal_heigth)
part_magnet = part_magnet.cut(cylinder_1)

Part.show(part_magnet)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_magnet").getObject("Shape"))

stl_file = u"part_magnet.stl"

Mesh.export(__objs__, stl_file)

setview()
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"part_magnet.py"{)}.read{(}{)}{)}'
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

maximal_diameter = 100

# insertion part_rotor
Mesh.insert(u"part_rotor.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_rotor").Placement = App.Placement(App.Vector(0, 0, 0), App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly").getObject("part_rotor").ShapeColor = (0.30,0.20,0.10)
FreeCADGui.getDocument("assembly").getObject("part_rotor").Transparency = 40

# insertion part_magnet for fixing the magnets
degre = 30
for i in range(int(360/degre)):
    axe_x = FreeCAD.Vector(1, 0, 0)    
    axe_y = FreeCAD.Vector(0, 1, 0)
    axe_z = FreeCAD.Vector(0, 0, 1)
    
    Mesh.insert(u"part_magnet.stl", "assembly")
    radius = maximal_diameter/2 + 3
    alpha=(i*degre*math.pi)/180
    magnet_vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 7.5)
    rotation_magnet_vector = App.Rotation(alpha*(360/(2*math.pi)) - 90, 0, 90)
    
    if i < 1:
        FreeCAD.getDocument("assembly").getObject("part_magnet").Placement = App.Placement(magnet_vector, rotation_magnet_vector)
        FreeCADGui.getDocument("assembly").getObject("part_magnet").ShapeColor = (0.50,0.50,0.50)
    elif i >= 1 and i < 10:
        FreeCAD.getDocument("assembly").getObject("part_magnet00" + str(i)).Placement = App.Placement(magnet_vector, rotation_magnet_vector)
        FreeCADGui.getDocument("assembly").getObject("part_magnet00" + str(i)).ShapeColor = (0.50,0.50,0.50)
    else:
        FreeCAD.getDocument("assembly").getObject("part_magnet0" + str(i)).Placement = App.Placement(magnet_vector, rotation_magnet_vector)
        FreeCADGui.getDocument("assembly").getObject("part_magnet0" + str(i)).ShapeColor = (0.50,0.50,0.50)
        
setview()

__objs__ = []
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rotor"))

for i1 in range(int(360/degre)):
    if i1 < 1:
        __objs__.append(FreeCAD.getDocument("assembly").getObject("part_magnet"))
    elif i1 >=1 and i1 < 10:
        __objs__.append(FreeCAD.getDocument("assembly").getObject("part_magnet00" + str(i1)))
    else:
        __objs__.append(FreeCAD.getDocument("assembly").getObject("part_magnet0" + str(i1)))

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

    # ok
    def test_assembly_plant(self):
        print("test_assembly_plant")

        if os.path.exists("assembly_plant.py"):
            os.remove("assembly_plant.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("assembly_plant.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh, math

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_plant"


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

maximal_diameter = 100
ecart = 8

# insertion assembly
for i in range(0, 20):
    if i < 1:
        Mesh.insert(u"assembly.stl", "assembly_plant")
        FreeCAD.getDocument("assembly_plant").getObject("assembly").Placement = App.Placement(App.Vector((i+1)*(maximal_diameter + ecart), 0, 0), App.Rotation(App.Vector(0,0,1), 0))
        FreeCADGui.getDocument("assembly_plant").getObject("assembly").ShapeColor = (0.10,0.10,0.10)
    elif i >= 1 and i < 10:
        Mesh.insert(u"assembly.stl", "assembly_plant")
        FreeCAD.getDocument("assembly_plant").getObject("assembly00" + str(i)).Placement = App.Placement(App.Vector((i+1)*(maximal_diameter + ecart), 0, 0), App.Rotation(App.Vector(0,0,1), 0))
        FreeCADGui.getDocument("assembly_plant").getObject("assembly00" + str(i)).ShapeColor = (0.10,0.10,0.10)
    else:
        Mesh.insert(u"assembly.stl", "assembly_plant")
        FreeCAD.getDocument("assembly_plant").getObject("assembly0" + str(i)).Placement = App.Placement(App.Vector((i+1)*(maximal_diameter + ecart), 0, 0), App.Rotation(App.Vector(0,0,1), 0))
        FreeCADGui.getDocument("assembly_plant").getObject("assembly0" + str(i)).ShapeColor = (0.10,0.10,0.10)

setview()

__objs__ = []

for i in range(0, 20):
    if i < 1:
        __objs__.append(FreeCAD.getDocument("assembly_plant").getObject("assembly"))
    elif i >= 1 and i < 10:
        __objs__.append(FreeCAD.getDocument("assembly_plant").getObject("assembly00" + str(i)))
    else:
        __objs__.append(FreeCAD.getDocument("assembly_plant").getObject("assembly0" + str(i)))

stl_file = u"assembly_plant.stl"

Mesh.export(__objs__, stl_file)

del __objs__
        """)

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"assembly_plant.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')


if __name__ == '__main__':
    unittest.main()
