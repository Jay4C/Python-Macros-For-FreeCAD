import FreeCAD, Part

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

box = Part.makeBox(540, 540, 15)

cylinder_1 = Part.makeCylinder(250, 10, FreeCAD.Vector(270, 270, 0))
cylinder_2 = Part.makeCylinder(245, 10, FreeCAD.Vector(270, 270, 0))
cylinder_3 = cylinder_1.cut(cylinder_2)
box = box.cut(cylinder_3)

# Fixing with the bottom support
cylinder_4 = Part.makeCylinder(3.5, 15, FreeCAD.Vector(60, 60, 0))
cylinder_5 = Part.makeCylinder(3.5, 15, FreeCAD.Vector(480, 60, 0))
cylinder_6 = Part.makeCylinder(3.5, 15, FreeCAD.Vector(60, 480, 0))
cylinder_7 = Part.makeCylinder(3.5, 15, FreeCAD.Vector(480, 480, 0))
box = box.cut(cylinder_4)
box = box.cut(cylinder_5)
box = box.cut(cylinder_6)
box = box.cut(cylinder_7)

# Fixing the sensors, the input and the output
cylinder_8 = Part.makeCylinder(5, 15, FreeCAD.Vector(270, 270, 0))
cylinder_9 = Part.makeCylinder(5, 15, FreeCAD.Vector(270, 140, 0))
cylinder_10 = Part.makeCylinder(5, 15, FreeCAD.Vector(270, 400, 0))
cylinder_11 = Part.makeCylinder(5, 15, FreeCAD.Vector(140, 270, 0))
box = box.cut(cylinder_8)
box = box.cut(cylinder_9)
box = box.cut(cylinder_10)
box = box.cut(cylinder_11)

Part.show(box)

DOC.recompute()

step_file = "C:\\part_top_support.stp"

Part.export([box], step_file)

setview()
