import unittest
import os
import pywinauto.mouse
import pywinauto.keyboard
import time


# Homopolar generator
# https://patentimages.storage.googleapis.com/0c/c9/14/0e4d740f16793e/WO1995008210A1.pdf
class UnitsTestsHGVersion1Parts(unittest.TestCase):
    # ok
    # https://www.visseriefixations.fr/tiges-filetees/acier-classe-4-6/tige-filetee-acier-4-6-brut-din-975/tige-filetee-m20-acier-4-6-brut-din-975.html
    def test_part_tige_filetee_m20_1000l(self):
        print("test_part_tige_filetee_m20_1000l")

        if os.path.exists("Scripts\\part_tige_filetee_m20_1000l.py"):
            os.remove("Scripts\\part_tige_filetee_m20_1000l.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\part_tige_filetee_m20_1000l.py", "w") as file:
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

stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/part_tige_filetee_m20_1000l.stl"

Mesh.export(__objs__, stl_file)

setview()
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(665*1.5), round(695*1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60*1.5), round(615*1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Python-Macros-For-FreeCAD\\\\HG\\\\Version_1\\\\Scripts\\\\part_tige_filetee_m20_1000l.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.visseriefixations.fr/ecrous/ecrous-hexagonaux/ecrou-hexagonal-hu/ecrou-hu-acier-brut-din-934/ecrou-hu-acier-brut-classe-8-din-934/ecrou-hu-m20-brut-din-934.html
    def test_part_ecrou_20m(self):
        print("test_part_ecrou_20m")

        if os.path.exists("Scripts\\part_ecrou_20m.py"):
            os.remove("Scripts\\part_ecrou_20m.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\part_ecrou_20m.py", "w") as file:
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

stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/part_ecrou_20m.stl"

Mesh.export(__objs__, stl_file)

setview()
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(670 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Python-Macros-For-FreeCAD\\\\HG\\\\Version_1\\\\Scripts\\\\part_ecrou_20m.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.visseriefixations.fr/rondelles-circlips/rondelles-plates/sans-chanfrein/serie-etroite-z/acier/rondelle-z-acier-zingue-blanc-nfe-25513/rondelle-z-0-20-z-blanc-nfe-25513.html
    def test_part_rondelle_20m(self):
        print("test_part_rondelle_20m")

        if os.path.exists("Scripts\\part_rondelle_20m.py"):
            os.remove("Scripts\\part_rondelle_20m.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\part_rondelle_20m.py", "w") as file:
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

stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/part_rondelle_20m.stl"

Mesh.export(__objs__, stl_file)

setview()
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(670 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Python-Macros-For-FreeCAD\\\\HG\\\\Version_1\\\\Scripts\\\\part_rondelle_20m.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.france-poulies.com/paliers/5370-palier-alesage-o20-aplique-2-trous.html
    def test_part_palier(self):
        print("test_part_palier")

        if os.path.exists("Scripts\\part_palier.py"):
            os.remove("Scripts\\part_palier.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\part_palier.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_palier"


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

# part_palier
x = 127
y = 38
z = 65
part_palier = Part.makeBox(x, y, z)

trou_arbre = Part.makeCylinder(20/2, y)

# Cut part_palier by trou_arbre
# rotation trou_arbre
axe_x = FreeCAD.Vector(1, 0, 0)
trou_arbre_vector = FreeCAD.Vector(0, 0, 0)
trou_arbre.rotate(trou_arbre_vector, axe_x, 90)

# translation trou_arbre
trou_arbre_vector = FreeCAD.Vector(x/2, 38, 33.3)
trou_arbre.translate(trou_arbre_vector)

part_palier = part_palier.cut(trou_arbre)

# Cut part_palier by trou_vis
trou_vis = Part.makeCylinder(13/2, 65)

# translation trou_vis
trou_vis_vector = FreeCAD.Vector((127-95)/2, 38/2, 0)
trou_vis.translate(trou_vis_vector)

part_palier = part_palier.cut(trou_vis)

# translation trou_vis
trou_vis_vector = FreeCAD.Vector(95, 0, 0)
trou_vis.translate(trou_vis_vector)

part_palier = part_palier.cut(trou_vis)

Part.show(part_palier)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_palier").getObject("Shape"))

stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/part_palier.stl"

Mesh.export(__objs__, stl_file)

setview()
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(670 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Python-Macros-For-FreeCAD\\\\HG\\\\Version_1\\\\Scripts\\\\part_palier.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.laserboost.com/
    def test_part_faraday_disc(self):
        print("test_part_faraday_disc")

        if os.path.exists("Scripts\\part_faraday_disc.py"):
            os.remove("Scripts\\part_faraday_disc.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\part_faraday_disc.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh, importDXF

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_faraday_disc"


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
d2 = 140 + 10*2
s = 3

cylinder_1 = Part.makeCylinder(d2/2, s)

cylinder_2 = Part.makeCylinder(d1/2, s)

cylinder_1 = cylinder_1.cut(cylinder_2)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_faraday_disc").getObject("Shape"))

stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/part_faraday_disc.stl"

Mesh.export(__objs__, stl_file)

dxf_file = u"part_faraday_disc.dxf"

importDXF.export(__objs__, dxf_file)

setview()

del __objs__
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(670 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Python-Macros-For-FreeCAD\\\\HG\\\\Version_1\\\\Scripts\\\\part_faraday_disc.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.aimant-boutique.fr/ferrite/anneaux-aimantes/anneau-40.0-x-20.0-x-10.0-mm-y35-ferrite-adherence-2-kg
    def test_part_magnet_1d40_2d20_10e(self):
        print("test_part_magnet_1d40_2d20_10e")

        if os.path.exists("Scripts\\part_magnet_1d40_2d20_10e.py"):
            os.remove("Scripts\\part_magnet_1d40_2d20_10e.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\part_magnet_1d40_2d20_10e.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_magnet_1d40_2d20_10e"


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
d2 = 40
s = 10

cylinder_1 = Part.makeCylinder(d2/2, s)

cylinder_2 = Part.makeCylinder(d1/2, s)

cylinder_1 = cylinder_1.cut(cylinder_2)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_magnet_1d40_2d20_10e").getObject("Shape"))

stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/part_magnet_1d40_2d20_10e.stl"

Mesh.export(__objs__, stl_file)

setview()
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(670 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Python-Macros-For-FreeCAD\\\\HG\\\\Version_1\\\\Scripts\\\\part_magnet_1d40_2d20_10e.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.aimant-boutique.fr/aimants-en-ferrite/anneaux-magnetiques/2957/anneau-magnetique-oe-30-0-x-10-0-x-10-0-mm-y35-ferrite
    def test_part_magnet_1d30_2d10_10e(self):
        print("test_part_magnet_1d30_2d10_10e")

        if os.path.exists("Scripts\\part_magnet_1d30_2d10_10e.py"):
            os.remove("Scripts\\part_magnet_1d30_2d10_10e.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\part_magnet_1d30_2d10_10e.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_magnet_1d30_2d10_10e"


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

d1 = 10
d2 = 30
s = 10

cylinder_1 = Part.makeCylinder(d2/2, s)

cylinder_2 = Part.makeCylinder(d1/2, s)

cylinder_1 = cylinder_1.cut(cylinder_2)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_magnet_1d30_2d10_10e").getObject("Shape"))

stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/part_magnet_1d30_2d10_10e.stl"

Mesh.export(__objs__, stl_file)

setview()
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(670 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Python-Macros-For-FreeCAD\\\\HG\\\\Version_1\\\\Scripts\\\\part_magnet_1d30_2d10_10e.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.aimant-boutique.fr/ferrite/anneaux-aimantes/anneau-140.0-x-60.0-x-20.0-mm-y30-ferrite
    def test_part_magnet_1d140_2d60_20e(self):
        print("test_part_magnet_1d140_2d60_20e")

        if os.path.exists("Scripts\\part_magnet_1d140_2d60_20e.py"):
            os.remove("Scripts\\part_magnet_1d140_2d60_20e.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\part_magnet_1d140_2d60_20e.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_magnet_1d140_2d60_20e"


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

d1 = 60
d2 = 140
s = 20

cylinder_1 = Part.makeCylinder(d2/2, s)

cylinder_2 = Part.makeCylinder(d1/2, s)

cylinder_1 = cylinder_1.cut(cylinder_2)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_magnet_1d140_2d60_20e").getObject("Shape"))

stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/part_magnet_1d140_2d60_20e.stl"

Mesh.export(__objs__, stl_file)

setview()
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(670 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Python-Macros-For-FreeCAD\\\\HG\\\\Version_1\\\\Scripts\\\\part_magnet_1d140_2d60_20e.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.visseriefixations.fr/tiges-filetees/acier-classe-4-6/tige-filetee-acier-4-6-brut-din-975/tige-filetee-m10-acier-4-6-brut-din-975.html
    def test_part_tige_filetee_m10_1000l(self):
        print("test_part_tige_filetee_m10_1000l")

        if os.path.exists("Scripts\\part_tige_filetee_m10_1000l.py"):
            os.remove("Scripts\\part_tige_filetee_m10_1000l.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\part_tige_filetee_m10_1000l.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_tige_filetee_m10_1000l"


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

d1 = 10
cylinder_1 = Part.makeCylinder(d1/2, 1000)

Part.show(cylinder_1)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_tige_filetee_m10_1000l").getObject("Shape"))

stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/part_tige_filetee_m10_1000l.stl"

Mesh.export(__objs__, stl_file)

setview()
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(665*1.5), round(695*1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60*1.5), round(615*1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Python-Macros-For-FreeCAD\\\\HG\\\\Version_1\\\\Scripts\\\\part_tige_filetee_m10_1000l.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.visseriefixations.fr/ecrous/ecrous-hexagonaux/ecrou-hexagonal-hu/ecrou-hu-acier-brut-din-934/ecrou-hu-acier-brut-classe-8-din-934/ecrou-hu-m10-brut-din-934.html
    def test_part_ecrou_10m(self):
        print("test_part_ecrou_10m")

        if os.path.exists("Scripts\\part_ecrou_10m.py"):
            os.remove("Scripts\\part_ecrou_10m.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\part_ecrou_10m.py", "w") as file:
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

d1 = 10
e = 18.9
h = 8

cylinder_1 = Part.makeCylinder(e/2, h)

cylinder_2 = Part.makeCylinder(d1/2, h)

cylinder_1 = cylinder_1.cut(cylinder_2)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_ecrou_10m").getObject("Shape"))

stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/part_ecrou_10m.stl"

Mesh.export(__objs__, stl_file)

setview()
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(670 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Python-Macros-For-FreeCAD\\\\HG\\\\Version_1\\\\Scripts\\\\part_ecrou_10m.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.visseriefixations.fr/rondelles-circlips/rondelles-plates/sans-chanfrein/serie-etroite-z/acier/rondelle-z-acier-zingue-blanc-nfe-25513/rondelle-z-0-10-z-blanc-nfe-25513.html
    def test_part_rondelle_10m(self):
        print("test_part_rondelle_10m")

        if os.path.exists("Scripts\\part_rondelle_10m.py"):
            os.remove("Scripts\\part_rondelle_10m.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\part_rondelle_10m.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_rondelle_10m"


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

d1 = 10.5
d2 = 20
s = 2

cylinder_1 = Part.makeCylinder(d2/2, s)

cylinder_2 = Part.makeCylinder(d1/2, s)

cylinder_1 = cylinder_1.cut(cylinder_2)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_rondelle_10m").getObject("Shape"))

stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/part_rondelle_10m.stl"

Mesh.export(__objs__, stl_file)

setview()
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(670 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Python-Macros-For-FreeCAD\\\\HG\\\\Version_1\\\\Scripts\\\\part_rondelle_10m.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.123roulement.com/paliers-UCF204
    def test_part_palier_4_fixations(self):
        print("test_part_palier_4_fixations")

        if os.path.exists("Scripts\\part_palier_4_fixations.py"):
            os.remove("Scripts\\part_palier_4_fixations.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\part_palier_4_fixations.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_palier_4_fixations"


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

# part_palier_4_fixations
x = 86
y = x
z = 33.3
part_palier_4_fixations = Part.makeBox(x, y, z)

# cylinder_1
r1 = 4
L1 = z
cylinder_1 = Part.makeCylinder(r1, L1)

# cylinder_2
r2 = 10
L2 = z
cylinder_2 = Part.makeCylinder(r2, L2)

# cut part_palier_4_fixations by trou_arbre
trou_arbre = Part.makeCylinder(r2, z)
trou_arbre_vector = FreeCAD.Vector(x/2, y/2, 0)
trou_arbre.translate(trou_arbre_vector)
part_palier_4_fixations = part_palier_4_fixations.cut(trou_arbre)

# cut part_palier_4_fixations by trou_vis
x1 = (x - 64)/2
y1 = (y - 64)/2
trou_vis = Part.makeCylinder(r1, z)
trou_vis_vector = FreeCAD.Vector(x1, y1, 0)
trou_vis.translate(trou_vis_vector)
part_palier_4_fixations = part_palier_4_fixations.cut(trou_vis)

x1 = 64 + (x - 64)/2
y1 = (y - 64)/2
trou_vis = Part.makeCylinder(r1, z)
trou_vis_vector = FreeCAD.Vector(x1, y1, 0)
trou_vis.translate(trou_vis_vector)
part_palier_4_fixations = part_palier_4_fixations.cut(trou_vis)

x1 = (x - 64)/2
y1 = 64 + (y - 64)/2
trou_vis = Part.makeCylinder(r1, z)
trou_vis_vector = FreeCAD.Vector(x1, y1, 0)
trou_vis.translate(trou_vis_vector)
part_palier_4_fixations = part_palier_4_fixations.cut(trou_vis)

x1 = 64 + (x - 64)/2
y1 = 64 + (y - 64)/2
trou_vis = Part.makeCylinder(r1, z)
trou_vis_vector = FreeCAD.Vector(x1, y1, 0)
trou_vis.translate(trou_vis_vector)
part_palier_4_fixations = part_palier_4_fixations.cut(trou_vis)

# Show part
Part.show(part_palier_4_fixations)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_palier_4_fixations").getObject("Shape"))

stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/part_palier_4_fixations.stl"

Mesh.export(__objs__, stl_file)

setview()
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(670 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Python-Macros-For-FreeCAD\\\\HG\\\\Version_1\\\\Scripts\\\\part_palier_4_fixations.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_part_tube(self):
        print("test_part_tube")

        if os.path.exists("Scripts\\part_tube.py"):
            os.remove("Scripts\\part_tube.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\part_tube.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_tube"


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

# part_tube
r = (140 + 10*2 + 5*2)/2
L = 700
e = 2

part_tube = Part.makeCylinder(r, L)

cylinder_1 = Part.makeCylinder(r - e, L)

part_tube = part_tube.cut(cylinder_1)

Part.show(part_tube)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_tube").getObject("Shape"))

stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/part_tube.stl"

Mesh.export(__objs__, stl_file)

setview()
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(670 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Python-Macros-For-FreeCAD\\\\HG\\\\Version_1\\\\Scripts\\\\part_tube.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.sculpteo.com/fr/
    def test_part_support(self):
        print("test_part_support")

        if os.path.exists("Scripts\\part_support.py"):
            os.remove("Scripts\\part_support.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\part_support.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh, math

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
EPS_C = EPS * -0.5

# tube diameter
d_tube = 140 + 10*2 + 5*2

# nut diameter
d_nut = 24

# main diameter
d1 = d_tube + 5*2 + 2*2 + d_nut*2 + 2*2

# maximum length
h1 = (700 - 170)/2

# hole length
h2 = h1 - 5

# inner diamter for fixing the tube
d_inner_tube = d_tube

# radius for fixing the device
r_f_d = (d_tube + 5*2 + 2*2 + d_nut)/2

# screw diameter
d_vis = 12.1

d3 = d1

d4 = d_tube + 5*2

d_arbre = 20.1

# part_palier_4_fixations dimensions
r_f_p = math.sqrt(math.pow(32, 2) + math.pow(32, 2))

d_mamelon = 16

d_vis_palier = 8.1

# Cylinder_1
cylinder_1 = Part.makeCylinder(d1/2, h1)

# Cut cylinder_1 by cylinder_2
cylinder_2 = Part.makeCylinder(d_inner_tube/2, h2)
cylinder_1 = cylinder_1.cut(cylinder_2)

# holes for fixing the device
degre = 15
for i in range(int(360/degre)):
    radius = r_f_d
    alpha=(i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(d_vis/2, h1)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

# Cylinder_3
cylinder_3 = Part.makeCylinder(d3/2, h2)

# Cut cylinder_3 by cylinder_4
cylinder_4 = Part.makeCylinder(d4/2, h2)
cylinder_3 = cylinder_3.cut(cylinder_4)

# Cut cylinder_1 by cylinder_3
cylinder_3_vector = FreeCAD.Vector(0, 0, 5)
cylinder_3.translate(cylinder_3_vector)
cylinder_1 = cylinder_1.cut(cylinder_3)

# Cut cylinder_1 by cylinder_5
cylinder_5 = Part.makeCylinder(d_arbre/2, h1)
cylinder_1 = cylinder_1.cut(cylinder_5)

# cut cylinder_1 by trou_vis for fixing the part_palier_4_fixations
for degre in [45, 45*3, 45*5, 45*7]:
    radius = r_f_p
    alpha = (degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(d_vis_palier/2, h1)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

# cut cylinder_1 by trou_mamelon for fixing the mamelon to poor mercury
for degre in [90]:
    radius = (86 + 25 + d_mamelon)/2
    alpha = (degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(d_mamelon/2, h1)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

Part.show(cylinder_1)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_support").getObject("Shape"))

stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/part_support.stl"

Mesh.export(__objs__, stl_file)

setview()
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(670 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Python-Macros-For-FreeCAD\\\\HG\\\\Version_1\\\\Scripts\\\\part_support.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.visseriefixations.fr/vis-a-tete-hexagonale/vis-a-tete-hexagonale-standard/acier-8-8-noir/th-acier-8-8-noir-filetage-total-din-933/th-m12x200-acier-8-8-noir-ef-din-933.html
    def test_part_vis_metal_m12_200l(self):
        print("test_part_vis_metal_m12_200l")

        if os.path.exists("Scripts\\part_vis_metal_m12_200l.py"):
            os.remove("Scripts\\part_vis_metal_m12_200l.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\part_vis_metal_m12_200l.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_vis_metal_m12_200l"


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

L = 200
k = 7.5
d1 = 12
e = 21.1

cylinder_1 = Part.makeCylinder(e/2, L+k)

cylinder_2 = Part.makeCylinder(d1/2, L)

cylinder_3 = Part.makeCylinder(e/2, L)

# cylinder_3 cut by cylinder_2
cylinder_3 = cylinder_3.cut(cylinder_2)

# cylinder_1 cut by cylinder_3
cylinder_3_vector = FreeCAD.Vector(0, 0, k)
cylinder_3.translate(cylinder_3_vector)
cylinder_1 = cylinder_1.cut(cylinder_3)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]
__objs__.append(FreeCAD.getDocument("part_vis_metal_m12_200l").getObject("Shape"))

stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/part_vis_metal_m12_200l.stl"

Mesh.export(__objs__, stl_file)

setview()
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(670 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Python-Macros-For-FreeCAD\\\\HG\\\\Version_1\\\\Scripts\\\\part_vis_metal_m12_200l.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.visseriefixations.fr/rondelles-circlips/rondelles-plates/sans-chanfrein/serie-etroite-z/acier/rondelle-z-acier-zingue-blanc-nfe-25513/rondelle-z-0-12-z-blanc-nfe-25513.html
    def test_part_rondelle_12m(self):
        print("test_part_rondelle_12m")

        if os.path.exists("Scripts\\part_rondelle_12m.py"):
            os.remove("Scripts\\part_rondelle_12m.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\part_rondelle_12m.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_rondelle_12m"


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

d1 = 13
d2 = 24
s = 2.5

cylinder_1 = Part.makeCylinder(d2/2, s)

cylinder_2 = Part.makeCylinder(d1/2, s)

cylinder_1 = cylinder_1.cut(cylinder_2)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_rondelle_12m").getObject("Shape"))

stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/part_rondelle_12m.stl"

Mesh.export(__objs__, stl_file)

setview()
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(670 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Python-Macros-For-FreeCAD\\\\HG\\\\Version_1\\\\Scripts\\\\part_rondelle_12m.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.visseriefixations.fr/ecrous/ecrous-hexagonaux/ecrou-hexagonal-hu/ecrou-hu-acier-brut-din-934/ecrou-hu-acier-brut-classe-8-din-934/ecrou-hu-m12-brut-din-934.html
    def test_part_ecrou_12m(self):
        print("test_part_ecrou_12m")

        if os.path.exists("Scripts\\part_ecrou_12m.py"):
            os.remove("Scripts\\part_ecrou_12m.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\part_ecrou_12m.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_ecrou_12m"


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

d1 = 12
e = 21.1
h = 10

cylinder_1 = Part.makeCylinder(e/2, h)

cylinder_2 = Part.makeCylinder(d1/2, h)

cylinder_1 = cylinder_1.cut(cylinder_2)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_ecrou_12m").getObject("Shape"))

stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/part_ecrou_12m.stl"

Mesh.export(__objs__, stl_file)

setview()
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(670 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Python-Macros-For-FreeCAD\\\\HG\\\\Version_1\\\\Scripts\\\\part_ecrou_12m.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.visseriefixations.fr/vis-a-tete-hexagonale/vis-a-tete-hexagonale-standard/acier-8-8-noir/th-acier-8-8-noir-filetage-total-din-933/th-m8x50-acier-8-8-noir-ef-din-933.html
    def test_part_vis_metal_m8_50l(self):
        print("test_part_vis_metal_m8_50l")

        if os.path.exists("Scripts\\part_vis_metal_m8_50l.py"):
            os.remove("Scripts\\part_vis_metal_m8_50l.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\part_vis_metal_m8_50l.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_vis_metal_m8_50l"


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

L = 50
k = 5.3
d1 = 8
e = 14.38

cylinder_1 = Part.makeCylinder(e/2, L+k)

cylinder_2 = Part.makeCylinder(d1/2, L)

cylinder_3 = Part.makeCylinder(e/2, L)

# cylinder_3 cut by cylinder_2
cylinder_3 = cylinder_3.cut(cylinder_2)

# cylinder_1 cut by cylinder_3
cylinder_3_vector = FreeCAD.Vector(0, 0, k)
cylinder_3.translate(cylinder_3_vector)
cylinder_1 = cylinder_1.cut(cylinder_3)

Part.show(cylinder_1)

DOC.recompute()

__objs__ = []
__objs__.append(FreeCAD.getDocument("part_vis_metal_m8_50l").getObject("Shape"))

stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/part_vis_metal_m8_50l.stl"

Mesh.export(__objs__, stl_file)

setview()
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(670 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Python-Macros-For-FreeCAD\\\\HG\\\\Version_1\\\\Scripts\\\\part_vis_metal_m8_50l.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.visseriefixations.fr/rondelles-circlips/rondelles-plates/sans-chanfrein/serie-etroite-z/acier/rondelle-z-acier-zingue-blanc-nfe-25513/rondelle-z-0-8-z-blanc-nfe-25513.html
    def test_part_rondelle_8m(self):
        print("test_part_rondelle_8m")

        if os.path.exists("Scripts\\part_rondelle_8m.py"):
            os.remove("Scripts\\part_rondelle_8m.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\part_rondelle_8m.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_rondelle_8m"


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

d1 = 8.4
d2 = 16
s = 1.5

cylinder_1 = Part.makeCylinder(d2/2, s)

cylinder_2 = Part.makeCylinder(d1/2, s)

cylinder_1 = cylinder_1.cut(cylinder_2)

Part.show(cylinder_1)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_rondelle_8m").getObject("Shape"))

stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/part_rondelle_8m.stl"

Mesh.export(__objs__, stl_file)

setview()
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(670 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Python-Macros-For-FreeCAD\\\\HG\\\\Version_1\\\\Scripts\\\\part_rondelle_8m.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.visseriefixations.fr/ecrous/ecrous-hexagonaux/ecrou-hexagonal-hu/ecrou-hu-acier-brut-din-934/ecrou-hu-acier-brut-classe-8-din-934/ecrou-hu-m8-brut-din-934.html
    def test_part_ecrou_8m(self):
        print("test_part_ecrou_8m")

        if os.path.exists("Scripts\\part_ecrou_8m.py"):
            os.remove("Scripts\\part_ecrou_8m.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\part_ecrou_8m.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_ecrou_8m"


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

d1 = 8
e = 14.38
h = 6.5

cylinder_1 = Part.makeCylinder(e/2, h)

cylinder_2 = Part.makeCylinder(d1/2, h)

cylinder_1 = cylinder_1.cut(cylinder_2)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_ecrou_8m").getObject("Shape"))

stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/part_ecrou_8m.stl"

Mesh.export(__objs__, stl_file)

setview()
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(670 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Python-Macros-For-FreeCAD\\\\HG\\\\Version_1\\\\Scripts\\\\part_ecrou_8m.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.leroymerlin.fr/produits/chauffage-plomberie/circuit-alimentation-en-eau/tube-et-raccord-alimentation/raccord-alimentation/lot-de-2-mamelons-a-visser-laiton-m-12-x-17-pour-tube-en-cuivre-65814231.html
    def test_part_mamelon_a_visser_12_17_m(self):
        print("test_part_mamelon_a_visser_12_17_m")

        if os.path.exists("Scripts\\part_mamelon_a_visser_12_17_m.py"):
            os.remove("Scripts\\part_mamelon_a_visser_12_17_m.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\part_mamelon_a_visser_12_17_m.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_mamelon_a_visser_12_17_m"

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

__objs__.append(FreeCAD.getDocument("part_mamelon_a_visser_12_17_m").getObject("Shape"))

stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/part_mamelon_a_visser_12_17_m.stl"

Mesh.export(__objs__, stl_file)

setview()
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(670 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Python-Macros-For-FreeCAD\\\\HG\\\\Version_1\\\\Scripts\\\\part_mamelon_a_visser_12_17_m.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.leroymerlin.fr/produits/chauffage-plomberie/circuit-alimentation-en-eau/tube-et-raccord-alimentation/raccord-alimentation/lot-de-2-manchons-a-visser-laiton-f-12-x-17-pour-tube-en-cuivre-65815253.html
    def test_part_manchon_a_visser_12_17_f(self):
        print("part_manchon_a_visser_12_17_f")

        if os.path.exists("Scripts\\part_manchon_a_visser_12_17_f.py"):
            os.remove("Scripts\\part_manchon_a_visser_12_17_f.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\part_manchon_a_visser_12_17_f.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_manchon_a_visser_12_17_f"

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

__objs__.append(FreeCAD.getDocument("part_manchon_a_visser_12_17_f").getObject("Shape"))

stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/part_manchon_a_visser_12_17_f.stl"

Mesh.export(__objs__, stl_file)

setview()
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(670 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Python-Macros-For-FreeCAD\\\\HG\\\\Version_1\\\\Scripts\\\\part_manchon_a_visser_12_17_f.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.123courroies.com/moyeu-amovible/71701-moyeu-amovible-ma2517-20-4014486251982.html
    def test_part_moyeu_amovible_generator(self):
        print("test_part_moyeu_amovible_generator")

        if os.path.exists("Scripts\\part_moyeu_amovible_generator.py"):
            os.remove("Scripts\\part_moyeu_amovible_generator.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\part_moyeu_amovible_generator.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_moyeu_amovible_generator"


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

# part_moyeu_amovible_generator
De = 85.5
L = 44.45
Di = 20
part_moyeu_amovible_generator = Part.makeCylinder(De/2, L)

cylinder_1 = Part.makeCylinder(Di/2, L)

# Cut part_moyeu_amovible_generator by cylinder_1
part_moyeu_amovible_generator = part_moyeu_amovible_generator.cut(cylinder_1)

Part.show(part_moyeu_amovible_generator)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_moyeu_amovible_generator").getObject("Shape"))

stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/part_moyeu_amovible_generator.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Python-Macros-For-FreeCAD\\\\HG\\\\Version_1\\\\Png\\\\part_moyeu_amovible_generator_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(690 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Python-Macros-For-FreeCAD\\\\HG\\\\Version_1\\\\Scripts\\\\part_moyeu_amovible_generator.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.123courroies.com/profil-z-10x6-spz-10x8/74122-poulie-trapezoidale-moyeu-amovible-spz500-2ma-4014486251364.html
    def test_part_poulie_generator(self):
        print("test_part_poulie_generator")

        if os.path.exists("Scripts\\part_poulie_generator.py"):
            os.remove("Scripts\\part_poulie_generator.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\part_poulie_generator.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_poulie_generator"


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

# part_poulie_generator
De = 504
L = 44.45
Di = 85.5
part_poulie_generator = Part.makeCylinder(De/2, L)

cylinder_1 = Part.makeCylinder(Di/2, L)

# Cut part_poulie_generator by cylinder_1
part_poulie_generator = part_poulie_generator.cut(cylinder_1)

Part.show(part_poulie_generator)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_poulie_generator").getObject("Shape"))

stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/part_poulie_generator.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Python-Macros-For-FreeCAD\\\\HG\\\\Version_1\\\\Png\\\\part_poulie_generator_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(690 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Python-Macros-For-FreeCAD\\\\HG\\\\Version_1\\\\Scripts\\\\part_poulie_generator.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')


class UnitsTestsHGVersion1Assemblies(unittest.TestCase):
    # ok
    def test_assembly_magnets_1d40_2d20_10e(self):
        print("test_assembly_magnets_1d40_2d20_10e")

        if os.path.exists("Scripts\\assembly_magnets_1d40_2d20_10e.py"):
            os.remove("Scripts\\assembly_magnets_1d40_2d20_10e.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\assembly_magnets_1d40_2d20_10e.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_magnets_1d40_2d20_10e"


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

assembly = "assembly_magnets_1d40_2d20_10e"

# part_magnet_1d40_2d20_10e
title = "part_magnet_1d40_2d20_10e"
stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/" + title + ".stl"

Mesh.insert(stl_file,assembly)
FreeCADGui.getDocument(assembly).getObject(title).ShapeColor = (0.10,0.10,0.10)
FreeCAD.getDocument(assembly).getObject(title).Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),0))

Mesh.insert(stl_file,assembly)
FreeCADGui.getDocument(assembly).getObject(title + "001").ShapeColor = (0.10,0.10,0.10)
FreeCAD.getDocument(assembly).getObject(title + "001").Placement = App.Placement(App.Vector(0,0,10),App.Rotation(App.Vector(0,0,1),0))

setview()

# Export
__objs__=[]
__objs__.append(FreeCAD.getDocument(assembly).getObject(title))
__objs__.append(FreeCAD.getDocument(assembly).getObject(title + "001"))

Mesh.export(__objs__,u"" + assembly + ".stl")

del __objs__
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(690 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Python-Macros-For-FreeCAD\\\\HG\\\\Version_1\\\\Scripts\\\\assembly_magnets_1d40_2d20_10e.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_assembly_shaft(self):
        print("test_assembly_shaft")

        if os.path.exists("Scripts\\assembly_shaft.py"):
            os.remove("Scripts\\assembly_shaft.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\assembly_shaft.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_shaft"


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

assembly = "assembly_shaft"

# part_tige_filetee_m20_1000l
part_tige_filetee_m20_1000l_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/part_tige_filetee_m20_1000l.stl"
Mesh.insert(part_tige_filetee_m20_1000l_stl_file,assembly)
FreeCADGui.getDocument(assembly).getObject("part_tige_filetee_m20_1000l").ShapeColor = (0.10,0.10,0.10)
FreeCAD.getDocument(assembly).getObject("part_tige_filetee_m20_1000l").Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),0))

# part_faraday_disc
color = (0.90,0.80,0.70)
i1 = round((1000 - 150*2)/23) - 3
title = 'part_faraday_disc'
stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/" + title + ".stl"
for i in range(0, i1):
    x = 0
    y = 0
    z = (150 + 20*2 + 3) + i * 23

    if i == 0:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i >= 1 and i < 10:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + "00" + str(i)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + "00" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i >= 10 and i < 100:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + "0" + str(i)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + "0" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i >= 100 and i < 1000:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + str(i)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))

# part_magnet_1d140_2d60_20e
color = (0.70,0.70,0.70)
i2 = round((1000 - 150*2)/23) - 4
title = 'part_magnet_1d140_2d60_20e'
stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/" + title + ".stl"
for i in range(0, i2):
    x = 0
    y = 0
    z = (150 + 20*2 + 3 + 3) + i * 23

    if i == 0:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i >= 1 and i < 10:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + "00" + str(i)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + "00" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i >= 10 and i < 100:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + "0" + str(i)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + "0" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i >= 100 and i < 1000:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + str(i)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))

# assembly_magnets_1d40_2d20_10e
color = (0.60,0.70,0.90)
i3 = round((1000 - 150*2)/23) - 4
title = 'assembly_magnets_1d40_2d20_10e'
stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/" + title + ".stl"
for i in range(0, i3):
    x = 0
    y = 0
    z = (150 + 20*2 + 3 + 3) + i * 23

    if i == 0:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i >= 1 and i < 10:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + "00" + str(i)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + "00" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i >= 10 and i < 100:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + "0" + str(i)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + "0" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i >= 100 and i < 1000:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + str(i)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))

# part_rondelle_20m
x = 0
y = 0
z = 150 + 20*2
part_rondelle_20m_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/part_rondelle_20m.stl"
Mesh.insert(part_rondelle_20m_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_rondelle_20m").ShapeColor = (0.10,0.20,0.30)
FreeCAD.getDocument(assembly).getObject("part_rondelle_20m").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))

x = 0
y = 0
z = 150 + 20*2 + 3 + (i1 - 1) * 23 + 3
part_rondelle_20m_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/part_rondelle_20m.stl"
Mesh.insert(part_rondelle_20m_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_rondelle_20m001").ShapeColor = (0.10,0.20,0.30)
FreeCAD.getDocument(assembly).getObject("part_rondelle_20m001").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))

# part_ecrou_20m
x = 0
y = 0
z = 150
part_ecrou_20m_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/part_ecrou_20m.stl"
Mesh.insert(part_ecrou_20m_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_ecrou_20m").ShapeColor = (0.20,0.50,0.70)
FreeCAD.getDocument(assembly).getObject("part_ecrou_20m").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))

x = 0
y = 0
z = 150 + 20
part_ecrou_20m_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/part_ecrou_20m.stl"
Mesh.insert(part_ecrou_20m_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_ecrou_20m001").ShapeColor = (0.20,0.50,0.70)
FreeCAD.getDocument(assembly).getObject("part_ecrou_20m001").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))

x = 0
y = 0
z = 150 + 20*2 + 3 + (i1 - 1) * 23 + 3*2
part_ecrou_20m_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/part_ecrou_20m.stl"
Mesh.insert(part_ecrou_20m_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_ecrou_20m002").ShapeColor = (0.20,0.50,0.70)
FreeCAD.getDocument(assembly).getObject("part_ecrou_20m002").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))

x = 0
y = 0
z = 150 + 20*2 + 3 + (i1 - 1) * 23 + 3*2 + 20
part_ecrou_20m_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/part_ecrou_20m.stl"
Mesh.insert(part_ecrou_20m_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_ecrou_20m003").ShapeColor = (0.20,0.50,0.70)
FreeCAD.getDocument(assembly).getObject("part_ecrou_20m003").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))

setview()

# Export
__objs__=[]
__objs__.append(FreeCAD.getDocument(assembly).getObject("part_tige_filetee_m20_1000l"))

title = "part_faraday_disc"
for i in range(0, i1):
    if i == 0:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title))
    elif i >= 1 and i < 10:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "00" + str(i)))
    elif i >= 10 and i < 100:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "0" + str(i)))
    elif i >= 100 and i < 1000:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + str(i)))

title = "part_magnet_1d140_2d60_20e"
for i in range(0, i2):
    if i == 0:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title))
    elif i >= 1 and i < 10:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "00" + str(i)))
    elif i >= 10 and i < 100:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "0" + str(i)))
    elif i >= 100 and i < 1000:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + str(i)))

title = "assembly_magnets_1d40_2d20_10e"
for i in range(0, i3):
    if i == 0:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title))
    elif i >= 1 and i < 10:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "00" + str(i)))
    elif i >= 10 and i < 100:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "0" + str(i)))
    elif i >= 100 and i < 1000:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + str(i)))

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_rondelle_20m"))
__objs__.append(FreeCAD.getDocument(assembly).getObject("part_rondelle_20m001"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_ecrou_20m"))
__objs__.append(FreeCAD.getDocument(assembly).getObject("part_ecrou_20m001"))
__objs__.append(FreeCAD.getDocument(assembly).getObject("part_ecrou_20m002"))
__objs__.append(FreeCAD.getDocument(assembly).getObject("part_ecrou_20m003"))

Mesh.export(__objs__,u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/" + assembly + ".stl")

del __objs__
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(690 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Python-Macros-For-FreeCAD\\\\HG\\\\Version_1\\\\Scripts\\\\assembly_shaft.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_assembly_support(self):
        print("test_assembly_support")

        if os.path.exists("Scripts\\assembly_support.py"):
            os.remove("Scripts\\assembly_support.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\assembly_support.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_support"


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

assembly = "assembly_support"

# part_palier_4_fixations dimensions
r_f_p = math.sqrt(math.pow(32, 2) + math.pow(32, 2))

# part_support
part_support_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/part_support.stl"
Mesh.insert(part_support_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_support").ShapeColor = (0.10,0.10,0.10)
FreeCAD.getDocument(assembly).getObject("part_support").Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),0))

# part_palier_4_fixations
x = -86/2
y = -86/2
z = (700 - 170)/2
part_palier_4_fixations_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/part_palier_4_fixations.stl"
Mesh.insert(part_palier_4_fixations_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_palier_4_fixations").ShapeColor = (0.30,0.50,0.70)
FreeCAD.getDocument(assembly).getObject("part_palier_4_fixations").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))

# part_rondelle_8m
color = (0.90, 0.80, 0.70)
i = 0
title = 'part_rondelle_8m'
stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/" + title + ".stl"
for degre in [45, 45*3, 45*5, 45*7]:
    radius = r_f_p
    alpha = (degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = (700 - 170)/2 - 5 - 1.5

    if i == 0:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i >= 1 and i < 10:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + "00" + str(i)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + "00" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i >= 10 and i < 100:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + "0" + str(i)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + "0" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i >= 100 and i < 1000:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + str(i)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    
    i += 1
    
color = (0.90, 0.80, 0.70)
title = 'part_rondelle_8m'
stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/" + title + ".stl"
for degre in [45, 45*3, 45*5, 45*7]:
    radius = r_f_p
    alpha = (degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = (700 - 170)/2 + 33.3

    if i == 0:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i >= 1 and i < 10:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + "00" + str(i)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + "00" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i >= 10 and i < 100:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + "0" + str(i)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + "0" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i >= 100 and i < 1000:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + str(i)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    
    i += 1

# part_ecrou_8m
color = (0.80, 0.90, 0.10)
i1 = 0
title = 'part_ecrou_8m'
stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/" + title + ".stl"
for degre in [45, 45*3, 45*5, 45*7]:
    radius = r_f_p
    alpha = (degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = (700 - 170)/2 + 33.3 + 1.5

    if i1 == 0:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i1 >= 1 and i1 < 10:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + "00" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + "00" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i1 >= 10 and i1 < 100:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + "0" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + "0" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i1 >= 100 and i1 < 1000:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + str(i1)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    
    i1 += 1

# part_vis_metal_m8_50l
color = (0.80, 0.00, 0.50)
i2 = 0
title = 'part_vis_metal_m8_50l'
stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/" + title + ".stl"
for degre in [45, 45*3, 45*5, 45*7]:
    radius = r_f_p
    alpha = (degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = (700 - 170)/2 - 5 - 1.5 - 5.3

    if i2 == 0:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i2 >= 1 and i2 < 10:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + "00" + str(i2)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + "00" + str(i2)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i2 >= 10 and i2 < 100:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + "0" + str(i2)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + "0" + str(i2)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i2 >= 100 and i2 < 1000:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + str(i2)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + str(i2)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    
    i2 += 1
    
# part_mamelon_a_visser_12_17_m
d_mamelon = 16
degre = 90
radius = (86 + 25 + d_mamelon)/2
alpha = (degre*math.pi)/180
x = radius*math.cos(alpha)
y = radius*math.sin(alpha)
z = (700 - 170)/2 - 5 - 11
color = (0.30, 0.50, 0.70)
part_mamelon_a_visser_12_17_m_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/part_mamelon_a_visser_12_17_m.stl"
Mesh.insert(part_mamelon_a_visser_12_17_m_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_mamelon_a_visser_12_17_m").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_mamelon_a_visser_12_17_m").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))

# part_manchon_a_visser_12_17_f
degre = 90
d_mamelon = 16
radius = (86 + 25 + d_mamelon)/2
alpha = (degre*math.pi)/180
x = radius*math.cos(alpha)
y = radius*math.sin(alpha)
z = (700 - 170)/2
color = (0.30, 0.60, 0.90)
part_manchon_a_visser_12_17_f_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/part_manchon_a_visser_12_17_f.stl"
Mesh.insert(part_manchon_a_visser_12_17_f_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_manchon_a_visser_12_17_f").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_manchon_a_visser_12_17_f").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))

setview()

# Export
__objs__ = []

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_support"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_palier_4_fixations"))

title = "part_rondelle_8m"
for i in range(0, 8):
    if i == 0:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title))
    elif i >= 1 and i < 10:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "00" + str(i)))
    elif i >= 10 and i < 100:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "0" + str(i)))
    elif i >= 100 and i < 1000:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + str(i)))

title = "part_ecrou_8m"
for i in range(0, 4):
    if i == 0:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title))
    elif i >= 1 and i < 10:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "00" + str(i)))
    elif i >= 10 and i < 100:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "0" + str(i)))
    elif i >= 100 and i < 1000:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + str(i)))

title = "part_vis_metal_m8_50l"
for i in range(0, 4):
    if i == 0:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title))
    elif i >= 1 and i < 10:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "00" + str(i)))
    elif i >= 10 and i < 100:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "0" + str(i)))
    elif i >= 100 and i < 1000:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + str(i)))

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_mamelon_a_visser_12_17_m"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_manchon_a_visser_12_17_f"))

Mesh.export(__objs__,u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/" + assembly + ".stl")

del __objs__
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(690 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Python-Macros-For-FreeCAD\\\\HG\\\\Version_1\\\\Scripts\\\\assembly_support.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_assembly_generator(self):
        print("test_assembly_generator")

        if os.path.exists("Scripts\\assembly_generator.py"):
            os.remove("Scripts\\assembly_generator.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\assembly_generator.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_generator"


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

assembly = "assembly_generator"

# tube diameter
d_tube = 140 + 10*2 + 5*2

# nut diameter
d_nut = 24

r_f_d = (d_tube + 5*2 + 2*2 + d_nut)/2

# assembly_shaft
assembly_shaft_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/assembly_shaft.stl"
Mesh.insert(assembly_shaft_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("assembly_shaft").ShapeColor = (0.10,0.10,0.10)
FreeCAD.getDocument(assembly).getObject("assembly_shaft").Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),0))

# part_tube
color = (0.20,0.50,0.70)
x = 0
y = 0
z = 150
part_tube_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/part_tube.stl"
Mesh.insert(part_tube_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_tube").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_tube").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))

# assembly_support
color = (0.20,0.00,0.70)
x = 0
y = 0
z = 150 + (700 - 170)/2 - 5
assembly_support_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/assembly_support.stl"
Mesh.insert(assembly_support_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("assembly_support").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("assembly_support").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,1,0),180))

# assembly_support
color = (0.20,0.00,0.70)
x = 0
y = 0
z = 700 - 110
assembly_support_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/assembly_support.stl"
Mesh.insert(assembly_support_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("assembly_support001").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("assembly_support001").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,1,0),0))

# part_rondelle_12m
i1 = 0
degre = 30
color = (0.30,0.90,0.30)
title = 'part_rondelle_12m'
stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/" + title + ".stl"
for i in range(int(360/degre)):
    radius = r_f_d
    alpha = (i*degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = 150 + (700 - 170)/2 - 5 - 5 - 2.5

    if i1 == 0:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i1 >= 1 and i1 < 10:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + "00" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + "00" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i1 >= 10 and i1 < 100:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + "0" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + "0" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i1 >= 100 and i1 < 1000:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + str(i1)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    
    i1 += 1

degre = 30
color = (0.30,0.90,0.30)
title = 'part_rondelle_12m'
stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/" + title + ".stl"
for i in range(int(360/degre)):
    radius = r_f_d
    alpha = (i*degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = 150 + (700 - 170)/2 + 180

    if i1 == 0:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i1 >= 1 and i1 < 10:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + "00" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + "00" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i1 >= 10 and i1 < 100:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + "0" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + "0" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i1 >= 100 and i1 < 1000:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + str(i1)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    
    i1 += 1

# part_ecrou_12m
i2 = 0
degre = 30
color = (0.10,0.50,0.10)
title = 'part_ecrou_12m'
stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/" + title + ".stl"
for i in range(int(360/degre)):
    radius = r_f_d
    alpha = (i*degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = 150 + (700 - 170)/2 + 180 + 2.5

    if i2 == 0:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i2 >= 1 and i2 < 10:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + "00" + str(i2)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + "00" + str(i2)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i2 >= 10 and i2 < 100:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + "0" + str(i2)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + "0" + str(i2)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i2 >= 100 and i2 < 1000:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + str(i2)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + str(i2)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    
    i2 += 1

# part_vis_metal_m12_200l
i3 = 0
degre = 30
color = (0.00,0.90,0.90)
title = 'part_vis_metal_m12_200l'
stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/" + title + ".stl"
for i in range(int(360/degre)):
    radius = r_f_d
    alpha = (i*degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = 150 + (700 - 170)/2 - 5 - 5 - 2.5 - 7.5

    if i3 == 0:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i3 >= 1 and i3 < 10:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + "00" + str(i3)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + "00" + str(i3)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i3 >= 10 and i3 < 100:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + "0" + str(i3)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + "0" + str(i3)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i3 >= 100 and i3 < 1000:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + str(i2)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + str(i2)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    
    i3 += 1

# part_rondelle_20m
color = (0.40,0.30,0.70)
x = 0
y = 0
z = 150 - 5 - 33.3 - 3
part_rondelle_20m_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/part_rondelle_20m.stl"
Mesh.insert(part_rondelle_20m_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_rondelle_20m").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_rondelle_20m").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,1,0),0))

# part_rondelle_20m
color = (0.40,0.30,0.70)
x = 0
y = 0
z = 150 + 700 + 5 + 33.3
part_rondelle_20m_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/part_rondelle_20m.stl"
Mesh.insert(part_rondelle_20m_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_rondelle_20m001").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_rondelle_20m001").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,1,0),0))

# part_ecrou_20m
color = (0.50,0.00,0.40)
x = 0
y = 0
z = 150 - 5 - 33.3 - 3 - 3 - 16 - 1
part_ecrou_20m_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/part_ecrou_20m.stl"
Mesh.insert(part_ecrou_20m_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_ecrou_20m").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_ecrou_20m").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,1,0),0))

# part_ecrou_20m
color = (0.50,0.00,0.40)
x = 0
y = 0
z = 150 + 700 + 5 + 33.3 + 3
part_ecrou_20m_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/part_ecrou_20m.stl"
Mesh.insert(part_ecrou_20m_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_ecrou_20m001").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_ecrou_20m001").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,1,0),0))

# part_rondelle_20m
color = (0.40,0.30,0.70)
x = 0
y = 0
z = 150 - 5 - 33.3 - 3 - 3 - 16 - 3
part_rondelle_20m_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/part_rondelle_20m.stl"
Mesh.insert(part_rondelle_20m_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_rondelle_20m002").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_rondelle_20m002").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,1,0),0))

# part_rondelle_20m
color = (0.40,0.30,0.70)
x = 0
y = 0
z = 150 + 700 + 5 + 33.3 + 3 + 16 + 4
part_rondelle_20m_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/part_rondelle_20m.stl"
Mesh.insert(part_rondelle_20m_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_rondelle_20m003").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_rondelle_20m003").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,1,0),0))

# part_palier
color = (0.20,0.60,0.20)
x = - 127/2
y = 65/2
z = 150 - 5 - 33.3 - 3 - 3 - 16 - 3 - 1 - 38 + 1
part_palier_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/part_palier.stl"
Mesh.insert(part_palier_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_palier").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_palier").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),90))

# part_palier
color = (0.20,0.60,0.20)
x = - 127/2
y = 65/2
z = 150 + 700 + 5 + 33.3 + 3 + 3 + 38 - 18
part_palier_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/part_palier.stl"
Mesh.insert(part_palier_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_palier001").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_palier001").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),90))

# part_rondelle_20m
color = (0.40,0.30,0.70)
x = 0
y = 0
z = 150 - 5 - 33.3 - 3 - 16 - 3 - 1 - 38 - 16 + 11
part_rondelle_20m_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/part_rondelle_20m.stl"
Mesh.insert(part_rondelle_20m_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_rondelle_20m004").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_rondelle_20m004").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,1,0),0))

# part_rondelle_20m
color = (0.40,0.30,0.70)
x = 0
y = 0
z = 150 + 700 + 5 + 33.3 + 3 + 38 - 18 + 38 + 3
part_rondelle_20m_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/part_rondelle_20m.stl"
Mesh.insert(part_rondelle_20m_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_rondelle_20m005").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_rondelle_20m005").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,1,0),0))

# part_ecrou_20m
color = (0.50,0.00,0.40)
x = 0
y = 0
z = 150 - 5 - 33.3 - 3 - 16 - 3 - 1 - 38 - 16 + 11 - 3 - 16 - 1
part_ecrou_20m_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/part_ecrou_20m.stl"
Mesh.insert(part_ecrou_20m_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_ecrou_20m002").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_ecrou_20m002").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,1,0),0))

# part_ecrou_20m
color = (0.50,0.00,0.40)
x = 0
y = 0
z = 150 + 700 + 5 + 33.3 + 3 + 38 - 18 + 38 + 3 + 3
part_ecrou_20m_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/part_ecrou_20m.stl"
Mesh.insert(part_ecrou_20m_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_ecrou_20m003").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_ecrou_20m003").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,1,0),0))

# part_moyeu_amovible_generator
'''
color = (0.60,0.60,0.60)
x = 0
y = 0
z = 150 - 5 - 33.3 - 3 - 16 - 3 - 1 - 38 - 16 + 11 - 3 - 16 - 1 - 21.5
part_moyeu_amovible_generator_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/part_moyeu_amovible_generator.stl"
Mesh.insert(part_moyeu_amovible_generator_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_moyeu_amovible_generator").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_moyeu_amovible_generator").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
'''

# part_poulie_generator
'''
color = (0.60,0.10,0.10)
x = 0
y = 0
z = 150 - 5 - 33.3 - 3 - 16 - 3 - 1 - 38 - 16 + 11 - 3 - 16 - 1 - 21.5
part_poulie_generator_stl_file = u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/part_poulie_generator.stl"
Mesh.insert(part_poulie_generator_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_poulie_generator").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_poulie_generator").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
'''

setview()

# Export
__objs__ = []

__objs__.append(FreeCAD.getDocument(assembly).getObject("assembly_shaft"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_tube"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("assembly_support"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("assembly_support001"))

title = "part_rondelle_12m"
for i in range(0, int(360/30)):
    if i == 0:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title))
    elif i >= 1 and i < 10:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "00" + str(i)))
    elif i >= 10 and i < 100:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "0" + str(i)))
    elif i >= 100 and i < 1000:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + str(i)))

title = "part_rondelle_12m"
for i in range(int(360/30), int(360/30) * 2):
    if i == 0:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title))
    elif i >= 1 and i < 10:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "00" + str(i)))
    elif i >= 10 and i < 100:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "0" + str(i)))
    elif i >= 100 and i < 1000:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + str(i)))

title = "part_ecrou_12m"
for i in range(0, int(360/30)):
    if i == 0:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title))
    elif i >= 1 and i < 10:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "00" + str(i)))
    elif i >= 10 and i < 100:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "0" + str(i)))
    elif i >= 100 and i < 1000:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + str(i)))

title = "part_vis_metal_m12_200l"
for i in range(0, int(360/30)):
    if i == 0:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title))
    elif i >= 1 and i < 10:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "00" + str(i)))
    elif i >= 10 and i < 100:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "0" + str(i)))
    elif i >= 100 and i < 1000:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + str(i)))

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_rondelle_20m"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_rondelle_20m001"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_ecrou_20m"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_ecrou_20m001"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_palier"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_palier001"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_rondelle_20m002"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_rondelle_20m003"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_rondelle_20m004"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_rondelle_20m005"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_ecrou_20m002"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_ecrou_20m003"))

# __objs__.append(FreeCAD.getDocument(assembly).getObject("part_moyeu_amovible_generator"))

# __objs__.append(FreeCAD.getDocument(assembly).getObject("part_poulie_generator"))

Mesh.export(__objs__,u"C:/Users/Jason/Documents/Devs/Python-Macros-For-FreeCAD/HG/Version_1/Stl/" + assembly + ".stl")

del __objs__

# Generate PNG files
file = 'C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Python-Macros-For-FreeCAD\\\\HG\\\\Version_1\\\\Png\\\\assembly_generator_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(690 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Python-Macros-For-FreeCAD\\\\HG\\\\Version_1\\\\Scripts\\\\assembly_generator.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')


if __name__ == '__main__':
    unittest.main()
