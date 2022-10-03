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

stl_file = u"part_tige_filetee_m20_1000l.stl"

Mesh.export(__objs__, stl_file)

setview()
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(665*1.5), round(695*1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60*1.5), round(615*1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"part_tige_filetee_m20_1000l.py"{)}.read{(}{)}{)}'
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

stl_file = u"part_ecrou_20m.stl"

Mesh.export(__objs__, stl_file)

setview()
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(670 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

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

stl_file = u"part_rondelle_20m.stl"

Mesh.export(__objs__, stl_file)

setview()
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(670 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"part_rondelle_20m.py"{)}.read{(}{)}{)}'
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

stl_file = u"part_palier.stl"

Mesh.export(__objs__, stl_file)

setview()
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(670 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"part_palier.py"{)}.read{(}{)}{)}'
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

stl_file = u"part_faraday_disc.stl"

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
            'exec{(}open{(}"part_faraday_disc.py"{)}.read{(}{)}{)}'
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

stl_file = u"part_magnet_1d40_2d20_10e.stl"

Mesh.export(__objs__, stl_file)

setview()
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(670 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"part_magnet_1d40_2d20_10e.py"{)}.read{(}{)}{)}'
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

stl_file = u"part_magnet_1d30_2d10_10e.stl"

Mesh.export(__objs__, stl_file)

setview()
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(670 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"part_magnet_1d30_2d10_10e.py"{)}.read{(}{)}{)}'
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

stl_file = u"part_magnet_1d140_2d60_20e.stl"

Mesh.export(__objs__, stl_file)

setview()
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(670 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"part_magnet_1d140_2d60_20e.py"{)}.read{(}{)}{)}'
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

stl_file = u"part_tige_filetee_m10_1000l.stl"

Mesh.export(__objs__, stl_file)

setview()
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(665*1.5), round(695*1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60*1.5), round(615*1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"part_tige_filetee_m10_1000l.py"{)}.read{(}{)}{)}'
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

stl_file = u"part_ecrou_10m.stl"

Mesh.export(__objs__, stl_file)

setview()
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(670 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"part_ecrou_10m.py"{)}.read{(}{)}{)}'
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

stl_file = u"part_rondelle_10m.stl"

Mesh.export(__objs__, stl_file)

setview()
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(670 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"part_rondelle_10m.py"{)}.read{(}{)}{)}'
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
stl_file = u"" + title + ".stl"

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
            'exec{(}open{(}"assembly_magnets_1d40_2d20_10e.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    #
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
part_tige_filetee_m20_1000l_stl_file = u"part_tige_filetee_m20_1000l.stl"
Mesh.insert(part_tige_filetee_m20_1000l_stl_file,assembly)
FreeCADGui.getDocument(assembly).getObject("part_tige_filetee_m20_1000l").ShapeColor = (0.10,0.10,0.10)
FreeCAD.getDocument(assembly).getObject("part_tige_filetee_m20_1000l").Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),0))

# part_faraday_disc
color = (0.90,0.80,0.70)
i1 = round((1000 - (20 + 40 + 20*2 + 20 + 20)*2)/23) + 1
title = 'part_faraday_disc'
stl_file = u"" + title + ".stl"
for i in range(0, i1):
    x = 0
    y = 0
    z = 20 + 40 + 20*2 + 20 + 20 + i * 23

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
i2 = round((1000 - (20 + 40 + 20*2 + 20 + 20 + 3)*2)/23)
title = 'part_magnet_1d140_2d60_20e'
stl_file = u"" + title + ".stl"
for i in range(0, i2):
    x = 0
    y = 0
    z = 20 + 40 + 20*2 + 20 + 20 + 3 +i * 23

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
i3 = round((1000 - (20 + 40 + 20*2 + 20 + 20 + 3)*2)/23)
title = 'assembly_magnets_1d40_2d20_10e'
stl_file = u"" + title + ".stl"
for i in range(0, i3):
    x = 0
    y = 0
    z = 20 + 40 + 20*2 + 20 + 20 + 3 +i * 23

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

Mesh.export(__objs__,u"" + assembly + ".stl")

del __objs__
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(690 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"assembly_shaft.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')


if __name__ == '__main__':
    unittest.main()
