import os
import time
import unittest
import pywinauto.mouse
import pywinauto.keyboard


# https://patents.google.com/patent/US1061206A/en?q=tesla+turbine&before=priority:19900101
class UnitTestsPatentUS1061206ATeslaTurbineVersion1(unittest.TestCase):
    # ok
    # https://www.visseriefixations.fr/tiges-filetees/acier-classe-4-6/tige-filetee-acier-4-6-brut-din-975/tige-filetee-m30-acier-4-6-brut-din-975.html
    def test_part_tige_filetee_m30_1000l(self):
        print("test_part_tige_filetee_m30_1000l")

        if os.path.exists("part_tige_filetee_m30_1000l.py"):
            os.remove("part_tige_filetee_m30_1000l.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_tige_filetee_m30_1000l.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_tige_filetee_m30_1000l"


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

# tige_filetee_m30_1000l
tige_filetee_m30_1000l = Part.makeCylinder(30/2, 1000)

Part.show(tige_filetee_m30_1000l)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_tige_filetee_m30_1000l").getObject("Shape"))

stl_file = u"part_tige_filetee_m30_1000l.stl"

Mesh.export(__objs__, stl_file)

setview()
    """)

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"part_tige_filetee_m30_1000l.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.visseriefixations.fr/ecrous/ecrous-autofreines/ecrou-hexagonal-autofreine-nylstop/ecrou-nylstop-acier-zingue-blanc-din-985/ecrou-nylstop-m30-z-blanc-din-985.html
    def test_part_ecrou_30m(self):
        print("test_part_ecrou_30m")

        if os.path.exists("part_ecrou_30m.py"):
            os.remove("part_ecrou_30m.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_ecrou_30m.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_ecrou_30m"


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

d1 = 30
e = 50.85
h = 30

cylinder_1 = Part.makeCylinder(e/2, h)

cylinder_2 = Part.makeCylinder(d1/2, h)

cylinder_1 = cylinder_1.cut(cylinder_2)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_ecrou_30m").getObject("Shape"))

stl_file = u"part_ecrou_30m.stl"

Mesh.export(__objs__, stl_file)

setview()
        """)

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"part_ecrou_30m.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.visseriefixations.fr/rondelles-circlips/rondelles-plates/sans-chanfrein/serie-etroite-z/acier/rondelle-z-acier-zingue-blanc-nfe-25513/rondelle-z-0-30-z-blanc-nfe-25513.html
    def test_part_rondelle_30m(self):
        print("test_part_rondelle_30m")

        if os.path.exists("part_rondelle_30m.py"):
            os.remove("part_rondelle_30m.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_rondelle_30m.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_rondelle_30m"


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

d1 = 31 
d2 = 52
s = 4

cylinder_1 = Part.makeCylinder(d2/2, s)

cylinder_2 = Part.makeCylinder(d1/2, s)

cylinder_1 = cylinder_1.cut(cylinder_2)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_rondelle_30m").getObject("Shape"))

stl_file = u"part_rondelle_30m.stl"

Mesh.export(__objs__, stl_file)

setview()
        """)

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"part_rondelle_30m.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # Based on : https://e-steel.arcelormittal.com/FR/fr/Tube/Tube-acier/Tube-rond-en-acier/Tube-rond-soud%C3%A9-en-acier/p/000000000002007451
    def test_part_blade(self):
        print("test_part_blade")

        if os.path.exists("part_blade.py"):
            os.remove("part_blade.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_blade.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh, importDXF

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_blade"


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

diametre_maximal = 406.4 - 8*2 - 5*2

# part_blade
part_blade = Part.makeCylinder(diametre_maximal/2, 3)

# part_blade cut by cylinder_1
cylinder_1 = Part.makeCylinder(30/2, 3)
part_blade = part_blade.cut(cylinder_1)

# holes for evacuating the fluid from all the blades
degree = 45
for i in range(int(360/degree)):
    radius = 52/2 + 10
    alpha=(i*degree*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(10, 3)
    hole.translate(hole_vector)
    part_blade = part_blade.cut(hole)

Part.show(part_blade)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_blade").getObject("Shape"))

stl_file = u"part_blade.stl"

Mesh.export(__objs__, stl_file)

dxf_file = u"part_blade.dxf"

importDXF.export(__objs__, dxf_file)

setview()
    """)

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"part_blade.py"{)}.read{(}{)}{)}'
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

# insertion part_tige_filetee_m30_1000l
Mesh.insert(u"part_tige_filetee_m30_1000l.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_tige_filetee_m30_1000l").Placement = App.Placement(App.Vector(0, 0, 0), App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly").getObject("part_tige_filetee_m30_1000l").ShapeColor = (0.50,0.40,0.30)

# insertion part_ecrou_30m _ 1
Mesh.insert(u"part_ecrou_30m.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_ecrou_30m").Placement = App.Placement(App.Vector(0, 0, 40.2 + 3 + 5), App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly").getObject("part_ecrou_30m").ShapeColor = (0.90,0.80,0.70)

# insertion part_ecrou_30m _ 2
Mesh.insert(u"part_ecrou_30m.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_ecrou_30m001").Placement = App.Placement(App.Vector(0, 0, 1000 - 40.2 - 3 - 5 - 7), App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly").getObject("part_ecrou_30m001").ShapeColor = (0.90,0.80,0.70)

# insertion part_rondelle_30m
Mesh.insert(u"part_rondelle_30m.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_rondelle_30m").Placement = App.Placement(App.Vector(0, 0, 40.2 + 3 + 5 + 30), App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly").getObject("part_rondelle_30m").ShapeColor = (0.60,0.50,0.40)

# insertion part_blade
Mesh.insert(u"part_blade.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_blade").Placement = App.Placement(App.Vector(0, 0, 40.2 + 3 + 5 + 30 + 4), App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly").getObject("part_blade").ShapeColor = (0.30,0.20,0.10)

number_of_steps = 123

# insertion part_rondelle_30m
for i in range(0, number_of_steps):
    location = 40.2 + 3 + 5 + 30 + (i+1)*7
    
    if i < 9:
        Mesh.insert(u"part_rondelle_30m.stl", "assembly")
        FreeCAD.getDocument("assembly").getObject("part_rondelle_30m00" + str(i+1)).Placement = App.Placement(App.Vector(0, 0, location), App.Rotation(App.Vector(0,0,1), 0))
        FreeCADGui.getDocument("assembly").getObject("part_rondelle_30m00" + str(i+1)).ShapeColor = (0.60,0.50,0.40)
    elif i < 99:
        Mesh.insert(u"part_rondelle_30m.stl", "assembly")
        FreeCAD.getDocument("assembly").getObject("part_rondelle_30m0" + str(i+1)).Placement = App.Placement(App.Vector(0, 0, location), App.Rotation(App.Vector(0,0,1), 0))
        FreeCADGui.getDocument("assembly").getObject("part_rondelle_30m0" + str(i+1)).ShapeColor = (0.60,0.50,0.40)
    else:
        Mesh.insert(u"part_rondelle_30m.stl", "assembly")
        FreeCAD.getDocument("assembly").getObject("part_rondelle_30m" + str(i+1)).Placement = App.Placement(App.Vector(0, 0, location), App.Rotation(App.Vector(0,0,1), 0))
        FreeCADGui.getDocument("assembly").getObject("part_rondelle_30m" + str(i+1)).ShapeColor = (0.60,0.50,0.40)
        
# insertion part_blade
for i in range(0, number_of_steps):
    location = 40.2 + 3 + 5 + 30 + 4 + (i+1)*7
    
    if i < 9:
        Mesh.insert(u"part_blade.stl", "assembly")
        FreeCAD.getDocument("assembly").getObject("part_blade00" + str(i+1)).Placement = App.Placement(App.Vector(0, 0, location), App.Rotation(App.Vector(0,0,1), 0))
        FreeCADGui.getDocument("assembly").getObject("part_blade00" + str(i+1)).ShapeColor = (0.30,0.20,0.10)
    elif i < 99:
        Mesh.insert(u"part_blade.stl", "assembly")
        FreeCAD.getDocument("assembly").getObject("part_blade0" + str(i+1)).Placement = App.Placement(App.Vector(0, 0, location), App.Rotation(App.Vector(0,0,1), 0))
        FreeCADGui.getDocument("assembly").getObject("part_blade0" + str(i+1)).ShapeColor = (0.30,0.20,0.10)
    else:
        Mesh.insert(u"part_blade.stl", "assembly")
        FreeCAD.getDocument("assembly").getObject("part_blade" + str(i+1)).Placement = App.Placement(App.Vector(0, 0, location), App.Rotation(App.Vector(0,0,1), 0))
        FreeCADGui.getDocument("assembly").getObject("part_blade" + str(i+1)).ShapeColor = (0.30,0.20,0.10)

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
