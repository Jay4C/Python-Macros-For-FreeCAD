import FreeCAD, Part, Drawing

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_cathode"


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

cylinder_1 = Part.makeCylinder(9.525, 101.6)

cylinder_2 = Part.makeCylinder(8.525, 101.6)

cut_1 = cylinder_1.cut(cylinder_2)

box_1 = Part.makeBox(4, 10, 25)

cut_2 = cut_1.cut(box_1)

Part.show(cut_2)

DOC.recompute()

step_file = "C:\\part_cathode.stp"

Part.export([cut_2], step_file) 

setview()
        