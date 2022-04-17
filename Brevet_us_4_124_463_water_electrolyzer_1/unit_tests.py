import time
import unittest
import os
import pywinauto.mouse
import pywinauto.keyboard


class brevet_us_4_124_463_water_electrolyzer_1_for_proof_of_concept(unittest.TestCase):
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
    def test_part_vis_metal_m5_100l(self):
        print("test_part_vis_metal_m5_100l")

        if os.path.exists("part_vis_metal_m5_100l.py"):
            os.remove("part_vis_metal_m5_100l.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_vis_metal_m5_100l.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_vis_metal_m5_100l"


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

cylinder_1 = Part.makeCylinder(6, 102)

cylinder_2 = Part.makeCylinder(2.5, 100)

cylinder_3 = Part.makeCylinder(6, 100)

# cylinder_3 cut by cylinder_2
cylinder_3 = cylinder_3.cut(cylinder_2)

# cylinder_1 cut by cylinder_3
cylinder_3_vector = FreeCAD.Vector(0, 0, 2)
cylinder_3.translate(cylinder_3_vector)
cylinder_1 = cylinder_1.cut(cylinder_3)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_vis_metal_m5_100l").getObject("Shape"))

stl_file = u"part_vis_metal_m5_100l.stl"

Mesh.export(__objs__, stl_file)

setview()
        """)

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"part_vis_metal_m5_100l.py"{)}.read{(}{)}{)}'
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

cylinder_1 = Part.makeCylinder(32, 2)

cylinder_2 = Part.makeCylinder(2.5, 2)

cylinder_1 = cylinder_1.cut(cylinder_2)

# holes for fixing the disc anode and the disc cathode
degree = 60
for i in range(int(360/degree)):
    radius = 32 - 3.5 - 2.5
    alpha=(i*degree*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(2.5, 2)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

# holes for letting the gas mixture to go out
for i in range(int(360/degree)):
    radius = 14.25
    alpha=(i*degree*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(6, 2)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

degrees = [30, 90, 150, -30, -90, -150]

for degree in degrees:
    radius = 24
    alpha=(int(degree)*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(6, 2)
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

cylinder_1 = Part.makeCylinder(32, 1)

cylinder_2 = Part.makeCylinder(2.5, 1)

cylinder_1 = cylinder_1.cut(cylinder_2)

# holes for fixing the anodes and letting the mixture to go out
degree = 30
for i in range(int(360/degree)):
    radius = 32 - 3.5 - 2.5
    alpha=(i*degree*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(2.5, 1)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)
    
# holes for fixing the cathodes
degrees = [60, 180, 300]
for degree in degrees:
    radius = 32
    alpha=(degree*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(9, 1)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

# holes for letting the gas mixture to go out
degree = 90
for i in range(int(360/degree)):
    radius = 7.5
    alpha=(i*degree*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(2.5, 1)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

# holes for letting the gas mixture to go out
degree = 45
for i in range(int(360/degree)):
    radius = 17.5
    alpha=(i*degree*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(2.5, 1)
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

cylinder_1 = Part.makeCylinder(32, 2)

cylinder_2 = Part.makeCylinder(2.5, 2)

cylinder_1 = cylinder_1.cut(cylinder_2)

# holes for fixing the disc anode and the disc cathode
degree = 60
for i in range(int(360/degree)):
    radius = 32 - 3.5 - 2.5
    alpha=(i*degree*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(2.5, 2)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

# holes for letting the gas mixture to go out
for i in range(int(360/degree)):
    radius = 14.25
    alpha=(i*degree*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(6, 2)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

degrees = [30, 90, 150, -30, -90, -150]

for degree in degrees:
    radius = 24
    alpha=(int(degree)*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(6, 2)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

Part.show(cylinder_1)

DOC.recompute()

# insertion part_rondelle_m5_12d - 0
Mesh.insert(u"part_rondelle_m5_12d.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_rondelle_m5_12d").Placement = App.Placement(App.Vector(0, 0, -1), App.Rotation(App.Vector(0,1,0), 0))
FreeCADGui.getDocument("assembly").getObject("part_rondelle_m5_12d").ShapeColor = (0.67,0.33,0.50)

# insertion part_rondelle_m5_12d - 1
Mesh.insert(u"part_rondelle_m5_12d.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_rondelle_m5_12d001").Placement = App.Placement(App.Vector(0, 0, 2), App.Rotation(App.Vector(0,1,0), 0))
FreeCADGui.getDocument("assembly").getObject("part_rondelle_m5_12d001").ShapeColor = (0.67,0.33,0.50)

# For placing all the part_rondelle_m5_12d for fixing the anodes and the cathodes
i1 = 2
degree = 60
for i in range(int(360/degree)):
    radius = 32 - 3.5 - 2.5
    alpha=(i*degree*math.pi)/180
    part_rondelle_m5_d12_vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), -1)
    Mesh.insert(u"part_rondelle_m5_12d.stl", "assembly")
    FreeCAD.getDocument("assembly").getObject("part_rondelle_m5_12d00" + str(i1)).Placement = App.Placement(part_rondelle_m5_d12_vector, App.Rotation(App.Vector(0,1,0), 0))
    FreeCADGui.getDocument("assembly").getObject("part_rondelle_m5_12d00" + str(i1)).ShapeColor = (0.67,0.33,0.50)
    i1 += 1

# For placing all the part_rondelle_m5_12d for fixing the anodes and the cathodes
i1 = 8
degree = 60
for i in range(int(360/degree)):
    if i1 < 10:
        radius = 32 - 3.5 - 2.5
        alpha=(i*degree*math.pi)/180
        part_rondelle_m5_d12_vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 2)
        Mesh.insert(u"part_rondelle_m5_12d.stl", "assembly")
        FreeCAD.getDocument("assembly").getObject("part_rondelle_m5_12d00" + str(i1)).Placement = App.Placement(part_rondelle_m5_d12_vector, App.Rotation(App.Vector(0,1,0), 0))
        FreeCADGui.getDocument("assembly").getObject("part_rondelle_m5_12d00" + str(i1)).ShapeColor = (0.67,0.33,0.50)
    else:
        radius = 32 - 3.5 - 2.5
        alpha=(i*degree*math.pi)/180
        part_rondelle_m5_d12_vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 2)
        Mesh.insert(u"part_rondelle_m5_12d.stl", "assembly")
        FreeCAD.getDocument("assembly").getObject("part_rondelle_m5_12d0" + str(i1)).Placement = App.Placement(part_rondelle_m5_d12_vector, App.Rotation(App.Vector(0,1,0), 0))
        FreeCADGui.getDocument("assembly").getObject("part_rondelle_m5_12d0" + str(i1)).ShapeColor = (0.67,0.33,0.50)
    
    i1 += 1

# insertion part_vis_metal_m5_100l - 0
Mesh.insert(u"part_vis_metal_m5_100l.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_vis_metal_m5_100l").Placement = App.Placement(App.Vector(0, 0, 5), App.Rotation(App.Vector(1,0,0), 180))
FreeCADGui.getDocument("assembly").getObject("part_vis_metal_m5_100l").ShapeColor = (0.00,0.00,1.00)

# For placing all the part_vis_metal_m5_100l for fixing the anodes and the cathodes
i1 = 1
degree = 60
for i in range(int(360/degree)):
    radius = 32 - 3.5 - 2.5
    alpha=(i*degree*math.pi)/180
    vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), -3)
    Mesh.insert(u"part_vis_metal_m5_100l.stl", "assembly")
    FreeCAD.getDocument("assembly").getObject("part_vis_metal_m5_100l00" + str(i1)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,1,0), 0))
    FreeCADGui.getDocument("assembly").getObject("part_vis_metal_m5_100l00" + str(i1)).ShapeColor = (0.00,0.00,1.00)
    i1 += 1

# insertion part_ecrou_5m - 0
Mesh.insert(u"part_ecrou_5m.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_ecrou_5m").Placement = App.Placement(App.Vector(0, 0, -5), App.Rotation(App.Vector(0,1,0), 0))
FreeCADGui.getDocument("assembly").getObject("part_ecrou_5m").ShapeColor = (1.00,1.00,1.00)

# For placing all the part_ecrou_5m for fixing the anodes and the cathodes
i1 = 1
degree = 60
for i in range(int(360/degree)):
    radius = 32 - 3.5 - 2.5
    alpha=(i*degree*math.pi)/180
    vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 3)
    Mesh.insert(u"part_ecrou_5m.stl", "assembly")
    FreeCAD.getDocument("assembly").getObject("part_ecrou_5m00" + str(i1)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,1,0), 0))
    FreeCADGui.getDocument("assembly").getObject("part_ecrou_5m00" + str(i1)).ShapeColor = (1.00,1.00,1.00)
    i1 += 1

# For placing all the part_rondelle_m5_12d for fixing the anodes and the cathodes
i1 = 14
degree = 60
for i in range(int(360/degree)):
    radius = 32 - 3.5 - 2.5
    alpha=(i*degree*math.pi)/180
    part_rondelle_m5_d12_vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 7)
    Mesh.insert(u"part_rondelle_m5_12d.stl", "assembly")
    FreeCAD.getDocument("assembly").getObject("part_rondelle_m5_12d0" + str(i1)).Placement = App.Placement(part_rondelle_m5_d12_vector, App.Rotation(App.Vector(0,1,0), 0))
    FreeCADGui.getDocument("assembly").getObject("part_rondelle_m5_12d0" + str(i1)).ShapeColor = (0.67,0.33,0.50)
    i1 += 1

# insertion part_capacitor_plate - 0
Mesh.insert(u"part_capacitor_plate.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_capacitor_plate").Placement = App.Placement(App.Vector(0, 0, 8), App.Rotation(App.Vector(0,1,0), 0))
FreeCADGui.getDocument("assembly").getObject("part_capacitor_plate").ShapeColor = (1.00,1.00,0.00)

# For placing all the part_rondelle_m5_12d for fixing the anodes and the cathodes
i1 = 20
degree = 60
for i in range(int(360/degree)):
    radius = 32 - 3.5 - 2.5
    alpha=(i*degree*math.pi)/180
    part_rondelle_m5_d12_vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 9)
    Mesh.insert(u"part_rondelle_m5_12d.stl", "assembly")
    FreeCAD.getDocument("assembly").getObject("part_rondelle_m5_12d0" + str(i1)).Placement = App.Placement(part_rondelle_m5_d12_vector, App.Rotation(App.Vector(0,1,0), 0))
    FreeCADGui.getDocument("assembly").getObject("part_rondelle_m5_12d0" + str(i1)).ShapeColor = (0.67,0.33,0.50)
    i1 += 1

# insertion part_capacitor_plate - 1
Mesh.insert(u"part_capacitor_plate.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_capacitor_plate001").Placement = App.Placement(App.Vector(0, 0, 10), App.Rotation(App.Vector(0,0,1), 60))
FreeCADGui.getDocument("assembly").getObject("part_capacitor_plate001").ShapeColor = (1.00,0.67,0.00)

# For placing all the part_rondelle_m5_12d for fixing the anodes and the cathodes
i1 = 26
degree = 60
for i in range(int(360/degree)):
    radius = 32 - 3.5 - 2.5
    alpha=(i*degree*math.pi)/180
    part_rondelle_m5_d12_vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 11)
    Mesh.insert(u"part_rondelle_m5_12d.stl", "assembly")
    FreeCAD.getDocument("assembly").getObject("part_rondelle_m5_12d0" + str(i1)).Placement = App.Placement(part_rondelle_m5_d12_vector, App.Rotation(App.Vector(0,1,0), 0))
    FreeCADGui.getDocument("assembly").getObject("part_rondelle_m5_12d0" + str(i1)).ShapeColor = (0.67,0.33,0.50)
    i1 += 1

# insertion part_capacitor_plate - 2
Mesh.insert(u"part_capacitor_plate.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_capacitor_plate002").Placement = App.Placement(App.Vector(0, 0, 12), App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly").getObject("part_capacitor_plate002").ShapeColor = (1.00,1.00,0.00)

# For placing all the part_rondelle_m5_12d for fixing the anodes and the cathodes
i1 = 32
degree = 60
for i in range(int(360/degree)):
    radius = 32 - 3.5 - 2.5
    alpha=(i*degree*math.pi)/180
    part_rondelle_m5_d12_vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 13)
    Mesh.insert(u"part_rondelle_m5_12d.stl", "assembly")
    FreeCAD.getDocument("assembly").getObject("part_rondelle_m5_12d0" + str(i1)).Placement = App.Placement(part_rondelle_m5_d12_vector, App.Rotation(App.Vector(0,1,0), 0))
    FreeCADGui.getDocument("assembly").getObject("part_rondelle_m5_12d0" + str(i1)).ShapeColor = (0.67,0.33,0.50)
    i1 += 1

# insertion part_capacitor_plate - 3
Mesh.insert(u"part_capacitor_plate.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_capacitor_plate003").Placement = App.Placement(App.Vector(0, 0, 14), App.Rotation(App.Vector(0,0,1), 60))
FreeCADGui.getDocument("assembly").getObject("part_capacitor_plate003").ShapeColor = (1.00,0.67,0.00)

# For placing all the part_rondelle_m5_12d for fixing the anodes and the cathodes
i1 = 38
degree = 60
for i in range(int(360/degree)):
    radius = 32 - 3.5 - 2.5
    alpha=(i*degree*math.pi)/180
    part_rondelle_m5_d12_vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 15)
    Mesh.insert(u"part_rondelle_m5_12d.stl", "assembly")
    FreeCAD.getDocument("assembly").getObject("part_rondelle_m5_12d0" + str(i1)).Placement = App.Placement(part_rondelle_m5_d12_vector, App.Rotation(App.Vector(0,1,0), 0))
    FreeCADGui.getDocument("assembly").getObject("part_rondelle_m5_12d0" + str(i1)).ShapeColor = (0.67,0.33,0.50)
    i1 += 1

# For placing all the part_capacitor_plate
for i in range(4, 10):
    if i % 2 == 0:
        vector = App.Vector(0, 0, i*2 + 8)
        Mesh.insert(u"part_capacitor_plate.stl", "assembly")
        FreeCAD.getDocument("assembly").getObject("part_capacitor_plate00" + str(i)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
        FreeCADGui.getDocument("assembly").getObject("part_capacitor_plate00" + str(i)).ShapeColor = (1.00,1.00,0.00)
    else:
        vector = App.Vector(0, 0, i*2 + 8)
        Mesh.insert(u"part_capacitor_plate.stl", "assembly")
        FreeCAD.getDocument("assembly").getObject("part_capacitor_plate00" + str(i)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 60))
        FreeCADGui.getDocument("assembly").getObject("part_capacitor_plate00" + str(i)).ShapeColor = (1.00,0.67,0.00)

# For placing all the part_capacitor_plate
for i in range(10, 40):
    if i % 2 == 0:
        vector = App.Vector(0, 0, i*2 + 8)
        Mesh.insert(u"part_capacitor_plate.stl", "assembly")
        FreeCAD.getDocument("assembly").getObject("part_capacitor_plate0" + str(i)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
        FreeCADGui.getDocument("assembly").getObject("part_capacitor_plate0" + str(i)).ShapeColor = (1.00,1.00,0.00)
    else:
        vector = App.Vector(0, 0, i*2 + 8)
        Mesh.insert(u"part_capacitor_plate.stl", "assembly")
        FreeCAD.getDocument("assembly").getObject("part_capacitor_plate0" + str(i)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 60))
        FreeCADGui.getDocument("assembly").getObject("part_capacitor_plate0" + str(i)).ShapeColor = (1.00,0.67,0.00)

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
