import os
import time
import unittest
import pywinauto.mouse
import pywinauto.keyboard


class UnitTestsChasCampbellGravitationalEngineVersion1(unittest.TestCase):
    # ok
    # https://www.visseriefixations.fr/tiges-filetees/acier-classe-4-6/tige-filetee-acier-4-6-brut-din-975/tige-filetee-m20-acier-4-6-brut-din-975.html
    def test_part_tige_filetee_m20_1000l(self):
        print("test_part_tige_filetee_m20_1000l")

        if os.path.exists("part_tige_filetee_m20_1000l.py"):
            os.remove("part_tige_filetee_m20_1000l.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_tige_filetee_m20_1000l.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "tige_filetee_m20_1000l"


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

# tige_filetee_m20_1000l
tige_filetee_m20_1000l = Part.makeCylinder(20/2, 1000)

Part.show(tige_filetee_m20_1000l)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("tige_filetee_m20_1000l").getObject("Shape"))

stl_file = u"part_tige_filetee_m20_1000l.stl"

Mesh.export(__objs__, stl_file)

setview()
    """)

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"part_tige_filetee_m20_1000l.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.visseriefixations.fr/ecrous/ecrous-autofreines/ecrou-hexagonal-autofreine-nylstop/ecrou-nylstop-acier-zingue-blanc-din-985/ecrou-nylstop-m20-z-blanc-din-985.html
    def test_part_ecrou_20m(self):
        print("test_part_ecrou_20m")

        if os.path.exists("part_ecrou_20m.py"):
            os.remove("part_ecrou_20m.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_ecrou_20m.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_ecrou_20m"


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

d1 = 20
e = 32.95
h = 20

cylinder_1 = Part.makeCylinder(e/2, h)

cylinder_2 = Part.makeCylinder(d1/2, h)

cylinder_1 = cylinder_1.cut(cylinder_2)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_ecrou_20m").getObject("Shape"))

stl_file = u"part_ecrou_20m.stl"

Mesh.export(__objs__, stl_file)

setview()
        """)

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"part_ecrou_20m.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.visseriefixations.fr/rondelles-circlips/rondelles-plates/sans-chanfrein/serie-etroite-z/acier/rondelle-z-acier-zingue-blanc-nfe-25513/rondelle-z-0-20-z-blanc-nfe-25513.html
    def test_part_rondelle_20m(self):
        print("test_part_rondelle_20m")

        if os.path.exists("part_rondelle_20m.py"):
            os.remove("part_rondelle_20m.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_rondelle_20m.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_rondelle_20m"


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

d1 = 21
d2 = 36
s = 3

cylinder_1 = Part.makeCylinder(d2/2, s)

cylinder_2 = Part.makeCylinder(d1/2, s)

cylinder_1 = cylinder_1.cut(cylinder_2)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_rondelle_20m").getObject("Shape"))

stl_file = u"part_rondelle_20m.stl"

Mesh.export(__objs__, stl_file)

setview()
        """)

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"part_rondelle_20m.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.mypalletsonline.com/fr/palette-occasion-1000x1200/197-palette-bois-1000-x-1200-recycle-demi-lourde-3s.html
    def test_part_support_masselotte(self):
        print("test_part_support_masselotte")

        if os.path.exists("part_support_masselotte.py"):
            os.remove("part_support_masselotte.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_support_masselotte.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_support_masselotte"


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

length = 1200
width = 70
thickness = 20

box_1 = Part.makeBox(length, width, thickness)

cylinder_1 = Part.makeCylinder(20/2, 20)

# box_1 cut by cylinder_1
cylinder_1_vector = FreeCAD.Vector(600, 35, 0)
cylinder_1.translate(cylinder_1_vector)
box_1 = box_1.cut(cylinder_1)

Part.show(box_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_support_masselotte").getObject("Shape"))

stl_file = u"part_support_masselotte.stl"

Mesh.export(__objs__, stl_file)

setview()
        """)

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"part_support_masselotte.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.mypalletsonline.com/fr/palette-occasion-1000x1200/197-palette-bois-1000-x-1200-recycle-demi-lourde-3s.html
    def test_part_masselotte(self):
        print("test_part_masselotte")

        if os.path.exists("part_masselotte.py"):
            os.remove("part_masselotte.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_masselotte.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_masselotte"


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

length = 200
width = 70
thickness = 20

box_1 = Part.makeBox(length, width, thickness)

Part.show(box_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_masselotte").getObject("Shape"))

stl_file = u"part_masselotte.stl"

Mesh.export(__objs__, stl_file)

setview()
        """)

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"part_masselotte.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_assembly_slice_flywheel(self):
        print("test_assembly_slice_flywheel")

        if os.path.exists("assembly_slice_flywheel.py"):
            os.remove("assembly_slice_flywheel.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("assembly_slice_flywheel.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_slice_flywheel"


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

# part_support_masselotte
Mesh.insert(u"part_support_masselotte.stl","assembly_slice_flywheel")
FreeCADGui.getDocument("assembly_slice_flywheel").getObject("part_support_masselotte").ShapeColor = (0.10,0.10,0.10)
FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_support_masselotte").Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),0))

# part_masselotte
Mesh.insert(u"part_masselotte.stl","assembly_slice_flywheel")
FreeCADGui.getDocument("assembly_slice_flywheel").getObject("part_masselotte").ShapeColor = (0.90,0.80,0.70)
FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte").Placement = App.Placement(App.Vector(1000,0,-25),App.Rotation(App.Vector(1,0,0),90))

# part_masselotte
for i in range(1, 10):
    x = 1000
    y = -i * 20
    z = -25
    
    Mesh.insert(u"part_masselotte.stl","assembly_slice_flywheel")
    FreeCADGui.getDocument("assembly_slice_flywheel").getObject("part_masselotte00" + str(i)).ShapeColor = (0.90,0.80,0.70)
    FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte00" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),90))

# part_masselotte
for i in range(10, 20):
    x = 1000
    y = 90 + 20 * (i-10)
    z = -25
    
    Mesh.insert(u"part_masselotte.stl","assembly_slice_flywheel")
    FreeCADGui.getDocument("assembly_slice_flywheel").getObject("part_masselotte0" + str(i)).ShapeColor = (0.90,0.80,0.70)
    FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte0" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),90))

# part_masselotte
for i in range(20, 30):
    x = 0
    y = -20 * (i - 20)
    z = -25
    
    Mesh.insert(u"part_masselotte.stl","assembly_slice_flywheel")
    FreeCADGui.getDocument("assembly_slice_flywheel").getObject("part_masselotte0" + str(i)).ShapeColor = (0.90,0.80,0.70)
    FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte0" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),90))

# part_masselotte
for i in range(30, 40):
    x = 0
    y = 90 + 20 * (i-30)
    z = -25
    
    Mesh.insert(u"part_masselotte.stl","assembly_slice_flywheel")
    FreeCADGui.getDocument("assembly_slice_flywheel").getObject("part_masselotte0" + str(i)).ShapeColor = (0.90,0.80,0.70)
    FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte0" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),90))

setview()

# Export assembly_slice_flywheel
__objs__=[]
__objs__.append(FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_support_masselotte"))
__objs__.append(FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte"))

for i in range(1, 10):
    __objs__.append(FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte00" + str(i)))

for i in range(10, 20):
    __objs__.append(FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte0" + str(i)))

for i in range(20, 30):
    __objs__.append(FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte0" + str(i)))
    
for i in range(30, 40):
    __objs__.append(FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte0" + str(i)))

Mesh.export(__objs__,u"assembly_slice_flywheel.stl")

del __objs__
    """)

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"assembly_slice_flywheel.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_assembly_flywheel(self):
        print("test_assembly_flywheel")

        if os.path.exists("assembly_flywheel.py"):
            os.remove("assembly_flywheel.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("assembly_flywheel.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_flywheel"


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

# part_tige_filetee_m20_1000l
Mesh.insert(u"part_tige_filetee_m20_1000l.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_tige_filetee_m20_1000l").ShapeColor = (0.40,0.20,0.10)
FreeCAD.getDocument("assembly_flywheel").getObject("part_tige_filetee_m20_1000l").Placement = App.Placement(App.Vector(600,35,-(1000-20)/2),App.Rotation(App.Vector(0,0,1),0))

# assembly_slice_flywheel
Mesh.insert(u"assembly_slice_flywheel.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("assembly_slice_flywheel").ShapeColor = (0.10,0.20,0.40)
FreeCAD.getDocument("assembly_flywheel").getObject("assembly_slice_flywheel").Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),0))

# assembly_slice_flywheel
for i in range(1, 7):
    z = 70 * i
    
    Mesh.insert(u"assembly_slice_flywheel.stl","assembly_flywheel")
    FreeCADGui.getDocument("assembly_flywheel").getObject("assembly_slice_flywheel00" + str(i)).ShapeColor = (0.10,0.20,0.40)    
    FreeCAD.getDocument("assembly_flywheel").getObject("assembly_slice_flywheel00" + str(i)).Placement = App.Placement(App.Vector(0,0,z),App.Rotation(App.Vector(0,0,1),0))

# assembly_slice_flywheel
for i in range(7, 13):
    z = -70 * (i - 6)
    
    if i < 10:
        Mesh.insert(u"assembly_slice_flywheel.stl","assembly_flywheel")
        FreeCADGui.getDocument("assembly_flywheel").getObject("assembly_slice_flywheel00" + str(i)).ShapeColor = (0.10,0.20,0.40)    
        FreeCAD.getDocument("assembly_flywheel").getObject("assembly_slice_flywheel00" + str(i)).Placement = App.Placement(App.Vector(0,0,z),App.Rotation(App.Vector(0,0,1),0))
    else:
        Mesh.insert(u"assembly_slice_flywheel.stl","assembly_flywheel")
        FreeCADGui.getDocument("assembly_flywheel").getObject("assembly_slice_flywheel0" + str(i)).ShapeColor = (0.10,0.20,0.40)    
        FreeCAD.getDocument("assembly_flywheel").getObject("assembly_slice_flywheel0" + str(i)).Placement = App.Placement(App.Vector(0,0,z),App.Rotation(App.Vector(0,0,1),0))
        
setview()

# part_rondelle_20m
Mesh.insert(u"part_rondelle_20m.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_rondelle_20m").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m").Placement = App.Placement(App.Vector(600,35,70*6 + 20),App.Rotation(App.Vector(0,0,1),0))

# part_rondelle_20m
Mesh.insert(u"part_rondelle_20m.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_rondelle_20m001").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m001").Placement = App.Placement(App.Vector(600,35,-70*6 - 3),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_20m
Mesh.insert(u"part_ecrou_20m.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_ecrou_20m").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_flywheel").getObject("part_ecrou_20m").Placement = App.Placement(App.Vector(600,35,70*6 + 20 + 3),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_20m
Mesh.insert(u"part_ecrou_20m.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_ecrou_20m001").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_flywheel").getObject("part_ecrou_20m001").Placement = App.Placement(App.Vector(600,35,-70*6 - 3 - 20),App.Rotation(App.Vector(0,0,1),0))

# Export assembly_flywheel
__objs__=[]
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_tige_filetee_m20_1000l"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("assembly_slice_flywheel"))

for i in range(1, 10):
    __objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("assembly_slice_flywheel00" + str(i)))

for i in range(10, 13):
    __objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("assembly_slice_flywheel0" + str(i)))

__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m001"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_ecrou_20m"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_ecrou_20m001"))

Mesh.export(__objs__,u"assembly_flywheel.stl")

del __objs__
    """)

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"assembly_flywheel.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')


if __name__ == '__main__':
    unittest.main()
