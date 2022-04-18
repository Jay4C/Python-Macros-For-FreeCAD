import os
import time
import unittest
import pywinauto.mouse
import pywinauto.keyboard


# https://patents.google.com/patent/US3071705A/en?q=electrostatic+propulsion&q=F03H1%2f00&country=US&before=priority:19900101
class UnitTestsPatentUS3071705AElectrostaticPropulsionMeans(unittest.TestCase):
    # ok
    def test_part_electrode_laser_cutting(self):
        print("test_part_electrode_laser_cutting")

        if os.path.exists("part_electrode_laser_cutting.py"):
            os.remove("part_electrode_laser_cutting.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_electrode_laser_cutting.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh, importDXF

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_electrode_laser_cutting"


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

# part_electrode_laser_cutting
part_electrode_laser_cutting = Part.makeCylinder(maximal_diameter/2, 1)

cylinder_1 = Part.makeCylinder(5, 1)

# part_electrode_laser_cutting cut by cylinder_1
part_electrode_laser_cutting = part_electrode_laser_cutting.cut(cylinder_1)

# holes for the thrust
degree = 90
for i in range(int(360/degree)):
    radius = 15
    alpha = (i*degree*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(5, 1)
    hole.translate(hole_vector)
    part_electrode_laser_cutting = part_electrode_laser_cutting.cut(hole)

# holes for the thrust
degree = 30
for i in range(int(360/degree)):
    radius = 30
    alpha = (i*degree*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(5, 1)
    hole.translate(hole_vector)
    part_electrode_laser_cutting = part_electrode_laser_cutting.cut(hole)

# holes for fixing the electrodes together
degree = 15
for i in range(int(360/degree)):
    radius = 45
    alpha = (i*degree*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(2.5, 1)
    hole.translate(hole_vector)
    part_electrode_laser_cutting = part_electrode_laser_cutting.cut(hole)

Part.show(part_electrode_laser_cutting)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_electrode_laser_cutting").getObject("Shape"))

stl_file = u"part_electrode_laser_cutting.stl"

Mesh.export(__objs__, stl_file)

dxf_file = u"part_electrode_laser_cutting.dxf"

importDXF.export(__objs__, dxf_file)

setview()
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"part_electrode_laser_cutting.py"{)}.read{(}{)}{)}'
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

number_of_steps = 20

# insertion part_electrode_laser_cutting
Mesh.insert(u"part_electrode_laser_cutting.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_electrode_laser_cutting").Placement = App.Placement(App.Vector(0, 0, 0), App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly").getObject("part_electrode_laser_cutting").ShapeColor = (0.10,0.20,0.30)

# insertion part_electrode_laser_cutting
for i in range(1, number_of_steps):
    if i < 10:
        Mesh.insert(u"part_electrode_laser_cutting.stl", "assembly")
        FreeCAD.getDocument("assembly").getObject("part_electrode_laser_cutting00" + str(i)).Placement = App.Placement(App.Vector(0, 0, i*3), App.Rotation(App.Vector(0,0,1), 0))
        FreeCADGui.getDocument("assembly").getObject("part_electrode_laser_cutting00" + str(i)).ShapeColor = (0.50,0.40,0.30)
    elif i >= 10 and i < 100:
        Mesh.insert(u"part_electrode_laser_cutting.stl", "assembly")
        FreeCAD.getDocument("assembly").getObject("part_electrode_laser_cutting0" + str(i)).Placement = App.Placement(App.Vector(0, 0, i*3), App.Rotation(App.Vector(0,0,1), 0))
        FreeCADGui.getDocument("assembly").getObject("part_electrode_laser_cutting0" + str(i)).ShapeColor = (0.50,0.40,0.30)
    else:
        Mesh.insert(u"part_electrode_laser_cutting.stl", "assembly")
        FreeCAD.getDocument("assembly").getObject("part_electrode_laser_cutting" + str(i)).Placement = App.Placement(App.Vector(0, 0, i*3), App.Rotation(App.Vector(0,0,1), 0))
        FreeCADGui.getDocument("assembly").getObject("part_electrode_laser_cutting" + str(i)).ShapeColor = (0.50,0.40,0.30)
    
setview()

__objs__ = []

__objs__.append(FreeCAD.getDocument("assembly").getObject("part_electrode_laser_cutting"))

# append part_electrode_laser_cutting
for i in range(1, number_of_steps):
    if i < 10:
        __objs__.append(FreeCAD.getDocument("assembly").getObject("part_electrode_laser_cutting00" + str(i)))
    elif i >= 10 and i < 100:
        __objs__.append(FreeCAD.getDocument("assembly").getObject("part_electrode_laser_cutting0" + str(i)))
    else:
        __objs__.append(FreeCAD.getDocument("assembly").getObject("part_electrode_laser_cutting" + str(i)))

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
